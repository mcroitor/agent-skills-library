# Architecture Split Policy for Scientific Writing Editor

This document defines when to keep a unified skill and when to extract a dedicated reference-engineering skill.

## Current Position
- Keep a unified skill in the near term.
- Maintain clear module boundaries between writing logic and reference-export logic.
- Use measurable trigger rules for extraction decisions.

## Cognitive Domain Separation
### Writing Domain
- readability and flow
- argument quality
- claim-evidence alignment
- scientific tone calibration

### Reference Engineering Domain
- metadata normalization
- field mapping across schemas
- deterministic transforms
- BibTeX and Word XML export correctness
- interoperability validation

## Extraction Triggers
Trigger extraction when one or more of the following conditions is persistently true:

1. Capability expansion trigger
- Three or more newly added roadmap capabilities are reference-only (for example CSL, Zotero integration, Crossref or OpenAlex enrichment, ORCID reconciliation, citation deduplication engine).

2. Change-share trigger
- More than 50 percent of recent implementation changes target mapping, export, validation, and interoperability behavior rather than writing behavior.

3. Quality-gate trigger
- Export behavior requires independent test and release gates such as schema compatibility matrix checks, deterministic conversion snapshots, or round-trip conversion checks.

## Extraction Target
- Recommended new skill name: academic-reference-manager.
- Responsibility of extracted skill:
  - ISO 690:2022 normalization for reference metadata
  - BibTeX and references.xml generation
  - cross-format field mapping and warnings
  - export validation and deterministic behavior

## Transition Rules
- Keep Scientific Writing Editor as writing-first orchestration.
- Delegate reference pipeline tasks to the extracted skill after split.
- Preserve output contract ordering for backward compatibility.
- Maintain shared examples until migration is complete.

## Review Cadence
- Re-evaluate trigger conditions at each material scope expansion of bibliography features.
- Record split decision and rationale in repository change log or pull request notes.
