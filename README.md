# Anti-Defensive Writing · 学术写作原则

**阻止论文的防御性写作 —— 一个轻量级、零依赖的 AI 写作助手 Skill + 提示词，复制即用**

[English README](README_EN.md) · [中文 Skill](skills/anti-defensive-writing/SKILL.md) · [English Skill](skills/anti-defensive-writing-en/SKILL.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/pulls)

---

### Codex 插件安装

作者：**Adkid-Zephyr**。本仓库同时提供中文和英文 Skill。Codex 可以安装 Skill，也可以安装打包后的插件；仓库安装不等于官方插件目录已上架。

安装本仓库插件：

```bash
codex plugin marketplace add Adkid-Zephyr/anti-defensive-writing-Skill
codex plugin add anti-defensive-writing@adkid-zephyr-writing
```

安装后在新对话中选择 Anti-Defensive Writing 插件，并使用中文或英文 Skill 修改论文。

也可以把 [中文 Skill 链接](skills/anti-defensive-writing/SKILL.md) 交给 Codex，要求它安装这个 Skill。

插件发布包包含相同的两份 Skill，没有 MCP 服务或额外运行依赖。通过 `python3 scripts/build_plugin.py` 生成可上传到 OpenAI 发布后台的 ZIP；[隐私政策](PRIVACY.md)。官方目录发布状态以 OpenAI 后台为准，GitHub release 不是官方目录上架记录。

## 这是什么

很多人用 AI 改论文，改完越看越心虚：审稿人还没开口，自己先把「遗憾的是」「效果有限」「仍明显落后」写满了。结构是工作汇报式的，语言是自我审查式的——**等于提前把刀子递到审稿人手里，还附赠一份使用说明。**

这叫**防御性写作（Defensive Writing）**。

解药只有一条原则：

> **论文是一场学术发布会，不是项目总结。**
> 发布会只讲一件事：你最强的那个优势。

打不赢的指标不设为比赛，不占优的结果不说输，实验不是结果仓库、是论证工具。论文的说服力来自主张与证据高度一致，而不是比较项目最多。

## 效果对比

| | 防御性写作 | 发布会原则 |
|---|---|---|
| 劣势表述 | 虽然本方法在两个同领域数据集上提高了准确率，但必须承认，我们尚未测试跨领域泛化，因此应谨慎理解这些结果。 | 本方法在两个同领域数据集上提高了准确率；跨领域泛化尚未评估。 |
| 结构 | 我们首先尝试了 A，然后尝试了 B，最后选择了 C | 问题 X 很关键，现有方法缺 Y，本文提出 Z，证据如下 |
| 实验 | 附录式堆结果，全覆盖无重点 | 每个实验承担一个论证职责 |
| 结论 | 最后一段突然自我否定 | 只强化记忆点：解决了什么、证明了什么、为什么重要 |

## 快速开始

### 方式一：复制提示词（任何 AI 都能用）

直接复制 [`prompts/精简版提示词.txt`](prompts/精简版提示词.txt)（[English](prompts/quick-prompt-en.txt)），粘贴到你和 AI 的对话开头，然后发给它你的论文段落。复制即用，零门槛。

### 方式二：安装 Skill（Claude Code / Cursor / 其他 Agent 工具）

把对应语言的 skill 目录整个拷进你的 skills 目录即可：

```bash
# 中文版
cp -r skills/anti-defensive-writing ~/.claude/skills/

# English version
cp -r skills/anti-defensive-writing-en ~/.claude/skills/
```

之后对 AI 说「帮我改改这段论文」「润色一下 abstract」，它会自动按发布会原则工作。

## 十二条规则速览

- **叙事**：只围绕优势组织 · 不写工作汇报 · 打不过的维度不设为比赛 · 优势必须明说 · 控制比较范围 · 允许彻底重构故事
- **语言**：禁用自我削弱表达 · 不占优的结果不说输 · 不把局部现象上升为对整体方法的否定
- **实验**：每个实验必须有论证职责
- **结构**：摘要引言 = 发布会开场 · 结论只强化记忆点

完整规则与决策流程见 [SKILL.md](skills/anti-defensive-writing/SKILL.md)。

## 仓库结构

```
anti-defensive-writing/
├── skills/
│   ├── anti-defensive-writing/      # 中文 Skill
│   └── anti-defensive-writing-en/   # English Skill
├── prompts/
│   ├── 精简版提示词.txt           # 中文精简提示词(复制即用)
│   └── quick-prompt-en.txt       # English quick prompt
└── README.md / README_EN.md
```

## 适用场景

- 写/改论文摘要、引言、结论
- 压缩论文篇幅（砍哪段，这里给了决策优先级）
- 组织实验章节（每个实验该承担什么职责）
- 写 rebuttal 前的自查（不给审稿人递刀子清单）

## License

MIT。欢迎 PR，欢迎转发给你的同门。
