# Article Type Classification Guide

Correctly identifying article type is **critical** for selecting the appropriate weight profile. This guide helps you classify papers accurately.

---

## Quick Classification Flowchart

```
Does the paper report ORIGINAL DATA collection/analysis?
│
├─ YES: Did authors collect DATA themselves?
│   │
│   ├─ YES, empirical data:
│   │   │
│   │   ├─ Random assignment (RCT)? → EMPIRICAL (Experimental)
│   │   ├─ Observational (no assignment)? → EMPIRICAL (Observational)
│   │   └─ Single case, in-depth study? → CASE STUDY
│   │
│   └─ NO, data analyzed but not collected (secondary):
│       └─ Exists in literature? → Check below
│
└─ NO: Is this a SYNTHESIS of existing work?
    │
    ├─ Systematic protocol used (PRISMA)?
    │   └─ YES → SYSTEMATIC REVIEW
    │
    ├─ Multiple studies, no protocol?
    │   └─ YES → NARRATIVE REVIEW
    │
    └─ Conceptual argument, no empirical data?
        └─ YES → THEORETICAL/CONCEPTUAL
```

---

## Profile 1: Empirical / Experimental Research

### What It Is
Studies with **original data collection** from experimental or observational design. Answers: "What is happening?" or "Why did X occur?"

### Key Features

| Feature | Present | Example |
| --- | --- | --- |
| **Original Data** | ✅ Authors collected new data | Survey response, interview transcript, lab measurement |
| **Research Design** | ✅ Clear design strategy | RCT, quasi-experimental, observational cohort |
| **Participants/Sample** | ✅ Defined sample | 200 students, 50 hospitals, 1000 survey respondents |
| **Methods Section** | ✅ Detailed procedures | Data collection protocol, instruments, analysis procedure |
| **Results Section** | ✅ Data analysis | Descriptive stats, hypothesis tests, effect sizes |
| **Limitations** | ✅ Study-specific limitations | Sample limitations, generalizability, threats to validity |

### Subtypes

#### Experimental / RCT
- Random assignment to treatment/control
- Example: "Effect of X intervention on Y outcome"
- Use **Profile 1** with emphasis on methodology rigor

#### Quasi-Experimental
- Some control (matching, stratification) but not full random assignment
- Example: "Comparing two school districts implementing different curricula"
- Use **Profile 1** (weight methodology highly but acknowledge quasi-experimental limitations)

#### Observational / Cohort
- No intervention; observing naturally occurring groups
- Example: "Following employees who chose vs. didn't choose training program"
- Use **Profile 1** (emphasize confound control in analysis)

#### Survey / Cross-sectional
- Collect data at single time point
- Example: "Online survey of 500 teachers about job satisfaction"
- Use **Profile 1** (lower weight on internal validity if design is observational)

#### Longitudinal
- Multiple time points; follow participants over time
- Example: "Following cohort of students from K-12 to assess long-term effects of early intervention"
- Use **Profile 1** (weight attrition, dropout rates, retention methods)

### Red Flags (Mislabeled)

❌ **"Empirical" but actually:**
- Using only existing data (secondary analysis) from database
- Just analyzing other people's published data
- Logical analysis without new data collection

### Scoring Example

See [example-empirical-review.md](../examples/example-empirical-review.md) for full worked example.

---

## Profile 2: Systematic Review / Meta-Analysis

### What It Is
**Structured synthesis** of existing literature using explicit protocol (usually pre-registered). Answers: "What does the totality of evidence show?"

### Key Features

| Feature | Present | Example |
| --- | --- | --- |
| **Protocol** | ✅ Pre-registered (PROSPERO or equivalent) | Registration date before data extraction |
| **Search Strategy** | ✅ Comprehensive, reproducible | "Searched PubMed, EMBASE, ERIC using [keywords] from [dates]" |
| **Inclusion Criteria** | ✅ Explicit criteria defined a priori | Participant type, intervention, outcome, study design, language, publication type |
| **Study Selection** | ✅ Dual review (usually) | Two reviewers independently screened titles/abstracts/full text; disagreements resolved |
| **Risk of Bias** | ✅ Assessed for each study | Using Cochrane Risk of Bias Tool, ROBINS-I, or discipline-specific tool |
| **Data Extraction** | ✅ Standardized form | Extracted by two reviewers; verified |
| **Synthesis Method** | ✅ Described | Narrative, vote-counting, meta-analysis; heterogeneity assessed |
| **Results** | ✅ Summary of findings | May include forest plots, evidence tables, GRADE assessment |

### Subtypes

