---
type: brain
created: 2026-04-27
updated: 2026-04-29
tags:
  - ai
  - llm
  - warp
  - model-routing
sources:
  - Warp docs — Model choice
  - Artificial Analysis — GPT-5.5 is the new leading AI model, 2026-04-23
  - Current Warp session — GPT-5.5 available, 2026-04-29
---
# LLM Best Use Cases

## Core rule
Route by task, not by model prestige. Default to the cheapest/fastest model that can reliably do the job, and escalate only when the task has high ambiguity, high consequence, large context, or difficult tool use.

## Warp defaults
- **Auto (Responsive)** — Use when you want Warp to balance speed and quality without thinking about model choice.
- **Auto (Cost-efficient)** — Use for cleanup, summarization, formatting, low-stakes drafts, and repeated tasks where cost matters.
- **Auto (Genius)** — Use for deep debugging, architecture, hard decisions, `/plan`-style work, and anything where picking the wrong model costs more than credits.

## Manual routing
- **Claude Opus 4.7** — Hardest coding, agentic workflows, multi-file refactors, architecture decisions, long-context repository work, and tasks where hallucination avoidance matters.
- **Claude Opus 4.7 high/max** — Use when normal Opus is not enough: deep debugging, messy legacy code, high-stakes synthesis, or huge-context analysis.
- **Claude Sonnet 4.6** — Everyday engineering default: feature work, API integrations, tests, code review, and reliable implementation without Opus-level cost.
- **Claude Haiku 4.5** — Fast, low-risk volume work: classification, simple summaries, extraction, formatting, and first-pass cleanup.
- **GPT-5.4 high/xhigh** — Research-heavy reasoning, web synthesis, strategy, complex analysis, and tasks where OpenAI-style persistence is useful.
- **GPT-5.4 low/medium** — Standard writing, PM analysis, quick reasoning, and general knowledge work.
- **GPT-5.5 high/xhigh** — Current frontier reasoning in Warp. Use for hardest strategy, synthesis, multi-step planning, complex research, and tool-heavy tasks where the extra intelligence matters.
- **GPT-5.5 low/medium** — Strong general reasoning tier. Use when you want better-than-5.4 quality without automatically jumping to maximum effort.
- **GPT-5.3 / GPT-5.2 Codex** — Coding throughput, parallelizable code tasks, scripts, tests, and when OpenAI Codex behavior fits the repo better.
- **Gemini 3.1 Pro** — Massive document ingestion, long-context research, multimodal analysis, and cost-sensitive synthesis across many files.
- **GLM 5 / Kimi K2.5** — Budget hosted models for lower-stakes long-context or bilingual work when frontier accuracy is not required.

## April 2026 benchmark watchlist
- Artificial Analysis ranks **GPT-5.5 (xhigh)** as the external intelligence leader at score 60, ahead of Claude Opus 4.7 (max), Gemini 3.1 Pro Preview, and GPT-5.4 (xhigh) at 57.
- GPT-5.5 is available in the current Warp session even though the docs checked on 2026-04-29 lagged behind the live product. Treat live model picker/session evidence as stronger than stale docs.
- GPT-5.5's headline score has a caveat: Artificial Analysis reports very high AA-Omniscience hallucination rate versus Claude Opus 4.7 and Gemini 3.1 Pro. For fact-sensitive work, prefer models that abstain rather than guess, and require citations/web checks.
- GPT-5.5 medium reportedly matches Claude Opus 4.7 max on the Intelligence Index at lower benchmark-run cost, so watch for it as a future high-value general reasoning tier.
- Kimi K2.6 and MiMo-V2.5-Pro are strong external value models, but they should not be added to the Warp routing table unless available in Warp.

## Weekly update procedure
1. Check Warp model picker/current session first, then docs. If docs conflict with live availability, trust live availability and note the conflict.
2. Check Artificial Analysis for external leaders, speed, context, and cost.
3. Update this note only with the decision-relevant delta: what to use, when to use it, and what caveat matters.
4. Archive the source clipping with `processed_into:`. Do not preserve raw benchmark dumps unless the methodology itself needs re-reading.
