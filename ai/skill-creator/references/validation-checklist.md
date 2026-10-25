# Skill Validation Checklist

Condensed from the repository SKILL.md specification. Use it when the specification file itself is not available, or as a final review.

## Standard-required
- [ ] SKILL.md starts with YAML frontmatter enclosed by `---`
- [ ] `name`: at most 64 characters; lowercase letters, numbers, hyphens; no leading, trailing, or consecutive hyphens; equals the parent folder name
- [ ] `description`: present, at most 1024 characters, says what the skill does and when to use it, contains discovery keywords
- [ ] `compatibility` (if present): at most 500 characters

## Repository-required
- [ ] `# Title` aligned with the skill name
- [ ] `## Description`: 1-2 sentences
- [ ] `## When to Use`: bulleted list of scenarios
- [ ] `## Instructions`: numbered list, each step as `**Name** - description`

## Recommended
- [ ] Tools and Methods / Tools and Practices when the skill depends on tools or methods (use the variant that fits the category)
- [ ] Technologies and Standards for development skills
- [ ] Best Practices, Constraints
- [ ] Output Contract when output structure matters
- [ ] Input Recovery Rules when input may be incomplete or ambiguous
- [ ] Priority Rules when requirement conflicts are likely

## Section semantics
- [ ] Instructions = what to do; Constraints = what never to do or must have; Best Practices = preferred; Recommendations = optional; Priority Rules = conflict resolution
- [ ] No rule is repeated across sections
- [ ] Constraints can be followed without contradicting Instructions

## Size and structure
- [ ] SKILL.md under 500 lines; detailed material in `references/`, `templates/`, `examples/`, `scripts/`, or `assets/`
- [ ] Most important information early in the file
- [ ] Every relative link points to an existing file
- [ ] Only folders that contain files exist

## Discovery test
- [ ] Three to five realistic requests that should trigger the skill do match the description
- [ ] Two requests that should not trigger it do not match
