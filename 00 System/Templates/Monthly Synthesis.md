---
type: template
use: Monthly synthesis session — open this and say "let's do the monthly synthesis" to start
cadence: First week of each month (or whenever a month boundary passes)
---
## How to use this template
Open a new session and say: "let's do the monthly synthesis."
Claude runs the scripts, reviews the output, walks through the agenda below, and proposes updates. You approve or adjust each section. Target: 30-45 minutes.

---

## Monthly Synthesis Agenda

### 0. Pre-work (Claude runs automatically)
Before asking any questions, Claude runs these scripts and reads the output:

1. `00 System/scripts/brief-patterns.sh --last 4` — longitudinal pattern analysis across the month's briefs
2. `00 System/scripts/linkedin-performance-scaffold.sh --analyze` — cross-month LinkedIn performance report

Claude also reads:
- `01 World Model/01 State/Current State.md`
- `01 World Model/02 Rules/Decision Rules.md`
- All files in `01 World Model/03 Contexts/`
- All files in `04 Decisions/Active Plans/`

### 1. Energy and momentum review
Using the brief-patterns output:
- What's the energy trajectory across the month? (rising, falling, flat)
- Is the bottleneck shifting or stuck on the same thing?
- What avoidance patterns persisted all month?
- Surface any "planned vs actual" gaps — are outlooks consistently over-optimistic?

### 2. Prediction calibration
Review the month's prediction scorecards from weekly briefs:
- How many predictions were scored? What was the hit rate?
- Are predictions getting more or less accurate over time?
- Any systematic bias? (e.g., consistently over-optimistic about self-directed work, accurate about externally structured work)
- If fewer than 4 scored predictions exist this month, note it and move on — the calibration loop is still warming up.

### 3. Rule health audit
Walk through every rule in `Decision Rules.md`:
- **Which rules were tested this month?** (actively used in a real decision)
- **Which rules should graduate from provisional to durable?** (3+ confirming instances across briefs)
- **Which rules feel wrong, stale, or unhelpful?** (no evidence, or evidence against)
- **Are any new rules needed** based on patterns the briefs surfaced?

Propose specific updates to `Decision Rules.md` with the standard changelog format.

### 4. Context playbook audit
For each file in `01 World Model/03 Contexts/`:
- Is the `updated:` date more than 30 days old? If yes, flag for refresh.
- Does the playbook still reflect current reality?

Also ask: **Are there recurring decision contexts that don't have a playbook yet?** Check the briefs — if a topic came up in 3+ weekly briefs without a playbook, propose creating one.

### 5. Active plan staleness check
For each file in `04 Decisions/Active Plans/`:
- Is the `updated:` date more than 21 days old?
- Does the `status:` reflect reality, or has the plan been implicitly shelved?
- Propose: update the plan, explicitly mark it `on-hold`, or archive it.

### 6. LinkedIn performance review → skill update
Using the `linkedin-performance-scaffold.sh --analyze` output:
- Review per-pillar performance trends
- Review the "Proposed skill updates" section from performance logs
- Decide which proposed updates to apply to `.claude/skills/linkedin-creator/SKILL.md`
- Update the skill's "Current Performance Lessons" section with fresh data
- If no performance log exists for the current month, scaffold it:
  `00 System/scripts/linkedin-performance-scaffold.sh`

### 7. Wiki and knowledge audit (brief)
Quick checks:
- Are there distilled concepts in weekly briefs that should be standalone Wiki notes? (especially Themes)
- Are there People who appear in every brief but have no `02 Wiki/People/` note?
- Any sources worth preserving that were archived without re-retrieval consideration?

### 8. Priority recalibration
Based on everything above:
- Are the priorities in `Current State.md` still in the right order?
- Has anything emerged this month that should be elevated or dropped?
- Is the bottleneck statement still accurate?
- Propose specific updates to `Current State.md` if needed.

### 9. System health check
Answer these:
- Did the weekly synthesis run every week this month? (check brief dates for gaps)
- Is the inbox staying empty between syntheses?
- Did the system help with any real decisions this month, or was it just maintenance?
- What felt like friction — too heavy, too rigid, or missing something?
- Are any skills underperforming or unused?

### 10. Close
- Apply all approved updates (rules, state, contexts, plans, skill)
- Note what got smarter this month (1-3 sentences)
- Propose any `AGENTS.md` updates if the system itself needs to change
- Scaffold next month's LinkedIn performance log if it doesn't exist

---

## Signals the monthly synthesis is working
- Rules are graduating from provisional to durable (evidence accumulating)
- Stale plans get caught and either updated or archived
- LinkedIn skill improves based on real performance data
- Prediction accuracy improves over time
- The monthly session surfaces something the weekly sessions missed

## Signals it's drifting
- Monthly synthesis keeps getting skipped or delayed
- Rule audit finds no changes (rules aren't being tested)
- Active plans stay stale for 2+ months
- LinkedIn performance loop is broken (no logs, no skill updates)
- Predictions aren't being scored (calibration loop dead)
