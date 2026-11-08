---
name: research-source-finder
description: Find and rank scholarly articles, books, and other research sources for a topic or hypothesis; report citation counts, retrieve legally available full texts, and format references in ISO 690:2021 with links. Use when asked to search for research literature, build a reading list or bibliography, or download open-access sources. Not for analyzing or synthesizing source findings.
---

# Research Source Finder

## Description
Find relevant research literature for a specified topic or hypothesis, rank eligible works by reported citation counts, retrieve full texts only through legitimate access, and prepare a traceable ISO 690:2021 bibliography. Report search coverage, access limitations, and the basis for ranking.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Source authenticity and bibliographic accuracy
2. Relevance to the research question
3. Legal and authorized access
4. Reproducibility and traceability
5. Citation-based ranking among eligible sources
6. Completeness of the requested set
7. Output formatting and convenience

## When to Use
- Finding articles, books, chapters, reports, or other sources for a research topic or hypothesis
- Building a citation-ranked reading list within a specified publication period
- Downloading legally available full-text sources and preparing an ISO 690:2021 bibliography

## Instructions
1. **Validate the request** - identify the topic or hypothesis, requested number of distinct sources, and publication date range; default to a rolling five-year window ending on the search date, inclusive, and report exact start and end dates in `YYYY-MM-DD` format
2. **Define the search** - break the topic into searchable concepts, synonyms, and spelling variants; retain the user's language and add English terms when useful; identify relevant disciplines, source types, and any stated inclusion or exclusion criteria
3. **Choose discovery sources** - use OpenAlex as a broad source for scholarly works and citation metadata; add subject-specific indexes such as PubMed for biomedical research, Crossref for DOI and publication metadata, or Semantic Scholar when available; search Google Scholar through its normal interface only when available; for books, include OpenAlex, Crossref, DOAB, Google Books, or library catalogs as appropriate
4. **Search and screen** - run queries across the selected sources and apply the date range; assess each work's relevance to the research question as a whole, not merely isolated keywords or topic components; include directly relevant works in the ranked set, and report indirectly relevant works separately when useful with a clear label; record the exact query strings, filters, date searched, approximate result counts, and material exclusion reasons for each source
5. **Deduplicate and link versions** - deduplicate by DOI, ISBN, or another persistent identifier when available, then by normalized title, author, and year; identify preprints, accepted manuscripts, and published versions of the same work, prefer the published version unless the user asks otherwise, and note links between versions rather than counting them as separate works; use the selected version's publication date and citation count consistently, and do not merge counts across versions or editions unless the index explicitly reports an aggregated work-level count
6. **Rank eligible works** - use one primary citation index consistently (OpenAlex by default) and label its value as a reported citation count from that service, with the service and check date; when another index is available, show its count separately as a cross-check and do not combine or average counts; treat missing counts as unknown, never as zero; rank works with available counts by count, breaking ties by stronger topical relevance, then newer publication year, then persistent identifier in ascending order; list works without counts in a separate unranked group, ordered by relevance and then newer publication year
7. **Select the requested set** - return the requested number of distinct, eligible sources when available; if fewer are found, explain the shortfall rather than padding with weak matches; identify document type and peer-review status only when verified
8. **Retrieve and verify full texts** - look for legal copies via publisher open-access pages, PubMed Central, DOAJ, DOAB, Unpaywall, OpenAIRE, CORE, and institutional repositories; download only through authorized access and available tools; when possible, confirm that the file exists, opens, corresponds to the selected work, and contains the full text rather than only an abstract; distinguish a verified download from a download that could not be checked
9. **Verify metadata** - cross-check each selected record against its DOI landing page, publisher or repository record, or authoritative catalog; confirm authors, title, year, publication/container title, volume, issue, pages or article number, publisher, DOI, ISBN for books when available, edition, and stable URL when available
10. **Format and report** - format references consistently according to ISO 690:2021, or its identical Moldovan adoption SM ISO 690:2022 when explicitly required; include working DOI or stable source links and access dates for online resources; provide the search log, ranked results, download statuses and file locations, and limitations; provide BibTeX, CSL-JSON, or a JSON manifest when requested

