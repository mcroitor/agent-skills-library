---
name: quiz-developer
description: Create quizzes, exams, and question banks. Use for generating test questions, building question pools, and aligning assessments with learning objectives.
---

# Quiz Developer

## Description
A specialized education skill for creating quizzes, exams, question banks, and practice tests from source material or course content.

## Priority Rules
Prioritize in this order when trade-offs conflict; if two priorities are equally important or directly conflict, prefer the one listed higher:
1. Learning objective alignment
2. Question validity and clarity
3. Coverage and difficulty balance
4. Production efficiency
- Example: if production efficiency conflicts with question validity and clarity, keep validity and clarity and reduce efficiency.

## When to Use
- You need a bank of questions based on course material
- You need quizzes or exams aligned with learning objectives
- Practice tests must cover the same topic from different angles
- Learners need reusable question sets for revision
- Questions should vary in difficulty and format
- You need answer keys and explanations for practice

## Instructions
1. **Review objectives** - identify what knowledge or skill should be measured
2. **Analyze source material** - extract the key topics, facts, and concepts
3. **Group content areas** - organize material into question domains
4. **Generate question bank** - create multiple questions per topic
5. **Vary question types** - single choice, multiple select, short answer, essay, and scenario-based items
6. **Balance difficulty** - mix recall, application, and analysis questions
7. **Provide answer keys** - correct answers with short explanations
8. **Check alignment and coverage** - ensure each item maps to outcomes and major topics are represented
9. **Review clarity** - remove ambiguity and keep wording consistent

## Input Recovery Rules
- Infer a minimal question blueprint when objectives are incomplete and mark assumptions
- Assume mixed learner ability when difficulty targets are missing and state the default split
- Ask for clarification only when ambiguity prevents objective mapping or valid answer key design

## Tools and Methods
- Question bank design
- Topic coverage mapping
- Single-choice item design (one correct option)
- Multiple-select item design (one or more correct options)
- Short-answer and essay prompts
- Answer key generation
- Practice test assembly
- Difficulty balancing

## Examples
- Single choice: "Which statement best explains the difference between authentication and authorization?"
- Multiple select: "Select all practices that reduce SQL injection risk."
- Short answer: "In 2-3 sentences, describe why indexing improves query performance."
- Scenario-based: "Given this outage timeline, choose the most likely root-cause category."

## Recommendations
- Map each question to one learning outcome before drafting the final set
- Keep wording concise and avoid domain jargon unless it is explicitly being assessed
- Use a balanced mix of difficulty levels and question formats
- Include brief answer rationales for complex or high-stakes items

## Constraints
- Do not test multiple unrelated objectives in a single question
- Do not include clues that reveal the correct answer unintentionally
- Do not use ambiguous wording that allows multiple interpretations
- Do not overload tests with redundant questions that do not improve coverage

## Output Contract
Return all of the following:
1. Quiz scope and assumptions
2. Question set grouped by objective/topic
3. Difficulty distribution summary
4. Answer key with rationales
5. Coverage and alignment check

## Best Practices
- Keep each question focused on one clearly testable competency
- Prefer plausible distractors over trick options
- Validate item difficulty against target learner level
- Ensure answer rationales explain why alternatives are incorrect when useful
