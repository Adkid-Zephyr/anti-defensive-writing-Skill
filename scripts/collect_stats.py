#!/usr/bin/env python3
"""Archive GitHub aggregate counts; never run inside the distributed skill."""
import argparse
import copy
from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess

REPO = "Adkid-Zephyr/anti-defensive-writing-Skill"
ROOT = Path(__file__).resolve().parents[1]


def api(path, paginate=False):
    command = ["gh", "api", path]
    if paginate:
        command += ["--paginate", "--slurp"]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    data = json.loads(result.stdout)
    return [item for page in data for item in page] if paginate else data


def merge(previous, clones, releases, now):
    """Replace overlapping daily counts; retain old days and deleted assets."""
    state = copy.deepcopy(previous) if previous else {
        "schema_version": 1, "repository": REPO, "clone_days": {}, "assets": {}
    }
    if state["schema_version"] != 1 or state["repository"] != REPO:
        raise ValueError("Unexpected statistics schema or repository")
    state["updated_at"] = now.isoformat()
    state["latest_clone_window"] = clones
    for row in clones["clones"]:
        day = date.fromisoformat(row["timestamp"][:10])
        # Today's count is incomplete. The oldest boundary day may be partial.
        # Keep it out of the cumulative archive; future overlapping runs fill days.
        if now.date() - timedelta(days=14) < day < now.date():
            if row["count"] < 0 or row["uniques"] < 0:
                raise ValueError("Negative traffic count")
            state["clone_days"][day.isoformat()] = {
                "count": row["count"], "uniques": row["uniques"],
                "last_observed_at": now.isoformat(),
            }
    for asset in state["assets"].values():
        asset["present_in_latest_release_scan"] = False
    for release in releases:
        if release["draft"]:
            continue
        for asset in release["assets"]:
            if asset["download_count"] < 0:
                raise ValueError("Negative asset download count")
            state["assets"][str(asset["id"])] = {
                "name": asset["name"], "tag": release["tag_name"],
                "count": asset["download_count"], "url": asset["browser_download_url"],
                "last_observed_at": now.isoformat(),
                "present_in_latest_release_scan": True,
                "is_distribution": asset["name"].startswith("anti-defensive-writing-")
                and asset["name"].endswith(".zip"),
            }
    return state


def missing_days(days):
    if not days:
        return []
    first, last = date.fromisoformat(min(days)), date.fromisoformat(max(days))
    return [(first + timedelta(days=i)).isoformat()
            for i in range((last - first).days + 1)
            if (first + timedelta(days=i)).isoformat() not in days]


def report(state):
    days = state["clone_days"]
    window = state["latest_clone_window"]
    packages = sum(a["count"] for a in state["assets"].values() if a["is_distribution"])
    gaps = missing_days(days)
    period = f"{min(days)} — {max(days)} (UTC)" if days else "No complete days yet"
    rows = ["# 下载与克隆统计 / Download and clone statistics", "",
            f"Last collected (UTC): {state['updated_at']}", "",
            "| 指标 / Metric | 数值 / Count |", "| --- | ---: |",
            f"| 已保存日期的克隆累计 / Archived daily clones | {sum(d['count'] for d in days.values()):,} |",
            f"| 最近 API 窗口克隆 / Latest API window clones | {window['count']:,} |",
            f"| 最近窗口独立克隆者 / Window unique cloners | {window['uniques']:,} |",
            f"| 已观测发布 ZIP 下载 / Observed release ZIP downloads | {packages:,} |", "",
            f"Archived daily range: {period}; {len(days)} recorded days.", "",
            f"Missing dates inside range: {', '.join(gaps) if gaps else 'none'}.", "",
            "累计克隆仅覆盖保存的日期，不代表仓库上线以来的全部下载。最早窗口边界日和当天不纳入日累计；缺失日期不当作零。",
            "Historical clones before collection are unknown. The oldest boundary day and current day are excluded from the daily archive; missing dates are not zero.", "",
            "独立克隆者只展示 GitHub 最近窗口口径，不能逐日相加当作累计用户；克隆可能来自自动化。",
            "Unique cloners are the latest GitHub window value, never summed across days. Clones may include automation.", "",
            "ZIP 数字是已观测发布附件的累计计数，不能每天相加；被删除附件仅保留最后一次观测值。校验文件不算安装包。",
            "ZIP counts use each observed asset's cumulative counter, retaining the last observed value for deleted assets. Checksums are excluded.", "",
            "不统计使用次数；不包含源码 ZIP、Raw 文件、复制粘贴或未提供统计的第三方分发。克隆与 ZIP 不合并为用户数。",
            "No usage tracking. Source archives, raw files, copy/paste and unreported third-party distribution are not counted. Clones and ZIP downloads are not unique users.", "",
            "## 发布附件 / Release assets", "", "| Asset ID | File | Downloads | Present |",
            "| --- | --- | ---: | --- |"]
    for asset_id, a in sorted(state["assets"].items()):
        name = a["name"].replace("|", "\\|").replace("\n", " ")
        rows.append(f"| {asset_id} | {name} | {a['count']} | {a['present_in_latest_release_scan']} |")
    return "\n".join(rows) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "stats")
    args = parser.parse_args()
    state_path = args.output_dir / "history.json"
    previous = json.loads(state_path.read_text()) if state_path.exists() else None
    # Fetch all endpoints before writing anything. Authentication/API failure is not zero.
    clones = api(f"repos/{REPO}/traffic/clones")
    releases = api(f"repos/{REPO}/releases?per_page=100", paginate=True)
    state = merge(previous, clones, releases, datetime.now(timezone.utc))
    rendered = report(state)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    temporary = state_path.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(state_path)
    (args.output_dir / "README.md").write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
