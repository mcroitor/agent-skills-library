# Scientific Article Preparation Pipeline

Use this pipeline only when preparing or substantially revising a scientific article. Do not run it for standalone requests such as finding or analyzing sources.

## Entry Points

- For a new article, start at Stage 1.
- For a supplied manuscript that needs substantive revision, start at the earliest stage implicated by the request or identified by the reviewer; do not repeat unaffected upstream stages.
- For a review-only request, run Stage 5 only and report that the full pipeline was not run.
- When available, record the target venue, language, and citation style in the research definition. Ask the user to provide missing inputs that materially affect the requested work.

## Stages and Handoffs

Run the stages in order. Pass each stage's required output to the next, preserving source identifiers and traceability of claims to evidence.

1. **Define the research.** Record the research question, scope, and research type or methodology; state a hypothesis when appropriate. A hypothesis is not required for every theoretical or conceptual article. Handoff: a concise research definition. For a new article, obtain the user's confirmation of this definition before proceeding.
2. **Find sources.** Use the `research-source-finder` skill to identify relevant scholarly sources and verify their bibliographic details, identifiers, and lawful full-text availability. Handoff: bibliography with source identifiers, verification status, access limitations, and search strategy.
3. **Analyze sources.** Use the `scientific-paper-analyst` skill to analyze the collected sources. Handoff: an evidence matrix or equivalent traceable analysis covering relevant findings, contradictions, limitations, and research gaps.
4. **Prepare the article.** Use the `scientific-writing-editor` skill to produce a coherent article based on the analysis. Handoff: the manuscript, references, and a clear account of evidence limitations. Verify that every citation in the manuscript corresponds to the verified bibliography and that no unverified references were introduced.
5. **Review the article.** Use the `scientific-paper-reviewer` skill to assess the manuscript independently. Handoff: the final overall score on the skill's prescribed scale, critical issues, numbered comments, and the stage or stages requiring revision.

Do not duplicate the detailed methods or criteria defined by these skills. The reviewer must work in a separate agent or clean context, without access to the author's private reasoning or draft deliberations. If a required agent or skill is unavailable, stop at that stage, explain the blocker, and ask the user for the missing capability or inputs; do not claim the stage was completed. Continue only after the user resolves the blocker.

## Quality Gates and Revision

- Apply the `scientific-paper-reviewer` skill's review profile, scoring rules, critical criteria, and rejection gates. Do not override or reinterpret its classification of critical issues.
- The reviewer must assess the manuscript independently and must not raise its score merely to meet the acceptance threshold.
- Apply the final-review gate only to a full peer review. A desk review's purpose is to recommend whether the manuscript proceeds to full review; it does not satisfy the final-review gate, and no percentage may be inferred from its output.
- Clear the internal pipeline review gate only when the full review's final overall score is **at least 85%**, the reviewer's recommendation is **Accept** or **Minor Revision**, and no applicable critical criterion, absolute rejection trigger, or scientific fatal flaw blocks that recommendation. A score of 85% or higher alone is not sufficient.
- Use only the reviewer's final overall score and recommendation; never substitute an average, selected criterion, or recalculated score. If the reviewer's score and recommendation conflict, or a comparable full-review percentage is missing, report the mismatch and ask the user how to proceed rather than resolving it yourself.
- Describe the result as clearing or not clearing this pipeline's internal review gate, not as journal acceptance or publication acceptance; only the journal or responsible editor can make that decision.
- Route problems to the earliest applicable stage:

| Problem | Revision stage |
|---|---|
| Invalid or unclear research question, hypothesis (if applicable), scope, or research design | 1 — Research definition |
| Sources are insufficient, irrelevant, unreliable, or have unverified bibliographic details | 2 — Source search |
| Sources are misinterpreted, findings or limitations are omitted, or conclusions do not follow from evidence | 3 — Source analysis |
| The reasoning, structure, clarity, formatting, or presentation is deficient despite an adequate evidence base | 4 — Article preparation |

Route other remediable manuscript issues, including language, venue requirements, citation formatting, and ethical disclosures, to Stage 4. Escalate issues that cannot be resolved through the defined stages to the user rather than silently treating them as resolved. If issues affect multiple stages, list them and start at the earliest affected stage. Use targeted checks for localized revisions, while preserving traceability and rerunning all affected downstream stages; always perform a full final review.

If a claim requires empirical validation that is unavailable, do not fabricate or simulate evidence: narrow the claim to what the evidence supports, identify it as a hypothesis, limitation, or future research direction, or report that additional empirical work is required.

## Termination

Perform at most **three revision cycles** by default; the initial review does not count as a revision cycle, so there may be at most four reviews. Keep a revision log with cycle numbers and stable IDs for reviewer issues, their status, affected stage, and the changes made. Stop earlier if the same blocking issue IDs remain unresolved without material progress. If the internal review gate is not cleared within the limit, stop and report the latest score and recommendation, unresolved issues, and blockers. Distinguish this outcome from successful completion; never report the gate as cleared unless all its criteria are satisfied.

## Final Report

Report whether the internal review gate was cleared or the pipeline stopped without clearing it, the final review score and recommendation when available, unresolved issues, and any material evidence limitations or blockers. Do not present this pipeline outcome as an editorial or publication decision.
