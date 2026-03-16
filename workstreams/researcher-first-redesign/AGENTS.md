# AGENTS.md - Researcher-First Redesign Workspace

This file defines how collaborators (human and AI) should work in this folder.

## Scope

This workspace is for:

- product framing,
- UX and workflow redesign,
- strategy and sequencing,
- decision logging.

This workspace is not for direct production code edits unless explicitly requested.

## Collaboration rules

1. Prefer concise, decision-oriented writing.
2. Tie proposals to user pain, not only technical elegance.
3. Distinguish assumptions from validated facts.
4. Include trade-offs for each major recommendation.
5. Keep artifacts easy to hand off to implementation.

## Expected artifact types

- `problem-*.md`: Problem statements and context.
- `journey-*.md`: Current/future user journeys.
- `decision-*.md`: ADR-style decisions and rationale.
- `experiment-*.md`: Validation plans and success criteria.
- `handoff-*.md`: Approved changes to implement.

## Decision note template

Use this structure for decision files:

```md
# Decision: <title>

## Status
Proposed | Accepted | Rejected | Superseded

## Context
<what user/problem context drives this decision>

## Decision
<what we choose>

## Trade-offs
- Pros:
- Cons:

## Consequences
<what changes next>

## Validation
<how we know it worked>
```

## Quality bar for proposals

Every proposal should answer:

- Who benefits most?
- What pain is removed?
- What complexity is introduced?
- What is the smallest testable version?

## Promotion to implementation

A proposal can move from this folder to code changes only when:

1. decision status is `Accepted`,
2. a handoff artifact exists,
3. implementation scope is explicitly requested.
