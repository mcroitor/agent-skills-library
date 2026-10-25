---
name: skill-creator
description: Create new agent skills (SKILL.md plus optional templates, references, examples, scripts) that follow the repository skill specification, or revise existing ones. Use when asked to create, write, draft, convert into, review, validate, or improve a skill, SKILL.md, skill frontmatter, or skill description, including turning a prompt, workflow, or checklist into a reusable skill. Not for executing a skill's own task or for general prompt writing.
---

# Skill Creator

## Description
A skill for designing and writing agent skills that comply with the repository SKILL.md specification, with a discoverable description, a clear execution workflow, and bundled resources only where they help. It also validates and revises existing skills.

## When to Use
- Creating a new skill from an idea, a prompt, a workflow, or a checklist
- Converting an existing document or process into a skill folder
- Reviewing or validating a skill against the specification
- Improving a skill's description, structure, constraints, or output contract
- Splitting an oversized SKILL.md into SKILL.md plus resource files
- Preparing templates, examples, or references for a skill

## Instructions
1. **Clarify the purpose** - establish what task the skill performs, who or what triggers it, expected inputs and outputs, the skill category (development, education, testing, or common), and what is out of scope; gather missing details as set out in Input Recovery Rules
2. **Choose the name** - pick a short, descriptive name that satisfies the naming rules in Constraints and equals the folder name
3. **Write the frontmatter** - write the required fields within the limits in Constraints; the description states what the skill does, when to use it, discovery keywords, and, when neighbors exist, what it does not cover; add `license`, `compatibility`, `metadata`, or `allowed-tools` only when there is a real need
4. **Write the required body** - cover the mandatory body elements listed in Constraints with concrete scenarios and executable steps
5. **Add recommended sections selectively** - choose from Tools and Methods (or Tools and Practices), Technologies and Standards, Best Practices, Constraints, Output Contract, Input Recovery Rules, and Priority Rules; include a section only when it carries content that no other section already states
6. **Move bulk into resources** - put reusable output structures in `templates/`, background material in `references/`, demonstrations in `examples/`, executable tooling in `scripts/`, and static files in `assets/`; link them with relative paths from SKILL.md
7. **Validate** - run the [validation script](./scripts/validate_skill.py) for mechanical checks, then review the content against the [validation checklist](./references/validation-checklist.md), resolve doubts against the [specification](./references/skill.spec.md), and run the discovery check; a successful script run alone does not confirm conformance; fix every error and review each warning
8. **Deliver** - return the skill folder with the structure given in the Output Contract, and report assumptions made, the validation result, and open questions

## Tools and Methods
- The [skill template](./templates/skill-template.md) as the starting skeleton
- The [specification](./references/skill.spec.md) as the authoritative source for structure, section semantics, and naming; read it when the checklist does not settle a question
- The [validation checklist](./references/validation-checklist.md) for a quick review against the specification
- `scripts/validate_skill.py` for mechanical checks only: frontmatter fields and limits, required sections, step format, size, relative links, and empty folders; it does not judge description quality, rule duplication, section semantics, contradictions between sections, or the choice of recommended sections, which are reviewed by hand
- Discovery check: write three to five realistic user requests that should trigger the skill and two that should not, and confirm that the description separates them

## Best Practices
- Write the description for discovery: lead with what the skill does, then "Use when ..." with concrete task phrases users actually type
- Keep each instruction an action ("define", "extract", "compare") with a clear completion condition
- Keep the semantic boundaries: Instructions say what to do, Constraints say what never to do, Best Practices say what is preferable, Recommendations say what to consider, Priority Rules say how to resolve conflicts
- State each rule once; refer to another section instead of repeating it
- Put the most important information early; prefer 20-80 lines for simple skills and stay under 500 lines overall
- Match section names to the category conventions, for example Tools and Methods for research and education skills and Tools and Practices for technical ones

## Constraints
- Frontmatter must contain `name` and `description`
- `name`: lowercase letters, numbers, and single hyphens; at most 64 characters; no leading or trailing hyphen; identical to the folder name
- `description`: at most 1024 characters; `compatibility` (if present): at most 500 characters
- The body must contain `# Title`, `## Description` (at most two sentences), `## When to Use` (bulleted scenarios), and `## Instructions` (numbered steps, each written as a bold name, a hyphen, and a brief description)
- Do not invent frontmatter fields, tools, or sections that the specification does not allow without a stated domain reason
- Do not link to files, scripts, or skills that do not exist in the skill folder or the target repository
- Do not include secrets, credentials, or personal data in a skill or its examples
- Do not present a skill as conformant on the strength of the script alone, or as validated unless the checks were actually run

## Output Contract
Return the skill as a folder:

```text
skill-name/
├── SKILL.md
├── templates/     (only if used)
├── references/    (only if used)
├── examples/      (only if used)
├── scripts/       (only if used)
└── assets/        (only if used)
```

After the files, give a short report in this order: assumptions made; validation results, reported separately as script errors and warnings and as findings of the manual checklist review and discovery check; and open questions for the user. Create only the folders that contain files.

## Input Recovery Rules
- Use the available context first (the conversation, attached files, existing skills in the repository); ask only about decisions that materially change the result, such as scope boundaries, category, output format, or a name conflict; for everything else proceed with stated assumptions and list them in the report
- If the request is only a vague idea, ask one short batch of questions when the scope cannot be bounded without them; otherwise draft the skill with stated assumptions
- If the user supplies a prompt, workflow, or document, extract purpose, steps, constraints, and outputs from it and map them to the specification sections without adding unrelated rules
- If an existing skill is supplied, keep its name, section order, and wording where they are correct, and change only what the request or the validation requires
- If the category is unclear, use the Common/General conventions: Tools and Methods, Best Practices, Examples, and a simple structure
- If the target repository provides its own, newer specification, follow it over the bundled copy and say so

## Priority Rules
Prioritize in this order when requirements conflict:
1. Compliance with the standard-required elements (frontmatter, `name`, `description`)
2. Compliance with the repository-required sections and formats
3. Fidelity to the user's intent and domain
4. Discoverability of the skill through its description
5. Clarity and non-redundancy of instructions and constraints
6. Concision and progressive disclosure

## Examples
- Weak description: "Helps with documents." Strong description: "Extract tables and text from PDF files, merge or split them, and fill forms. Use when the user mentions a PDF file or asks to produce one. Not for Word or spreadsheet files."
- Weak step: "**Handle input** - deal with the data." Strong step: "**Validate input** - check the file for required columns and report missing ones before processing."
