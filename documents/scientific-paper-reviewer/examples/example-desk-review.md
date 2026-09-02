# Example: Desk Review (Rapid Evaluation)

**This example shows how to conduct a desk review (5–10 minutes) using the critical criteria checklist to quickly recommend accept/reject without full peer review.**

---

## Desk Review Context

**Scenario:** Editor receives 50 submissions per week. Each editor conducts 2–3 desk reviews daily to filter obvious rejects before sending to full peer review. A desk review focuses on critical stopping criteria only.

---

## Review Metadata

| Field | Value |
| --- | --- | 
| **Paper ID** | MS-2026-04-7823 |
| **Paper Title** | Efficacy of Blockchain-Based Learning Analytics for Student Engagement Prediction |
| **First Author** | Johnson, K. |
| **Submission Date** | 2026-04-01 |
| **Review Type** | Desk Review (Editor decision) |
| **Time Allocated** | 7 minutes |
| **Target Journal** | *International Journal of Educational Technology Research* |

---

## Critical Criteria Desk Review

*Use [critical-criteria-checklist.md](../assets/critical-criteria-checklist.md) — score ONLY critical criteria; others marked N/A.*

### ⚠ ABSOLUTE REJECTION TRIGGERS

#### [✓] Criterion 22: Research Ethics

**What I'm looking for:** IRB approval statement. Informed consent. Participant privacy protection.

**Evidence from manuscript:**

> Page 2: "This study received IRB approval from [Institution Name] (IRB #2026-02-1234)."
> 
> Page 6: "Student participants provided written informed consent. Data were de-identified..."

**Assessment:** ✅ **PASS** — Ethics standards met.

---

#### [✓] Criterion 23: Plagiarism Check

**What I'm checking:** Verbatim copy-paste? Missing citations? Unattributed quotations?

**Quick method:**
- Skim introduction (check citation density)
- Check if literature section paraphrases vs. copies
- Spot-check 2–3 paragraphs in methods

**Evidence:**

> Checked Pages 3–5 (Introduction). Literature is properly paraphrased with citations. No verbatim copying detected. 
> Methods section (Page 6): Clear methodological description, properly attributed.
> Spot-check: "Machine learning models were trained using scikit-learn (Pedregosa et al., 2011)" — properly cited.

**Assessment:** ✅ **PASS** — No plagiarism indicators.

---

### ⚠ SCIENTIFIC FATAL FLAWS

#### [✓] Criterion 7: Methodological Correctness

**For empirical papers:** Are methods clearly described? Reproducible?

**Evidence from manuscript:**

> Abstract: "Mixed-methods study combining student survey (n=250) and learning analytics data (n=8 online courses)."
>
> Methods section: Methods described but... **ISSUE:** No details on how blockchain was actually integrated. Page 7 states: "Blockchain-based architecture was implemented" but provides no technical details. No appendix with system diagram or code documentation.
>
> Data collection: "LMS data were extracted and run through blockchain validator..." — unclear. How exactly?
>
> **Analysis:** Survey data analyzed via descriptive statistics and thematic coding. Appropriate. But blockchain's role in analysis never explained.

**Assessment:** ⚠️ **MAJOR FLAW** — Methodology insufficiently described for reproducibility. Blockchain component especially unclear.

---

#### [✓] Criterion 9: Result Reliability & Validity

**For empirical papers:** Results supported by data? Confounds controlled?

**Evidence from manuscript:**

> Results section (Page 9): "Students predicted as 'high engagement' via blockchain model showed 23% higher final grades (p=.042)."
>
> **Issue 1:** No effect size reported (only p-value). Sample size not stated. Unclear if 23% difference is meaningful.
>
> **Issue 2:** No discussion of alternative explanations. Could student self-selection explain the difference? (Students more engaged might volunteer for this intervention.) No baseline equivalence check mentioned.
>
> **Issue 3:** Statistical power analysis absent. With p=.042, this is marginal significance. Unclear if adequate power.

**Assessment:** ⚠️ **MAJOR FLAW** — Results inadequately supported. Missing effect sizes, power analysis, and confound control.

---

#### [✓] Criterion 2: Scientific Novelty (Type-Dependent)

**Article type:** Empirical (so Criterion 2 is CRITICAL, not N/A).

**What's new?** Blockchain for learning analytics? Using ML for engagement prediction?

**Evidence from manuscript:**

> Introduction (Page 3): "Learning analytics has been applied to predict engagement (Smith et al., 2020; Chen et al., 2023). This is the first study to integrate blockchain..."
>
> **Assessment:** Blockchain is a new application domain, but... the underlying engagement prediction task is well-established. Adding blockchain doesn't constitute major innovation unless blockchain *improves* prediction (which wasn't clearly demonstrated—see Criterion 9 above).

**Assessment:** ⚠️ **QUESTIONABLE NOVELTY** — Blockchain appears to be a technical wrapper around standard ML prediction. Value-add not clear.

---

### ⚠ EDITORIAL FILTER

#### [✓] Criterion 25: Journal Scope

