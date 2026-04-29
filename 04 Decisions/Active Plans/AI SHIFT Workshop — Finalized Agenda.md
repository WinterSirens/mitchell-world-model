---
type: active-plan
created: 2026-04-27
updated: 2026-04-28
purpose: Finalized 3-hour workshop agenda with facilitation notes — ready to run on Maven
status: ready for review — demo task TBD pending Marily's input
---

# AI SHIFT Workshop — Finalized Agenda with Facilitation Notes

**Workshop title:** Build Your First Reliable AI Workflow in 3 Hours
**Format:** Live Maven workshop | 3 hours | Hands-on build session
**Running demo (wedge workflow):** TBD — candidates below. Marily's input needed to pick the task that resonates most with her audience.

---

## Choosing the live demo — Marily's input needed

The workshop needs a single recurring task that Mitchell builds live while students build their own in parallel. The task has to meet the wedge criteria (frequency ≥ weekly, currently 30+ min, output is document/text/analysis) AND resonate with Marily's audience specifically.

**Candidate 1: LinkedIn/content creation (voice/word vomit → polished posts)**
- Strengths: Universal pain point, AI failure is obvious (generic voice, clichés), visceral before/after, teaches Harvest especially well, already built and documented
- Risk: Not everyone in Marily's audience creates content — PMs and operators may find it tangential to their actual work

**Candidate 2: Weekly status reports / update emails**
- Common across PMs, operators, managers — nearly everyone writes them
- AI failure point: generic summaries, misses the point, over-formatted, doesn't highlight the right things

**Candidate 3: Meeting notes → action items + follow-up emails**
- Universal task, recurring, currently manual and time-consuming
- AI failure point: hallucinated action items, lost nuance, wrong priority order

**Candidate 4: Research briefs / competitive analysis summaries**
- More specialized but high-value for PM/strategy audience
- AI failure point: fabricated sources, shallow synthesis, generic takeaways

**Candidate 5: Client-facing deliverables (proposals, recaps, strategy docs)**
- High-stakes output where AI failure is most painful
- AI failure point: wrong tone for the client, missed requirements, generic language

**Decision needed from Marily:** What recurring task does your audience already struggle with when using AI? The one that makes them say "I just can't get it to sound right" or "it saves me nothing" — that's the one we demo.

Once the wedge is chosen, the same workflow goes into the lead magnet video. Build once, deploy in two places.

---

## Pre-workshop logistics

**Materials to prepare and distribute at session start (drop links in chat):**
1. Workflow Candidate Scorecard (fillable Google Doc)
2. Workflow Brief template
3. Context Pack template
4. Failure Map + Test Set template
5. 7-Day SHIFT Plan template
6. Mitchell's live demo workflow as a pre-filled reference for each template (students see the output before they build their own)

**Default task for stuck students:** If a student cannot pick a task by 0:35, point them to the demo task. "Build alongside my demo — you can swap to your own task after." This prevents them from falling behind during the build sections.

**Platform setup:** Screen share ready for live demo. Zoom Chat for polls and commitment prompts. Have Claude (or ChatGPT) open and a Claude Project pre-configured with the demo workflow loaded — don't set it up live, it burns time.

**Facilitation principle:** Students spend at least 60% of the time building, not watching. Each demo is 5–8 minutes. The remainder of each section is student work time.

---

## Agenda

### 0:00–0:15 — Why AI Still Feels Like More Work (15 min)

**Goal:** Establish the frame. Redefine the problem from "tool problem" to "handoff problem."

**Facilitation notes:**

Open with a chat prompt, not a monologue: *"What's one task where AI gave you output that was almost right but you couldn't actually use it? Drop it in chat."* Let 4–5 answers surface. Read 2–3 aloud. This does three things: warms the room, confirms the premise, and makes students feel seen immediately.

Deliver the thesis: *"Look at what just came in. These aren't tool problems. They're all the same problem: the handoff. You gave AI a task. AI produced something. The gap between what you gave it and what it needed is where everything went wrong. That's what we're fixing today."*

Introduce the through-line: *"For the next 3 hours, I'm going to build a workflow live — taking a messy recurring task from raw input to reliable output. You're going to build one for the task you bring today. By the end, you'll have a handoff system that works in any tool."*

One visual: a simple before/after of a messy input → polished output. Don't explain it yet. Let it land.

**Keep this section tight.** The frame is simple. Resist adding examples or backstory. Get to building as fast as possible.

**Output:** Shared frame. *"Tools change. The handoff stays."*

---

### 0:15–0:35 — Pick the Right Workflow (20 min)

**Goal:** Students commit to one specific recurring task. They score it, pick it, say it out loud, and lock it in for the session.

**Facilitation notes:**

Drop the Workflow Candidate Scorecard link in chat. Students list 2–3 recurring tasks they actually do. Score each against the wedge criteria:

- **Frequency:** Does this happen at least weekly?
- **Time cost:** Does it currently take 30+ minutes?
- **Output type:** Does it produce a document, text, analysis, or structured artifact?
- **Ownership:** Is this something you already do — not a new idea?