#### Systematic Review Only
- Narrative synthesis of study findings without statistical pooling
- Example: "Systematic review of qualitative studies on student experiences of online learning"
- More subjective than meta-analysis; still systematic
- Use **Profile 2** (weight search/methods/synthesis highly; lower weight on statistics)

#### Meta-Analysis
- Statistical pooling of quantitative findings
- Example: "Meta-analysis of 45 RCTs on effect of [intervention] on [outcome]"
- Uses **Profile 2** (weight statistics on heterogeneity assessment; publication bias)

#### Scoping Review
- Broader scope; less rigorous than systematic review
- Maps range of evidence; doesn't deeply appraise quality
- Example: "What interventions exist for [broad topic]?"
- Use **Profile 2** (weight search/methods; lower weight on risk of bias detail)

#### Rapid Review
- Systematic review with time/resource constraints (compressed timeline)
- Example: "Evidence synthesis on [COVID-19 topic] in 2 weeks"
- Still systematic, but acknowledges trade-offs
- Use **Profile 2** (document what was sacrificed due to speed; transparency critical)

### Red Flags (Mislabeled)

❌ **"Systematic Review" but actually:**
- No pre-registration / post-hoc protocol
- Single reviewer selecting studies (no dual review)
- Search strategy not documented
- No risk of bias assessment
- Just citing 10–20 papers (should cite 30+)
- No PRISMA checklist adherence

✅ **Truly systematic:**
- Pre-registered on PROSPERO
- Complete search strategy described (databases, keywords, dates)
- Dual independent reviewer selection
- Risk of bias assessed and reported

### Scoring Example

See [example-desk-review.md](../examples/example-desk-review.md) for example of a flawed "systematic review" desk rejection.

---

## Profile 3: Narrative Literature Review

### What It Is
**Authoritative synthesis** of existing literature without formal systematic protocol. Answers: "What is known about this topic? What organizing framework helps us understand it?"

### Key Features

| Feature | Present | Example |
| --- | --- | --- |
| **Topic Scope** | ✅ Clear, defined scope | "Review of [specific topic] from [date range] in [discipline]" |
| **Search Description** | ✅ How were papers selected? | "Searched PubMed, Google Scholar using [terms]; selected papers addressing [criteria]" |
| **Coverage** | ✅ Represents key literature | "Identified 150 papers; reviewed 50 seminal works" |
| **Author Expertise** | ✅ Author is recognized expert | Author has published extensively on topic |
| **Organization** | ✅ Thematic/logical organization | Papers organized by theme, theory, chronology, or novel framework |
| **Synthesis** | ✅ Not just summary | Compares papers, identifies tensions/contradictions, proposes integrative framework |
| **Limitations** | ✅ Acknowledged | "Review limited to English-language publications; does not include grey literature" |

### Subtypes

#### Comprehensive Review
- Broad coverage of topic
- Example: "Review of all empirical research on critical thinking interventions, 2000–2025"
- Thick breadth; may sacrifice depth per-study

#### Focused Review
- Narrower scope
- Example: "Review of critical thinking interventions in online learning contexts"
- Better depth; narrower applicability

#### Integrative Review
- Synthesizes diverse literature to propose new framework
- Example: "Integrating learning science and social-emotional learning literatures to understand classroom climate"
- Adds value through novel organizing framework

#### Scoping Review (Narrative variant)
- Maps range of evidence broadly
- Example: "What interventions exist for [topic]? Overview of landscape"
- Less appraisal of quality; more breadth

### Red Flags (Mislabeled)

❌ **"Review" but actually:**
- Only 5–10 papers cited (too few for comprehensive review; more like mini-literature section)
- No clear search strategy or article selection method
- Just summarizes papers without synthesis
- No documentation of scope or limitations
- Author is not an expert in field

✅ **Truly narrative review:**
- 30–50+ relevant papers cited
- Search method described (even if not "systematic")
- Articles organized thematically with synthesis
- Acknowledges what's NOT included and why

### Key Difference from Systematic Review

| Aspect | Narrative | Systematic |
| --- | --- | --- |
| **Protocol** | Post-hoc rationale | Pre-registered protocol |
| **Search** | Comprehensive but not exhaustive | Exhaustive, reproducible |
| **Selection** | Author judgment + criteria | Dual reviewer + criteria |
| **Bias control** | Implicit (author expertise) | Explicit (risk of bias assessment) |
| **Useful for** | Big-picture synthesis, frameworks | Evidence synthesis, effect estimation |

---

## Profile 4: Theoretical / Conceptual Paper

### What It Is
**Conceptual argument** proposing new theory, framework, model, or interpretation. Does NOT involve original empirical data collection. Answers: "What is a new way of understanding this phenomenon?"

### Key Features