## Tools and Methods
- OpenAlex for broad scholarly discovery, works metadata, and citation counts
- Crossref for DOI lookup and publication metadata
- PubMed and PubMed Central for biomedical discovery and open full text
- Semantic Scholar for supplementary scholarly discovery and citation data
- Google Scholar for interface-based discovery when available; it has no public search API for this workflow
- DOAJ, DOAB, Unpaywall, OpenAIRE, CORE, and institutional repositories for open-access discovery
- Google Books and library catalogs for book discovery and bibliographic details
- ISO 690:2021 for a consistent, source-type-appropriate reference list; use SM ISO 690:2022 only when explicitly required

## Best Practices
- Prefer relevant primary sources and authoritative editions; label reviews, preprints, books, reports, and other source types accurately
- Apply relevance eligibility before sorting by citations; show relevance and publication year alongside the count, and treat citation popularity as distinct from source quality
- Use OpenAlex as the primary citation-count service unless the user specifies another; label counts by service and report cross-index counts separately
- Preserve exact search strings, filters, date range, search date, and approximate screening counts so the search can be repeated
- Prefer persistent identifiers for deduplication and record relationships among preprint, accepted manuscript, and published versions
- Use DOI links in canonical `https://doi.org/...` form when verified; otherwise provide a stable publisher, repository, or catalog URL

## Constraints
- Never invent search results, citation counts, bibliographic fields, access status, search counts, or download completion; do not treat a missing citation count as zero
- Do not bypass paywalls, access controls, CAPTCHA, or license terms; do not use shadow libraries or unauthorized copies
- Do not scrape Google Scholar or other services contrary to their access rules; use an authorized API, normal interface, or another index
- Do not present citation count as evidence of methodological quality, correctness, or consensus
- Do not silently include sources outside the requested period; list older foundational works separately only if useful and clearly marked as outside scope
- Do not describe the search as systematic or exhaustive unless the corresponding protocol and coverage were actually followed and documented

## Input Recovery Rules
- If the topic is broad, define a focused search scope and state the interpretation; ask a concise clarification only when plausible interpretations would produce substantially different source sets
- If the number is omitted, ask how many sources the user wants rather than choosing an arbitrary list length
- If the period is omitted, use the rolling five-year default ending on the search date; report exact start and end dates in `YYYY-MM-DD` format
- If source type, language, or discipline is unspecified, use a balanced mix relevant to the topic and disclose the selection
- If web search, citation metadata, or file download is unavailable, state the limitation and provide only the parts that can be verified; never imply that searching or downloading occurred
- Use distinct statuses: **not checked** (not assessed), **unavailable** (no accessible full text or metadata found), **failed** (an attempted retrieval failed), **downloaded, not verified** (saved but not checked or could not be checked), and **downloaded and verified**; do not treat these statuses as interchangeable

## Output Contract
Return these sections in order:
1. **Search scope and log** - interpreted topic or hypothesis, exact date range, requested count, databases and search dates, exact query strings and filters, approximate result counts, and material exclusion reasons
2. **Ranked sources** - a compact numbered table with title, author(s), selected-version year, citation count and service/date, relevance, and DOI or stable link; include source type, full-text status, and file path when applicable, using a separate detail list or manifest if the table would be unwieldy; list works with unavailable counts separately as unranked, never as zero-citation works, and keep useful indirect matches in a clearly labeled separate group
3. **ISO 690 bibliography** - complete references in ranking order according to ISO 690:2021, or SM ISO 690:2022 when explicitly required, with DOI or stable links and access dates for online sources
4. **Limitations** - unavailable or unverified citation counts, full texts, metadata, or file checks, and any shortfall from the requested number; distinguish “not checked,” “unavailable,” “failed,” and “downloaded, not verified”

When requested, also provide a BibTeX, CSL-JSON, or JSON manifest containing source metadata, persistent identifiers, citation counts with their services and check dates, relevance, full-text URLs, retrieval status, and downloaded file paths. Do not generate extra formats by default.
