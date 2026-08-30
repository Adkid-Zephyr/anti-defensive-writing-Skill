# Anti-Defensive Writing

**Stop defensive writing in academic papers — a lightweight, zero-dependency Skill + prompt pack for AI writing assistants. Copy and go.**

[中文 README](README.md) · [English Skill](skills/anti-defensive-writing-en/SKILL.md) · [中文 Skill](skills/anti-defensive-writing/SKILL.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

---

## What is this

Many people use AI to polish their papers and end up with something that reads like a self-audit: before the reviewer says a word, the text is already full of "unfortunately", "limited improvement", and "still lags behind". Work-report structure, self-censoring language — **it hands the reviewer a knife, with a user manual attached.**

This is **defensive writing**.

The antidote is one principle:

> **A paper is a press conference, not a project summary.**
> A press conference says exactly one thing: your strongest advantage.

Never set a contest you cannot win. Never say you lost. Experiments are tools of argument, not a warehouse of results. Persuasion comes from tight claim-evidence alignment, not from the number of comparisons.

## Before / After

| | Defensive writing | Press-release principle |
|---|---|---|
| Weakness framing | Unfortunately, our method only achieves limited gains on small datasets | Our method performs best in data-scarce settings, at 1/5 the training cost of the baseline |
| Structure | We first tried A, then B, and finally chose C | Problem X matters, existing methods lack Y, we propose Z, evidence follows |
| Experiments | An appendix-style pile of results | Every experiment carries one argumentative duty |
| Conclusion | Sudden self-negation in the final paragraph | Reinforces the takeaway only |

## Quick start

### Option 1: Copy the prompt (works with any AI)

Copy [`prompts/quick-prompt-en.txt`](prompts/quick-prompt-en.txt) ([中文](prompts/精简版提示词.txt)) and paste it at the start of your AI conversation, then send your paper draft. ~400 words, zero setup.

### Option 2: Install the Skill (Claude Code / Cursor / other agent tools)

Copy the skill folder of your preferred language into your skills directory:

```bash
# English
cp -r skills/anti-defensive-writing-en ~/.claude/skills/

# 中文版
cp -r skills/anti-defensive-writing ~/.claude/skills/
```

Then just ask "polish this paragraph" or "revise my abstract" — the agent applies the press-release principle automatically.

## The 12 rules at a glance

**Narrative**: organize around strengths only · no work-report chronology · never set a contest you can't win · state advantages explicitly · limit comparison scope · allow full story restructuring
**Language**: ban self-weakening phrases · never say you lost
**Experiments**: every experiment needs an argumentative duty
**Structure**: abstract & intro = press-conference opening · conclusion only reinforces the takeaway

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
- Pre-rebuttal self-check (the "don't hand the reviewer a knife" checklist)

## License

MIT. PRs welcome — and feel free to share it with your labmates.
