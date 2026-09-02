---
name: scientific-paper-reviewer
description: Compose scholarly peer reviews using a comprehensive 25-criterion framework with adaptive weighting by article type. Evidence-based scoring, critical criteria gates, and publication recommendations for empirical, theoretical, review, and case study papers.
---

# Scientific Paper Reviewer

## Description

A specialized skill for conducting peer reviews of academic papers using a comprehensive 25-criterion evaluation framework with **adaptive weighting by article type**. Operates as an expert system: classifies paper type → applies specialized weight profile → evidence-based assessment → transparent publication recommendations.

**Architecture:**
1. **Article type classification** (empirical, theoretical, review, case study)
2. **Adaptive weight profile selection** (5 profiles optimized for each type)
3. **Evidence-based criterion scoring** (0–4 with mandatory justifications)
4. **Critical criterion gates** (absolute rejection triggers for ethics/plagiarism; type-dependent gates for methodology/novelty)
5. **Weighted aggregation** (sum of weighted criterion scores per profile)
6. **Recommendation mapping** (85%+ = Accept/Minor Revision; 65–84% = Major Revision; <65% = Reject)

**Key features:**
- Prevents formatting excellence from masking scientific weaknesses (weights prioritize methodology/evidence for empirical papers)
- Type-aware novelty assessment (conceptual contribution ≠ empirical discovery; reviews and case studies evaluated on transfer not discovery)
- Separates scientific quality from editorial scope alignment (papers may be excellent but out-of-scope)
- Supports both rapid desk reviews (unweighted) and high-stakes full reviews (weighted by profile)
- Mandatory evidence-based justifications for all low scores (protects against AI hallucination)

## Priority Rules

Prioritize in this order when requirements conflict:
1. **Accuracy of assessment** — every score must be supported by explicit manuscript evidence; no unsupported claims
2. **Research integrity** (Criteria 22, 23) — ethics violations and plagiarism are absolute rejection grounds
3. **Scientific validity** (Criteria 7, 9) — methodological soundness and result reliability determine publication feasibility
4. **Evidence-based justification** — all scores ≤1 require specific reference to section, page, table, or statement from manuscript
5. **Constructive improvement advice** — feedback must be actionable and clearly tied to criterion assessment

## When to Use

- Composing full peer reviews for journal submissions or conference papers
- Conducting desk reviews (rapid editorial screening) using critical criteria only
- Assessing manuscript scientific quality, contribution, and publication readiness
- Providing structured feedback across 25 standardized criteria organized by content block
- Generating publication recommendations (Accept, Minor Revision, Major Revision, Reject)
- Documenting review rationale and critical decision points with criterion-by-criterion justification
- Adapting review scope for different article types (empirical, theoretical, review, case study)

**⚠️ Mandatory prerequisites before beginning review:**
1. Confirm sufficient expertise in the paper's domain; if expertise mismatch exists, disclose in Confidence Level section
2. Access complete manuscript (full text, figures, tables, supplementary materials if referenced)
3. Commit to providing evidence-based justification: every score ≤1 must reference specific manuscript location
4. Ensure manuscript is not anonymized in a way that prevents evaluation

## Instructions

1. **Collect metadata** - record paper title, article type (empirical, theoretical, review, case study, other), and review scope (desk review vs. full review)
   - **Help:** See [references/article-type-guide.md](references/article-type-guide.md) for classification decision tree
2. **Read and understand the paper** - familiarize yourself with the full manuscript: abstract, introduction, methods, results, discussion, conclusions, and references
3. **Evaluate article type** - confirm the article type matches the author's claim; note article-specific adaptations (e.g., Criterion 8 is N/A for theoretical articles; Criteria 7–9 assess source selection/synthesis quality for reviews)
   - **Select weight profile:** Based on article type, select corresponding Adaptive Weight Profile (Empirical, Systematic Review, Narrative Review, Theoretical, or Case Study)
   - **Quick reference:** See [assets/weight-profiles-summary.md](assets/weight-profiles-summary.md) for all 5 profiles at a glance
   - **Document choice:** Record selected profile in Review Metadata for transparency and auditability
4. **Score each criterion** - evaluate each of the 25 criteria using the 0–4 scale plus special codes:
   - **0**: Criterion not met / absent entirely; critical deficiency
   - **1**: Serious shortcomings requiring substantial revision
   - **2**: Satisfactory but with notable gaps or weaknesses requiring correction
   - **3**: Good quality; minor remarks or room for improvement
   - **4**: Excellent; no remarks
   - **N/A** (not applicable): Criterion does not apply to this article type
   - **Unable to assess** (cannot assess): Impossible to evaluate based on provided materials; request clarification from authors
5. **Apply justification rule** - whenever scoring 0 or 1 on any criterion, provide a concise evidence-based explanation in the Comment column (1–3 sentences; required, not optional)
   - **Templates:** Use review templates from [templates/](templates/) directory matching your article type
   - **Example:** See [examples/example-empirical-review.md](examples/example-empirical-review.md) for a complete worked review
