---
category: AI Strategy
tags: [AI, LLM, Benchmarking, Productivity, Automation, archived]
source: https://artificialanalysis.ai/
created: 2026-04-28
archived: 2026-04-29
processed_into:
  - 02 Wiki/Concepts/LLM Best Use Cases.md
---
**Trigger:** I'm always trying to find the best model out there to use for Warp. I want to update [[LLM Best Use Cases]] in warp page weekly using https://artificialanalysis.ai/ and a live list of the most recent Warp.dev models to compare to the https://artificialanalysis.ai/ page, which then updates the [[LLM Best Use Cases]]. 
> [!summary] Executive Summary
> As of late April 2026, the AI landscape is highly competitive. OpenAI's **GPT-5.5 (xhigh)** currently holds the highest intelligence score, while open-weights models like **gpt-oss-120B** dominate in sheer speed and cost-efficiency. This document synthesizes current benchmark data with a comprehensive use-case directory to help you route tasks to the most efficient and capable models.

---

## Part 1: State of the AI Market (Artificial Analysis Report)

Based on the Artificial Analysis index, the current frontier models balance trade-offs between pure reasoning intelligence, output speed, and token cost.

### 🧠 Intelligence Leaderboard
The Intelligence Index aggregates 10 rigorous evaluations (including GDPval-AA, SciCode, and GPQA Diamond). 
* **#1: GPT-5.5 (xhigh)** - Score: 60 (Leads in GDPval-AA, AA-LCR, and general knowledge/accuracy).
* **#2: Claude Opus 4.7 (max)** - Score: 57 
* **#3: Gemini 3.1 Pro Preview** - Score: 57 (Notably strong in Humanity's Last Exam, GPQA Diamond, and MMMU-Pro).
* **#4: GPT-5.4 (xhigh)** - Score: 57
* **#5: Kimi K2.6 & MiMo-V2.5-Pro** - Score: 54

### ⚡ Speed & Latency (Output Tokens per Second)
Open-weights and optimized models significantly outpace frontier proprietary models in generation speed.
1.  **gpt-oss-120B (high)**: 205 tokens/sec
2.  **NVIDIA Nemotron 3 Super**: 157 tokens/sec
3.  **Gemini 3.1 Pro Preview**: 120 tokens/sec
4.  **Grok 4.20 0309 v2**: 88 tokens/sec
5.  **GPT-5.4 (xhigh)**: 79 tokens/sec

### 💰 Cost Efficiency (USD per 1M Tokens)
Prices vary drastically depending on the model's compute requirements. Smaller and open-weights models offer the best budget-friendly performance.
* **Most Affordable:** gpt-oss-120B (high) at **$0.30** / 1M tokens.
* **Mid-Tier Value:** MiMo-V2.5-Pro ($1.50) and Kimi K2.6 ($1.70).
* **Premium Frontier:** Claude Opus 4.7 (max) at **$10.00** and GPT-5.5 (xhigh) at **$11.30**.

### 🎨 Image Generation Top Models
From the Image Arena ELO scores:
1.  **GPT Image 2 (high)** (ELO: 1334)
2.  **GPT Image 1.5 (high)** (ELO: 1272)
3.  **Nano Banana 2 (Gemini 3.1 Flash Image)** (ELO: 1261)

---

## Part 2: Model Selection & Use Case Directory
Reference [[LLM Best Use Cases]] and update. 

> [!tip] How to use this table
> Match your specific project needs (e.g., speed, budget, coding logic, massive context) to the ideal model variant below. 
