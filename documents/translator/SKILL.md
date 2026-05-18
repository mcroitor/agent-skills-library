---
name: translator
description: Translate written content across languages while preserving meaning, tone, register, and terminology. Use for general translation, technical translation, and localization decisions when needed.
---

# Translator

## Description
A skill for translating written content across languages with attention to meaning, register, and domain-specific terminology while preserving communicative intent and readability.

## Priority Rules
Prioritize in this order when trade-offs conflict; if two priorities overlap, prefer the higher item:
1. Semantic accuracy and meaning preservation
2. Natural tone and readability in target language
3. Cultural and context appropriateness
4. Terminology consistency and style alignment

## When to Use
- Translating product documentation and user guides
- Localizing software interfaces and error messages
- Converting technical documents, manuals, and specifications
- Adapting marketing and communications content
- Supporting multilingual collaboration and knowledge sharing
- Building terminology glossaries for consistency

## Instructions
1. **Define context** - source and target languages, audience, domain, and tone expectations
2. **Establish terminology** - identify domain-specific terms, product names, and neologisms; create or reference glossary
3. **Translate draft** - render content meaning-for-meaning, not word-for-word, adapting phrasing for naturalness
4. **Review for tone** - verify formality, voice, and style match target audience and source intent
5. **Localize references** - adapt examples, currency, dates, units, and cultural references appropriately
6. **Validate consistency** - check terminology usage, capitalization, and formatting alignment
7. **Edit and polish** - resolve ambiguities, improve readability, and verify no content loss
8. **Document translations** - record glossary, style decisions, and translator notes for reproducibility

## Input Recovery Rules
- When audience context is missing, use neutral professional language and document assumptions
- Assume literal translation is not desired; prioritize natural, idiomatic target language
- Ask for clarification whenever the source language or target language is missing or ambiguous
- Ask for clarification when domain, tone, or terminology scope materially affects translation strategy

## Constraints
- Do not translate proper names or untranslatable terms without explicit instruction
- Do not sacrifice clarity for literal fidelity to source phrasing
- Do not omit terminology consistency without documenting exceptions
- Do not alter communicative intent just to preserve sentence structure
- Flag source ambiguities that materially affect translation meaning
- Preserve or appropriately adapt formality, politeness, and professional register
- Do not over-request context when a neutral, documented assumption is sufficient

## Deliverables
- Core deliverable: translated content in the target language
- Include a terminology glossary only when domain, product, or terminology consistency matters
- Include translation notes only when ambiguities, style decisions, or localization choices need to be recorded
- Include a style and tone summary only when the translation must be reused or governed across multiple outputs

## Tools and Practices
- Translation memory systems: memoQ, Trados, OmegaT
- Terminology management: Termbase, shared glossaries, domain corpora
- Localization frameworks: i18n/l10n standards, string extraction tools
- Quality assurance: spell check, terminology validation, consistency checks
- Collaborative workflows: version control for translation assets, review cycles

## Output Contract
Return all of the following:
1. Complete translated content in target language
2. Any unresolved source ambiguities or meaning-sensitive decisions that affect the translation
3. Terminology glossary and translation notes when domain terms, localization, or reproducibility require them
4. Reviewer recommendation only when human review is needed or would materially improve quality

## Best Practices
- Build and maintain a terminology database for repeated translation work
- Use parallel text (source and target side-by-side) during review
- Involve native speakers and domain experts in validation cycles
- Document style preferences (formal/informal, active/passive, abbreviation rules)
- Test translations in context (UI, document flow, readability)
- Keep translatable strings separate from code and configuration when possible
