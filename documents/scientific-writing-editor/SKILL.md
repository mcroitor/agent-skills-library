---
name: scientific-writing-editor
description: Edit and structure scientific writing with evidence-qualified language, clear argument flow, and citation consistency for reports, papers, and research communications.
---

# Scientific Writing Editor

## Description
A base skill for improving scientific writing quality, argument coherence, and evidence traceability across research-oriented documents.

Use ISO 690:2022 as the default standard for citations and bibliography formatting unless another style is explicitly required.

## Priority Rules
Prioritize in this order when requirements conflict:
1. Scientific accuracy and factual integrity
2. Claim-evidence alignment
3. Clarity and readability for the intended audience
4. Concision and stylistic polish

## When to Use
- Editing scientific reports and research summaries
- Improving claim-evidence reasoning in draft text
- Aligning tone, certainty, and methodological language
- Standardizing citation style and reference hygiene
- Generating bibliography exports in BibTeX format (using BibTeX-compatible entry types)
- Generating Microsoft Word bibliography Sources XML (references.xml) output for import

## Instructions
1. **Identify scope** - determine document type, audience, and expected depth
2. **Map claims to evidence** - verify each major claim has explicit support
3. **Edit for scientific tone** - calibrate certainty and avoid overstatement
4. **Strengthen structure** - improve paragraph intent, transitions, and logical flow
5. **Normalize references** - apply ISO 690:2022 consistently for in-text citations and bibliography unless another style is explicitly requested; use assets/iso-690-2022.md as the normalization and validation guide
6. **Plan export targets** - determine output_format (bibtex, references_xml, both) and citation_system (author-date or numeric)
7. **Map canonical fields** - transform normalized reference data using references/ms-office-bibliography-mapping.md and preserve non-mappable fields explicitly
8. **Generate format outputs** - produce BibTeX using templates/bibtex-entry-templates.md and Microsoft Word bibliography Sources XML (references.xml) using templates/references-xml-template.xml
9. **Run validation pass** - check citation/bibliography consistency, mapping warnings, and structural validity before final output
10. **Finalize quality pass** - check coherence, terminology consistency, and ambiguity

## Input Recovery Rules
- Assume a scientific audience with domain familiarity when audience is not specified
- Assume evidence-qualified writing style by default
- Assume ISO 690:2022 when citation style is not specified
- Assume output_format=both when export target is not specified
- Assume citation_system=author-date when the citation system is not specified
- Ask for clarification only when methodological framing is unclear or when mandatory source metadata is missing for all provided references

## Constraints
- Do not introduce unsupported claims
- Do not collapse nuanced findings into absolute statements
- Do not mix citation styles in one output unless explicitly requested
- Do not use citation styles other than ISO 690:2022 unless explicitly requested
- Do not silently drop non-mappable fields during BibTeX to Word XML conversion; report them as mapping warnings
- Do not emit malformed BibTeX entries or invalid XML structures

## Deliverables
- Edited scientific text with improved clarity and flow
- Claim-evidence consistency notes
- Citation consistency and reference normalization notes
- BibTeX bibliography output when requested
- Microsoft Word bibliography Sources XML (references.xml) output when requested
- Validation report with mapping warnings and completeness checks

## Output Contract
- Return output in this order:
	1. Scope and assumptions (output format, citation system, style overrides)
	2. ISO 690:2022 compliance summary
	3. BibTeX output block (when requested)
	4. Microsoft Word bibliography Sources XML (references.xml) output block (when requested)
	5. Validation report (field completeness, mapping warnings, unresolved issues)
- Include a mapping warning list for fields that cannot be represented 1:1 across formats.
- Prefer stable and reproducible output ordering for identical source metadata input.

## Module Boundaries
- Core Writing Workflow scope:
	- argumentation quality
	- claim-evidence alignment
	- scientific tone and readability
	- structure and terminology consistency
- Citation and Export Workflow scope:
	- ISO 690:2022 normalization
	- bibliography metadata normalization
	- BibTeX generation
	- references.xml generation for Word import
	- field mapping and export validation
- Boundary rule:
	- Writing tasks must not depend on export internals.
	- Export tasks must not alter scientific claims or manuscript meaning.

## Extraction Trigger Rules
- Use measurable extraction criteria from references/architecture-split-policy.md.
- Trigger evaluation should focus on:
	- growth of metadata and interoperability-only capabilities
	- change-share concentration in mapping and export logic
	- introduction of independent export quality gates
- When triggers are met, extract Citation and Export Workflow into a dedicated skill and preserve output contract compatibility.

## Tools and Methods
- ISO 690:2022 normalization workflow
- BibTeX and BibLaTeX field harmonization
- MS Office bibliography XML mapping workflow
- Reference data deduplication and key stabilization
- Export validation checklist

## Technologies and Standards
- ISO 690:2022
- BibTeX
- BibLaTeX
- Microsoft Word bibliography Sources XML (references.xml)
- JabRef MS Office field mapping guidance

## Writing Standards
- Prefer explicit claim-evidence-reasoning chains
- Distinguish results, interpretation, and speculation
- Keep terminology stable and define uncommon terms

## References
- references/ms-office-bibliography-mapping.md - entry type and field mapping rules for BibTeX/BibLaTeX and Word bibliography XML
- references/architecture-split-policy.md - governance policy and measurable criteria for extracting a dedicated reference-engineering skill

## Templates
- templates/bibtex-entry-templates.md - normalized BibTeX output patterns by source type
- templates/references-xml-template.xml - baseline Word bibliography XML layout for references export

## Examples
- examples/example-input-sources.md - normalized sample source metadata
- examples/example-output-bibtex.bib - sample BibTeX output from the same input
- examples/example-output-references.xml - sample references.xml output from the same input
- examples/example-validation-report.md - expected validation report structure

## Citation Assets
- assets/iso-690-2022.md - quick reference for ISO 690:2022 citation systems, source templates, and bibliography validation checklist
