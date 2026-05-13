# SKILL.md Specification

This document combines two layers:

- the baseline requirements from the [Agent Skills Open Standard](https://agentskills.io/) and [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
- the repository conventions used in this project to keep skills consistent and easier to review

---

## Directory Structure

A skill is a folder containing a `SKILL.md` file with optional subdirectories for resources:

```text
skill-name/
├── SKILL.md                          # Required — frontmatter + instructions
├── scripts/                          # Optional: executable code (.py, .js, .sh, .ps1)
├── references/                       # Optional: informational material
├── templates/                        # Optional: reusable prompt/output templates
├── examples/                         # Optional: demonstrations and samples
└── assets/                           # Optional: static support files
```

### Directory Purpose Reference

| Folder | Purpose | Example Content |
| ------ | ------- | --------------- |
| `scripts/` | Executable tooling | `analyze.py`, `validate.sh` |
| `references/` | Informational material | `policy.md`, `api-docs.md` |
| `templates/` | Reusable templates | `prompt-template.md`, `output-schema.json` |
| `examples/` | Demonstrations | `example-input.md`, `example-output.md` |
| `assets/` | Static support files | `styles.css`, `images/` |

**Note**: Start with `references/` and `assets/` as defined in the base standard. Add `templates/`, `examples/` as the ecosystem grows.

---

## Template

```markdown
---
name: [skill-name]
description: [What the skill does and when to use it. Include keywords for discovery.]
license: [Optional: Apache-2.0, MIT, etc.]
compatibility: [Optional: environment requirements]
metadata:
  author: [Optional: author name]
  version: "1.0"
---

# [Skill Name]

## Description
[Short 1-2 sentences about the skill purpose]

## When to Use
- [Use case 1]
- [Use case 2]
- [Use case N]

## Instructions
1. **[Step 1]** - [brief description]
2. **[Step 2]** - [brief description]
3. **[Step N]** - [brief description]

## [Optional Sections]

### Tools and Methods / Tools and Practices
- [Tool/method 1]
- [Tool/method N]

### Technologies and Standards
- [Technology 1]
- [Technology N]

### Best Practices
- [Best practice 1]
- [Best practice N]

### Examples
- [Example 1]
- [Example N]

### Recommendations
- [Recommendation 1]
- [Recommendation N]

### Constraints
- [Constraint 1]
- [Constraint N]

### Deliverables / Artifacts
- [Deliverable 1]
- [Deliverable N]

### Output Contract
[Structure and order of the skill output]

### Input Recovery Rules
[How to handle missing or incomplete input]

### Priority Rules
[How to resolve conflicts between requirements]

### [Custom Sections]
[Any additional domain-specific sections]
```

---

## Frontmatter Specification

| Field           | Required | Description                                                                                                                                                                |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`          | Yes      | Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen or contain consecutive hyphens. Must match the parent directory name. |
| `description`   | Yes      | What the skill does and when to use it. Max 1024 characters. Should include keywords that help agents identify relevant tasks.                                             |
| `license`       | No       | License name or reference to a bundled license file.                                                                                                                       |
| `compatibility` | No       | Max 500 characters. Indicates environment requirements (intended product, system packages, network access, etc.).                                                          |
| `metadata`      | No       | Arbitrary key-value mapping for additional metadata (author, version, etc.).                                                                                               |
| `allowed-tools` | No       | Space-delimited list of pre-approved tools the skill may use. Experimental — support may vary between agent implementations.                                               |

---

## Section Explanations

The open standard requires YAML frontmatter with `name` and `description`. The markdown body is flexible. In this repository, the sections below are project conventions that make skills more predictable and easier to compose.

### Section Status Matrix

Use this matrix as a fast validation checklist when reviewing or creating a skill.

| Element | Status | Notes |
| ------- | ------ | ----- |
| YAML frontmatter | standard-required | Must include at least `name` and `description` |
| Frontmatter `name` | standard-required | Must match the parent directory name |
| Frontmatter `description` | standard-required | Used for discovery and skill selection |
| `# Title` | repo-required | Human-readable title aligned with the skill name |
| `## Description` | repo-required | Body-level description for quick understanding |
| `## When to Use` | repo-required | Primary activation scenarios |
| `## Instructions` | repo-required | Ordered execution workflow |
| `## Tools and Methods` / `## Tools and Practices` | recommended | Use when the skill depends on specific tools or methods |
| `## Technologies and Standards` | recommended | Especially useful for development-oriented skills |
| `## Best Practices` | recommended | Preferred patterns that improve outcomes |
| `## Constraints` | recommended | Hard boundaries, prohibitions, or non-negotiable rules |
| `## Output Contract` | recommended | Strongly preferred when output structure matters |
| `## Input Recovery Rules` | recommended | Strongly preferred when inputs may be incomplete or ambiguous |
| `## Priority Rules` | recommended | Strongly preferred when requirement conflicts are likely |
| `## Examples` | optional | Add when examples materially improve clarity |
| `## Recommendations` | optional | Use for lower-priority guidance |
| `## Deliverables` / `## Artifacts` | optional | Use when the skill produces tangible outputs |
| Custom sections | optional | Add only when they carry domain-specific value |

### Repository-Required Sections

#### YAML Frontmatter

Metadata in YAML format at the top of the file, enclosed by `---`.

- **Status**: Required
- **Purpose**: Skill discovery and identification
- **Important**: `name` must match the folder name exactly

#### `# Title`

The human-readable skill name in the markdown body. It should correspond to the frontmatter `name`, but does not need to use the same slug format.

- **Status**: Required in this repository
- **Format**: `# [Skill Name]`
- **Example**: `# PHP Developer`

#### `## Description`

A concise 1-2 sentence summary of what the skill does and its value.

- **Status**: Frontmatter description is required by the standard; body description is required in this repository
- **Purpose**: Quick understanding of skill purpose
- **Note**: Frontmatter `description` is for discovery, body `## Description` can provide more detail

#### `## When to Use`

Bullet list of scenarios where this skill should be applied.

- **Status**: Required in this repository
- **Purpose**: Help users/agents know when to use this skill
- **Format**: Bulleted list with "-" or "*"
- **Example**:

  - Building web applications in PHP
  - Creating REST APIs and backend services

#### `## Instructions`

Numbered step-by-step workflow for executing the skill.

- **Status**: Required in this repository
- **Purpose**: Core actionable guidance
- **Format**: Numbered list with bold step names
- **Execution**: Default execution workflow unless the skill explicitly defines alternative flow behavior
- **Example**:

  1. **Understand requirements** - define behavior and constraints
  2. **Plan structure** - use MVC or layered architecture

---

### Optional Sections

#### `## Tools and Methods` / `## Tools and Practices`

Tools, frameworks, and methodologies used by this skill.

- **Status**: Optional (recommended)
- **When to use**: When the skill involves specific tools or methodologies
- **Naming**: Use either "Tools and Methods" or "Tools and Practices" consistently within a category

#### `## Technologies and Standards`

Programming languages, frameworks, libraries, and technical standards.

- **Status**: Optional (recommended for development skills)
- **When to use**: When the skill requires specific technologies

#### `## Best Practices`

Recommended approaches and patterns to follow.

- **Status**: Optional (recommended)
- **When to use**: When there are clear best practices to follow

#### `## Examples`

Concrete examples of inputs, outputs, or use cases.

- **Status**: Optional
- **When to use**: When examples help clarify skill usage

#### `## Recommendations`

Suggested approaches and guidance.

- **Status**: Optional
- **When to use**: When there are recommendations that don't fit "Best Practices"

#### `## Constraints`

Explicit limitations, boundaries, or rules to follow.

- **Status**: Optional
- **When to use**: When the skill has specific constraints to observe

#### `## Deliverables` / `## Artifacts`

Expected outputs or tangible results from using the skill.

- **Status**: Optional
- **When to use**: When the skill produces specific deliverables

#### `## Output Contract`

Defines the structure and order of the skill's output.

- **Status**: Optional
- **When to use**: When the skill has strict output formatting requirements
- **Note**: Can be used in any skill, not just education

#### `## Input Recovery Rules`

Rules for handling missing, incomplete, or ambiguous input.

- **Status**: Optional
- **When to use**: When the skill needs to handle various input scenarios gracefully
- **Note**: Can be used in any skill, not just education

#### `## Priority Rules` / `## Behavior Priority`

Defines how to resolve conflicts between requirements or behaviors.

- **Status**: Optional
- **When to use**: When there are competing priorities to resolve
- **Note**: Can be used in any skill, not just education
- **Semantics**: Overrides the default execution strength ordering within the scope of the skill

#### `## [Custom Sections]`

Any additional domain-specific sections tailored to the skill.

- **Status**: Optional
- **Examples**: Docker, GitHub Actions, MariaDB Focus Areas, Plugin Types
- **When to use**: When domain-specific subdivisions are needed

---

## Naming Conventions

### Frontmatter `name` Field

- Max 64 characters
- Lowercase letters, numbers, and hyphens only
- Must not start or end with a hyphen
- Must not contain consecutive hyphens
- Must match the parent directory name exactly

### Tools Section Variants

To ensure consistency, use these preferred names:

- `Tools and Methods` - for methodology-heavy skills (research, education)
- `Tools and Practices` - for practical/technical skills
- `Tools` - only when it's a simple list without methods

### Technology Section Variants

- `Technologies and Standards` - preferred for development skills
- `Technologies and Stacks` - when emphasizing full stack combinations

### Output Section Variants

- `Deliverables` - for skills producing tangible outputs
- `Artifacts` - for skills producing documentation/specific items
- `Output Contract` - for skills with strict output structure

---

## Section Semantics

Clear behavioral distinctions between sections help agents understand execution priority:

| Section | Execution Behavior |
| ------- | ------------------ |
| **Instructions** | Mandatory execution workflow — must be followed in order |
| **Constraints** | Hard prohibitions or requirements — must not be violated |
| **Best Practices** | Preferred approaches — follow unless conflicting with constraints |
| **Recommendations** | Optional guidance with lowest priority — follow when helpful |
| **Priority Rules** | Conflict resolution logic — defines how to resolve competing requirements |

### Semantic Boundaries

- **Instructions** = "what to do" (mandatory sequence)
- **Constraints** = "what NOT to do" or "must have" (hard boundaries)
- **Best Practices** = "how to do better" (preferred but not required)
- **Recommendations** = "consider doing" (optional, lowest priority)
- **Priority Rules** = "when conflicts arise" (resolution logic)

---

## Execution Strength Semantics

Instruction strength hierarchy helps orchestration, merging, and conflict resolution:

| Section | Strength | Description |
| ------- | -------- | ----------- |
| **Instructions** | strong | Default ordered workflow unless the skill defines an alternative flow |
| **Constraints** | absolute | Cannot be violated under any circumstances |
| **Best Practices** | medium | Recommended approach, deviation allowed with justification |
| **Recommendations** | weak | Optional guidance, lowest execution priority |
| **Priority Rules** | varies | Defines resolution when other sections conflict and can override the default ordering within the skill |

This hierarchy enables:

- Automated conflict resolution between skills
- Skill merging with clear precedence
- Validation of skill consistency
- Orchestration of multiple skills

---

## Progressive Disclosure

Agent Skills use a four-stage progressive disclosure pattern to minimize context usage:

1. **Advertise** (~100 tokens per skill) — Skill names and descriptions are injected into the system prompt, so the agent knows what skills are available.

2. **Load** (< 5000 tokens recommended) — When a task matches a skill's domain, the agent loads the full SKILL.md body with detailed instructions.

3. **Read resources** (as needed) — The agent fetches supplementary files (references, templates, assets) only when required.

4. **Run scripts** (as needed) — The agent executes scripts bundled with a skill.

**Keep SKILL.md under 500 lines** as a guideline, and move detailed reference material to separate files in `references/` or `assets/` when the file becomes too large.

---

## Category-Specific Conventions (Optional)

These are helpful patterns, not rigid requirements. Use them as guidance when writing skills for these domains.

### Development Skills

Common sections:

- Technologies and Standards
- Tools and Practices
- Best Practices

### Education Skills

Common sections:

- Tools and Methods
- Examples
- Recommendations
- Output Contract

### Common/General Skills

Common sections:

- Tools and Methods
- Best Practices
- Examples
- Simpler structure

### Testing Skills

Common sections:

- Tools and Practices
- Examples
- Constraints

---

## Notes

- **Frontmatter is mandatory** — Always include YAML frontmatter with `name` and `description`
- **Size limit** — Prefer to keep SKILL.md under 500 lines as a guideline; use `references/` and `assets/` for detailed content
- **Depth variation is acceptable** — Some skills can be brief (20-30 lines) while others detailed (60-80 lines)
- **Custom sections are encouraged** — If a skill needs domain-specific sections, add them
- **Avoid redundancy** — Don't repeat information across sections
- **Progressive disclosure** — Put the most important information early in the file
- **Respect execution strength** — When orchestrating multiple skills, Constraints override Instructions, Instructions override Best Practices, etc.

---

## References

- [Agent Skills Specification](https://agentskills.io/) — Official open standard documentation
- [Microsoft Agent Framework - Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) — Implementation details
- [Anthropic Skills Blog Post](https://nayakpplaban.medium.com/agent-skills-standard-for-smarter-ai-bde76ea61c13) — Overview and usage guide
