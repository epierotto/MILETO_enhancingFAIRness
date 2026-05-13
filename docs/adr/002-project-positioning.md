# ADR 002: Position Ss2db as a spreadsheet-first research-data packaging workflow

- Status: Accepted
- Date: 2026-05-13
- Owners: Project maintainers
- Related: docs/landscape.md

## Context

The project overlaps with several tool categories (ETL, ERD generation, data catalogs, metadata tooling). Without explicit positioning, contributors may propose scope changes that dilute the main value and make upstream review harder.

## Decision

Position `Enhancing FAIRness / Ss2db` as a **spreadsheet-first research-data packaging workflow** that produces:

- SQLite database output,
- FAIR-oriented metadata JSON,
- ERD artifacts,
- PDF technical documentation.

The project focus is the end-to-end conversion path from template-driven spreadsheets to portable dataset packages.

## Alternatives considered

- Reposition as a generic ETL pipeline framework.
- Reposition as a full data catalog or governance platform.

## Consequences

- Roadmap and documentation should prioritize spreadsheet-template UX and reproducible packaging.
- Feature proposals that move toward catalog/orchestration platform scope should be treated as out-of-scope unless they directly improve the packaging workflow.
- Upstream contributors get clearer criteria for reviewing change proposals.

## Why upstream should want this

Clear positioning improves contributor alignment, reduces scope creep, and makes PR review faster by grounding decisions in a shared product boundary.

## Migration and compatibility

No runtime or data-format migration is required. This is a documentation and governance decision that informs future prioritization.
