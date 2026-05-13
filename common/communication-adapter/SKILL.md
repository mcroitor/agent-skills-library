---
name: communication-adapter
description: Adapt communication to different audiences. Use for tailoring messages to technical or non-technical audiences, stakeholder updates, decision framing, and clarifying misaligned communication.
---

# Communication Adapter

## Description
A general-purpose skill for adapting technical and non-technical communication to audience context, goals, and required level of detail.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Clarity for the specific audience
2. Actionability of the message
3. Appropriate level of detail
4. Trade-off transparency

## When to Use
- The same message must work for different audiences
- Technical content needs business-friendly framing
- Stakeholder updates require concise, clear status
- Decisions require explicit options and trade-offs
- Misalignment is caused by language or detail mismatch

## Instructions
1. **Identify audience** - role, context, and baseline knowledge
2. **Define communication goal** - inform, align, decide, or unblock
3. **Select format** - brief update, deep-dive, plan, or FAQ
4. **Adjust depth** - include only the most critical details for the audience's understanding, with an optional technical appendix for additional context
5. **Use clear structure** - context, key points, decision, next actions
6. **Surface trade-offs** - benefits, costs, and risks in plain language
7. **Validate clarity** - remove ambiguity and jargon where unnecessary; prioritize clarity over exhaustive detail when conflicts arise

## Input Recovery Rules
- Infer reasonable audience characteristics when not specified
- Ask for clarification only when the communication goal or target audience is completely undefined

## Constraints
- Do not use jargon without explanation for non-technical audiences
- Do not omit trade-offs or risks from decision-oriented messages
- Do not provide excessive detail that obscures the main message

## Tools and Methods
- Audience mapping
- Message pyramid
- Plain-language rewriting
- Executive summary templates
- Decision framing

## Output Contract
Return all of the following:
1. Target audience and communication goal
2. Adapted message in the chosen format
3. Key trade-offs or risks, when relevant
4. Recommended next action or decision point
5. Explicit assumptions if audience context was inferred

## Best Practices
- Match terminology and level of detail to the audience's baseline knowledge
- Lead with the main point before supporting detail
- Make decisions, blockers, and next actions easy to scan
- Preserve accuracy when simplifying technical content
