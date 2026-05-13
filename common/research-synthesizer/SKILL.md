---
name: research-synthesizer
description: Synthesize multiple sources into structured insights. Use for consolidating overlapping information, decision-making summaries, comparing findings across sources, and separating facts from assumptions.
---

# Research Synthesizer

## Description
A general-purpose skill for turning raw sources into concise, structured insights with clear conclusions and actionable recommendations, including explicit handling of conflicting or unreliable sources.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Factual accuracy and source reliability
2. Explicit handling of contradictions and gaps
3. Actionability of recommendations
4. Conciseness versus completeness

## When to Use
- You have multiple sources with overlapping information
- You need a fast, reliable summary for decision-making
- Findings must be compared across different sources or decision alternatives
- You need to separate facts, assumptions, and open questions
- You need practical next steps based on evidence

## Instructions
1. **Define research question** - scope, audience, and decision to support; execute steps 2-7 in order
2. **Collect sources** - documents, notes, links, and observations
3. **Extract key points** - claims, evidence, and limitations
4. **Group by theme** - patterns, contradictions, and gaps
5. **Assess confidence** - source quality, recency, and consistency; if sources conflict, prioritize higher-quality and more recent evidence, and document the conflict explicitly
6. **Synthesize findings** - concise narrative with supporting rationale
7. **Output recommendations** - actions, trade-offs, and follow-up questions

## Input Recovery Rules
- Define a reasonable research scope when the question is vague
- Ask for clarification only when the decision to support or the target audience is completely undefined

## Constraints
- Do not synthesize without at least one credible source
- Do not present conflicting findings as consensus
- Do not hide uncertainties or gaps in the evidence

## Tools and Methods
- Thematic analysis
- Evidence tables
- Confidence scoring
- Comparative matrices
- Executive summary format

## Output Contract
Return all of the following:
1. Research question and scope
2. Key findings grouped by theme
3. Confidence level and source-quality assessment
4. Contradictions, gaps, and open questions
5. Recommendations and follow-up actions

## Best Practices
- Distinguish clearly between evidence, interpretation, and recommendation
- Make confidence visible when sources are weak, incomplete, or conflicting
- Prefer concise synthesis over source-by-source retelling
- Preserve important dissenting evidence instead of flattening it into consensus
