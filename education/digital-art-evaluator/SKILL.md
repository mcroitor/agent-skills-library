---
name: digital-art-evaluator
description: Evaluate digital artwork based on assignment compliance, technical skill, and tool utilization. Use for grading student art projects, analyzing technical execution, and assessing the appropriateness of digital tools.
---

# Digital Art Evaluator

## Description
A specialized education skill for the objective and technical evaluation of digital artwork. It focuses on the alignment between the final piece and the assignment requirements, the level of the student's technical proficiency in drawing and digital art, the effective use of digital tools and software, and the fair handling of modern digital and AI-assisted workflows.

## When to Use
- You need to grade a student's digital art submission against a specific brief
- You want to assess a student's technical skill level (e.g., anatomy, perspective, color theory)
- You need to evaluate if the chosen digital tools (brushes, layers, software features) were used correctly and effectively
- You are providing constructive feedback on a digital art piece to help a student improve
- You need to determine if a piece of art meets the technical requirements of a course module

## Instructions
1. **Analyze the Assignment Brief** - Identify the core requirements, constraints, and goals of the task (e.g., "create a character concept using complementary colors").
2. **Evaluate Assignment Compliance** - Compare the submitted artwork against the brief. Check for missing elements, ignored constraints, or successful fulfillment of goals.
3. **Assess Technical Drawing Skills** - Analyze fundamental art principles:
    - **Composition & Perspective**: Balance, focal points, and spatial accuracy.
    - **Anatomy & Form**: Proportions, volume, and structural integrity.
    - **Color & Lighting**: Value range, color harmony, and light source consistency.
    - **Line Work & Rendering**: Confidence of lines, blending quality, and edge control.
4. **Evaluate Tool Utilization** - Analyze the technical digital execution:
    - **Software Proficiency**: Use of layers, masks, blending modes, and selection tools.
    - **Brushwork**: Appropriateness of brush choices for the intended effect.
    - **Workflow Efficiency**: Evidence of non-destructive editing or advanced tool usage (if required).
    - **Appropriateness Over Complexity**: Evaluate tool usage based on fitness for the assignment and result, not on the sheer number of advanced features used.
5. **Synthesize Findings** - Combine the compliance, skill, and tool analysis into a coherent evaluation.
6. **Formulate Feedback** - Provide specific, actionable advice for improvement based on the identified gaps.
7. **Handle AI-Assisted Cases** - When AI assistance is visible or declared, distinguish between original student execution, paint-over/editing, and generated content; then check whether that workflow complies with the assignment policy.

## Priority Rules
- Prioritize in this order:
  1. Assignment Compliance (Did they do what was asked?)
  2. Technical Execution (Is the art fundamentally sound?)
  3. Tool Proficiency (Did they use the digital medium effectively?)
  4. Aesthetic Appeal (Is the final result visually pleasing?)
- If priorities conflict, resolve them by strictly following the order above.
- Technical inaccuracies that materially reduce readability, structure, or visual communication must lower the evaluation even when the piece is aesthetically appealing.

## Output Contract
- Return output in this order:
    1. **Compliance Summary**: A clear statement on whether the artwork meets the assignment requirements.
    2. **Technical Skill Analysis**: Detailed breakdown of drawing fundamentals (Perspective, Anatomy, Color, etc.).
    3. **Tool & Technique Evaluation**: Analysis of the digital tools and methods used.
    4. **AI/Process Note**: Only when relevant; state whether AI assistance or process constraints affected the evaluation.
    5. **Overall Grade/Rating**: Based on the provided rubric or a general scale.
    6. **Actionable Feedback**: Specific steps the student can take to improve.
- Use a structured format (bullet points or tables) for the analysis sections.
- When rubric criteria are provided, score each criterion independently and justify deductions with observable evidence rather than averaging unrelated weaknesses.

## Evaluation Calibration
- Beginner: prioritize demonstrated understanding of fundamentals and assignment intent over polish.
- Intermediate: expect consistency, clearer intentionality, and better control of drawing and workflow decisions.
- Advanced: expect strong structural accuracy, deliberate artistic choices, and disciplined digital workflow execution.
- Calibrate grades against learner level first; do not inflate scores solely because the result is visually attractive.

## Optional Rubric Mode
- When rubric criteria are provided, evaluate each criterion independently.
- Justify each deduction with observable evidence from the artwork or stated process notes.
- Avoid averaging unrelated categories when one major criterion clearly fails.
- If rubric weights are missing, assume equal weighting and mark the assumption explicitly.

## Input Recovery Rules
- If the assignment brief is missing, ask the user for the requirements or infer them from the context and mark them as assumptions.
- If the artwork is provided without technical details (e.g., no layer info), evaluate based on the visible final result and note the limitation.
- If the student's level (beginner/intermediate/advanced) is unknown, assume a baseline based on the course context and explicitly state this.
- Do not infer advanced workflow usage, AI assistance, or hidden process quality without visible evidence or an explicit process description.
- Separate directly observable evidence from probable assumptions whenever the source material is incomplete.

## AI-Assisted Artwork Handling
- Distinguish between original student execution, AI-assisted ideation, paint-over, compositing, and fully generated output when possible.
- Evaluate whether AI usage complies with the assignment or course policy before treating it as a quality factor.
- Do not penalize AI-assisted workflows unless they violate explicit assignment requirements, disclosure rules, or learning objectives.
- If AI involvement is suspected but unconfirmed, label it as uncertainty rather than as a violation.

## Constraints
- Do not confuse "personal style" with "technical error" unless the style violates the assignment brief.
- Avoid vague praise (e.g., "looks great"); use descriptive, technical language (e.g., "strong use of atmospheric perspective").
- Ensure feedback is constructive and tied to observable evidence in the artwork.
- Do not reward tool complexity by itself; reward appropriate and effective tool use.
- Do not treat missing workflow evidence as proof of poor process quality.

## Tools and Methods
- Formal Analysis of Art
- Digital Art Workflow Audit
- Color Theory Application
- Anatomical and Perspective Validation
- Rubric-based Grading
- AI-assisted workflow review

## Best Practices
- Reference specific areas of the image when giving feedback.
- Distinguish between "conceptual failure" (wrong idea) and "technical failure" (wrong execution).
- Encourage the use of industry-standard digital techniques (e.g., non-destructive workflows).
- Align the rigor of the evaluation with the student's current educational level.
- Mark confidence limits when the evaluator only has access to the final exported image.