6. **Identify critical criteria** - check if any critical criteria (⚠ markers) scored 0–1:
   - **Desk review checklist:** Use [assets/critical-criteria-checklist.md](assets/critical-criteria-checklist.md) for rapid screening
   - Criterion 2 (Scientific novelty)
   - Criterion 7 (Methodological correctness)
   - Criterion 9 (Result reliability)
   - Criterion 22 (Research ethics)
   - Criterion 23 (Plagiarism/fabrication)
   - Criterion 25 (Alignment with journal scope)
   - **Decision rule:** Any critical criterion ≤1 automatically triggers Major Revision or Reject, regardless of aggregate score
7. **Identify hard-reject grounds** - check the desk-reject checklist (page 2 of template) for go/no-go conditions
8. **Calculate aggregate score** - apply the formula: 
   - **Option A (Unweighted, simple, recommended for desk reviews):**
   $$\text{Score \%} = \frac{\text{Sum of scores}}{\text{Max applicable criteria (excluding N/A, Unable to assess)}} \times 100\%$$
   - **Option B (Weighted by article type, recommended for full reviews):** Select Adaptive Weight Profile matching article type; see "How to Calculate Weighted Score" section for detailed formula
   - **Worksheet:** Use [assets/calculation-worksheet.md](assets/calculation-worksheet.md) to track your calculations step-by-step
9. **Determine recommendation** - map aggregate score and critical criterion status to recommendation:
   - **85–100%, no critical ≤1** → Accept or Minor Revision
   - **65–84%, no critical ≤1** → Major Revision
   - **< 65% OR any critical ≤1** → Major Revision or Reject
   - **Hard-reject grounds present** → Desk Reject (Reject without full review)
   - **Interpretation guide:** See [assets/score-interpretation-guide.md](assets/score-interpretation-guide.md) for detailed meaning of each score range
10. **Compose major and minor comments** - separate substantial concerns (logic, methodology, contribution) from minor issues (style, formatting, citations)
11. **Document reviewer confidence** - disclose conflict of interest and confidence level (high/medium/low) in the assessment
12. **Finalize recommendation** - select one of four outcomes with explicit rationale connecting criterion scores to the decision

## The 25-Criterion Evaluation Framework

### Block 1: Content & Scientific Value (5 criteria)

| № | Criterion | Codes | Description |
| --- | --- | --- | --- |
| 1 | **Topic Relevance and Problem Formulation** | 0–4 | Relevance and timeliness of the research problem in the current scientific landscape; clarity of problem formulation |
| 2 | **⚠ Scientific Novelty** | 0–4 | Originality and type of contribution: conceptual, methodological, empirical, or applied; extent of new insight relative to prior work |
| 3 | **Clarity of Aims, Objectives, and Research Questions** | 0–4, N/A | Explicit, measurable, and focused statement of research aims, research questions, or hypotheses |
| 4 | **Theoretical Significance** | 0–4, N/A | Potential to advance theory, conceptual frameworks, or understanding within the discipline |
| 5 | **Practical Applicability and Value of Results** | 0–4, N/A | Applicability and potential impact on practice, policy, or applied domains |

### Block 2: Methodology & Results (8 criteria)

| № | Criterion | Codes | Description |
| --- | --- | --- | --- |
| 6 | **Completeness and Currency of Literature Review** | 0–4 | Comprehensive, up-to-date coverage of relevant prior work; identification of research gaps |
| 7 | **⚠ Methodological Correctness** | 0–4, N/A | Soundness of research design, method selection, sampling, and procedural rigor; correctness of analytical approach |
| 8 | **Statistical Analysis Correctness** | 0–4, N/A, Unable to assess | Appropriateness of statistical tests, assumptions verification, and absence of errors (empirical works only) |
| 9 | **⚠ Result Reliability and Validity** | 0–4 | Robustness and reproducibility of findings; absence of overgeneralization; sufficient data support for claims |
| 10 | **Quality and Clarity of Illustrative Materials** | 0–4 | Professional presentation of tables, figures, and illustrations; clarity and relevance to text |
| 11 | **Discussion of Study Limitations** | 0–4 | Explicit acknowledgment and analysis of study limitations, constraints, and boundary conditions |
| 12 | **Validity and Alignment of Conclusions** | 0–4 | Conclusions directly supported by results; no logical gaps or overstatement |
| 13 | **Reproducibility** | 0–4, N/A, Unable to assess | Availability and transparency of data, code, protocols, or materials enabling independent verification; alignment with open science standards (Open Science Framework, FAIR principles) |

### Block 3: Presentation & Format (8 criteria)

