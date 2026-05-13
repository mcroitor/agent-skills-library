---
name: ai-prompt-engineer
description: Design, test, and optimize prompts for LLM applications. Use for building prompt templates, improving response quality, designing structured outputs, creating role-specific instructions, and evaluating prompt variants.
---

# AI Prompt Engineer

## Description
A skill for designing, testing, and optimizing prompts and context strategies for LLM applications, with focus on reliability, accuracy, and controllable output format.

## Priority Rules
Prioritize in this order when trade-offs conflict; if two priorities overlap, prefer the higher item in the list:
1. Reliability and correctness
2. Safety and policy compliance
3. Output determinism and schema compliance
4. Maintainability and change safety
5. Latency
6. Token efficiency

## When to Use
- Building prompt templates for assistants and copilots
- Improving response quality and reducing hallucinations
- Designing structured outputs (JSON, markdown, tool calls)
- Creating role/task-specific instructions
- Evaluating prompt variants and selecting best-performing ones
- Tuning context windows and retrieval prompts in RAG systems

## Instructions
1. **Define task contract** - objective, constraints, expected output schema
2. **Build baseline prompt** - separate system constraints, task instructions, user context, and tool invocation rules
3. **Add format control** - explicit output format and validation rules
4. **Inject context safely** - delimiters, source ordering, relevance filters
5. **Test edge cases** - ambiguous input, missing data, adversarial prompts
6. **Evaluate quality** - prioritize in this order: accuracy and consistency first; then safety (policy compliance and data security); then token cost and latency
7. **Iterate systematically** - version prompts and compare against benchmarks
8. **Operationalize** - fallback prompts, retries, and monitoring hooks

## Input Recovery Rules
- Infer reasonable defaults when requirements are incomplete
- Mark all assumptions explicitly in the output
- Ask for clarification only when ambiguity affects reliability, safety, or evaluation validity

## Constraints
- Do not rely on role prompting without explicit task instructions or constraints
- Do not mix instructions and examples ambiguously
- Do not request or expose hidden chain-of-thought
- Do not optimize token cost at the expense of correctness
- Do not overload prompts with redundant or conflicting instructions

## Tools and Methods
- Role + goal + constraints framing
- Few-shot examples and counterexamples
- Step-by-step decomposition only when task complexity benefits from intermediate reasoning structure
- Output schema anchoring
- Guardrail instructions and refusal boundaries
- Retrieval-aware prompting for RAG

## Output Contract
Return all of the following:
1. Prompt objective
2. Final prompt template
3. Input variables and constraints
4. Output schema and validation checks
5. Failure modes and mitigations
6. Test cases and expected results
7. Optimization notes and trade-offs

## Failure Prevention
- Check prompt variants against the same benchmark set before selecting a winner
- Validate that schema constraints and refusal behavior remain stable across edge cases
- Test prompts after model, retrieval, or tool interface changes before reusing them in production
- Review prompt changes for regression risk, not only for local output improvements

## Evaluation Criteria
- Task completion rate
- Factual correctness
- Format compliance
- Hallucination and safety violation rate
- Response latency and token usage
- Stability across model versions

## Schema Robustness Rules
- Minimize optional fields in structured outputs
- Avoid ambiguous enum values
- Define validation expectations explicitly (required fields, type checks, and rejection behavior)

## Deliverables
- Prompt templates library
- Prompt version history and changelog
- Evaluation dataset and benchmark report
- Failure mode catalog with mitigations
- Production prompt playbook

## Best Practices
- Prompts must define observable success conditions
- Treat prompts as versioned artifacts
- Use deterministic settings for evaluation
- Validate strict schemas before downstream use
- Isolate system instructions from user input
- Re-test prompts when model or context changes
