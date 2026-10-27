import importlib.util
from datetime import datetime, timezone
from pathlib import Path
import unittest
from unittest.mock import patch
import tempfile
import subprocess

spec = importlib.util.spec_from_file_location("stats", Path(__file__).resolve().parents[1] / "scripts/collect_stats.py")
stats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats)
NOW = datetime(2026, 10, 27, 12, tzinfo=timezone.utc)


def traffic(day="2026-10-26", count=10):
    return {"count": count, "uniques": 3, "clones": [
        {"timestamp": day + "T00:00:00Z", "count": count, "uniques": 3}]}


def releases(count=290, asset_id=1, name="anti-defensive-writing-1.0.0.zip"):
    return [{"draft": False, "tag_name": "v1", "assets": [
        {"id": asset_id, "name": name, "download_count": count,
         "browser_download_url": "https://example.com/package.zip"}]}]


class StatisticsTests(unittest.TestCase):
    def test_overlap_replaces_counts_including_downward_corrections(self):
        state = stats.merge(None, traffic(), releases(), NOW)
        self.assertEqual(stats.merge(state, traffic(), releases(), NOW), state)
        state = stats.merge(state, traffic(count=8), releases(300), NOW)
        self.assertEqual(sum(d["count"] for d in state["clone_days"].values()), 8)
        self.assertEqual(state["assets"]["1"]["count"], 300)

    def test_old_days_retained_and_missing_days_not_zero_filled(self):
        state = stats.merge(None, traffic("2026-10-20"), [], NOW)
        state = stats.merge(state, traffic("2026-10-22"), [], NOW)
        self.assertEqual(stats.missing_days(state["clone_days"]), ["2026-10-21"])
        self.assertNotIn("2026-10-21", state["clone_days"])

    def test_partial_days_excluded(self):
        for day in ("2026-10-13", "2026-10-27"):
            self.assertFalse(stats.merge(None, traffic(day), [], NOW)["clone_days"])

    def test_deleted_and_replaced_assets_keep_separate_ids(self):
        state = stats.merge(None, traffic(), releases(), NOW)
        state = stats.merge(state, traffic(), releases(5, asset_id=2), NOW)
        self.assertFalse(state["assets"]["1"]["present_in_latest_release_scan"])
        self.assertEqual(sum(a["count"] for a in state["assets"].values()), 295)

    def test_checksums_excluded_and_uniques_not_added(self):
        state = stats.merge(None, traffic(), releases(name="SHA256SUMS"), NOW)
        self.assertFalse(state["assets"]["1"]["is_distribution"])
        self.assertIn("ZIP downloads | 0 |", stats.report(state))
        self.assertIn("Window unique cloners | 3 |", stats.report(state))

    def test_api_failure_preserves_saved_files(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "history.json"
            path.write_text("{}")
            with patch("sys.argv", ["collect_stats.py", "--output-dir", directory]), \
                 patch.object(stats, "api", side_effect=subprocess.CalledProcessError(1, "gh")):
                with self.assertRaises(subprocess.CalledProcessError):
                    stats.main()
            self.assertEqual(path.read_text(), "{}")

    def test_release_pagination(self):
        with patch.object(stats.subprocess, "run") as run:
            run.return_value.stdout = '[[{"id": 1}], [{"id": 2}]]'
            self.assertEqual(stats.api("releases", True), [{"id": 1}, {"id": 2}])
            self.assertIn("--paginate", run.call_args.args[0])


if __name__ == "__main__":
    unittest.main()
