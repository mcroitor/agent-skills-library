---
name: rubric-designer
description: Design grading rubrics with observable criteria. Use for creating analytic and holistic rubrics, defining level descriptors, and ensuring consistent scoring across reviewers.
---

# Rubric Designer

## Description
A specialized education skill for designing analytic and holistic grading rubrics with observable criteria, level descriptors, and consistent scoring logic.

## When to Use
- You need a reusable rubric for practical tasks, projects, or essays
- Criteria and levels must be explicit for multiple reviewers
- You need stable scoring across learners and cohorts
- Rubric quality must be validated before assessment use
- Assessment Writer requires a dedicated rubric design step

## Instructions
1. **Review input context** - assignment type, learning outcomes, learner level, and assessment stakes
2. **Select rubric strategy** - analytic by default; holistic only for rapid overall evaluation
3. **Define criteria** - one observable competency per criterion with independent assessability
4. **Set level architecture** - 3-5 levels per criterion, including minimum-performance and full-alignment anchors
5. **Write level descriptors** - measurable, non-overlapping evidence language per level
6. **Define scoring model** - weights, normalization, total points, and pass threshold (if needed)
7. **Validate rubric quality** - coverage, consistency, and conflict checks before output

## Priority Rules
- Prioritize in this order:
  1. Criterion observability
  2. Rubric validity
  3. Reviewer consistency
  4. Scoring completeness
  5. Output compactness
- If priorities conflict, resolve them by strictly following the order above; when priorities feel equally relevant, prioritize criterion observability first
- Example: if output compactness conflicts with reviewer consistency, keep reviewer consistency and reduce compactness

## Output Contract
- Return output in this order: rubric overview, criteria table, scoring model, calibration notes, alignment check
- Rubric must be presented as a structured table
- Criteria table must include: criterion, level scale, descriptors, and weight
- Alignment check must map each criterion to one learning outcome

## Input Recovery Rules
- If learning outcomes are missing, infer likely outcomes from assignment context and mark assumptions
- If assignment context is incomplete, generate a minimal viable rubric and mark unknown fields
- Ask for clarification only when ambiguity prevents defining observable criteria or level descriptors
- Never fabricate external standards, policy requirements, or grading scales

## Constraints
- Apply constraints in this sequence: descriptor validity first, then scoring consistency, then format compactness
- Do not output criteria that are not observable in submitted evidence
- Do not use overlapping descriptors that can map to multiple levels simultaneously
- Do not produce inconsistent level counts across criteria unless explicitly requested

## Criterion Quality Rules
- Each criterion measures exactly one observable competency
- Criteria are independently assessable
- Level descriptors are distinct, measurable, and non-overlapping
- Criteria in one rubric use the same level count
- Weights sum to 100% (or are explicitly normalized)

## Descriptor Language Rules
- Use observable evidence verbs: identifies, applies, compares, justifies, documents
- Avoid subjective labels without evidence indicators

## Calibration Guidance
- Adjacent levels must differ by observable evidence quality, not wording intensity

## Failure Prevention
- Do not reward formatting over demonstrated competency
- Do not duplicate the same competency across criteria
- Do not create criteria that cannot realistically be observed

## Tools and Methods
- Analytic rubric design
- Holistic rubric design
- Objective-to-criterion mapping
- Descriptor calibration
- Criterion-based scoring

## Best Practices
- Keep criteria concise, evidence-based, and reviewer-testable
- Calibrate adjacent levels with concrete evidence thresholds
- Validate weights against assessment stakes before finalizing rubric
- Preserve rubric compactness without sacrificing criterion validity