| № | Criterion | Codes | Description |
| --- | --- | --- | --- |
| 14 | **Alignment of Title, Abstract, and Content** | 0–4 | Title, abstract, and content are aligned; abstract accurately summarizes the paper |
| 15 | **Abstract Informativeness and Correctness** | 0–4 | Abstract is informative, structured (background–methods–results–conclusions), and concise |
| 16 | **Keyword Correctness** | 0–4, N/A | Keywords are precise, discipline-appropriate, and representative of paper content |
| 17 | **Logical Structure and Coherence** | 0–4 | Clear narrative flow; coherent section organization; effective transitions and argument continuity |
| 18 | **Scientific Terminology Correctness** | 0–4 | Appropriate, consistent, and precise use of domain-specific terminology throughout |
| 19 | **Language Clarity and Scientific Style** | 0–4 | Readable, well-written prose; appropriate academic tone; minimized ambiguity and jargon overuse |
| 20 | **Formatting Quality** | 0–4 | Compliance with journal formatting guidelines; professional appearance (spacing, fonts, margins, numbering) |
| 21 | **Bibliography Correctness, Completeness, and Currency** | 0–4 | Citation accuracy, completeness, current scholarship representation, and consistent formatting |

### Block 4: Ethics, Transparency & Fit (4 criteria)

| № | Criterion | Codes | Description |
| --- | --- | --- | --- |
| 22 | **⚠ Compliance with Research Ethics** | 0–4, N/A | Adherence to ethical standards: informed consent, IRB approval, data confidentiality, absence of fabrication/falsification |
| 23 | **⚠ Absence of Plagiarism and Improper Borrowing** | 0–4, Unable to assess | No evidence of plagiarism, self-plagiarism, or improper citation/paraphrasing |
| 24 | **Transparency of Funding and Conflict of Interest Disclosure** | 0–4 | Funding sources disclosed; conflicts of interest (or their absence) explicitly stated by authors |
| 25 | **⚠ Alignment with Journal Scope (Aims & Scope)** | 0–4 | Alignment with journal scope, target audience, and submission requirements; appropriate article type |

## Scoring Scale and Codes

| Code | Meaning |
| --- | --- |
| **0** | Criterion not met / absent entirely; critical deficiency |
| **1** | Serious shortcomings requiring substantial revision |
| **2** | Satisfactory but with notable gaps or weaknesses requiring correction |
| **3** | Good quality; minor remarks or room for improvement |
| **4** | Excellent; no remarks |
| **N/A** | Not applicable for this article type |
| **Unable to assess** | Cannot assess based on provided materials; request author clarification |

### Mandatory Justification Rule
When scoring **0 or 1** on any criterion, the reviewer **must** provide:
1. Concise evidence-based explanation (1–3 sentences) in the Comment column — **non-optional**
2. Explicit reference to manuscript location: section name, page, table number, or specific statement
3. If evidence is not found in manuscript, state explicitly: "Not addressed in manuscript"

### Absolute Rejection Triggers (Hard Reject Criteria)

These criteria, if scored 0–1, **automatically trigger Reject** regardless of aggregate score or article type:

- **Criterion 22: Research Ethics** (0–1) — IRB violations, informed consent failures, fabrication evidence, undisclosed conflicts of interest
- **Criterion 23: Plagiarism Absence** (0–1) — evidence of plagiarism, self-plagiarism, or substantial unattributed borrowing

### Scientific Fatal Flaws (Major Revision / Reject Triggers)

These criteria, if scored 0–1, trigger **Major Revision or Reject** depending on article type:

- **Criterion 7: Methodological Correctness** (0–1) — fundamental design flaws, invalid statistical approach, inappropriate methods for research question
  - Exception for *review papers*: assess source selection quality; if 0–1, indicates major systematic review failure (bias, inadequate search strategy)
- **Criterion 9: Result Reliability and Validity** (0–1) — data insufficient, major analytical errors, conclusions unsupported by results
  - Applies to all article types; cannot be circumvented

### Editorial Filters (Not Critical for Scientific Assessment)

- **Criterion 25: Alignment with Journal Scope** (0–1) — does **NOT** trigger automatic rejection; indicates desk reject at editorial screening stage
  - A scientifically excellent paper misaligned with journal scope = Desk Reject by editor, not Reviewer Reject
  - Reviewer should note: "Excellent quality but out of scope"

### Nuanced Critical Criterion: Scientific Novelty

- **Criterion 2: Scientific Novelty** — score depends on article type:
  - **Empirical/Experimental papers**: 0–1 triggers Major Revision or Reject
  - **Theoretical papers**: 0–1 triggers Major Revision; conceptual contribution counts as novelty
  - **Systematic Reviews / Literature Reviews**: 0–1 only if systematic approach itself is not novel; replication of prior reviews ≠ rejection
  - **Dataset Papers / Negative Results Papers / Replication Studies**: Low novelty is expected; score reflects dataset quality/methodological rigor instead
  - **Guideline for decision**: If article type accepts limited empirical novelty, use Criterion 2 to assess contribution within its category rather than absolute originality

## Scoring Calculation & Recommendation Logic

### Formula for Overall Quality Score
$$\text{Overall Score \%} = \frac{\text{Sum of numeric scores (0–4)}}{\text{Maximum applicable criteria (excluding N/A and Unable to assess)}} \times 100\%$$

### Interpretation Guidelines

| Score Range (Weighted or Unweighted) | Guideline (absent critical ≤1) |
| --- | --- |
| **85–100%** | **Accept** or **Minor Revision** |
| **65–84%** | **Major Revision** |
| **< 65%** | **Reject** |

