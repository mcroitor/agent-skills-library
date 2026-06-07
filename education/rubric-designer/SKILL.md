---
name: rubric-designer
description: Design grading rubrics for open-ended questions. The main output is a Criteria and Levels Table — one row per criterion, one column per compliance level, with observable evidence descriptors — backed by a seven-step methodology. Use for analytic rubrics with explicit criteria, observable level descriptors, and a formal scoring model (binary, multi-level, with penalties, with weights, or combined) that maps each criterion to a learning objective.
---

# Rubric Designer

## Description
A specialized education skill for designing grading rubrics for open-ended questions, grounded in a seven-step methodology ([references/croitor_grading_rubric.en.md](references/croitor_grading_rubric.en.md)). It produces analytic rubrics whose criteria derive from measurable learning objectives, whose level descriptors use observable evidence language, and whose final score is computable from a documented formula. The output is platform-independent and suitable for structured assessment workflows.

> **Main output:** the Criteria and Levels Table — one row per criterion, one column per compliance level, with observable evidence descriptors in each cell. The seven-step methodology, scoring model, calibration notes, alignment check, and structured-rubric checklist exist to support, justify, and validate this table.

When full rubric documentation is requested, the reviewer should be able to start scoring from the Criteria and Levels Table alone. The surrounding sections provide context, traceability, scoring logic, and validation evidence for that table.

This skill focuses on the rubric artifact. Assessment design (assignment framing, instructions, feedback guidance) is delegated to **Assessment Writer**, which calls this skill when a full rubric is required.

## When to Use
- You need a reusable rubric for an open-ended question: essay, report, code, math solution, project deliverable
- Criteria must be derived from measurable learning objectives
- Multiple reviewers (or an AI grader) must apply the rubric consistently
- The rubric must support a computable final score (binary, multi-level, with penalties, with weights, or combined)
- The rubric must be unambiguous, structured, and consistent across applications
- Assessment Writer has requested a rubric artifact for a defined assessment

## Instructions
Follow the seven-step methodology. Steps are ordered; do not skip a step.

1. **Define the learning objectives verified by the assessment tool** - enumerate the specific, measurable objectives (course, topic, lesson) that this assessment checks; record assumptions when objectives are inferred
2. **Identify measurable criteria** - one criterion per learning objective; each criterion must be observable in submitted evidence and independently assessable
3. **Define compliance levels with operational descriptions** - default 5-level scale `{0%, 25%, 50%, 75%, 100%}` with concrete evidence anchors (binary `{0%, 100%}` is acceptable when the task admits no partial credit); describe what evidence justifies each level, not just labels like "good" or "partial"
4. **Assign weighting coefficients** - if criteria are not equally important, set weights `q_i` so that `sum(q_i) > 0` and weights are normalized in the final formula; if equal, set `q_i = 1` for all
5. **Define penalty points** - per-criterion (`D_i`) and/or global (`D`) penalty per counted error if the task tolerates penalties for residual defects (e.g., runtime failures, style violations); set to `0` when penalties are not used
6. **Test the rubric on real or representative submissions** - apply the rubric to at least one full-mark, one partial-mark, and one near-zero submission; verify that scores match expert judgment and that levels do not overlap; document any calibration notes
7. **Adjust the rubric** - if testing reveals ambiguity, overlap, or unfair scores, return to step 3 (and if needed to step 1); freeze the rubric only after a calibration pass

## Rubric Type Selection
Choose the rubric type that matches the assessment and apply the corresponding formula.

| Type | When to use | Formula |
| --- | --- | --- |
| **Binary** | Atomic tasks where only complete compliance counts | `G = (sum P_i) / N`, `P_i in {0, 100}` |
| **Multi-level** | Tasks that admit partial credit on a single dimension | `G = (sum P_i) / N`, `P_i in {0, 25, 50, 75, 100}` (or custom scale) |
| **With penalties** | Errors must be subtracted even when core criteria are met | per-criterion: `G = (sum max(0, 100 - k_i * D_i)) / N`; global: `G = max(0, (sum P_i) / N - k * D)` |
| **With weights** | Criteria have unequal importance | `G = (sum P_i * q_i) / (sum q_i)` |
| **Combined** | Realistic case: partial levels + per-criterion penalties + weights | `P_i = max(0, L_i - k_i * D_i)`, then `G = (sum P_i * q_i) / (sum q_i)`; add `- k * D` for global penalty |

All percentages are reported on a 0-100 scale and can be mapped to any conventional grading scale.

## Default Compliance Level Scale
Use the 5-level scale below unless a different scale is justified. Document deviations explicitly.

| Percentage | Interpretation | Evidence anchor |
| --- | --- | --- |
| 0% | Completely incorrect | The response does not address the criterion |
| 25% | Almost incorrect | The response contains significant errors that block the goal |
| 50% | Partially correct | The response addresses the criterion with material gaps or errors |
| 75% | Almost correct | The response addresses the criterion with minor issues only |
| 100% | Correct | The response fully satisfies the criterion in observable evidence |

## Structured Rubric Requirements
A structured rubric must satisfy all five of the following. These are non-negotiable; any violation forces a return to the corresponding step in the Instructions.

1. **Completeness of criteria** - all assessed aspects appear as separate criteria; no hidden sub-scoring
2. **Clarity of formulations** - each level describes observable evidence, not subjective impressions
3. **Operationalization of criteria** - criteria and levels are expressed via measurable or verifiable indicators
4. **Avoidance of subjective assessments** - phrases like "qualitative analysis" or "deep understanding" are replaced by concrete evidence indicators
5. **Structuredness** - the rubric has a tabular structure (criterion × level) and a closed set of allowed values, so it can be serialized (table, JSON, XML) and processed algorithmically

