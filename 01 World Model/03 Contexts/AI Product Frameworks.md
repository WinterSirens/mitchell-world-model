---
type: situation
updated: 2026-04-27
purpose: Reusable AI product decision frameworks from professional knowledge base
source: Notion > Areas > Product (Archived)
note: These are studied and internalized frameworks, not active project work
---
## What this file is
Reference frameworks for AI product decisions. Use these when evaluating trade-offs in course design, lead magnet architecture, or any AI product you're building or advising on. These also inform your credibility and teaching depth for the SHIFT Gear System.

---

## AI PM Trade-offs Decision Framework

### Core Principle
User experience is sacred. Only trade it off when you know what you're doing and have a clear rationale. The difference between a deliberate bet and hoping for the best is intentionality.

### Decision Checklist (use when facing any AI product trade-off)
1. Am I trading off on UX? If yes, do I know exactly why?
2. What will I learn from this trade-off in the long term?
3. Is this learning material to improving the experience later?
4. What's the time horizon before I can reverse or improve this?
5. If I'm wrong about the learning, what's the impact on users?
6. Is this a "know what I'm doing" moment, or am I guessing?

### Seven Common Trade-offs
- **Accuracy vs. Speed** — How real-time must the output be? Trading off accuracy heavily just to be fast rarely builds user trust.
- **Complexity vs. Simplicity** — Can you afford to own this black box? Simpler is often better if it works.
- **Data Quality vs. Quantity** — More data doesn't solve dirty data. Garbage in, garbage out.
- **Generalization vs. Specificity** — Build separate specialized models when one general model would sacrifice user experience.
- **Privacy vs. Personalization** — Collect only what you need. Trust matters more than a 2% improvement.
- **Ethics vs. Business Goals** — Ethics is a long-term business decision, not optional.
- **Explainability vs. Performance** — Do users or regulators need to understand why? Answer before choosing a black box.

---

## Eval Framework (QA System for Probabilistic AI Outputs)

### Three Components
- **Golden Queries** — 10-100 realistic user inputs that represent actual use cases
- **Quality Rubric** — 4-5 measurable dimensions that define what "good" looks like
- **Measurement System** — Automated + human validation working together

### Key Insight
Build the eval set before writing a single line of prompt code. The eval set tells you where to point the product.

### Types of Evals
| Type | Cost | Speed | When |
|---|---|---|---|
| Automated | Near zero | Instant | Every build/commit |
| AI Judge | ~$0.01/eval | Minutes | Weekly monitoring, A/B tests |
| Human | ~$1/eval | Days | Pre-launch, major changes |
| Agent Evals | $0.05-$1/eval | Hours | Multi-step agent flows |

**Target:** 80%+ correlation between AI judge and human evaluators.

### Agentic Failure Modes (test for these in evals)
- **Compound Error** — Error in step N corrupts step N+1
- **Premature Commitment** — Acts before full context
- **Hallucinated Tool Use** — Calls tool with wrong parameters
- **Infinite Loop** — Retries failed action forever
- **Scope Creep** — Does more than asked

> For anything you cannot afford to get wrong even 1% of the time, use hooks not prompts. Programmatic enforcement provides deterministic guarantees. Prompt-based instructions have a non-zero failure rate.

---

## Foundational Model Strategy (added 2026-04-27)
### Core principle
Don't engineer functions a foundation model is likely to subsume in 6 months. When the gap between today's model capability and the desired product behavior is small and trending closed, default to wait, not build.
### Decision check
- Is the function I'm about to build something a base model already does at 70-80%, with the gap closing?
- If yes: defer building the workaround. Re-evaluate in 6 months.
- If no, or the gap is structural (privacy, determinism, integration, evals, domain data): build now — this is product surface, not model surface.
### Why this matters for SHIFT
- This rule keeps the course honest: "systems over tools" doesn't mean "build infrastructure for problems the model will solve for free next quarter."
- It also informs Gear progression — some workflows shouldn't be moved up the gears at all if the model is about to make the prior gear obsolete.
### Source
AI PM Bootcamp — productization session, 2026-04-24. See `03 Sources/Meetings/2026-04-24 AI PM Bootcamp — Productization.md`.
## Relevance to PLF Course
These frameworks are credential-level knowledge that separates the SHIFT Gear System from generic "AI tips" content. The eval framework maps directly to the T (Telemetry) step of SHIFT. The trade-offs framework maps directly to Gear 3-6 decisions (when to delegate, automate, or go autonomous). The foundational model strategy informs which workflows are worth automating at all. Use these to add depth to course modules and to answer sharp questions from the Stuck Implementer's more advanced segment.

---

## Notion Source
- [Product Page](https://www.notion.so/68c7f0bf036243a5bfaef0e2ae098841) (Archived)
- [AI PM Trade-offs Decision Framework](https://www.notion.so/32c078c0111881d9a786c59b95ee6600)
- [What Is an Eval?](https://www.notion.so/330078c0111881d9bf3ff39ece533f06)