**Note:** Thresholds apply identically whether using unweighted or weighted scoring. The choice of weighting method (Option A or B) does not change the interpretation of the final percentage score.

### Decision Overrides

- **Absolute rejection triggers** (Criteria 22, 23 scored 0–1) → **Reject** (hard reject, no revision possible)
- **Scientific fatal flaws** (Criteria 7, 9 scored 0–1 in applicable article types) → **Major Revision or Reject**
- **Novelty issues** (Criterion 2 scored 0–1) → **Major Revision** (not automatic Reject; depends on article type; see nuanced guidance above)
- **Journal scope mismatch** (Criterion 25 scored 0–1) → **Desk Reject recommendation to editor** (not Reviewer Reject; paper quality ≠ scope fit)
- **≥2 "Unable to assess" codes in Methodology block** → Request additional materials from authors before final decision
- **Hard-reject grounds present** (see checklist below) → **Desk Reject** (editorial screening, no full review required)

## Adaptive Weighting by Article Type

**Overview:** Different article types prioritize different criteria. Instead of uniform weighting, select the weight profile matching the article's type, then apply weights to calculate the final score.

**Why adaptive weighting?**
- Empirical papers are judged primarily on methodology and result reliability
- Systematic reviews are judged on search rigor, synthesis quality, and evidence integration
- Theoretical papers are judged on conceptual novelty and argumentative coherence
- Case studies are judged on case uniqueness and methodological soundness
- Literature reviews are judged on comprehensiveness and critical synthesis

**For detailed rationale on each profile, see:** [references/weight-profile-rationale.md](references/weight-profile-rationale.md)

**Workflow:**
1. Identify article type (already done in Instruction Step 3)
2. Select corresponding weight profile below (or consult [assets/weight-profiles-summary.md](assets/weight-profiles-summary.md) for quick reference)
3. Apply weights to applicable criteria when calculating aggregate score
4. Document selected profile in Review Metadata section

### Weight Profile 1: Empirical / Experimental Research

**Rationale:** Answers "Is the result rigorously demonstrated?"

| Criterion | Category | Weight |
| --- | --- | --- |
| 2 | Scientific Novelty | 8% |
| 7 | Methodological Correctness | 15% |
| 8 | Statistical Analysis | 8% |
| 9 | Result Reliability & Validity | 15% |
| 12 | Conclusions Validity | 8% |
| 22 | Research Ethics | 10% |
| 23 | Plagiarism Absence | 10% |
| Others (1, 3–6, 10–11, 13–21, 24–25) | Supporting criteria | 26% |

**Aggregation formula:**
$$\text{Weighted Score} = \sum (\text{Criterion score} \times \text{Weight}) / 100$$

---

### Weight Profile 2: Systematic Review / Meta-Analysis

**Rationale:** Answers "Is the evidence synthesis systematic and unbiased?"

| Criterion | Category | Weight |
| --- | --- | --- |
| 6 | Literature Review Completeness & Search Rigor | 15% |
| 7 | Systematic Review Methodology (inclusion criteria, bias assessment, PRISMA compliance) | 15% |
| 8 | Statistical Analysis / Meta-analysis (if applicable) | 8% |
| 9 | Evidence Synthesis Quality & Absence of Cherry-Picking | 15% |
| 12 | Conclusions from Evidence | 8% |
| 2 | Novel Contribution (e.g., new synthesis, gap identification) | 10% |
| 22 | Research Ethics | 10% |
| 23 | Plagiarism Absence | 10% |
| Others (1, 3–5, 10–11, 13–21, 24–25) | Supporting criteria | 9% |

**Key adaptations:**
- Criterion 7 focuses on systematic methodology (search strategy, bias, protocol)
- Criterion 8 is N/A for narrative reviews; weighted only for meta-analyses
- Criterion 6 includes primary methodological focus (search comprehensiveness)

---

### Weight Profile 3: Narrative Literature Review

**Rationale:** Answers "Is this a comprehensive, insightful, and well-synthesized review?"

| Criterion | Category | Weight |
| --- | --- | --- |
| 6 | Literature Completeness & Coverage | 20% |
| 9 | Critical Synthesis & Balanced Evaluation | 15% |
| 4 | Theoretical Significance & Conceptual Framing | 15% |
| 2 | Novel Insight / Gap Identification | 12% |
| 12 | Conclusions & Future Directions | 10% |
| 17 | Logical Structure & Narrative Flow | 10% |
| 22 | Research Ethics | 8% |
| 23 | Plagiarism Absence | 10% |
| Others (1, 3, 5, 7–8, 10–11, 13–16, 18–21, 24–25) | Supporting criteria | 0% (informational only) |

**Key adaptations:**
- Criteria 7 and 8 → N/A (no original empirical methods)
- Criterion 9 emphasizes critical evaluation and balanced presentation
- Criterion 17 emphasizes narrative coherence and readability

---

### Weight Profile 4: Theoretical / Conceptual Paper

