---
name: academic-manuscript-editor
description: Edit and prepare academic manuscripts for submission using IMRAD logic, venue requirements, reviewer-oriented revisions, and publication-ready structure.
---

# Academic Manuscript Editor

## Description
A specialized skill for manuscript-focused editing, including section architecture, submission readiness, and reviewer-oriented revision.

Use ISO 690:2022 as the default citation and bibliography standard unless the target venue explicitly requires another style.

## Priority Rules
Prioritize in this order when requirements conflict:
1. Methodological and reporting correctness
2. IMRAD coherence and argument continuity
3. Journal/conference compliance
4. Concision and style refinement

## When to Use
- Revising full manuscripts and preprints
- Improving abstracts, introductions, and discussion sections
- Aligning manuscripts with author guidelines
- Preparing rebuttals and response-to-reviewers documents

## Instructions
1. **Set target venue context** - define journal/conference constraints and formatting rules
2. **Audit manuscript architecture** - validate IMRAD logic, section purpose, and narrative continuity
3. **Refine key sections** - optimize title, abstract, contribution statement, and discussion scope
4. **Check reporting completeness** - ensure methods/results are reproducible and sufficiently detailed
5. **Harden citation and formatting** - standardize references, tables, figures, and cross-references; use ISO 690:2022 and validate with assets/iso-690-2022.md unless venue rules override
6. **Prepare submission package** - finalize cover letter and reviewer-response framing

## Input Recovery Rules
- Assume IMRAD manuscript format when no format is provided
- Assume submission to a peer-reviewed venue when publication context is unspecified
- Assume ISO 690:2022 when citation style is not specified by the venue or user
- Ask for clarification only when venue-specific rules materially change structure

## Constraints
- Do not alter reported results without explicit source updates
- Do not mask limitations or uncertainty
- Do not claim novelty without explicit comparative justification
- Do not mix citation styles in one manuscript
- Do not use a citation style different from ISO 690:2022 unless venue rules or user instructions explicitly require it

## Deliverables
- Publication-ready manuscript edits by section
- Submission-readiness checklist
- Reviewer-response draft and revision rationale

## Tools and Practices
- IMRAD conventions and author guidelines
- Reviewer-oriented revision workflows
- Reporting checklists (for example, CONSORT, PRISMA, STROBE when relevant)
- ISO 690:2022 citation and bibliography compliance guide: assets/iso-690-2022.md

## References
- references/ms-office-bibliography-mapping.md - entry type and field mapping rules for BibTeX/BibLaTeX and Word bibliography XML

## Templates
- templates/bibtex-entry-templates.md - normalized BibTeX output patterns by source type
- templates/references-xml-template.xml - baseline Word bibliography XML layout for references export

## Examples
- examples/example-input-sources.md - normalized sample source metadata
- examples/example-output-bibtex.bib - sample BibTeX output from the same input
- examples/example-output-references.xml - sample references.xml output from the same input
- examples/example-validation-report.md - expected validation report structure

## Assets
- assets/iso-690-2022.md - quick reference for ISO 690:2022 citation systems, source templates, and bibliography validation checklist
