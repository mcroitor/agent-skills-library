# AI Prompt Engineer

## Description
A skill for designing, testing, and optimizing prompts and context strategies for LLM applications, with focus on reliability, accuracy, and controllable output format.

## When to Use
- Building prompt templates for assistants and copilots
- Improving response quality and reducing hallucinations
- Designing structured outputs (JSON, markdown, tool calls)
- Creating role/task-specific instructions
- Evaluating prompt variants and selecting best-performing ones
- Tuning context windows and retrieval prompts in RAG systems

## Instructions
1. **Define task contract** - objective, constraints, expected output schema
2. **Build baseline prompt** - role, context, rules, examples
3. **Add format control** - explicit output format and validation rules
4. **Inject context safely** - delimiters, source ordering, relevance filters
5. **Test edge cases** - ambiguous input, missing data, adversarial prompts
6. **Evaluate quality** - accuracy, consistency, safety, token cost, latency
7. **Iterate systematically** - version prompts and compare against benchmarks
8. **Operationalize** - fallback prompts, retries, and monitoring hooks

## Prompt Design Techniques
- Role + goal + constraints framing
- Few-shot examples and counterexamples
- Step-by-step decomposition
- Output schema anchoring
- Guardrail instructions and refusal boundaries
- Retrieval-aware prompting for RAG

## Evaluation Criteria
- Task completion rate
- Factual correctness
- Format compliance
- Hallucination and safety violation rate
- Response latency and token usage
- Stability across model versions

## Deliverables
- Prompt templates library
- Prompt version history and changelog
- Evaluation dataset and benchmark report
- Failure mode catalog with mitigations
- Production prompt playbook

## Best Practices
- Keep prompts explicit and testable
- Treat prompts as versioned artifacts
- Use deterministic settings for evaluation
- Validate strict schemas before downstream use
- Isolate system instructions from user input
- Re-test prompts when model or context changes