**Rationale:** Answers "Does this advance understanding conceptually?"

| Criterion | Category | Weight |
| --- | --- | --- |
| 2 | Scientific Novelty (conceptual, not empirical) | 20% |
| 4 | Theoretical Significance | 18% |
| 3 | Clarity of Concepts, Research Questions, Hypotheses | 15% |
| 12 | Conclusions: Logical Consistency & Coherence | 12% |
| 1 | Relevance & Problem Significance | 10% |
| 17 | Logical Structure & Argument Flow | 10% |
| 22 | Research Ethics | 8% |
| 23 | Plagiarism Absence | 7% |
| Others (6–11, 13–16, 18–21, 24–25) | Supporting criteria | 0% (informational only) |

**Key adaptations:**
- Criteria 7–9 → N/A (no empirical data collection)
- Criterion 2 prioritizes conceptual novelty over empirical discovery
- Criterion 17 emphasizes argumentation clarity
- Statistical criteria (8, 13) are not applicable

---

### Weight Profile 5: Case Study / Descriptive Report

**Rationale:** Answers "Is the case well-documented, analyzed, and transferable?"

| Criterion | Category | Weight |
| --- | --- | --- |
| 1 | Case Relevance & Problem Significance | 12% |
| 2 | Case Uniqueness & Research Contribution | 15% |
| 7 | Case Selection, Data Collection Rigor | 15% |
| 9 | Data Quality & Finding Support | 15% |
| 5 | Practical Applicability & Transferability | 12% |
| 12 | Conclusions: Generalizability Awareness | 10% |
| 17 | Narrative Clarity | 8% |
| 22 | Research Ethics & Participant Confidentiality | 10% |
| 23 | Plagiarism Absence | 7% |
| Others (3, 4, 6, 8, 10, 11, 13–16, 18–21, 24–25) | Supporting criteria | 0% (informational only) |

**Key adaptations:**
- Criterion 2 assesses case uniqueness, not scientific novelty
- Criterion 7 emphasizes data collection soundness and case documentation
- Criterion 5 (practical significance) emphasizes transferability rather than universal claims
- Statistical analysis (8) typically N/A

---

### How to Calculate Weighted Score

**Step 1:** Score all applicable criteria (0–4, N/A, or Unable to assess)

**Step 2:** Select weight profile matching article type

**Step 3:** For each criterion with a weight > 0%:
$$\text{Weighted Contribution} = \text{Criterion Score (0–4)} \times \frac{\text{Criterion Weight}}{100}$$

**Step 4:** Sum all weighted contributions:
$$\text{Final Weighted Score} = \sum \text{Weighted Contributions}$$

**Step 5:** Convert to percentage (maximum = 4.0):
$$\text{Weighted Score \%} = \frac{\text{Final Weighted Score}}{4.0} \times 100\%$$

**Step 6:** Apply recommendation mapping:
- **85–100%** (weighted, no absolute rejections) → **Accept** or **Minor Revision**
- **65–84%** (weighted, no fatal flaws) → **Major Revision**
- **< 65%** OR fatal flaws present → **Major Revision or Reject**

**Note on N/A and Unable to assess:**
- Criteria marked N/A receive 0% weight automatically
- Criteria marked "Unable to assess" are excluded from both numerator and denominator, then score is renormalized to 100%

**Use [assets/calculation-worksheet.md](assets/calculation-worksheet.md) to systematically calculate your weighted scores.**

---

### Recommendation: Use Adaptive Weighting for High-Stakes Reviews

| Review Type | Recommendation |
| --- | --- |
| Journal desk review (5–10 min) | Unweighted (equal criteria) |
| Full peer review (standard) | Weighted profile (select by article type) |
| Appeals / re-review | Weighted profile + confidence justification |

## Hard-Reject Conditions (Desk Reject / Immediate Rejection)

**Use [assets/critical-criteria-checklist.md](assets/critical-criteria-checklist.md) for systematic desk review screening (5–10 min).**

**Absolute rejection** — Recommend **Reject** without full review if ANY of the following apply:

- [ ] Research ethics violation or fabrication evidence (Criterion 22 = 0–1)
- [ ] Substantial plagiarism or self-plagiarism (Criterion 23 = 0–1)

**Major Revision or Reject** — Recommend **Major Revision** or **Reject** depending on severity and article type:

- [ ] Fundamental methodological errors or invalid approach (Criterion 7 = 0–1)
- [ ] Unreliable, unsubstantiated, or contradicted results (Criterion 9 = 0–1)

**Editorial screening (Desk Reject by editor, not reviewer)** — Note for editorial decision:

- [ ] Misalignment with journal scope or target audience (Criterion 25 = 0–1)
  - *Action*: Recommend editor send Desk Reject; paper may be excellent but out of scope
  - *Reviewer role*: Complete assessment if requested, but flag scope mismatch

**Conditional rejection depending on article type** — Check article type before rejecting on novelty grounds:

- [ ] No scientific novelty — BUT check article type (reviews, datasets, negative results, replications may have low novelty by design; see Criterion 2 nuanced guidance)

