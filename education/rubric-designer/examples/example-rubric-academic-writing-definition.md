# Example Request - Full Documentation for "What Is Academic Writing?"

This example demonstrates the full-documentation behavior of the Rubric Designer skill. Use it as a reference when the user asks not only for a rubric, but for the full supporting documentation around that rubric.

---

## Executive Summary

> **The main output of this skill is the Criteria and Levels Table in Section 3.**
>
> All other sections (rubric overview, learning-objective alignment, scoring model, calibration, alignment check, checklist) exist to **support, justify, and validate** this table. The table itself — one row per criterion, one column per compliance level, with observable evidence descriptors in each cell — is the rubric artifact that reviewers will use directly.
>
> When a reviewer opens this document, they should be able to start scoring from Section 3 alone. Sections 1-2 provide context, and Sections 4-7 document how the table was built and verified.

---

## Example Request (input to the skill)

> Create a full grading-rubric document for this assignment.
>
> In 120-180 words, answer the question: "What is academic writing?"
>
> Your response must:
>
> - define the concept clearly;
> - identify at least two distinguishing characteristics of academic writing;
> - use precise academic language.
>
> Submission: one short written response.

Inferred learning outcomes are explicitly marked.

The full-documentation response below follows the section order required by the skill.

---

## 1. Rubric Overview

- **Assessment name**: Short written response "What is academic writing?"
- **Course / topic / lesson**: _Inferred_: "Academic Writing" / "Introduction to academic discourse" / "Definition of academic writing"
- **Rubric type**: With weights
- **Compliance level scale**: `{0, 25, 50, 75, 100}`
- **Pass threshold (if defined)**: 60%
- **Scope and assumptions**: All learning objectives below are inferred from the brief. Defaults: 5-level scale, no penalties (`D_i = 0`, `D = 0`). Weighted scoring is used because conceptual correctness matters more than stylistic polish.

## 2. Learning Objectives and Criteria Alignment

| # | Learning objective (measurable) | Criterion ID | Brief evidence check |
| --- | --- | --- | --- |
| LO-1 | _Inferred_: Define academic writing accurately | C-1 | The response states what academic writing is in conceptually correct terms |
| LO-2 | _Inferred_: Distinguish academic writing from informal or everyday writing using observable characteristics | C-2 | The response names and explains at least two distinguishing characteristics |
| LO-3 | _Inferred_: Use clear, precise, and appropriately formal academic language | C-3 | The response is coherent, precise, and uses an appropriate register |

## 3. Criteria and Levels Table

Criteria and Levels table presents an evaluation rubric. This table is the main output.

One row per criterion. Levels are listed in the same order for every criterion. Mark unused cells with `-`.

| ID | Criterion | Weight `q_i` | Penalty `D_i` per error | 0% | 25% | 50% | 75% | 100% | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | Conceptual definition of academic writing | 3 | 0 | No definition is provided, or the response defines a different concept | A definition is attempted, but it is mostly incorrect or seriously misleading | A partially correct definition is given, but it is incomplete or vague | The definition is mostly correct, with a minor conceptual gap or imprecision | The response defines academic writing accurately as a formal, evidence-oriented, structured form of writing used in scholarly or educational contexts | This criterion has the highest weight because it is the core learning objective |
| C-2 | Distinguishing characteristics | 2 | 0 | No distinguishing characteristics are given | One characteristic is named, but it is incorrect, irrelevant, or unexplained | One correct characteristic is explained, or two are listed with minimal explanation | Two correct characteristics are given, but one is under-explained or imprecisely stated | At least two correct distinguishing characteristics are clearly explained, such as formality, evidence use, structure, citation, or audience awareness | Characteristics must distinguish academic writing from informal everyday writing |
| C-3 | Language precision and register | 1 | 0 | The response is incoherent or uses clearly inappropriate language for the task | The response is understandable only in fragments and uses mostly informal or imprecise language | The response is understandable but inconsistent in clarity or register | The response is clear and mostly precise, with minor language or register issues | The response is clear, concise, precise, and consistently appropriate in academic register | This criterion evaluates expression, not conceptual correctness |

Sum of weights: `sum(q_i) = 3 + 2 + 1 = 6`.

## 4. Scoring Model

### 4.1 Formula

```text
G = sum(P_i * q_i) / sum(q_i)
```

### 4.2 Parameter legend

| Symbol | Meaning | Value in this rubric |
| --- | --- | --- |
| `N` | number of criteria | 3 |
| `P_i` | compliance level for criterion `i` | `{0, 25, 50, 75, 100}` |
| `q_i` | weight of criterion `i` | see table in section 3 |
| `G` | final grade in percent | `0 <= G <= 100` |

### 4.3 Worked Example

Sample submission A:

> Academic writing is writing used in universities and research. It is more formal than everyday writing and usually follows a clear structure. It often uses evidence and sources to support ideas. Academic writing tries to explain ideas clearly and objectively.

| Criterion | `P_i` | `q_i` | Contribution | Comment |
| --- | --- | --- | --- | --- |
| C-1 Conceptual definition of academic writing | 75 | 3 | `75 * 3 = 225` | Mostly correct definition; the role of scholarly purpose is implied rather than stated explicitly |
| C-2 Distinguishing characteristics | 100 | 2 | `100 * 2 = 200` | Formality, structure, evidence use, and objectivity are clearly identified |
| C-3 Language precision and register | 75 | 1 | `75 * 1 = 75` | Clear and appropriate overall, but still somewhat generic and repetitive |
| **Total** | - | `sum(q_i) = 6` | `225 + 200 + 75 = 500` | `G = 500 / 6 = 83.33%` |

Arithmetic:

```text
G = ( (75*3) + (100*2) + (75*1) ) / 6
  = ( 225 + 200 + 75 ) / 6
  = 500 / 6
  = 83.33%
```

Result: **83.33%**.

## 5. Calibration Notes

| Submission type | `G` computed | `G` expected | Match? | Adjustment |
| --- | --- | --- | --- | --- |
| Full-mark sample: accurate definition, at least two well-explained characteristics, precise academic register | 100% | 100% | yes | none |
| Partial-mark sample: the worked example above | 83.33% | 80-85% | yes | none |
| Near-zero sample: "Academic writing is when students write anything for class" | `((25*3) + (0*2) + (25*1)) / 6 = 16.67%` | 10-20% | yes | none |

Reviewer disagreements: one reviewer initially wanted to give full credit on C-1 to any response mentioning formality and sources. Resolution: keep C-1 at 75 unless the response explicitly defines the concept itself, not just its features.

## 6. Alignment Check

- [x] Every criterion `C-i` traces to exactly one learning objective `LO-i`
- [x] No learning objective is un-assessed
- [x] No criterion is ungrounded by a learning objective
- [x] Gaps and justifications: none

Traceability summary: `C-1 -> LO-1`, `C-2 -> LO-2`, `C-3 -> LO-3`.

## 7. Structured-Rubric Checklist

- [x] **Completeness** - definition, distinguishing characteristics, and language quality are each assessed explicitly
- [x] **Clarity** - each level describes observable qualities of the written response
- [x] **Operationalization** - the rubric checks definition accuracy, number and quality of characteristics, and register precision
- [x] **No subjectivity** - vague praise is avoided; criteria specify what evidence the response must contain
- [x] **Structuredness** - the rubric uses a fixed level scale and a weighted scoring model that can be represented in table, JSON, or XML form
