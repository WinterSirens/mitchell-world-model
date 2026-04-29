---
name: plugin-security-audit
description: "Perform a security audit on third-party MCP servers or custom skills before installing them into Claude. Triggers when a user uploads plugin code, links to a plugin repo, pastes MCP server configuration, or mentions wanting to evaluate, vet, audit, or security-check a plugin, MCP server, skill, connector, or extension. Also triggers on phrases like 'is this plugin safe', 'should I install this', 'check this MCP server', 'review this skill for security', 'audit this extension', or any mention of plugin/skill security, trust, or risk assessment. Use this skill whenever a user is considering adding any third-party tooling to their Claude setup and wants to understand the risks before doing so."
---

# Plugin Security Audit

Evaluate third-party MCP servers and custom skills for security risks before connecting them to Claude. This skill combines automated static analysis (when source code is available) with a structured risk assessment checklist (for remote services or when code isn't accessible).

## Why This Matters

Third-party plugins operate inside Claude's trust boundary. A malicious or poorly-built plugin can:
- Inject hidden instructions that hijack Claude's behavior (prompt injection)
- Request permissions far beyond what it needs (scope creep)
- Exfiltrate conversation data, files, or credentials to external servers
- Pull in compromised dependencies that execute arbitrary code

Most plugin authors aren't adversarial — but many are careless. This skill helps you distinguish safe plugins from risky ones and make informed go/no-go decisions.

## Trigger

The user wants to evaluate a plugin before installing it. They may provide:
- Source code files (uploaded or linked)
- An MCP server URL or configuration block
- A GitHub repo link
- A SKILL.md or skill folder
- Just a name/description and a request for guidance

## Execution Model

This skill runs as an **investigation, not an interview**. Claude does the research and presents findings — the user reviews and makes the final call. Start with whatever the user provides, run automated checks where possible, then investigate the remaining risk areas using web search, documentation analysis, and source code review. Produce a final risk report at the end.

If the user only has a plugin name or URL (no source code), skip straight to the Investigative Risk Assessment and use web research to gather what you can. Be explicit about what couldn't be verified without source access.

## Phase 1: Automated Static Analysis

Run these checks when source code is available. Read the relevant reference file first:
→ Read `references/automated-checks.md` before executing any scans.

The automated checks cover:
1. **Prompt injection surface scan** — Search tool descriptions, system prompts, and response templates for instruction-like content
2. **Permission and capability mapping** — Enumerate what the plugin can access (filesystem, network, shell, credentials)
3. **Outbound network analysis** — Identify all external domains, API endpoints, and data transmission patterns
4. **Dependency audit** — Check for known vulnerabilities, unpinned versions, and suspicious packages
5. **Code execution risk** — Flag eval(), exec(), subprocess, shell invocations, and dynamic code generation
6. **Credential handling** — Find hardcoded secrets, insecure storage patterns, and token transmission

Each check produces a finding with a severity level:
- **CRITICAL** — Likely exploitable, blocks installation
- **HIGH** — Serious risk, needs remediation or strong justification
- **MEDIUM** — Notable concern, acceptable with awareness
- **LOW** — Minor issue or best-practice deviation
- **INFO** — Observation, no action needed

## Phase 2: Investigative Risk Assessment

Claude performs this assessment proactively using available evidence — source code analysis, web research (GitHub, npm/PyPI, documentation sites), README and config file inspection, and any other accessible information. Do NOT quiz the user with questions they'd need to go research themselves. The user came to Claude because they don't know what to look for.

→ Read `references/manual-assessment.md` for the full checklist and investigation targets.

**Investigation approach:**
1. **Start with what's available.** Source code, README, package manifest, documentation, GitHub repo, npm/PyPI page — extract as much as possible before involving the user.
2. **Use web search aggressively.** Look up the publisher, check download counts, find the repo, read the docs, check for security advisories or community discussion.
3. **Only ask the user about things Claude genuinely cannot determine** — e.g., "Do you actually need the filesystem access this plugin requests, or is that a feature you'd never use?" or "Is this publisher someone your team already trusts?"
4. **When evidence is unavailable, say so directly** and add it to the research backlog — don't ask the user to go find it during the conversation.

The assessment covers:
1. **Publisher trust signals** — Who made this? Open source? Verified? Maintained?
2. **Scope justification** — Does what it requests match what it claims to do?
3. **Data flow mapping** — Where does your data go? What gets sent externally?
4. **Prompt injection resilience** — How does it handle untrusted content?
5. **Failure mode analysis** — What happens when things go wrong?
6. **Update and maintenance risk** — Could a future update introduce new risks?

## Phase 3: Risk Report

After completing both phases (or just Phase 2 if no source code), produce a structured risk report.

→ Read `references/report-template.md` for the output format.

The report includes:
- Overall risk rating (Critical / High / Medium / Low)
- Summary of findings by category
- Specific go/no-go recommendation with conditions
- Mitigation steps if the user decides to proceed
- A "research backlog" of items the user should investigate further that the skill couldn't determine automatically

## Important Constraints

Be honest about the limits of this analysis:
- Static analysis catches patterns, not intent. A clean scan doesn't guarantee safety.
- Remote MCP servers execute code you can't see. The audit can only evaluate what's declared, not what actually runs server-side.
- Dependencies can change. A safe package today could be compromised tomorrow.
- This skill identifies risks and surfaces them for human judgment. It does not make the final call — the user does.

Never tell the user a plugin is "safe" in absolute terms. Use language like "no risks identified in the areas we checked" or "low risk based on available evidence, with these caveats."

When the user's provided information is insufficient to assess a risk area, say so explicitly and add it to the research backlog rather than assuming it's fine.
