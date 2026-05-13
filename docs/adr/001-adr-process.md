# ADR 001: Use ADRs for architecture proposals and decisions

- Status: Accepted
- Date: 2026-05-13
- Owners: Project maintainers
- Related: N/A

## Context

The project needs a lightweight, consistent way to document non-trivial technical proposals and decisions, especially for changes intended to be contributed upstream.

## Decision

Adopt Architecture Decision Records under `docs/adr/` as the single location for both proposals and final decisions.

Use status values to represent lifecycle:

- `Proposed`
- `Accepted`
- `Rejected`
- `Superseded`

Use 3-digit incremental naming: `NNN-short-kebab-title.md`.

## Alternatives considered

- Keep separate folders for drafts and decisions (for example `docs/proposals/` and `docs/decisions/`).
- Document decisions only in PR descriptions and issues.

## Consequences

- Decision history becomes easier to discover and reference.
- Contributors can attach architectural rationale directly to PRs.
- Maintainers must keep ADR statuses updated as decisions evolve.

## Why upstream should want this

This improves review quality by making rationale explicit, reduces repeated context-sharing across PRs, and creates a durable decision record without adding heavy process.

## Migration and compatibility

No code/runtime impact. Existing and new architecture proposals should be documented in `docs/adr/` moving forward.
