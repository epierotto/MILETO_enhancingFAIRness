# ADR 004: Define Web v1 scope and ERD rendering strategy

- Status: Proposed
- Date: 2026-05-13
- Owners: Project maintainers
- Related: docs/adr/003-web-mode-architecture.md

## Context

Web mode needs a narrow first milestone that validates architecture and user value quickly. Current ERD generation depends on system Graphviz (`dot`), which reduces portability. The web path should avoid hard system-level graphics dependencies for v1.

## Decision

Web v1 scope will include:

- async conversion jobs,
- SQLite output,
- metadata JSON output,
- interactive ERD visualization in the web UI.

Web v1 will explicitly exclude:

- PDF generation.

ERD strategy for web v1:

- backend emits graph data (entities, attributes, relationships),
- frontend renders interactive ERD from that data,
- no hard dependency on system Graphviz for web mode.

High-fidelity static export (publication-grade ERD/PDF) is a later phase after interactive web ERD is stable.

## Alternatives considered

- Include PDF in v1 and accept larger scope/risk.
- Keep server-side Graphviz as required dependency for web mode.
- Delay ERD in web mode and ship only SQLite/metadata.

## Consequences

- Faster delivery of a coherent and testable web MVP.
- Better portability for local and containerized usage.
- Some users may miss PDF output in early web releases.
- A follow-up milestone is required for high-fidelity export parity.

## Why upstream should want this

This keeps the migration focused, reduces operational friction, and de-risks the web transition while preserving core data-packaging value.

## Migration and compatibility

- Existing CLI/native flows continue to support current documentation outputs during transition.
- Web mode communicates v1 limits clearly and adds export capabilities in subsequent milestones.
