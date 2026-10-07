# Anti-Defensive Writing

**Stop defensive writing in academic papers — a lightweight, zero-dependency Skill + prompt pack for AI writing assistants. Copy and go.**

[中文 README](README.md) · [English Skill](skills/anti-defensive-writing-en/SKILL.md) · [中文 Skill](skills/anti-defensive-writing/SKILL.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/pulls)

---

### Install as a Codex plugin

Publisher: **Adkid-Zephyr**. This repository includes Chinese and English skills. A repository-installed plugin is separate from a published listing in the official plugin directory.

```bash
codex plugin marketplace add Adkid-Zephyr/anti-defensive-writing-Skill
codex plugin add anti-defensive-writing@adkid-zephyr-writing
```

After installation, start a new conversation, select Anti-Defensive Writing, and use its Chinese or English skill to revise your paper. You can also give Codex the [Chinese skill URL](skills/anti-defensive-writing/SKILL.md) or [English skill URL](skills/anti-defensive-writing-en/SKILL.md) and ask it to install the skill.

The plugin bundles the same two skills and has no MCP server or extra runtime dependencies. Run `python3 scripts/build_plugin.py` to build the ZIP for OpenAI submission. See the [privacy policy](PRIVACY.md). Official directory publication is determined by the OpenAI dashboard; a GitHub release is not an official directory listing.

## What is this

Many people use AI to polish their papers and end up with something that reads like a self-audit: before the reviewer says a word, the text is already full of "unfortunately", "limited improvement", and "still lags behind". Work-report structure, self-censoring language — **it hands the reviewer a knife, with a user manual attached.**

This is **defensive writing**.

The antidote is one principle:

> **A paper is a press conference, not a project summary.**
> Build the main line around genuine strengths while retaining information needed to understand and test claims.

Identify self-undermining by meaning, not word matching: the examples above are not banned strings, and necessary negative experimental facts must remain. Comparison frames and trade-offs need evidence; do not present unevaluated matters as established, and narrow claims when evidence is insufficient. Experiments are tools of argument, not a warehouse of results. Persuasion comes from tight claim-evidence alignment, not from the number of comparisons.

## Before / After

| | Defensive writing | Press-release principle |
|---|---|---|
| Weakness framing | Although our method improves accuracy on two in-domain datasets, we must acknowledge that cross-domain generalization has not been tested, so these results should be interpreted cautiously. | Our method improves accuracy on two in-domain datasets; cross-domain generalization has not been evaluated. |
| Structure | We first tried A, then B, and finally chose C | Problem X matters, existing methods lack Y, we propose Z, evidence follows |
| Experiments | An appendix-style pile of results | Every experiment carries at least one duty, including defining boundaries or presenting key counterevidence |
| Conclusion | Sudden self-negation in the final paragraph | Reinforces the takeaway only |

## Quick start

### Option 1: Copy the prompt (works with any AI)

Copy [`prompts/quick-prompt-en.txt`](prompts/quick-prompt-en.txt) ([中文](prompts/精简版提示词.txt)) and paste it at the start of your AI conversation, then send your paper draft. Copy and use, zero setup.

### Option 2: Install the Skill (Claude Code / Cursor / other agent tools)

Copy the skill folder of your preferred language into your skills directory:

```bash
# English
cp -r skills/anti-defensive-writing-en ~/.claude/skills/

# 中文版
cp -r skills/anti-defensive-writing ~/.claude/skills/
```

Then just ask "polish this paragraph" or "revise my abstract" — the agent applies the press-release principle automatically.

## Rules at a glance

- **Narrative**: organize around genuine strengths · use an argument chain, not work-report chronology · support comparison frames with evidence · state advantages explicitly · limit comparison scope
- **Language**: identify self-undermining by meaning · retain necessary facts · never turn a local observation into a verdict on the whole method
- **Experiments**: at least one argumentative duty per experiment, including applicable boundaries and key counterevidence; unfavorable results alone do not justify removal
- **Disclosure**: necessary facts, boundaries, key counterevidence, and explicit response obligations always remain; moving material preserves visibility and connection to claims
- **Structure**: establish the problem and contribution first in abstracts and introductions, with qualifiers alongside affected claims · reinforce the conclusion takeaway without expanding self-negation
- **Scope**: local revision preserves wording habits and paragraph structure, never rewrites whole paragraphs, and leaves problem-free parts untouched; no whole-paper reordering without authorization, only restructuring recommendations beyond scope. Each experiment within the requested scope has an explicit duty; structural checks cover only paper parts within the requested scope, including any abstract, introduction, or conclusion the request includes, under applicable rules; flag unresolved issues

Full rules and decision flow in [SKILL.md](skills/anti-defensive-writing-en/SKILL.md).

## Repository structure

```
anti-defensive-writing/
├── skills/
│   ├── anti-defensive-writing/      # 中文 Skill
│   └── anti-defensive-writing-en/   # English Skill
├── prompts/
│   ├── 精简版提示词.txt           # 中文精简提示词
│   └── quick-prompt-en.txt       # English quick prompt (copy & paste)
└── README.md / README_EN.md
```

## Use cases

- Writing / revising abstracts, introductions, conclusions
- Cutting paper length (the decision rules tell you what to cut first)
- Organizing the experiments section
- Defensive-writing self-checks in rebuttals or reviewer responses; answer existing questions directly with evidence

This tool is neither a general-purpose guide to removing AI-sounding prose nor a complete rebuttal method.

## License

MIT. PRs welcome — and feel free to share it with your labmates.