## Input Recovery Rules

- Assume **full peer review** (all 25 criteria) when review scope is not specified; use desk review only when explicitly requested
- Assume a **0–4 scoring scale** with code options (N/A, Unable to assess) when scoring guidance is not provided
- Assume **IMRAD structure** (Introduction–Methods–Results–Analysis–Discussion) for empirical/experimental research unless article type indicates otherwise
- Assume **English-language scientific writing conventions** unless the paper's language or discipline provides contrary evidence
- Assume **constructive tone** in all justifications even when scoring is critically low
- Assume **critical criteria enforcement** (automatic escalation on ≤1 scores) unless the venue explicitly waives critical-criterion policies
- Ask for clarification only when:
  - Critical manuscript content is missing (incomplete sections, unreadable figures, data unavailable)
  - Article type is ambiguous or misclassified
  - Reviewer expertise gaps prevent fair assessment of specific methods (use confidence level reporting instead)

## Article-Type Adaptations

### Empirical / Experimental Research
- All 25 criteria apply as stated
- Criterion 8 (statistical correctness) is required; may be marked as N/A only for purely qualitative work
- Criteria 7, 9: Focus on methodological design, data quality, and result robustness

### Theoretical / Conceptual Papers
- Criterion 8 → mark as **N/A** (statistical analysis not applicable)
- Criteria 7, 9: Assess logical coherence, theoretical soundness, and argument validity instead of empirical rigor
- Criterion 13: Prioritize precision of conceptual definitions and terminology

### Systematic Reviews / Literature Reviews
- Criteria 7–9: Assess quality of source selection, synthesis methodology, and evidence integration rather than original empirical methods
- Criterion 8 → mark as **N/A** unless meta-analysis is performed
- Criterion 6: Emphasize completeness of search strategy and source coverage

### Case Studies / Descriptive Reports
- Criteria 2, 3, 4: Focus on uniqueness of case and clarity of research questions
- Criterion 7: Assess data collection rigor and case representativeness
- Criterion 9: Assess transferability and practical relevance

### Humanities & Social Sciences (Philosophy, History, Philology, Law, Theology)
- **Criterion 2 (Novelty):** Assess conceptual/interpretive contribution, not empirical discovery; novel reading, framework, or synthesis counts
- **Criterion 7 (Methodology):** Evaluate hermeneutic rigor, source critique quality, argument coherence instead of quantitative validity
- **Criterion 9 (Reliability):** Assess evidentiary support for interpretations; multiple reasonable interpretations ≠ unreliability
- **Criteria 8, 13 (Statistics, Reproducibility):** Mark as **N/A** unless empirical data collection (e.g., surveys, interviews) is core method
- **Criterion 6 (Literature Review):** Prioritize comprehensive philosophical/historical grounding; primary source engagement
- **Presentation (Block 3):** Argumentation clarity more important than standard formatting; hermeneutic transparency valued

## Constraints

- Do not assign scores without explicit justification when scoring 0 or 1; include specific manuscript reference (section, page, table, figure)
- Do not assign scores based on assumption or inference; if evidence is not in manuscript, state "Not addressed" explicitly
- Do not override critical-criterion escalation rules based on aggregate percentage alone
- Do not recommend acceptance if any absolute rejection trigger (Criteria 22, 23 = 0–1) is met
- Do not reject on novelty grounds (Criterion 2) without first confirming article type appropriateness for the claimed contribution level
- Do not assess novelty (Criterion 2) against unpublished or in-preparation work outside the scope of the review
- Do not use "Unable to assess" codes as an excuse for noncommittal assessment; request author clarification when marked
- Do not impose citation or formatting standards (Criterion 20–21) beyond the venue's stated requirements
- Do not mix review types (desk review vs. full review); choose one mode at the start and commit to it
- Maintain reviewer anonymity and confidentiality per COPE and ICMJE ethical standards
- **Critical:** Every score ≤1 must cite specific evidence from the manuscript. Never score without verifiable basis.

## Deliverables

**For Full Peer Review:**
1. Review metadata (paper title, article type, review date, reviewer identifier if applicable)
2. Completed 25-criterion evaluation table with scores and justifications
3. Aggregate score summary (percentage, breakdown by block)
4. Major concerns section (substantial issues affecting scientific value, methodology, or contribution)
5. Minor concerns section (style, formatting, citations, clarity)
6. Publication recommendation (one of four outcomes) with explicit rationale
7. Revision guidance (if Major/Minor Revision recommended): specific, actionable suggestions
8. Reviewer confidence disclosure (COI statement, confidence level)
9. Closing remarks for editorial team

**For Desk Review (rapid screening):**
1. Critical criteria assessment (2, 7, 9, 22, 23, 25) only
2. Hard-reject condition check
3. Single recommendation (Accept for full review / Desk Reject)
4. Brief rationale (2–3 sentences)

## Output Contract

Return output in this order:

