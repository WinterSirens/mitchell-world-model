---
name: ai-prd-builder
description: Build PRDs for internal AI solutions, automations, and tooling following the CPMAI framework. Use when the user asks to create a PRD, product requirements document, spec, or proposal for AI tools, GenAI applications, Rovo Agents, automation workflows, or ML-based solutions. Triggers on phrases like "write a PRD", "create requirements for", "spec out this AI tool", "document this automation", or "help me define this AI project".
---

# AI PRD Builder

Build product requirements documents for internal AI solutions following the CPMAI (Cognitive Project Management for AI) framework. Designed for environments handling sensitive data where compliance and security considerations matter.

## Workflow

1. **Gather context** → Ask clarifying questions if missing critical info
2. **Determine solution type** → GenAI/Automation (default) or Traditional ML
3. **Generate PRD** → Follow CPMAI phases, adapt depth to complexity
4. **Review and iterate** → Refine based on feedback

## Before Starting

Ask for any missing critical information:

- **Problem statement**: What business problem are we solving?
- **Solution concept**: What's the proposed approach?
- **Stakeholders**: Who needs this? Who's impacted?
- **Success criteria**: How do we know it worked?

Skip questions if context is already provided.

## Solution Type Detection

**GenAI/Automation** (most common):
- LLM-based tools, chatbots, RAG systems
- Rovo Agents, workflow automation
- Prompt-based solutions, API integrations
- Pre-trained model usage

**Traditional ML** (edge case):
- Custom model training required
- Prediction/classification on proprietary data
- Real-time inference at scale
- When no existing model fits the use case

Adapt PRD sections based on type. See `references/genai-adaptations.md` for GenAI-specific guidance.

## PRD Structure

Generate PRDs following this structure. Adapt depth based on solution complexity.

### 1. Executive Summary
- Problem statement (1-2 sentences)
- Proposed solution (1-2 sentences)
- Expected impact and success metrics
- Timeline and key milestones

### 2. Business Understanding (CPMAI Phase 1)
- Business objectives and why now
- Stakeholders and decision owners
- Success criteria with measurable targets
- Constraints (budget, timeline, compliance, tech stack)
- Cost-benefit analysis
- AI Go/No-Go assessment

See `references/phase1-business.md` for detailed guidance.

### 3. Data Requirements (CPMAI Phase 2)
- Data sources needed
- Data access and ownership
- Quality assessment and gaps
- Privacy and compliance considerations

See `references/phase2-data.md` for detailed guidance.

### 4. Solution Design (CPMAI Phases 3-4)

**For GenAI/Automation:**
- Architecture overview
- Prompt strategy / RAG design
- Integration points
- Human-in-the-loop requirements

**For Traditional ML:**
- Data preparation approach
- Model selection rationale
- Training and validation strategy

See `references/phase34-solution.md` for detailed guidance.

### 5. Evaluation Plan (CPMAI Phase 5)
- Success metrics (business KPIs + technical metrics)
- Testing approach
- Acceptance criteria
- Monitoring and alerting strategy

See `references/phase5-evaluation.md` for detailed guidance.

### 6. Operationalization (CPMAI Phase 6)
- Deployment architecture
- Rollout plan (MVP scope → iterations)
- Maintenance and governance
- Retraining/refinement triggers

See `references/phase6-operations.md` for detailed guidance.

### 7. Risks and Compliance
- Identified risks with mitigations
- Compliance requirements (financial data handling)
- Trustworthy AI considerations
- Rollback and incident response plan

### 8. Appendix (as needed)
- Technical specifications
- Integration diagrams
- Stakeholder RACI
- Open questions for stakeholder review

## Go/No-Go Decisions

Include Go/No-Go assessment after Business Understanding section. Frame as conversation starters, not blockers:

```
## Go/No-Go Assessment

| Dimension | Status | Notes |
|-----------|--------|-------|
| Business feasibility | Go/Maybe/No-Go | [rationale] |
| Data feasibility | Go/Maybe/No-Go | [rationale] |
| Technical feasibility | Go/Maybe/No-Go | [rationale] |

**Recommendation**: [Proceed / Proceed with conditions / Pause until X resolved]
```

## Compliance Considerations

For solutions handling sensitive data (customer info, financial data, proprietary systems):

- Data classification and handling requirements
- Access controls and audit logging
- PII anonymization or protection needs
- Regulatory requirements that may apply
- Security review and approval process

When uncertain about specific compliance frameworks, flag as "Requires compliance/security team input" rather than guessing.

## Output Format

- Generate PRD in Markdown
- Use clear headers and concise prose
- Avoid excessive bullet points in narrative sections
- Include tables for structured comparisons
- Flag open questions and assumptions clearly

## Complexity Scaling

**Simple solutions** (single integration, clear scope):
- Streamlined PRD, 2-3 pages
- Focus on Phases 1, 5, 6
- Lighter data and solution sections

**Complex solutions** (multiple integrations, novel approach):
- Comprehensive PRD, 5-8 pages
- Full CPMAI coverage
- Detailed risk and compliance analysis
