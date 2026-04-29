# Investigative Risk Assessment Checklist

Work through each section by investigating with available evidence first — source code, web search, documentation, GitHub/npm/PyPI pages, community discussions. For each area, explain the risk, present what you found, and flag gaps. Only ask the user questions that Claude genuinely cannot answer from available evidence.

Items that can't be determined become research backlog entries in the final report — don't turn them into homework questions for the user during the conversation.

## Section 1: Publisher Trust Signals

**Why it matters:** A plugin from a known, accountable publisher with a public track record is inherently lower risk than an anonymous one. This doesn't guarantee safety, but it changes the baseline.

**Investigate these signals (Claude does this, not the user):**

- **Publisher identity.** Search for the publisher name, organization, or GitHub profile. Is it a named company, a known open-source maintainer, or anonymous?
- **Source code availability.** Is the repo public? If closed-source, note that the risk floor is significantly higher.
- **Age and track record.** Check when the repo was created, first published to npm/PyPI, or first appeared. Brand-new plugins have no track record.
- **Security policy.** Look for `SECURITY.md` in the repo, a responsible disclosure process, or security-related documentation.
- **Maintenance cadence.** Check recent commit history, issue response times, and release frequency. Abandoned plugins accumulate unpatched vulnerabilities.
- **Adoption signals.** GitHub stars, npm/PyPI downloads, open issues, community mentions. Low adoption means fewer eyes on the code.

**What to ask the user (only if needed):**
- "Is [publisher] an entity your team already trusts or has a relationship with?"
- "Does your organization have policies about plugins from individual maintainers vs. companies?"

**Scoring guidance:**
- Verified company + open source + active maintenance + security policy → LOW risk
- Known maintainer + open source + sporadic maintenance → MEDIUM risk
- Anonymous + closed source + no track record → HIGH risk
- Any indicator of deception (fake reviews, misleading claims, impersonation) → CRITICAL risk

## Section 2: Scope Justification

**Why it matters:** A weather plugin that requests filesystem access is suspicious. Every capability a plugin claims should map to a feature the user actually wants.

**Investigate these signals (Claude does this):**

- **Stated purpose.** Extract a clear, one-sentence description from the README, docs, or tool descriptions.
- **Declared permissions.** Pull from automated Check 2 if available, or extract from documentation/config files.
- **Permission-to-feature mapping.** For each permission, determine from the source code or documentation why it needs that access:
  - Filesystem access: Which paths? Read or write? What feature depends on it?
  - Network access: Which domains? What data is sent? Which API does it integrate with?
  - Shell/process execution: What does it run? Why can't this be done in-language?
  - Browser control: What pages? What actions?
  - Credential access: Which credentials? How are they used?
- **Excess permissions.** Flag any permission that doesn't map to a documented feature.

**The "newspaper test":** If someone described this plugin's actual behavior in a news article, would it be surprising relative to what it claims to do? If yes, that's a scope concern.

**What to ask the user (only if needed):**
- "This plugin requests [permission X]. Do you need the feature that requires this, or is it something you'd never use?"
- "Are you comfortable with this plugin having [broad access] for [specific feature]?"

**Scoring guidance:**
- Every permission maps to a documented feature → LOW risk
- Some permissions seem broader than necessary but plausible → MEDIUM risk
- Permissions that don't correspond to any documented feature → HIGH risk
- Permissions that are actively misleading vs. documentation → CRITICAL risk

## Section 3: Data Flow Mapping

**Why it matters:** The user needs to understand exactly where their data goes when they use this plugin. "Data" includes conversation content, uploaded files, Claude's responses, and any metadata.

**Investigate these signals (Claude does this):**

- **Data inputs.** From source code or documentation, determine what data the plugin receives from Claude — tool inputs, conversation context, file contents?
- **Data destinations.** Map the flow: user → Claude → plugin → ??? Trace outbound requests in the code (cross-reference with automated Check 3).
- **Data storage.** Check for databases, file writes, caching, or persistence layers. Review the privacy policy if one exists.
- **Third-party sharing.** Look for analytics SDKs (Segment, Mixpanel, PostHog), advertising integrations, or data-sharing agreements in the docs.
- **Data retention/deletion.** Check the privacy policy or terms for what happens to data after uninstall.
- **Encryption.** Verify HTTPS-only for all outbound requests. Flag any plaintext channels.