1. **Review Metadata**
   - Paper title, article type, submission date, reviewer ID
   - Review scope (Full / Desk)
   - **Weighting profile selected:** Which of the 5 Adaptive Weight Profiles was used (Empirical, Systematic Review, Narrative Review, Theoretical, Case Study)
   - **Justification for profile selection:** Brief note if article type was ambiguous or if profile was adapted

2. **Criteria Evaluation Table**
   - All 25 criteria (or critical subset for desk review)
   - Organized by Block (1–4)
   - Columns: Nr., Criterion, Score (0–4 / N/A / Unable to assess), Reviewer Comment (required when score ≤1)

3. **Aggregate Score Summary**
   - Total points earned
   - Maximum applicable points (excluding N/A, Unable to assess)
   - Overall percentage score
   - Distribution by block (optional but recommended)

4. **Major Concerns Section**
   - Numbered list of substantial issues impacting scientific contribution, methodology, or publication fit
   - Each concern references relevant criteria
   - Tone: professional, constructive, evidence-based

5. **Minor Concerns Section**
   - Numbered list of minor issues: style, formatting, terminology, clarity refinements
   - Each concern includes suggested correction or clarification
   - Optional but recommended for Major/Minor Revision decisions

6. **Publication Recommendation**
   - [ ] **Accept** — No changes required; paper meets journal standards across criteria
   - [ ] **Minor Revision** — Solid contribution; request small revisions (clarity, formatting, minor methodology) not requiring revalidation
   - [ ] **Major Revision** — Significant improvements needed (methodology, analysis, evidence integration, restructuring); resubmission required with point-by-point response
   - [ ] **Reject** — Fundamental issues cannot be resolved; recommend authors consider alternative venues
   - **Rationale:** 2–3 sentences connecting criteria scores and critical assessment to the chosen outcome

7. **Revision Guidance** (if Major/Minor Revision)
   - Priority 1 (Critical): Address all issues tied to criteria ≤1, especially critical criteria
   - Priority 2 (Major): Resolve systematic gaps in methodology, evidence, or structure
   - Priority 3 (Minor): Polish presentation, terminology, and format

8. **Reviewer Metadata**
   - Conflict of Interest: [ ] None / [ ] Yes (specify nature)
   - **Expertise Assessment** (REQUIRED BEFORE BEGINNING REVIEW):
     - [ ] **High:** Domain expertise matches paper scope; comfortable assessing all 25 criteria
     - [ ] **Medium:** General expertise; some criteria (especially methodology-specific) may need specialist input
     - [ ] **Low / Expertise Mismatch:** Paper outside main research area; recommend escalation to specialist; still review but explicitly disclose limitations
   - **If Expertise is Medium or Low:**
     - Avoid detailed scoring of Criteria 7–9 (methodology-specific assessments) if you cannot verify correctness
     - Mark "Unable to assess" rather than guess
     - Recommend editor consider specialist co-reviewer
   - Confidence Level: [ ] High / [ ] Medium / [ ] Low (brief explanation if Medium/Low)

9. **Closing Remarks**
   - Brief professional summary for editorial team
   - Any special considerations (methodological novelty, interdisciplinary aspects, resource constraints noted)

## Tools and Practices

- Peer-review best practices and ICMJE/COPE ethical guidelines
- Desk-reject screening methodology for rapid editorial filtering
- Discipline-specific evaluation frameworks and reporting standards (CONSORT, PRISMA, STROBE, etc.)
- Critical-criterion escalation and override logic for decision-making consistency
- Article-type adaptation rules for heterogeneous submission portfolios
- Reviewer confidence self-assessment and COI disclosure protocols

## Usage Modes

### Full Peer Review (20–30 minutes per paper)
- Complete all 25 criteria
- Score all applicable criteria; mark N/A or Unable to assess as appropriate
- **Select Adaptive Weight Profile** matching article type (5 profiles available)
- Calculate aggregate score using **Weighted formula** (Option B)
- Provide justifications for all scores ≤1 (mandatory)
- Compose major and minor comments sections
- Map weighted score to recommendation using thresholds (85%, 65%)
- Disclose reviewer confidence and COI
- **Document selected weight profile in Review Metadata**

### Desk Review (Rapid Screening; 5–7 minutes per paper)
- Evaluate critical criteria only (2, 7, 9, 22, 23, 25) + criteria 1 and 14 for context
- Check hard-reject conditions
- Provide brief rationale (2–3 sentences)
- Recommend Accept for full review OR Desk Reject
- Escalate to full review if critical criteria pass but hard-reject conditions absent

## References

- **ICMJE Recommendations** (International Committee of Medical Journal Editors) — ethical conduct, conflicts of interest, and peer-review standards
- **COPE Guidelines** (Committee on Publication Ethics) — professional standards for reviewers, editors, and publishers; plagiarism, data integrity, and ethics policies
- **Reporting Guidelines by Discipline:**
  - CONSORT (Consolidated Standards of Reporting Trials) — clinical trials
  - PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) — systematic reviews
  - STROBE (Strengthening the Reporting of Observational Studies in Epidemiology) — observational studies
  - ARRIVE (Animal Research: Reporting In Vivo Experiments) — animal research
  - Others as appropriate to discipline