**Mitchell's demo:** "Here's how my demo task scored." Walk through the scorecard live — fast, 2 minutes. Score it on all four criteria. Commit.

**Common mistakes to redirect:**
- Task too big: "My entire client onboarding workflow." → "What's the one document or deliverable inside that workflow? Start there."
- Task too vague: "Write better emails." → "Which emails? Weekly client updates? Cold outreach? Pick one specific output."
- Task not yet recurring: "I want to start writing proposals." → "That's great — pick something you already do, not something you want to do. You need real inputs to test with."

**Commitment prompt (Zoom Chat):** *"What task did you pick? One sentence, in chat now."* Read 3–4 aloud. This gets people off the fence and surfaces anyone who needs the default.

**Time flag:** If a student still can't commit by 0:30, give them the default: "Use the demo task I'm building. Swap to yours after if you want." Don't let anyone stall the group.

**Student output:** Workflow Candidate Scorecard — one task scored and selected

---

### 0:35–1:05 — S: Specify the Output (30 min)

**Goal:** Students write a Workflow Brief — a precise definition of what AI should produce, who it's for, what done looks like, and what done does not look like.

**Facilitation notes:**

Open with the key insight: *"Most people give AI vague instructions because they haven't decided what they want yet. This step is not prompting. It's deciding — for yourself — what the output actually needs to be."*

**Mitchell's Workflow Brief, built live (5–7 min):**

