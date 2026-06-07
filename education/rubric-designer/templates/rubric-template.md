# Rubric Template

Reusable template for an analytic grading rubric produced by the Rubric Designer skill. Fill every section; if a section does not apply, write "N/A" and explain why.

---

## Executive Summary

> **The main output of this skill is the Criteria and Levels Table in Section 3.**
>
> All other sections (rubric overview, learning-objective alignment, scoring model, calibration, alignment check, checklist) exist to **support, justify, and validate** this table. The table itself — one row per criterion, one column per compliance level, with observable evidence descriptors in each cell — is the rubric artifact that reviewers will use directly.
>
> When a reviewer opens this document, they should be able to start scoring from Section 3 alone. Sections 1-2 provide context, and Sections 4-7 document how the table was built and verified.

---

## 1. Rubric Overview

- **Assessment name**: _\<name of the assessment tool>_
- **Course / topic / lesson**: _\<course, topic, lesson identifiers>_
- **Rubric type**: _\<binary / multi-level / with penalties / with weights / combined>_
- **Compliance level scale**: _\<e.g., {0, 25, 50, 75, 100}>_
- **Pass threshold (if defined)**: _\<percentage or "not defined">_
- **Scope and assumptions**: _\<inferred objectives, defaults, deviations from skill defaults — list them all>_

## 2. Learning Objectives and Criteria Alignment

Map every learning objective to exactly one criterion. No objective is left un-assessed; no criterion is ungrounded.

| # | Learning objective (measurable) | Criterion ID | Brief evidence check |
| --- | --- | --- | --- |
| LO-1 | _\<objective statement, observable verb>_ | C-1 | _\<what the reviewer looks at>_ |
| LO-2 | _\<...>_ | C-2 | _\<...>_ |
| ... | _\<...>_ | ... | _\<...>_ |

## 3. Criteria and Levels Table ★ **MAIN OUTPUT**

Criteria and Levels table presents an evaluation rubric. This table is the main output artifact.

One row per criterion. Levels are listed in the same order for every criterion. Mark unused cells with `-`.

| ID | Criterion | Weight `q_i` | Penalty `D_i` per error | 0% | 25% | 50% | 75% | 100% | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | _\<one observable competency>_ | _\<int >= 0>_ | _\<int >= 0>_ | _\<evidence missing or wrong>_ | _\<significant errors, blocks goal>_ | _\<material gaps, partial work>_ | _\<minor issues only>_ | _\<fully satisfies criterion>_ | _\<optional reviewer hints>_ |
| C-2 | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ |
| ... | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ |

Sum of weights: _\<sum(q_i) > 0>_. Binary rubrics use only the 0% and 100% columns.

## 4. Scoring Model

State the formula in mathematical form, list every parameter, and show a worked numeric example.

### 4.1 Formula

Write the formula for the rubric type selected in section 1.

Example for the combined rubric:

`P_i = max(0, L_i - k_i * D_i)`

`G = max(0, ( sum(P_i * q_i) / sum(q_i) ) - k * D)`
If the rubric is not combined, replace the example above with the exact formula used.

### 4.2 Parameter legend

| Symbol | Meaning | Value in this rubric |
| --- | --- | --- |
| `N` | number of criteria | _\<N>_ |
| `L_i` | compliance level for criterion `i` | drawn from the level scale |
| `P_i` | score for criterion `i` after penalties | `P_i = max(0, L_i - k_i * D_i)` |
| `k_i` | number of errors counted for criterion `i` | non-negative integer |
| `D_i` | per-criterion penalty per error for criterion `i` | integer; `0` if not used |
| `q_i` | weight of criterion `i` | non-negative integer |
| `k` | total number of errors (for global penalty) | non-negative integer |
| `D` | global penalty per error | integer; `0` if not used |
| `G` | final grade in percent | `0 <= G <= 100` |

### 4.3 Worked Example

Apply the rubric to a sample submission.

| Criterion | `L_i` | `k_i` | `D_i` | `q_i` | `P_i` | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | _\<0/25/50/75/100>_ | _\<int>_ | _\<int>_ | _\<int>_ | _\<int>_ | _\<why this level, this many errors>_ |
| C-2 | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ |
| ... | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ | _\<...>_ |
| **Total** | - | `k =` _\<int>_ | `D =` _\<int>_ | `sum(q_i) =` _\<int>_ | - | `G =` _\<percent>_ |

Show the arithmetic:

`G = ( (P_1 * q_1) + (P_2 * q_2) + ... ) / sum(q_i) - k * D = _\<percent>_`

## 5. Calibration Notes

| Submission type | `G` computed | `G` expected | Match? | Adjustment |
| --- | --- | --- | --- | --- |
| Full-mark sample | _\<...>_ | _\<...>_ | _\<yes/no>_ | _\<change or "none">_ |
| Partial-mark sample | _\<...>_ | _\<...>_ | _\<yes/no>_ | _\<...>_ |
| Near-zero sample | _\<...>_ | _\<...>_ | _\<yes/no>_ | _\<...>_ |

Reviewer disagreements: _\<list and resolution>_.

## 6. Alignment Check

- [ ] Every criterion `C-i` traces to exactly one learning objective `LO-i`
- [ ] No learning objective is un-assessed (or gap is justified below)
- [ ] No criterion is ungrounded by a learning objective
- [ ] Gaps and justifications: _\<list or "none">_

## 7. Structured-Rubric Checklist

- [ ] **Completeness** - all assessed aspects appear as separate criteria
- [ ] **Clarity** - each level describes observable evidence
- [ ] **Operationalization** - criteria and levels are expressed via measurable or verifiable indicators
- [ ] **No subjectivity** - subjective phrases are replaced by concrete evidence indicators
- [ ] **Structuredness** - rubric is tabular with a closed set of allowed values; serializable to JSON or XML