## Priority Rules
Apply in this order; earlier rules have higher priority unless a later rule explicitly states an exception:

1. **Alignment to learning objectives** - every criterion traces to a stated objective; ungrounded criteria are removed
2. **Criterion observability** - each criterion must be assessable from submitted evidence
3. **Rubric validity** - levels, weights, and penalties must produce defensible scores
4. **Reviewer consistency** - level descriptors must yield the same level across reviewers for the same evidence
5. **Structured-rubric suitability** - structuredness, clarity, and operationalization take precedence over compactness
6. **Output compactness** - keep the artifact concise, but never at the cost of validity

If priorities conflict (for example, compactness vs reviewer consistency), preserve the higher-priority rule and explicitly note the deviation.

## Output Contract
Return the grading rubric only, presented by the Criteria and Levels Table by default. If full rubric documentation is requested or clearly implied, include the following sections in this order. The Executive Summary is **only required for full documentation** requests.

1. **Executive summary** (full docs only) - explicitly state that the main output is the Criteria and Levels Table in section 3 and that the remaining sections support, justify, and validate it
2. **Rubric overview** - assessment name, course/topic/lesson, rubric type, compliance level scale, pass threshold (if defined), scope and assumptions
3. **Learning objectives and criteria alignment** - a table mapping each learning objective to exactly one criterion, plus a brief evidence check
4. **Criteria and levels table** ★ **main output** - rows are criteria, columns are level percentages, cells contain observable evidence descriptors; include weight `q_i`, per-criterion penalty `D_i`, and any per-criterion notes
5. **Scoring model** - state the formula in mathematical form, list all parameters (`N`, `L_i`, `P_i`, `k_i`, `D_i`, `q_i`, `k`, `D`), and show a worked numeric example on a sample submission
6. **Calibration notes** - include at least one full-mark, one partial-mark, and one near-zero sample, plus reviewer disagreements and adjustments
7. **Alignment check** - confirm that every criterion maps to exactly one learning objective, that no objective is left un-assessed, and record any justified gaps
8. **Structured-rubric checklist** - confirm completeness, clarity, operationalization, avoidance of subjectivity, and structuredness

## Input Recovery Rules
- If learning objectives are missing, infer them from assignment context, mark all assumptions explicitly, and surface them in the rubric overview
- If the assignment description is incomplete, generate a minimal viable rubric and clearly label every unknown field
- If weights, penalties, or the level scale are not specified, default to: equal weights `q_i = 1`, no penalties `D_i = D = 0`, 5-level scale `{0, 25, 50, 75, 100}`; document every default
- If the assessment type does not match any of the rubric types in the selection table, request clarification before inventing a custom type
- Ask for clarification only when ambiguity prevents defining observable criteria or level descriptors
- Never fabricate external standards, policy requirements, or grading scales that were not provided

## Constraints
- Apply constraints in this sequence: structured-rubric suitability first, then criterion observability, then scoring consistency, then format compactness
- Do not output criteria that are not observable in submitted evidence
- Do not use overlapping descriptors that can map to multiple levels simultaneously
- Do not produce inconsistent level counts across criteria unless explicitly requested
- Do not combine learning objectives into a single criterion; one objective, one criterion
- Do not reward formatting over demonstrated competency
- Do not duplicate the same competency across criteria

## Criterion Quality Rules
- Each criterion measures exactly one observable competency
- Criteria are independently assessable
- Level descriptors are distinct, measurable, and non-overlapping
- Criteria in one rubric use the same level count
- Weights sum to a positive value and are normalized in the formula
- Compliance percentages are drawn from a closed set (binary or 5-level by default)

## Descriptor Language Rules
- Use observable evidence verbs: identifies, applies, compares, justifies, documents, compiles, executes, returns, handles, validates
- Avoid subjective labels without evidence indicators: replace "good", "deep", "qualitative" with concrete indicators
- State what evidence must be present, not how impressive the work "looks"

## Calibration Guidance
- Adjacent levels must differ by observable evidence quality, not by wording intensity
- Apply the rubric to at least one full-mark, one partial-mark, and one near-zero submission before freezing it
- Record any reviewer disagreements and how they were resolved

## Failure Prevention
- Do not reward formatting over demonstrated competency
- Do not duplicate the same competency across criteria
- Do not create criteria that cannot realistically be observed in the submission medium (text, code, file, artifact)
- Do not freeze a rubric that fails any of the five structured-rubric requirements

## Tools and Methods
- Seven-step rubric methodology
- Analytic rubric design
- Learning-objective to criterion mapping
- Compliance-level calibration (binary or 5-level)
- Weighted and penalty-based scoring
- Worked-example numeric scoring

## Best Practices
- Treat the Criteria and Levels Table as the main artifact; design and review it first
- Derive criteria from measurable learning objectives, not from assignment logistics
- Express every level descriptor as observable evidence
- Calibrate with at least one full, one partial, and one near-zero sample before release
- State the final-grade formula in mathematical form and include a worked example
- Keep the rubric compact, but never at the cost of validity, observability, or structured-rubric suitability
- Reuse the rubric template at [templates/rubric-template.md](templates/rubric-template.md) for consistent artifacts

## References
- [Croitor - Methodology for Creating Grading Rubrics for Open-Ended Questions](references/croitor_grading_rubric.en.md) - foundational methodology
- [Rubric template](templates/rubric-template.md) - reusable artifact structure
- [Example rubric - C++ IntStack assignment](examples/example-rubric-cpp-intstack.md) - standard request example that returns the default rubric-only output
- [Example rubric - Academic writing definition question](examples/example-rubric-academic-writing-definition.md) - full-documentation request example for a concept-definition response
