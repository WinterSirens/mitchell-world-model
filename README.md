# Mitchell World Model

A personal knowledge system and decision-support vault built in Obsidian. The system compounds with use — every decision logged, synthesis pass, and rule added makes the next session more useful.

## What this is

A structured Obsidian vault that serves as a personal operating system: tracking current state, maintaining durable decision rules, storing synthesized knowledge, and logging outcomes over time. AI agents (Claude/Oz) interact with this vault to support decisions, run weekly syntheses, and maintain the knowledge base.

## Setup

### Prerequisites

- [Obsidian](https://obsidian.md/) (free)
- Obsidian plugins (configured in `.obsidian/`):
  - **Templater** — template engine for structured notes
  - **Cowork** — enables AI agent project context (requires the `Personal World Model/` folder)

### Getting started

1. Clone the repository:
   ```bash
   git clone git@github.com:WinterSirens/mitchell-world-model.git
   ```
2. Open Obsidian → **Open folder as vault** → select the cloned directory.
3. Enable community plugins when prompted (Templater, Cowork, etc.).
4. Templater should point to `00 System/Templates/` for template files.

## Vault structure

```
.claude/skills/          # Custom AI agent skills for this vault
00 Inbox/                # Raw dump zone — unprocessed captures and clippings
  Clippings/             # Web articles saved via Obsidian web clipper
00 System/               # Vault infrastructure (templates, readmes)
  Templates/
  Readmes/
01 World Model/          # Personal operating system — high-trust, decision-relevant
  01 State/              # Current State.md — snapshot of priorities and constraints
  02 Rules/              # Decision Rules.md — durable and provisional rules with change log
  03 Contexts/           # Recurring scenario playbooks (no log trail, updated: frontmatter)
  04 Reviews/            # Timestamped decision outcomes and retrospectives
02 Wiki/                 # Permanent knowledge base — processed, evergreen, retrievable
  Concepts/
  Projects/
  People/
  Themes/
  Syntheses/
03 Sources/              # Preserved upstream inputs with a re-retrieval reason
  Articles/
  Podcasts/
  Meetings/
  Chats/
  Research Notes/
04 Decisions/            # Forward-looking decision artifacts
  Weekly Briefs/
  Decision Memos/
  Active Plans/
90 Archive/              # Processed originals after distillation, organized by YYYY-MM/
Personal World Model/    # Required by Cowork plugin — do not rename or move
```

## Key workflows

### Weekly synthesis
Open a new agent session and say **"let's do the weekly synthesis."** The agent reads `00 Inbox/`, triages each note, proposes Goldilocks distillations to the correct files, and then either archives the processed original with `processed_into:` or preserves the source in `03 Sources/` only when there is a clear re-retrieval reason. See `00 System/Templates/Weekly Synthesis.md` for the full agenda.

### Decision support
Share the decision context in a session. The agent reads `01 World Model/01 State/Current State.md` and `01 World Model/02 Rules/Decision Rules.md`, simulates YES / NO / WAIT options, recommends one action, and surfaces the strongest counterargument.

### Note routing
| Content type | Destination |
|---|---|
| About Mitchell (identity, goals, state, rules) | `01 World Model/` |
| Durable synthesized knowledge | `02 Wiki/` |
| Raw upstream material worth re-reading | `03 Sources/` |
| Processed originals after distillation | `90 Archive/YYYY-MM/` |
| Changes what to do next (memos, plans, briefs) | `04 Decisions/` |
| Unprocessed | `00 Inbox/` |

The default is **distill, then archive**. `03 Sources/` is for upstream material whose original form is likely to be useful again — not a second archive.

## AI agent context

This vault uses `AGENTS.md` as the operating manual for AI agents. `CLAUDE.md` points to it. Any agent working in this vault should read `AGENTS.md` first and treat the markdown files as the source of truth over project memory.

Custom skills in `.claude/skills/` extend agent capabilities for vault-specific tasks.

## Version control

```bash
git add .
git commit -m "describe what changed"
git push
```

Commit regularly after synthesis sessions or significant updates. The `.gitignore` excludes `.DS_Store` and Obsidian workspace state files (open tabs, cursor positions).
