# 上游比较页交付核验

## 交付
- `docs/upstream-comparison.html`：保留原版美术，最小纠偏；一文两阅读路径，demo 先行。
- `docs/upstream-comparison-hero.png`：实际 Chromium 1280×1200 页首截图，当前 PNG 原字节内嵌 HTML。
- `docs/upstream-comparison-mobile.png`：实际 390×844 页首截图，内嵌之后生成。
- 旧 `docs/upstream-comparison-full.png` 删除：不让修订中间版全文截图误认最终版。最后几处收紧只涉及页首以外正文，hero/mobile 可见内容与最终文件一致。

## 来源与归属
完整阅读 HTML（仅过滤 base64 图片）及当前六入口、HEAD 对应六份原文。重新执行双仓库 `git ls-remote … refs/heads/main`：Adkid-Zephyr/main、toRolex origin/main、本地 HEAD 同为 `102c8b21acf5eda3a0aef3d9779a65db646c8980`。六入口合计 +212/−134，净增 78 行；blob 前缀逐一对 git 核实。

归属固定为：**上游至当前总差异，包含既有未提交修改和本系列修订；没有更早基线无法逐项归因。** 同 SHA 仅排除已提交领先差异，不排除既有未提交修改。

`/tmp/anti-defensive-baseline.rHmfy2` 是 2026-10-01 16:14Z 系列中期同步前快照；此时两版 skill 已修订，四个其他入口仍等于 HEAD，不是整个会话前基线。`/tmp/arena-sync-final.V9tZRv` 是 16:32Z Arena 定稿合并前快照。二者差异结合保留的 Arena 16:35Z 交付记录，可确证后两轮同步及合并；不能据此归因最初所有改动。

Arena 真正结论：保留 Sol 主体；采纳 Grok 请求范围验收、K3 两版提示词负面判断证据边界。K3 残留词形禁令/不说输、独立删除实验指令及同步遗漏，因此未整体替换。删除七级、改 LICENSE/badge 等只标「本轮明确不采用的方向（并非真实候选）」，不冒充真实提案历史。

## 内容纠偏
- demo 按钮、JS、静态对照统一标「说明性风险推演，不是上游规则实测输出」；上游 README 本身已保留未评估边界。原文不再将未测试事实划删除线。
- 不声称上游默认不利实验是噪音，或允许逃避已提出审稿问题；仅描述真实条文和未明确约束的歧义。
- 移除无来源的中文定稿翻译过程描述，改双语静态核对。
- 修复自查七条被误称删除、中文 skill 净增长错误、结构原文不变等说法。中文 94→118 行，英文 123→167 行。
- 旧 data URI 标 PNG、字节实为 JPEG；现只内嵌当前真 PNG：签名 `89504e470d0a1a0a`，1280×1200，297760 bytes。

## 实际验证
通过 ego-browser / Chromium：
- 桌面 1280×1200，逐个点击三按钮；各状态内容、唯一 aria-pressed 正确；原句只有两处语气删除线，未测试事实保留。
- 专家目录锚点正常跳转。
- 390×844：整页 scrollWidth=390，无整体横向溢出，对照单列。
- 禁用 JS 重载：七个正文节与静态 demo 保留；最终内嵌图加载成功，naturalWidth=1280、naturalHeight=1200。
- Network 离线状态，本地文件可重载、按钮可用；资源属性无外链。
- 打印媒体：目录与按钮隐藏，静态示例与七节保留；实际 CDP 输出 PDF 至 `/tmp/upstream-comparison-final-print.pdf`，2424915 bytes。未做打印机实测、逐页版式审查。
- HTML LSP 诊断零项；`git diff --check` 通过。
- 浏览器 TaskSpace 已完成关闭。最后仅收紧页首外文案、删除旧 full；未再次整页浏览器渲染，不影响已验收交互、布局 CSS 或截图可见页首。

六入口最终 SHA-256 与本子任务读取时一致；没有修改源文件、其他仓库文件、remotes、branch、index，未提交。仅写 HTML、hero/mobile 和本交付记录，删除旧 full。

## 未验证
模型改写效果、误删率、过度保留风险、双语运行等效性和触发准确率都未做模型对照。既有未提交修改的逐项作者归属不可证明。页面示例不能证明上游模型会误删，也不能证明当前规则改善效果。
