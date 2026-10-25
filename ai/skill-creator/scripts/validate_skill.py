#!/usr/bin/env python3
"""Validate a skill folder against the repository SKILL.md specification.

Usage: python validate_skill.py path/to/skill-folder
Exit code 1 if errors are found, otherwise 0.
"""
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
STEP_RE = re.compile(r"^\d+\. \*\*[^*]+\*\* - \S")
REQUIRED_SECTIONS = ["Description", "When to Use", "Instructions"]
LINK_RE = re.compile(r"\]\((\.{1,2}/[^)#\s]+)")


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    parts = text[3:].split("\n---", 1)
    if len(parts) < 2:
        return None, text
    fields = {}
    for line in parts[0].splitlines():
        match = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields, parts[1].lstrip("-").lstrip("\n")


def section_text(body, title):
    pattern = re.compile(r"^## " + re.escape(title) + r"\s*$", re.M)
    found = pattern.search(body)
    if not found:
        return None
    rest = body[found.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def validate(folder):
    errors, warnings = [], []
    skill_file = folder / "SKILL.md"
    if not skill_file.is_file():
        return [f"SKILL.md not found in {folder}"], warnings

    text = skill_file.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    if fields is None:
        return ["Missing or unterminated YAML frontmatter"], warnings

    name = fields.get("name", "")
    if not name:
        errors.append("Frontmatter: 'name' is missing")
    else:
        if len(name) > 64:
            errors.append(f"Frontmatter: name is {len(name)} characters (max 64)")
        if not NAME_RE.match(name):
            errors.append("Frontmatter: name must use lowercase letters, numbers, and single hyphens, without leading or trailing hyphens")
        if name != folder.resolve().name:
            errors.append(f"Frontmatter: name '{name}' does not match folder '{folder.resolve().name}'")

    description = fields.get("description", "")
    if not description:
        errors.append("Frontmatter: 'description' is missing")
    elif description in (">", "|", ">-", "|-"):
        warnings.append("Frontmatter: multi-line description is not checked by this script")
    else:
        if len(description) > 1024:
            errors.append(f"Frontmatter: description is {len(description)} characters (max 1024)")
        if "use when" not in description.lower() and "use for" not in description.lower():
            warnings.append("Frontmatter: description does not say when to use the skill")

    if len(fields.get("compatibility", "")) > 500:
        errors.append("Frontmatter: compatibility is longer than 500 characters")

    if not re.search(r"^# \S", body, re.M):
        errors.append("Body: missing '# Title'")

    for title in REQUIRED_SECTIONS:
        if section_text(body, title) is None:
            errors.append(f"Body: missing required section '## {title}'")

    desc_body = section_text(body, "Description")
    if desc_body is not None:
        sentences = [s for s in re.split(r"(?<=[.!?])\s+", desc_body.strip()) if s]
        if len(sentences) > 2:
            warnings.append(f"Body: '## Description' has {len(sentences)} sentences (spec asks for 1-2)")

    use_body = section_text(body, "When to Use")
    if use_body is not None and not re.search(r"^\s*[-*] \S", use_body, re.M):
        errors.append("Body: '## When to Use' has no bulleted items")

    instr = section_text(body, "Instructions")
    if instr is not None:
        steps = [ln for ln in instr.splitlines() if re.match(r"^\d+\.", ln)]
        if not steps:
            errors.append("Body: '## Instructions' has no numbered steps")
        for ln in steps:
            if not STEP_RE.match(ln):
                warnings.append(f"Body: step not in '**Name** - description' format: {ln[:60]}")

    if section_text(body, "Constraints") is None:
        warnings.append("Body: no '## Constraints' section (recommended)")

    line_count = len(text.splitlines())
    if line_count > 500:
        warnings.append(f"SKILL.md has {line_count} lines (guideline: under 500)")

    for link in sorted(set(LINK_RE.findall(body))):
        if not (folder / link).exists():
            errors.append(f"Broken relative link: {link}")

    for sub in ("scripts", "references", "templates", "examples", "assets"):
        sub_path = folder / sub
        if sub_path.is_dir() and not any(sub_path.iterdir()):
            warnings.append(f"Empty folder: {sub}/")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_skill.py path/to/skill-folder")
        return 2
    errors, warnings = validate(Path(sys.argv[1]))
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