[Filled in once the demo task is chosen. The brief will define: what the output is, who it's for, what format it takes, what "done" means, and what "not done" means. The done/not-done distinction is the most useful part of the brief — emphasize it. Students often skip it.]

Students build their own Workflow Brief in parallel. Give 15–18 minutes.

**Facilitation move at 0:55:** Check the room. "Who has a clear 'done means' statement?" Ask 2–3 people to share. Redirect anyone who's still vague: the brief doesn't need to be perfect, it needs to be specific enough to feed the next step.

**Rabbit hole warning:** Students sometimes want to perfect the output spec before moving on. Set the expectation: *"This is v1. It will get better after we build the context pack and run the first test. Specific and imperfect beats vague and polished."*

**Student output:** Workflow Brief — filled out for their task

**Key teaching point:** Specify is not prompting. It's making a decision before you involve AI.

---

### 1:05–1:35 — H: Harvest the Context (30 min)

**Goal:** Students build a Context Pack — the reusable material that stops AI from producing generic output.

**Facilitation notes:**

This is where the biggest insight usually lands. Frame it: *"The reason AI sounds generic is not because AI is bad at writing. It's because you haven't given it the raw material it needs to sound like you. The Context Pack is that material — and once you build it, you use it every time."*

**Mitchell's Context Pack, built live (6–8 min):**

[Filled in once the demo task is chosen. The Context Pack will include: best examples (3 that worked), worst examples (2 that didn't), style rules (5–7 specific rules drawn from what makes AI go wrong for this task), source material (a genuinely messy real input — not cleaned up), and constraints (what AI must not do). The messiness of the source material demonstrates why this step matters.]

Students build their Context Pack for their task. Give 18–20 minutes.

**Reflection prompt at 1:25:** *"What does AI consistently get wrong for this task? Whatever it is — that's probably missing from your Context Pack."* Give 2 minutes for students to add it.

**Student output:** Context Pack — examples (best/worst), style rules, source material, constraints

**Key teaching point:** Context is not a longer prompt. It's a reusable package you hand to AI at the start of every run. You build it once and it compounds.

---

### 1:35–1:45 — Break (10 min)

Tell students to do two things during the break: (1) find one more example for their Context Pack, (2) think of one way the output could go wrong. This primes them for Inspect.

---

### 1:45–2:10 — I: Inspect for Gaps and Failure Modes (25 min)

**Goal:** Students map where their workflow will fail and build 3–5 test inputs to catch it.

**Facilitation notes:**

Frame: *"Before you run this in production, you need to know where it breaks. Not to fix everything today — but to know what to watch. A failure you've mapped is manageable. A failure that surprises you in front of a client is not."*

**Mitchell's Failure Map, shown live (4–5 min):**

[Filled in once the demo task is chosen. The Failure Map will list 5–6 specific ways AI gets the output wrong for this task — hallucination, over-formatting, generic language, losing the original point, sanitizing the voice, wrong person/tone. These should be drawn from real experience running the workflow, not hypothetical.]

**Test Set:** 3–5 real inputs to validate the workflow before relying on it. Show what each type tests:

- **Easy input:** A clean, well-structured real input — AI should handle this well on the first pass
- **Messy input:** A real input with tangents, missing pieces, or unclear structure — the kind of thing that actually shows up in practice
- **Edge case:** An input that stresses the workflow — too short, too personal, too opinionated, or too ambiguous

Students map failure modes and write 3 test inputs for their own task (18–20 min).

**Facilitation move:** Ask students to share one failure mode in chat. Read 4–5. "Notice what's happening — these aren't random failures. They're patterns. And most of them are fixable in H (Harvest) by adding a constraint or a better example."

**Student output:** Failure Map + Test Set (3–5 real inputs)

**Key teaching point:** Inspection is not about eliminating all failure. It's about knowing which failures are acceptable and which are showstoppers — before you're in a situation where it matters.

---

### 2:10–2:40 — F: Feed and Test (30 min)

**Goal:** Students run their workflow with real inputs, see what breaks, and make their first refinement.

**Facilitation notes:**

This is the hands-on peak. Students have a Brief, a Context Pack, and a Test Set. Now they build.

**Mitchell's live demo (8–10 min):**

1. Feed the **easy input** — show the raw input, paste it into the configured AI tool, show the output. Evaluate aloud: "Would I use this? What's off?" Name the specific gap.
2. Feed the **messy input** — show what breaks. AI produces output that misses the point or distorts the voice. This is a Harvest problem: the system needs a rule about what to prioritize when the input is unclear. Add it. Run again.
3. Feed the **edge case** — show how the refined handoff handles the same problem better. It's not perfect. That's fine. "Version 1 is supposed to be better than what you had. Not finished."

Students run their own Test Set. Give 15–18 minutes.

**While students work:** Mitchell is available for live troubleshooting. Common fixes:
- Output is generic → Check H (Harvest): are the examples strong enough? Are the style rules specific enough?
- AI ignores the constraints → Move them to the top of the instruction set
- Output structure is wrong → Go back to S (Specify): the format wasn't clear enough
- AI keeps writing the wrong kind of content → The Brief needs a sharper "not done means" statement

**Facilitation move:** With 5 minutes left, ask: "What's one thing you changed in your handoff based on the test?" This surfaces the pattern-matching they're doing and names it as methodology, not troubleshooting.

**Student output:** Reusable AI Handoff v1 — prompt, Claude Project, Custom GPT, or structured instruction set in whatever tool they're using

**Key teaching point:** Feed is not prompting until something works. It's running a structured test, observing what breaks, and updating the handoff based on evidence.

---

### 2:40–2:55 — T: Telemetry and the Gear Roadmap (15 min)

**Goal:** Students leave with a 7-Day SHIFT Plan and a clear picture of where this goes.

**Facilitation notes:**

Keep Telemetry practical and brief. This is not a metrics lecture. It's the answer to "okay, I have a handoff — now what?"

**Mitchell's Telemetry, shown simply (3–4 min):**

- **What I watch:** Time spent reviewing vs. regenerating (more time reviewing = system is working). Quality of output on the first pass. When I stop editing the output — that's the signal the system has calibrated.
- **When I iterate:** If I'm editing the output on most runs, something is wrong in H (Harvest) — probably a missing example or a style rule that isn't specific enough.
- **7-Day Plan:** Run the workflow on 3 real inputs this week. Log one thing you changed after each run. One refinement per run, not five. The goal is a handoff that improves incrementally, not one that's rebuilt every time.

**Gear preview — show visually, keep brief (5 min):**

1. **Manual** — AI assists at the margins (what most people are doing now)
2. **Collaborator** — AI works alongside you in a Claude Project or shared workspace
3. **Delegator** — AI drafts, you review and approve
4. **Automated** — The process runs on a schedule without you starting it
5. **Autonomous (human in loop)** — AI executes, you approve before it ships
6. **Autonomous (human on loop)** — AI ships, you monitor metrics and intervene on exceptions

"Today you built Gear 1–2 on one task. The full course reveals how to climb the gears across any workflow you care about — including taking what we built today all the way to Gear 4 or 5."

**Don't sell the course here.** Seed the curiosity. *"The next version of this system runs automatically. I don't even need to start it. That's what climbing the gears looks like. I'll show you exactly how in the course."* Leave it there.

**Student output:** 7-Day SHIFT Plan

---

### 2:55–3:00 — Close (5 min)

**Facilitation notes:**

Recap the transformation arc — don't read the list, just say it conversationally: *"You came in with a task you've been trying to make AI do reliably. You're leaving with a workflow brief, context pack, failure map, test set, a reusable handoff, and a 7-day plan. That's not a better prompt. That's a system."*

Repeat the thesis one more time: *"You don't need to keep up with every tool. You need a repeatable way to turn work into AI-ready workflows. That's what SHIFT gives you."*

**CTAs — in this order, not all at once:**

1. **Newsletter** — drop the link in chat. *"Weekly system-building content — not tool reviews. If today felt useful, this is where the rest goes."*
2. **Deeper course waitlist** — *"The full Gear System. How to take any task from Gear 1 to Gear 6. Waitlist is open — link in chat."*
3. **Workflow teardown submissions** — *"Send me your AI Handoff v1 after today. I'll review submissions and share patterns in the newsletter — anonymized unless you want credit."* This extends the relationship and generates content.

---

## Timing risk notes

- **Most likely overrun:** H (Harvest) and F (Feed and Test). Students slow down when building context packs and when running live tests. If running long, compress T (Telemetry) to 10 minutes and cut the Gear preview to a single slide.
- **Most likely underrun:** The frame section (0:00–0:15) if the room is already warmed up and engaged. Bank those minutes into S (Specify) if students need more time on their Workflow Brief.
- **Buffer:** The break is the safety valve. If ahead of schedule, give the break early and use the extra time in Feed. If behind, cut the break to 7 minutes.