**Does this fit *International Journal of Educational Technology Research*?**

**Journal scope:** "Publishes empirical research on digital technologies in education."

**Paper topic:** Blockchain + learning analytics + engagement prediction

**Assessment:** ✅ **PASS** — Fits journal scope (technology in education).

---

## Desk Review Decision Matrix

| Criterion | Status | Issue Severity |
| --- | --- | --- |
| C22 (Ethics) | ✅ PASS | None |
| C23 (Plagiarism) | ✅ PASS | None |
| C7 (Methodology) | ❌ FAIL | **MAJOR** — Blockchain methodology unexplained; insufficient detail for reproducibility |
| C9 (Results) | ❌ FAIL | **MAJOR** — Results inadequately supported; missing effect sizes, power analysis, confound control |
| C2 (Novelty) | ⚠️ QUESTIONABLE | **MODERATE** — Blockchain is new application but value-add not clear; may be incremental |
| C25 (Scope) | ✅ PASS | None |

---

## Desk Review Recommendation

**Decision:** 🔴 **DESK REJECT**

**Primary Reasons:**

1. **Criterion 7 failure (Methodology):** Blockchain component is inadequately explained. The paper claims to use "blockchain-based architecture" but never describes what blockchain actually does or how it differs from standard ML pipelines. This is a fundamental methodological gap. Authors must provide technical specification before consideration.

2. **Criterion 9 failure (Results):** Results lack standard scientific reporting:
   - No effect size (Cohen's d or similar)
   - No power analysis
   - No baseline equivalence check (selection bias not ruled out)
   - Marginal statistical significance (p=.042) with no discussion of practical significance
   
   These gaps suggest either careless analysis or insufficient rigor.

3. **Criterion 2 question (Novelty):** Even if methodology and results were sound, novelty is limited. Blockchain's specific contribution to engagement prediction is not demonstrated. Paper reads like "standard ML + blockchain buzzword."

---

## Editor Letter to Authors

---

**RE: MS-2026-04-7823 — Desk Review Decision**

Dear Dr. Johnson,

Thank you for submitting "Efficacy of Blockchain-Based Learning Analytics for Student Engagement Prediction" to *International Journal of Educational Technology Research*.

After desk review, we regret that we are unable to move your manuscript to full peer review at this time. While your topic falls within our journal's scope, the manuscript has several critical issues that require substantial revision before it can be considered further:

**1. Insufficient Methodological Detail**

The paper claims to use a "blockchain-based architecture" for learning analytics (Page 7), but the technical implementation is unclear. Specifically:

- How does your blockchain-based system differ from standard machine learning pipelines?
- What role does blockchain play in engagement prediction? (Is it only data storage? Validation? Consensus?)
- What blockchain platform was used? (Ethereum? Hyperledger? Custom?)
- Can you provide a system architecture diagram or pseudocode in an appendix?

This level of detail is essential for methodological rigor and reproducibility.

**2. Results Lack Standard Statistical Reporting**

Your key finding (23% higher grades, p=.042) requires:

- Effect size (Cohen's d) with 95% confidence interval
- A priori power analysis showing adequate power for this effect size
- Baseline equivalence check or statistical controls for potential selection bias (Did higher-engagement students self-select into the intervention?)
- Discussion of practical vs. statistical significance

The marginal p-value combined with missing effect sizes raises concerns about result reliability.

**3. Unclear Contribution of Blockchain**

It is not evident from the manuscript why blockchain specifically improves engagement prediction. Your results could plausibly be achieved with standard ML (without blockchain). Please clarify:

- What does blockchain add beyond standard machine learning?
- Do you have evidence that blockchain improves prediction accuracy compared to non-blockchain baselines?
- Is blockchain necessary for this application?

**Next Steps**

We invite you to address these three issues and resubmit. A revised manuscript should include:

1. Detailed technical specification of your blockchain implementation (with appendix if needed)
2. Complete statistical reporting (effect sizes, power analysis, baseline checks)
3. Clear justification of blockchain's role in improving engagement prediction

If you can substantially address these concerns, we will be happy to reconsider your work for full peer review.

Sincerely,

Editor, IJETR

---

## Key Takeaways from This Desk Review

**How to desk review efficiently (5–10 minutes):**

1. ✅ **Read abstract carefully** — Does study type match critical criteria expectations?
2. ✅ **Scan Methods (2 min)** — Can you understand what authors did? Major gaps?
3. ✅ **Skim Results (2 min)** — Are claims supported? Effect sizes? Stats reported?
4. ✅ **Check ethics/scope (1 min)** — IRB approval? Journal fit?
5. ✅ **Decide** — Pass/Fail critical criteria? If any FAIL → Desk Reject.

**In this example:**
- ❌ C7 & C9 failed → Desk Reject
- Even though C2 (novelty) was questionable, the methodology/results failures alone justify rejection

**Desk reviews save time:** Rejects 40–50% of submissions before full peer review. Only "good enough" manuscripts move to full review (where they receive 20–30 min detailed attention).