| Feature | Present | Example |
| --- | --- | --- |
| **Novel Idea** | ✅ New theory/framework/interpretation | Not just rehashing existing theory |
| **Clear Concepts** | ✅ Core concepts precisely defined | Defined with properties, boundaries, relationships |
| **Theoretical Rationale** | ✅ Why this framework? What problem does it solve? | Explains gap it fills |
| **Logic/Argumentation** | ✅ Premises → conclusions | Deductive or abductive reasoning clear |
| **Grounding** | ✅ Grounded in existing theory or observation | References relevant literatures; doesn't appear arbitrary |
| **Implications** | ✅ What does theory explain/predict? | Proposes testable predictions or new research directions |
| **No Original Data** | ✅ Paper doesn't report data collection | If data included, use Profile 1 instead |

### Subtypes

#### Theoretical Framework / Model
- Proposes how concepts relate
- Example: "A framework for understanding transfer of learning across contexts"
- Visual diagram often included; propositions testable

#### Philosophical / Conceptual Analysis
- Analyzes concepts, interpretations, meanings
- Example: "What does 'critical thinking' actually mean? A philosophical analysis"
- May question common assumptions; interpretive approach

#### Position Paper / Essay
- Author argues for a position
- Example: "Why behaviorism is inadequate for understanding learning"
- Persuasive; critique of existing theory/practice

#### Conceptual Model / Taxonomy
- Organizes knowledge into new structure
- Example: "Taxonomy of online learning interactions"
- Classifies/organizes existing knowledge in new way

### Red Flags (Mislabeled)

❌ **"Theoretical" but actually:**
- Just reviewing/explaining existing theory (should be Profile 3: Narrative Review)
- Including original data (should be Profile 1: Empirical)
- Unclear what's new (no clear novel contribution)
- Concepts poorly defined; reader can't understand model

✅ **Truly theoretical:**
- Explicitly states what's new (novel framework, integration, critique)
- Concepts precisely defined
- Clear implications or testable predictions
- Grounded in existing literature but advancing beyond it

---

## Profile 5: Case Study / Descriptive Report

### What It Is
**In-depth study of single case** (person, organization, event, program) using multiple data sources to understand phenomenon. Answers: "What is happening in this particular case? What can we learn?"

### Key Features

| Feature | Present | Example |
| --- | --- | --- |
| **Bounded Case** | ✅ Clear case definition | "The implementation of [program] in [school] during [time period]" |
| **Rich Context** | ✅ Detailed setting description | Context matters for understanding case; thoroughly described |
| **Multiple Sources** | ✅ Multiple data sources | Interviews + documents + observation + archival data |
| **Qualitative Data** | ✅ Thick description | Field notes, interview excerpts, document quotes |
| **Systematic Collection** | ✅ Planned data collection | Not random anecdotes; systematic sampling/collection |
| **Analysis** | ✅ Interpretive analysis | Themes identified; patterns discussed; meaning constructed |
| **Limitations** | ✅ Single case limitation acknowledged | No statistical generalization; findings transferable to similar contexts |

### Subtypes

#### Clinical Case Report
- Individual patient/client case
- Example: "Clinical case: Treatment of [condition] using [approach]"
- Often in medicine, psychology, social work
- Use **Profile 5** (weight ethical confidentiality highly; rigor of documentation)

#### Educational Case Study
- Study of classroom, school, program, or student
- Example: "How one high school implemented competency-based grading"
- Use **Profile 5** (weight transferability; context description)

#### Organizational Case Study
- Study of organization, project, initiative
- Example: "Organizational change process at [company]"
- Use **Profile 5** (weight analytical insight; mechanism explanation)

#### Ethnographic Study / Field Study
- Immersive observation of culture/context
- Example: "Ethnographic study of online learning community norms"
- Use **Profile 5** (weight researcher reflexivity; data collection rigor)

#### Descriptive Report / Field Report
- Description of phenomenon, program, intervention in context
- Example: "Description of innovative teaching practice in [context]"
- Use **Profile 5** (weight practical insight; applicability)

### Red Flags (Mislabeled)

❌ **"Case Study" but actually:**
- Comparing multiple cases → Use Profile 1 or 2 (comparative study)
- Just anecdote without systematic data collection
- No documentation of methods; purely personal account
- Lacks analytical depth; just narrative

✅ **Truly case study:**
- Single case (or small set) studied in depth
- Multiple data sources systematically collected
- Clear methods for data collection/analysis
- Rich analytical insight beyond description

### Key Distinction: Single Case vs. Comparative

