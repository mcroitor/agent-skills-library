---
name: rubric-designer-compact
description: Design a grading rubric for open-ended questions. Returns only the Criteria and Levels Table — one row per criterion, one column per compliance level, with observable evidence descriptors. No supporting documentation.
---

# Rubric Designer (Compact)

## Description
A minimal skill for producing an analytic rubric artifact: the Criteria and Levels Table only. Derives criteria from measurable learning objectives, assigns 5-level compliance descriptors with observable evidence, and outputs a ready-to-use table. No alignment docs, scoring model docs, calibration notes, or checklists.

## Priority Rules
1. **Alignment to learning objectives** — every criterion traces to a stated objective; ungrounded criteria removed
2. **Criterion observability** — each criterion assessable from submitted evidence
3. **Level distinctness** — adjacent levels differ by observable evidence quality, not wording intensity
4. **Structured output** — tabular, closed value sets, serializable to JSON/CSV

## When to Use
- LLM context window is constrained
- Only the rubric table is needed (no supporting documentation)
- Automated or programmatic rubric consumption
- Rapid rubric generation for known assessment types

## Instructions
1. **Identify objectives** — list measurable learning objectives from the assessment brief; infer if missing
2. **Define criteria** — one observable competency per objective; independently assessable
3. **Set levels** — 5-level scale `{0%, 25%, 50%, 75%, 100%}` with evidence anchors
4. **Assign weights** — equal `q_i = 1` unless unequal importance justified
5. **Define penalties** — per-criterion `D_i` and/or global `D` if task tolerates error deductions; else `0`
6. **Output table** — emit the Criteria and Levels Table only

## Output Contract
Return **only** the Criteria and Levels Table in this exact format:

```markdown
| ID | Criterion | Weight `q_i` | Penalty `D_i` | 0% | 25% | 50% | 75% | 100% | Notes |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | _\<one observable competency>_ | _\<int >= 0>_ | _\<int >= 0>_ | _\<evidence missing or wrong>_ | _\<significant errors, blocks goal>_ | _\<material gaps, partial work>_ | _\<minor issues only>_ | _\<fully satisfies criterion>_ | _\<optional reviewer hints>_ |
| C-2 | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ |
```

## Input Recovery Rules
- Missing objectives → infer from brief, mark assumptions in Notes column
- Unspecified weights → `q_i = 1`
- Unspecified penalties → `D_i = 0`, `D = 0`
- Unspecified scale → 5-level `{0, 25, 50, 75, 100}`
- Ambiguity preventing observable criteria → ask for clarification

## Constraints
- No criteria ungrounded in learning objectives
- No overlapping level descriptors
- Consistent level count across all criteria
- One objective → one criterion
- No reward for formatting over competency

## Descriptor Language
- Use evidence verbs: identifies, applies, compares, justifies, documents, compiles, executes, returns, handles, validates
- Replace "good", "deep", "qualitative" with concrete indicators
- State what evidence must be present, not how impressive the work "looks"

## Best Practices
- Default to `q_i = 1`, `D_i = 0` unless justification provided
- Keep table minimal — reviewers should score from the table alone
- Calibrate mentally on full/partial/near-zero samples before emitting