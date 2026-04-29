# GenAI Adaptations

When building PRDs for GenAI/Automation solutions, adapt CPMAI phases as follows.

## Phase Translations

| Traditional ML | GenAI/Automation Equivalent |
|----------------|----------------------------|
| Model training | Prompt engineering |
| Training data | Knowledge base / RAG corpus |
| Model selection | LLM provider/model selection |
| Hyperparameter tuning | Prompt iteration and testing |
| Model retraining | Prompt refinement, knowledge refresh |
| Feature engineering | Context design, input formatting |
| Model drift | Prompt degradation, knowledge staleness |
| Validation dataset | Eval set / golden examples |

## Data Requirements (Phase 2)

**Focus shifts from training data to:**
- Knowledge base content for RAG
- Example inputs/outputs for prompt design
- Test cases for evaluation
- Context sources (APIs, databases, documents)

**Key questions:**
- What knowledge does the LLM need access to?
- How will context be retrieved and injected?
- How fresh does the knowledge need to be?
- What examples will guide expected behavior?

## Solution Design (Phases 3-4)

**Replace model development with:**
- Prompt architecture (system prompt, user prompt templates)
- RAG design (chunking strategy, embedding model, retrieval logic)
- Tool/function calling design
- Output parsing and validation
- Error handling and fallbacks

**Key decisions:**
- Which LLM and why (capability, cost, latency, data handling)
- Prompt complexity vs. reliability tradeoff
- Context window management strategy
- Caching and optimization approach

## Evaluation (Phase 5)

**Metrics shift to:**
- Response quality (accuracy, relevance, helpfulness)
- Hallucination rate
- Task completion rate
- User satisfaction
- Cost per interaction
- Latency metrics

**Testing approach:**
- Golden set evaluation (expected input → expected output)
- A/B testing different prompt versions
- Human evaluation for subjective quality
- Edge case and adversarial testing

## Operationalization (Phase 6)

**Unique considerations:**
- Prompt versioning and deployment
- Knowledge base refresh pipelines
- LLM provider management (rate limits, costs, version updates)
- Fallback strategies when API unavailable
- Token usage monitoring and optimization

**Refinement triggers:**
- Quality score drops below threshold
- New use cases require prompt expansion
- Knowledge base content becomes stale
- LLM provider releases improved model
- Cost optimization needed

## Trustworthy AI for GenAI

**Additional considerations:**
- Hallucination mitigation (grounding, citations, confidence signals)
- Prompt injection prevention
- Output filtering and safety guardrails
- Data privacy in prompts and responses
- Transparency about AI-generated content
- Human review for high-stakes outputs