- **Peer Review Standards** — best practices for constructive, timely, and evidence-based review
- **Research Ethics Frameworks** — IRB protocols, informed consent, data privacy, and research integrity standards
- **Open Science & Reproducibility:**
  - FAIR Data Principles (Findable, Accessible, Interoperable, Reusable) for data stewardship
  - Open Science Framework (OSF) and preregistration standards
  - Transparency in reporting: Open Access publishing, code sharing, data availability statements

---

## Framework Architecture

This skill implements an **expert system approach** to peer review:

```
Paper submitted
    ↓
Step 1: Classify article type
    ↓
Step 2: Select adaptive weight profile (5 profiles by type)
    ↓
Step 3: Score 25 criteria with evidence-based justifications
    ↓
Step 4: Apply critical criterion gates (ethics, methodology, novelty)
    ↓
Step 5: Calculate weighted aggregate score (type-specific weights)
    ↓
Step 6: Map to recommendation (85%+ Accept/Minor; 65–84% Major Rev; <65% Reject)
    ↓
Output: Structured review with clear rationale
```

**Why this matters:**
- **Type-aware assessment:** Empirical papers prioritize methodology (40%); theoretical papers prioritize concepts (40%); reviews prioritize synthesis (40%)
- **Prevents systematic bias:** A poorly formatted empirical paper with excellent methods gets a realistic score; a beautifully written review with shallow synthesis doesn't mask weak analysis
- **Scalable to new types:** Adding new article types (protocols, research notes, datasets) requires only a new weight profile, not redesigning the entire framework

---

## Quick Navigation

### 📋 Assets — Working Materials for Reviewers

| Resource | Purpose |
| --- | --- |
| [weight-profiles-summary.md](assets/weight-profiles-summary.md) | 1-page table: all 5 weight profiles side-by-side |
| [calculation-worksheet.md](assets/calculation-worksheet.md) | Spreadsheet-style form for step-by-step score calculation |
| [critical-criteria-checklist.md](assets/critical-criteria-checklist.md) | 5–10 min desk review checklist for rapid screening |
| [score-interpretation-guide.md](assets/score-interpretation-guide.md) | How to interpret final score; common scoring mistakes |

### 📝 Templates — Review Templates by Article Type

| Article Type | Template |
| --- | --- |
| Empirical / Experimental | [review-template-empirical.md](templates/review-template-empirical.md) |
| Systematic Review / Meta-Analysis | [review-template-systematic-review.md](templates/review-template-systematic-review.md) |
| Narrative Literature Review | [review-template-narrative-review.md](templates/review-template-narrative-review.md) |
| Theoretical / Conceptual | [review-template-theoretical.md](templates/review-template-theoretical.md) |
| Case Study / Descriptive | [review-template-case-study.md](templates/review-template-case-study.md) |
| Reviewer Metadata | [metadata-template.md](templates/metadata-template.md) |

### 📖 Examples — Worked-Through Complete Reviews

| Example | Purpose |
| --- | --- |
| [example-empirical-review.md](examples/example-empirical-review.md) | Full peer review of empirical paper (10 pages); shows weighted scoring with Profile 1 |
| [example-desk-review.md](examples/example-desk-review.md) | Rapid desk review (5 min); demonstrates rejection rationale |

### 📚 References — Detailed Guides and Standards

| Reference | Content |
| --- | --- |
| [reporting-guidelines.md](references/reporting-guidelines.md) | CONSORT, PRISMA, STROBE, ARRIVE, SRQR requirements by study type |
| [icmje-cope-standards.md](references/icmje-cope-standards.md) | Authorship, conflicts of interest, data access, research ethics standards |
| [weight-profile-rationale.md](references/weight-profile-rationale.md) | Why each of the 5 profiles weighs criteria differently; how to extend to new types |
| [article-type-guide.md](references/article-type-guide.md) | Decision tree for classifying empirical vs. review vs. case vs. theoretical papers |

---

## References

- **ICMJE Recommendations** (International Committee of Medical Journal Editors) — ethical conduct, conflicts of interest, and peer-review standards
  - Detailed standards: See [references/icmje-cope-standards.md](references/icmje-cope-standards.md)
- **COPE Guidelines** (Committee on Publication Ethics) — professional standards for reviewers, editors, and publishers; plagiarism, data integrity, and ethics policies
  - Detailed standards: See [references/icmje-cope-standards.md](references/icmje-cope-standards.md)
- **Reporting Guidelines by Discipline:**
  - All guidelines documented in: [references/reporting-guidelines.md](references/reporting-guidelines.md)
- **Peer Review Standards** — best practices for constructive, timely, and evidence-based review
- **Research Ethics Frameworks** — IRB protocols, informed consent, data privacy, and research integrity standards
- **Open Science & Reproducibility:**
  - FAIR Data Principles (Findable, Accessible, Interoperable, Reusable) for data stewardship
  - Open Science Framework (OSF) and preregistration standards
  - Transparency in reporting: Open Access publishing, code sharing, data availability statements
