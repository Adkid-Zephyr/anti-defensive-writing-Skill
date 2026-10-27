# 下载与克隆累计

统计结果见 [统计页](../stats/README.md)，原始累计数据见 [history.json](../stats/history.json)。这是仓库维护工具，不会进入插件发布包，也不会在使用 Skill 时运行。

## 手动采集

需要 Python 3.9+、GitHub CLI，以及有权读取本仓库流量的 GitHub 登录态。在仓库根目录运行：

```sh
python3 scripts/collect_stats.py
python3 -m unittest discover -s tests -v
```

脚本只读取 GitHub API，并更新本地 stats/；不会自动提交、推送或修改账号。采集失败会报错，不会把失败记成零。

## 每日自动采集

`.github/workflows/statistics.yml` 合入默认分支后每天 08:23 UTC 运行，也支持 Actions 手动触发。

1. 为本仓库创建 fine-grained personal access token：只选择本仓库，授予 **Administration: Read-only**（读取流量需要）。不要在聊天、代码或日志中粘贴 token。
2. 在仓库 Settings → Secrets and variables → Actions 中添加名为 `TRAFFIC_TOKEN` 的 secret。
3. 允许工作流用 `GITHUB_TOKEN` 写入仓库内容；若默认分支禁止机器人推送，需要按仓库规则调整保存方式，不要为统计关闭保护。
4. 手动运行一次 `Archive download statistics`，确认成功并检查 stats/ 的更新。只有成功运行才表示自动采集已启用。

`TRAFFIC_TOKEN` 仅传给采集步骤；提交统计使用工作流的 `GITHUB_TOKEN`。当前工作流不会创建任何访问令牌。公共仓库长时间无活动可能暂停 schedule；留意 Actions 状态及统计页的最后更新时间，凭据到期也会中断采集。

## 口径与历史边界

- GitHub 克隆接口只返回最近 14 天。按 UTC 日期覆盖更新，重叠窗口不相加，允许 GitHub 修正旧计数。跳过当天及最老窗口边界日，避免把不完整日期计入日累计。
- 保留已经采集的旧日期。缺失日期标为缺失，不补零，也不根据日均量推算历史。采集停顿超过窗口可导致无法补回的断档。
- 最近窗口的独立克隆者来自 GitHub 原始汇总，不能跨日相加计算累计用户。自动化、自行测试和重复克隆可能计入次数。
- Release 附件用稳定 asset ID 保存其累计下载数，每日覆盖，绝不累加每日快照。被删除附件保留最后一次观测值（其后、删除前的下载可能遗漏）。替换上传使用新 ID。
- 只把 `anti-defensive-writing-*.zip` 计为发布包；SHA256SUMS 单独显示。已删除且从未观测的附件无法补回。
- GitHub 自动生成的源码 ZIP、Raw 文件、复制粘贴、第三方分发和 Skill 实际使用次数不在本统计中。克隆和发布包下载分开显示，不合成独立用户数。
- 仅保存 GitHub 汇总数字，不收集用户身份、论文、提示词或使用遥测。隐私政策关于插件的承诺不变。

接口依据：[GitHub Traffic API](https://docs.github.com/en/rest/metrics/traffic) 和 [Release assets API](https://docs.github.com/en/rest/releases/assets)。
