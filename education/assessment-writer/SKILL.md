---
name: assessment-writer
description: Design practical assessments and grading criteria. Use for creating assignment criteria, rubrics, performance tasks, and ensuring consistent evaluation across reviewers.
---

# Assessment Writer

## Description
A specialized education skill for designing practical assessments and grading criteria that measure applied learning outcomes, with rubric engineering delegated to Rubric Designer when a full rubric artifact is required.

## When to Use
- You want assessment criteria for assignments
- You need clear rubrics for practical tasks, individual assignments, projects, or essays
- You need performance-based evaluation instead of quizzes
- Grading standards must be consistent across reviewers
- You need actionable assessment criteria tied to outcomes

## Instructions
1. **Review objectives** - identify what knowledge or skill should be measured
2. **Choose assessment format** - practical task, individual assignment, project, essay, portfolio, or mixed performance assessment; use rubrics as the primary evaluation mechanism
3. **Define assessment criteria scope** - specify what outcomes must be evaluated and which evidence is required
4. **Delegate rubric design** - always use Rubric Designer for rubric tables, level architecture, and descriptor calibration
5. **Define scoring policy** - points, weighting principles, and grading policy expectations
6. **Check alignment** - ensure assessment criteria and rubric outputs map to learning outcomes
7. **Refine for clarity** - remove wording that reveals expected answers or bypasses the intended cognitive challenge

## Tools and Methods
- Bloom taxonomy alignment
- Performance task design
- Assessment design
- Scoring policy design

## Examples
- Practical task: "Implement input validation for the registration form and explain your test cases."
- Individual assignment: "Prepare a one-page architecture decision summary with trade-off analysis."
- Essay assessment: "Explain the CAP theorem and justify one real-world trade-off in 400-600 words."

## Recommendations
- Define assessment scope before requesting rubric detail
- Delegate rubric tables, criteria levels, and descriptor calibration to Rubric Designer
- Keep scoring policy aligned with learning outcomes and assessment stakes
- Include brief feedback guidance for each major assessed area

## Best Practices
- Use assessment formats that require observable learner evidence rather than recall alone
- Keep criteria language explicit enough for inter-reviewer consistency
- Apply scoring weights by learning outcome impact; if impact is unclear, start with equal weights and note the assumption
- Label all inferred assumptions so reviewers can quickly validate them

## Output Contract
- Always structure the response in this order:
	1. Assessment overview
	2. Learning outcomes
	3. Assessment instructions
	4. Rubric requirements or rubric table
	5. Scoring and weighting
	6. Feedback guidance
	7. Alignment check
- Apply this output order within Behavior Priority; if a conflict occurs, prioritize assessment validity first and explicitly note any output-order deviation
- Assessment overview must state assignment type, target level, and scope assumptions
- If a full rubric is required, use Rubric Designer output for section 4
- Scoring and weighting must state total points, weighting model, and pass threshold (if defined)

## Input Recovery Rules
- If assignment type is missing, infer from context and mark assumption explicitly
- If learning outcomes are missing, infer likely outcomes from assignment context and explicitly mark inferred outcomes
- If learning outcomes are vague, rewrite them into measurable statements before assessment design
- If source input is incomplete, produce a minimal viable assessment plan with clearly labeled assumptions
- If rubric-specific input is missing, pass labeled assumptions to Rubric Designer instead of inventing hidden detail
- If constraints conflict, apply this order and explicitly state the final resolution and rationale: assessment validity -> scoring model -> coverage scope
- Ask for clarification only when ambiguity materially affects assessment validity
- Never fabricate external standards, policy requirements, or grading scales that were not provided

## Adaptation Rules
- Adjust rubric complexity and criterion granularity by prioritizing learner level first, assignment duration second, assessment stakes third, and expected autonomy fourth; if factors tie, apply this same order as the tie-break rule
- Adapt assignment framing and evidence expectations to discipline context (for example: software engineering, research writing, mathematics, laboratory work, design, policy analysis)

## Failure Mode Prevention
- Do not reward formatting over demonstrated competency
- Do not request rubric complexity that exceeds assessment value
- Avoid assessment designs that can be completed through shallow copying or generic AI-generated responses without authentic learner reasoning

## Behavior Priority
- Priority order:
	1. Validity of assessment
	2. Clarity of evaluation
	3. Criterion observability
	4. Reviewer consistency
	5. Rubric compactness

## Constraints
- When constraints interact, use this simplified rule: preserve assessment validity first; if validity is unaffected, preserve scoring coherence; then maximize coverage within the remaining scope.
- Assessment validity: define observable outcomes, authentic evidence, and task fit before requesting rubric detail.
- Scoring and coverage: keep weighting coherent, avoid redundant assessed areas, and use Rubric Designer for level architecture and descriptor quality.
