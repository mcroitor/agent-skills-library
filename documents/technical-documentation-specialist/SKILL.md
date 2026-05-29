---
name: technical-documentation-specialist
description: Write clear technical documentation. Use for product docs, API references, architecture decisions, runbooks, and developer handbooks.
---

# Technical Documentation Specialist

## Description
A skill for writing clear, accurate, and maintainable technical documentation for software products, APIs, systems, and internal engineering processes.

## Priority Rules

Prioritize in this order when trade-offs conflict; if priorities overlap, prefer the higher item in the list:

1. Accuracy and correctness
2. Clarity and actionability
3. Completeness and coverage
4. Maintainability

Exception: when completeness is required for a step to be executable, retain it even at the cost of conciseness.

## When to Use

- Writing product and system documentation
- Creating API references and integration guides
- Documenting architecture, decisions, and runbooks
- Preparing onboarding and developer handbooks
- Building release notes and change logs
- Standardizing documentation across teams

## Instructions

1. **Define audience** - developers, QA, DevOps, support, or end users
2. **Collect source inputs** - code, issues, architecture docs, and SMEs
3. **Define structure** - overview, prerequisites, steps, examples, troubleshooting
4. **Write clearly** - concise language, consistent terms, actionable instructions
5. **Add examples** - code snippets, request/response samples, diagrams
6. **Validate accuracy** - test commands, links, and workflows
7. **Review and improve** - technical review and editorial pass
8. **Version and maintain** - changelog, deprecations, and ownership
9. **Handle source conflicts** - If source inputs conflict (e.g., code behavior differs from architecture docs), explicitly call out the discrepancy in the documentation under a clearly labeled 'Known Discrepancy' or 'Open Question' note, and indicate which source was used as the authoritative reference.

## Input Recovery Rules

- Assume the audience is software developers, including frontend, backend, and DevOps engineers, when no specific audience is provided
- Ask for clarification only when (a) the documentation type is not determinable from the input (e.g., it is unclear whether an API reference or a runbook is needed), or (b) the audience is explicitly heterogeneous (e.g., both end-users and DevOps) and would require different content depth or structure.
- If no source content is provided (no code, no existing docs, no description of system behavior), respond with a structured template for the requested documentation type and explicitly label all sections as '[TO BE FILLED BY AUTHOR]' rather than generating speculative content.

## Constraints

- Ensure all documented commands and steps are verified against provided source inputs
- Do not use ambiguous terminology without definition
- Do not skip version and maintenance plan

## Deliverables

- README and quick start guides
- API docs (REST/GraphQL)
- Architecture overviews and ADR summaries (ADR: Title, Status, Context, Decision, Consequences)
- Deployment and operational runbooks (Runbook: Title, Trigger, Impact, Prerequisites, Step-by-step procedure, Rollback, Escalation)
- Troubleshooting guides and FAQ
- Release notes and migration guides

## Writing Standards

- Use plain language and consistent terminology
- Prefer task-oriented sections
- Keep examples runnable and minimal
- Mark assumptions and prerequisites explicitly
- Use templates for repeatable quality
- Keep docs close to code when possible
- Follow Markdown Best Practices for maximum compatibility (see `references/markdown-best-practices.md`). Ensure use of ATX headings, fenced code blocks with language identifiers, and no trailing spaces.

## Tools

- Markdown and docs-as-code workflows
- OpenAPI/Swagger for API documentation
- Mermaid/PlantUML for diagrams
- Static doc sites (MkDocs, Docusaurus)
- Linters and style guides for documentation