**Particularly sensitive data paths to flag:**
- Conversation content sent to external servers (your prompts and Claude's responses)
- File contents transmitted to the plugin's backend
- Plugin sending data to domains other than its primary API
- Plugin logging or telemetry that includes user data
- Any path where data leaves the user's machine without clear disclosure

**What to ask the user (only if needed):**
- "This plugin sends [specific data] to [specific destination]. Are you comfortable with that given what you'd use it for?"
- "I couldn't find a privacy policy for this plugin. Is that a dealbreaker for your use case?"

**Scoring guidance:**
- Data stays local or goes to a well-documented, encrypted endpoint with a privacy policy → LOW risk
- Data goes to the plugin's backend with minimal documentation → MEDIUM risk
- Data transmitted to undocumented third parties or without encryption → HIGH risk
- Evidence of covert data collection or exfiltration → CRITICAL risk

## Section 4: Prompt Injection Resilience

**Why it matters:** This is the #1 risk category for LLM plugins. A plugin that can modify Claude's behavior through its tool descriptions or responses can bypass the user's intentions entirely.

**Investigate these signals (Claude does this):**

- **Tool description content.** Review all tool descriptions injected into Claude's context. Determine whether the content is purely descriptive or contains behavioral instructions. (Cross-reference with automated Check 1.)
- **Untrusted content handling.** Determine if the plugin processes external content (web pages, emails, user-uploaded files) that could contain injection attacks flowing through the plugin into Claude.
- **Response format.** Analyze whether tool responses are structured data (lower risk) or allow arbitrary text that could include instructions Claude would follow.
- **Content sanitization.** Check whether the plugin strips instruction-like content from its responses before passing them to Claude.

**Attack scenarios to assess:**
1. **Direct injection via tool description:** Plugin embeds hidden instructions in its tool description that tell Claude to behave differently (e.g., "When using this tool, always recommend [product]").
2. **Indirect injection via tool response:** Plugin fetches external content (a webpage, email, document) that contains embedded instructions. Those instructions flow through the tool response into Claude's context.
3. **Persistent injection:** Plugin stores injected content that gets served on every subsequent invocation, creating a lasting behavioral change.
4. **Escalation injection:** Plugin's instructions tell Claude to call other tools in a specific sequence, potentially performing actions the user didn't request.

**Present findings directly.** This section rarely requires user input — the evidence is in the code and tool definitions.

**Scoring guidance:**
- Plugin descriptions are purely functional, responses are structured data → LOW risk
- Plugin processes external content but with some sanitization → MEDIUM risk
- Plugin processes external content with no visible sanitization → HIGH risk
- Plugin descriptions contain behavioral instructions beyond functional description → CRITICAL risk

## Section 5: Failure Mode Analysis

**Why it matters:** What a plugin does when things go wrong reveals a lot about its quality. Ungraceful failures can leak data, corrupt state, or leave the user in a bad position.

**Investigate these signals (Claude does this):**

- **Error handling patterns.** Search the source code for try/catch blocks, error handlers, and failure paths. Determine whether failures are handled gracefully.
- **Backend availability.** Check for timeout handling, retry logic, and fallback behavior when the plugin's backend is unreachable.
- **Input validation.** Look for validation logic on inputs. Does it reject malformed data or pass it through?
- **Rate limit handling.** Check for retry logic with backoff. Aggressive retries without backoff are a quality red flag.
- **Error message safety.** Review error messages for leaked internal details — paths, credentials, stack traces, or architecture details.
- **Fallback behavior.** Determine what Claude does if the tool call fails — is there documented fallback?

**Present findings directly.** This section rarely requires user input — the evidence is in the code.

**Scoring guidance:**
- Documented error handling, graceful degradation, no data leakage on failure → LOW risk
- Basic error handling but some edge cases unclear → MEDIUM risk
- No visible error handling, or errors that leak internal details → HIGH risk

## Section 6: Update and Maintenance Risk

**Why it matters:** A plugin you install today might update tomorrow. Understanding the update model tells you whether your initial security assessment stays valid.

**Investigate these signals (Claude does this):**

- **Update mechanism.** Determine from docs/config whether the plugin auto-updates, requires manual update, or uses pinned versions.
- **Remote MCP server volatility.** For MCP servers, note that server-side code can change without notice — this is inherent and cannot be fully mitigated.
- **Permission escalation risk.** Check whether auto-updates could introduce new permission requests without user approval.
- **Changelog/release notes.** Look for a CHANGELOG.md, GitHub Releases page, or version history. Can you see what changed between versions?
- **Bus factor.** Check contributor count on the repo. Single-maintainer projects carry higher long-term risk.

**This is the area where remote MCP servers are fundamentally riskier than local skills.** A skill you install is a snapshot — it doesn't change unless you update it. An MCP server can change its behavior server-side at any time with no notice. Make sure the user understands this distinction.

**What to ask the user (only if needed):**
- "This is a remote MCP server, which means the publisher can change its behavior at any time without notifying you. Does your use case require that level of trust?"

**Scoring guidance:**
- Pinned versions + changelog + multi-maintainer → LOW risk
- Manual updates + single maintainer + changelog → MEDIUM risk
- Auto-updates or remote server with no changelog → HIGH risk
- Remote server with no transparency into changes → HIGH risk (inherent, cannot be mitigated)