| Aspect | Single Case (Profile 5) | Multiple Cases (Profile 1) |
| --- | --- | --- |
| **Purpose** | Understand this specific case deeply | Compare patterns across cases |
| **Sample** | 1–3 cases | 4+ cases |
| **Analysis** | Within-case analysis; transferability | Between-case comparison; generalization |
| **Generalization** | Not statistical; transferability assessed | Statistical or pattern-based |

---

## Ambiguous Cases: How to Classify

### "Is This Empirical or Case Study?"

**Scenario:** Paper describes a class implementation of teaching method with student outcomes.

**Decision rule:**
- **If:** Data from random sample of classes, control group, statistical analysis → Profile 1 (Empirical)
- **If:** Single class, rich description, no comparison group → Profile 5 (Case Study)

---

### "Is This Systematic or Narrative Review?"

**Scenario:** Paper reviews literature on topic and proposes new framework.

**Decision rule:**
- **If:** Pre-registered, exhaustive search, dual review, PRISMA → Profile 2 (Systematic)
- **If:** Authoritative synthesis, no protocol, clear search rationale → Profile 3 (Narrative)

**Note:** Both are valid; they serve different purposes.

---

### "Is This Theoretical or Review?"

**Scenario:** Paper analyzes concept of "engagement" in learning contexts.

**Decision rule:**
- **If:** Proposes new theory/framework; conceptual contribution → Profile 4 (Theoretical)
- **If:** Reviews existing theories of engagement; no new theory → Profile 3 (Narrative Review)

---

### "Does This Data Exist?"

**Scenario:** Paper analyzes institutional student records.

**Decision rule:**
- **If:** Authors collected data themselves (even if source is records) → Profile 1 (Empirical)
- **If:** Authors reanalyze existing published dataset (secondary analysis) → Profile 1 (Empirical, acknowledge secondary data)

---

## Decision Tree: Step-by-Step Classification

1. **Does paper report data analysis of ANY kind?**
   - No → Go to 5 (Conceptual)
   - Yes → Go to 2

2. **Did authors collect the data themselves?**
   - Yes → Go to 3 (Empirical)
   - No → Go to 4 (Synthesis)

3. **Is this DATA FROM SINGLE CASE or small group studied in-depth?**
   - Yes → Profile 5 (Case Study)
   - No → Profile 1 (Empirical) — with subtype noted

4. **Is this synthesis using SYSTEMATIC PROTOCOL?**
   - Yes → Profile 2 (Systematic Review)
   - No → Profile 3 (Narrative Review)

5. **Is the paper proposing NEW THEORY/FRAMEWORK?**
   - Yes → Profile 4 (Theoretical)
   - No → Profile 3 (Narrative Review of existing concepts)

---

## Common Misclassifications and Corrections

| Misclassification | Correct Classification | Why |
| --- | --- | --- |
| "Meta-review" called Systematic | Profile 2 (document limitations) | Still a review; may lack full rigor |
| Pilot study called Empirical | Profile 1 (note small N, preliminary) | Empirical, but acknowledge pilot nature |
| Data paper called Empirical | Profile 1 (note focus on data quality) | Empirical; data is the contribution |
| Literature paper (no data) called Empirical | Profile 3 or 4 | Not empirical without data collection |
| Scoping review called Systematic | Profile 2 (note scoping nature) | Systematic process but broader scope |
| Single-author reflection | Profile 4 (Theoretical/Essay) | Not empirical; conceptual contribution |

---

## Checklist: Verify Your Classification

✅ **Profile 1 (Empirical):**
- [ ] Original data collected by authors
- [ ] Research design clearly stated (RCT, observational, etc.)
- [ ] Methods section with procedures
- [ ] Results section with data analysis
- [ ] Multiple participants/sites (unless single case → Profile 5)

✅ **Profile 2 (Systematic Review):**
- [ ] Pre-registered protocol
- [ ] Search strategy documented
- [ ] Dual reviewer study selection
- [ ] Risk of bias assessment
- [ ] PRISMA checklist mentioned

✅ **Profile 3 (Narrative Review):**
- [ ] Synthesis of existing literature
- [ ] No systematic protocol (or explicit note that informal)
- [ ] 30+ papers cited
- [ ] Thematic organization with synthesis
- [ ] Author is recognized expert

✅ **Profile 4 (Theoretical):**
- [ ] No original data collection
- [ ] Proposes new theory, framework, or model
- [ ] Concepts clearly defined
- [ ] Implications or testable predictions
- [ ] Grounded in existing literature

✅ **Profile 5 (Case Study):**
- [ ] Single case (or 2–3 in-depth cases)
- [ ] Multiple data sources
- [ ] Rich description of context
- [ ] Analytical insight beyond narrative
- [ ] Transferability discussed (not statistical generalization)
