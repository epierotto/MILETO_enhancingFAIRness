# Decision: Shift from DB-first to researcher-first onboarding

## Status
Accepted

## Context

The current workflow delivers strong standardization and output quality, but it can require users to pre-apply relational modeling and metadata practices before first success. For many researchers, this creates high upfront cognitive load and weakens adoption.

## Decision

Adopt a researcher-first product direction:

- accept imperfect spreadsheet inputs,
- guide users through assisted structure and metadata completion,
- preserve high-quality outputs (SQLite, ERD, PDF, metadata JSON) as the end goal,
- keep advanced controls available without making them mandatory for first-run success.

## Trade-offs

- Pros:
  - Lower entry barrier for non-DB users.
  - Better first-run success likelihood.
  - Stronger alignment with researcher workflows.
  - Preserves existing output value proposition.
- Cons:
  - More UX and inference complexity.
  - Additional ambiguity handling and trust UX needed.
  - Potential increase in implementation scope before measurable impact.

## Consequences

- Prioritize design and implementation of a guided pre-conversion layer.
- Reframe validation feedback into actionable remediation.
- Introduce a metadata wizard for required terms.
- Plan beginner and advanced interaction modes.

## Validation

Track at least:

- time to first successful conversion,
- first-run completion rate,
- number of validation loops per user session,
- novice user satisfaction on setup and correction steps.
