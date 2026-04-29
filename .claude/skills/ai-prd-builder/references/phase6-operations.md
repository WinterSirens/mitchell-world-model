# Phase 6: Operationalization

## Deployment Architecture

### Options
| Type | Best For | Considerations |
|------|----------|----------------|
| Cloud ML/API | Scalable workloads, variable demand | Vendor dependency, data transfer costs |
| On-premise | Regulated data, low latency needs | Hardware costs, maintenance overhead |
| Hybrid | Sensitive training, cloud inference | Complexity, data transfer security |
| Edge | Offline operation, distributed endpoints | Model size constraints, update complexity |

### GenAI-Specific
- API-based (Claude, OpenAI): Fastest to deploy, ongoing costs, less control
- Self-hosted: More control, higher operational burden
- Platform-native (Rovo, etc.): Simplified ops, platform constraints

## Rollout Strategy

### MVP-First Approach
1. **MVP scope**: Smallest useful version that proves value
2. **Limited rollout**: Controlled user group for validation
3. **Iterate**: Expand scope based on learnings
4. **Full deployment**: After proven stable and valuable

### Rollout Phases
| Phase | Scope | Success Criteria | Duration |
|-------|-------|------------------|----------|
| MVP | [Core feature, limited users] | [Metrics] | [X weeks] |
| Expand | [Additional features/users] | [Metrics] | [X weeks] |
| GA | [Full scope] | [Metrics] | Ongoing |

## Maintenance & Governance

### Ongoing Operations
- Performance monitoring and reporting
- Incident response procedures
- Access control management
- Cost tracking and optimization

### Model/Prompt Lifecycle
- Version control for prompts and configurations
- Change approval workflow
- Rollback procedures
- Documentation requirements

### Refinement Triggers

**For GenAI:**
- Prompt updates when accuracy drops
- RAG knowledge base refresh cadence
- Model version upgrades (API provider updates)

**For ML:**
- Retraining when performance degrades
- Data drift detection triggers
- Scheduled retraining cycles

## Governance Framework

### Key Controls
- Access control and audit logging
- Change management process
- Security review requirements
- Compliance checkpoints

### Documentation Requirements
- Model/system card (what it does, limitations)
- Operational runbook
- Incident response procedures
- Stakeholder communication plan

## Section Template

```markdown
## Operationalization

### Deployment Architecture
- Environment: [Cloud/On-prem/Hybrid]
- Hosting: [API/Self-hosted/Platform]
- Infrastructure: [Key technical details]

### Rollout Plan
| Phase | Scope | Timeline | Success Criteria |
|-------|-------|----------|------------------|
| MVP | [Description] | [Date] | [Metrics] |
| Phase 2 | [Description] | [Date] | [Metrics] |

### Maintenance
- Monitoring: [Tools and dashboards]
- On-call: [Team responsible]
- Refresh cadence: [When knowledge/models updated]

### Governance
- Change approval: [Process]
- Access control: [Who can access what]
- Audit logging: [What's tracked]
- Compliance reviews: [Frequency, owner]

### Rollback Plan
- Trigger conditions: [When to rollback]
- Rollback procedure: [Steps]
- Communication plan: [Who to notify]
```
