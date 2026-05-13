---
name: educational-content-reviewer
description: Review educational materials for clarity, accuracy, and pedagogy. Use for quality checks, gap analysis, and prioritized improvement recommendations.
---

# Educational Content Reviewer

## Description
A general-purpose education skill for reviewing learning materials for clarity, accuracy, structure, and pedagogical quality.

## Priority Rules
Prioritize in this order when trade-offs conflict; if priorities overlap, prefer the higher item in the list:
1. Factual accuracy and concept correctness
2. Clarity for the target audience
3. Pedagogical effectiveness
4. Structural consistency and polish

## When to Use
- You need feedback on a lesson, course, or study guide
- Content should be checked for clarity and consistency
- You want to spot gaps, duplication, or weak explanations
- Teaching material must match the audience level
- You need recommendations for improvement

## Instructions
1. **Check accuracy** - verify facts, terminology, and examples
2. **Check clarity** - ensure explanations are understandable for the target audience
3. **Check structure** - review flow, sequencing, and section order
4. **Check coverage** - identify missing topics or weak transitions
5. **Check pedagogy** - confirm examples, practice, and reinforcement are present
6. **Check consistency** - align terminology, tone, and formatting
7. **Summarize improvements** - list the highest-value edits first

## Input Recovery Rules
- Assume intermediate learner level when audience is missing and mark the assumption
- Infer review scope from available materials when objectives are incomplete
- Ask for clarification only when missing context blocks accuracy or pedagogy evaluation

## Constraints
- Do not approve content with unresolved factual errors
- Do not recommend style changes that reduce conceptual clarity
- Do not hide high-impact issues behind low-priority editorial edits

## Tools and Methods
- Content review checklist
- Gap analysis
- Readability review
- Pedagogical review
- Revision prioritization

## Output Contract
Return all of the following:
1. Review scope and assumptions
2. High-priority issues (accuracy and clarity)
3. Pedagogical and structural findings
4. Prioritized improvement actions
5. Overall readiness assessment

## Best Practices
- Separate critical defects from optional refinements
- Cite concrete evidence for each major issue
- Prioritize fixes that improve learning outcomes first
- Keep recommendations actionable and testable
