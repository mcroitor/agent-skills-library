---
name: curriculum-developer
description: Build course and module structures from learning goals. Use for curriculum mapping, lesson sequencing, pacing design, and outcome-aligned assessments.
---

# Curriculum Developer

## Description
A specialized education skill for creating course structures, modules, lessons, and teaching sequences from learning goals and subject matter. One module = one lecture (mandatory) + one lab (optional) + individual work (optional).

## Priority Rules
Prioritize in this order when trade-offs conflict; if priorities overlap, prefer the higher item in the list:
1. Learning outcome alignment
2. Prerequisite coherence and sequencing
3. Learner workload balance
4. Reusability and maintainability

## When to Use
- You need a full course or module structure
- Learning goals must be turned into lesson plans
- Content needs to be organized for teaching
- Multiple lessons must build toward a final outcome
- You need a reusable curriculum framework

## Instructions
1. **Define course purpose** - audience, level, and expected results
2. **Break into modules** - themes, learning units, and lesson boundaries
3. **Design lesson flow** - intro, explanation, practice, and recap
4. **Align activities** - exercises, examples, and assignments to outcomes
5. **Add pacing guidance** - duration, sequencing, and workload balance
6. **Include assessments** - quizzes, tasks, or checkpoints per module
7. **Review coherence** - ensure lessons build logically toward the goal

## Required Input Data
The following must be provided (or explicitly defaulted) before generating a curriculum:

| Data | Description | Example |
| --- | --- | --- |
| `total_hours` | Total academic hours for the course | 120 |
| `theory_hours` | Lecture/theory hours | 30 |
| `lab_hours` | Laboratory hours (0 if none) | 45 |
| `individual_work_hours` | Individual work hours (0 if none) | 45 |
| `num_sessions` | Number of lecture sessions | 15 |
| `audience` | Target learner group and level | 2nd year, Game Design |
| `subject` | Course subject and scope | C++ Programming |

If any value is missing, infer it from the available data and label the assumption explicitly.

## Input Recovery Rules
- Infer a minimal course outline when subject depth or duration is missing and label assumptions
- Infer prerequisite level from stated audience when prior knowledge is not provided
- Infer `total_hours`, `theory_hours`, `lab_hours`, `individual_work_hours`, and `num_sessions` from any subset using typical ratios (e.g., 1 theory hour → 1.5 lab + 1.5 individual work) and label all assumptions
- Ask for clarification only when ambiguity prevents outcome alignment or sequencing decisions

## Constraints
- Do not include lessons that are not tied to explicit learning outcomes
- Do not sequence advanced topics before prerequisite concepts
- Do not overload modules with workload that exceeds the stated learning pace
- Every lecture must map to at least one learning outcome
- Lab and individual work hours must not exceed `lab_hours` and `individual_work_hours` respectively

## Tools and Methods
- Curriculum mapping
- Module and lesson planning
- Outcome alignment
- Teaching sequence design
- Rubric-aware structuring

## Output Contract
Return all of the following sections. Use the template at `templates/curriculum-template.md` for a reusable structure.

### 1. Course card
Course title, faculty, program, author, semester, total hours breakdown (theory, lab, individual work), evaluation form, credits.

### 2. Lecture-based pacing table (separate table)
One row per lecture session. Group rows by module (Roman numeral headers). Columns:

| Nr. | Topic | Theory | Lab | Individual work |
| --- | --- | --- | --- | --- |
| I. | **Module title** | _hrs_ | _hrs_ | _hrs_ |
| 1. | Lecture title | _hrs_ | _hrs_ | _hrs_ |
| 2. | Lecture title | _hrs_ | _hrs_ | _hrs_ |

The sum of Theory, Lab, and Individual work columns must match `theory_hours`, `lab_hours`, and `individual_work_hours` respectively.

### 3. Competencies and learning outcomes
List general and professional competencies, plus learning outcomes with codes.

### 4. Learning outcomes per module
For each module: content units, key terms, expected outcomes, abilities, responsibility and autonomy descriptors.

### 5. Individual work descriptions
For each individual assignment: expected product, implementation strategy, evaluation criteria, deadline.

### 6. Assessment plan
Formative and summative assessment methods, grading formula, exam structure.

### 7. Methodical suggestions
Teaching-learning-evaluation methodology description.

### 8. Recommended bibliography
Sources in standard citation format.

## Best Practices
- Keep each module focused on a small set of measurable outcomes
- Use consistent lesson templates to improve delivery quality
- Validate sequencing by dependency, not by topic preference
- Include periodic checkpoints to detect pacing issues early
- Reuse the curriculum template at `templates/curriculum-template.md` for consistent artifacts
