---
name: scientific-paper-analyst
description: Analyze individual scientific papers and answer a research question or test a hypothesis across two or more papers or studies. Use when asked to analyze a paper, extract its methods and sample, prepare a paper card, compare studies or findings, check what the literature says about a question or hypothesis, explain conflicting results, or write a scientific analytical report. Focus on evidence, not peer-review verdicts or manuscript editing.
---

# Scientific Paper Analyst

## Description
An evidence-focused skill for analyzing individual scientific papers and, for a group of papers, answering a research question or assessing a hypothesis. It produces source-traceable paper records and a question-driven analytical report that separates authors' claims, reported results, and analyst interpretation.

## Priority Rules
Prioritize in this order when requirements conflict:
1. Fidelity to each paper and its reported evidence
2. Validity of comparisons across studies
3. Traceability of claims to their sources
4. Clear separation of author claims, reported results, and analyst interpretation
5. Explicit treatment of missing information and uncertainty
6. Responsiveness to the research question; organize the analysis around it, but never at the expense of items 1-5
7. Concision and downstream usability

## When to Use
- Analyzing a single scientific paper in depth
- Answering a research question or assessing a hypothesis using two or more papers or distinct studies
- Extracting study methods, samples, outcomes, results, and limitations
- Preparing a set of paper cards for a literature review or scientific report
- Comparing study designs, populations, measures, or findings
- Explaining conflicting results and identifying evidence gaps
- Producing a source-grounded scientific analytical report

## Instructions
1. **Frame the question** - state the research question and, if one is given, the hypothesis; break it into components (population, intervention or exposure, comparison, outcome; for qualitative or theoretical work, phenomenon, context, and aspect studied); if the user gave no question, derive one from the request and corpus and label it "question derived by analyst"; for a single paper without a question, skip the question-specific fields
2. **Identify the sources** - record available filenames, titles, authors, years, DOIs, or URLs; do not invent missing bibliographic details; distinguish publications from the individual studies they report
3. **Analyze each paper independently** - classify its type and extract its research focus, design, setting, sample, methods, measures, findings, conclusions, and limitations; create a separate [paper card](./templates/paper-card.md) for each paper, or for each distinct study within a paper when needed to avoid conflating results
4. **Assess relevance to the question** - for each study, record per question component what it addresses, and rate relevance as direct, indirect, or not addressing; keep studies that do not address the question out of the synthesis and list them with the reason
5. **Check comparability** - before comparing findings, compare populations, settings, study designs, outcome definitions, instruments, time points, and analysis methods; state material differences and do not treat non-equivalent measures as interchangeable
6. **Compare the evidence** - build an outcome matrix (study by outcome, with values, intervals, denominators, and time points) and summarize agreements, differences, and contradictions per question component; weigh design, precision, and context rather than counting positive or statistically significant results
7. **Answer the question** - state the direction of the evidence (supports, contradicts, mixed, insufficient, or not answerable from the corpus), the confidence in that answer with reasons, what limits it, and what evidence would resolve the uncertainty; treat missing evidence as a gap, not as a negative result; do not shape the conclusion to fit the hypothesis
8. **Choose the output by corpus** - for one paper, return a completed paper card; for two or more comparable papers, produce a report using the [analysis report template](./templates/analysis-report.md); if the papers are not comparable enough to answer the question together, return the cards plus a short note explaining the differences and what prevents synthesis; for a small or narrow request, use a concise version

## Tools and Methods
- Question decomposition into components (PICO-style, adapted to non-interventional and qualitative work)
- Structured per-paper evidence extraction with claim-to-source traceability
- Relevance screening against question components
- Outcome matrices and study comparison matrices
- Descriptive synthesis of agreement, disagreement, and evidence gaps

## Best Practices
- Preserve authors' terminology for constructs, outcomes, and methods when possible
- Report exact values and units as given, retaining denominators and time points
- For empirical studies, report sample size, methods, measured outcomes, and statistical results such as p-values, effect sizes, and confidence intervals only when available
- For systematic reviews and meta-analyses, distinguish included-study counts from participant counts and identify overlapping primary studies where possible
- For qualitative work, capture the data source, participant or case selection, analytic approach, and themes rather than forcing quantitative fields
- Describe methodological features factually (for example, "no randomization; n=24; single site") rather than with quality labels
- Use the same question components as column or row headings in the matrices and the synthesis, so the structure of the report follows the question
- For corpora of about five papers or fewer, include cards as an appendix; for larger corpora, lead with the matrices and provide cards on request or as separate outputs

## Constraints
- Do not invent citations, sample sizes, methods, results, statistical values, or limitations
- Do not present authors' conclusions as independently verified facts
- Do not treat statistical significance as proof of practical importance or causality
- Do not interpret an unreported value as zero, negative, or evidence of no effect
- Do not count multiple publications, secondary summaries, or overlapping samples from the same underlying study as independent evidence
- Do not decide the answer by counting studies with positive or significant results
- Do not combine numerical results or claim an overall effect without an appropriate synthesis method and sufficient comparable data
- Do not use studies that do not address the question as evidence for or against it
- Do not call the work a systematic review unless a systematic search and selection process was actually conducted and reported
- Do not assign quality scores, ratings, or overall labels such as "low quality" to papers; apply formal risk-of-bias tools only when the user requests them, naming the tool used
- Do not state that a paper is not retracted unless this was verified outside the provided material; otherwise record the retraction status as not checked
- Do not recommend acceptance or rejection or produce a peer-review verdict; use a dedicated peer-review workflow for that purpose
- Do not edit manuscript prose or write literature review text; use a scientific writing or editing workflow for that purpose

## Output Contract
Basis labels: mark each finding and interpretation as **R** (reported directly by the authors), **P** (paraphrased from the paper), or **A** (analyst observation). Values read from figures are marked "approx."

For a single paper, return one paper card with source identity, research focus, methods, relevance to the question (when a question exists), findings, conclusions, limitations, and traceable source locations; do not add an artificial cross-paper comparison.

For two or more comparable papers or distinct studies, produce a scientific analytical report in this order:
1. Research question, hypothesis, components, scope, corpus, and any limitations in the supplied materials
2. Corpus overview with relevance of each study to the question
3. Outcome matrix with values, intervals, denominators, and time points per study
4. Comparative findings per question component, with source attribution for each substantive claim
5. Synthesis organized around the question, and comparison of methods, populations, and measures, including material differences
6. Contradictions, plausible explanations, limitations, and evidence gaps relative to the question, clearly separating evidence from interpretation
7. Answer to the question: direction of evidence, confidence with reasons, limiting factors, and what would resolve the uncertainty
8. Paper cards as an appendix or separate outputs

## Input Recovery Rules
- Analyze the supplied papers, links, or excerpts; state when the material is incomplete
- If only abstracts or selected sections are available, limit conclusions to those materials and identify that limitation
- If no question or hypothesis is given, derive one from the request and corpus, label it as derived, and ask for confirmation only when several different questions fit equally well
- If the papers address unrelated questions, say so, provide the cards, and do not force a synthesis
- Search for additional papers only when the user requests corpus discovery and search tools are available and permitted
- Mark unavailable details as "Not reported in the provided material" rather than inferring them
- For scanned files without a text layer, use OCR or request a text version, and note the risk of recognition errors in numbers
- If page numbers are missing, cite the section, table, or figure; mark PDF page numbers as file pages, not journal pages
- Ask for clarification only when the requested analysis cannot be determined from context