# Architecture Decision Records (ADR)

This directory stores architecture proposals and decisions for this project.

## Purpose

- Keep non-trivial technical decisions explicit, searchable, and reviewable.
- Give contributors and maintainers a short record of why a change was proposed.
- Improve upstream PR friendliness by linking major changes to a clear rationale.

## When to write an ADR

Create an ADR for changes that affect architecture, behavior, or long-term maintenance, for example:

- Data model or schema strategy changes
- Public CLI or workflow behavior changes
- Core module boundaries or responsibilities
- Major dependency/tooling choices

For small refactors or typo fixes, an ADR is usually not needed.

## Naming and numbering

- File name format: `NNN-short-kebab-title.md`
- Example: `001-template-file-layout.md`
- Numbering is 3 digits and incremental.

## Lifecycle

Each ADR has one status:

- `Proposed`: under discussion
- `Accepted`: approved and in effect
- `Rejected`: considered, not adopted
- `Superseded`: replaced by a newer ADR

## Workflow

1. Copy `docs/adr/_template.md` to a new numbered file.
2. Set status to `Proposed` and fill sections concisely.
3. Reference the ADR in related PRs/issues.
4. Update status when decision is made (`Accepted`/`Rejected`).
5. If replaced later, mark old ADR as `Superseded` and link the new one.

## Scope guidance

- One ADR should cover one decision.
- Prefer short, concrete records over long narratives.
- If uncertain, start with `Proposed`; refinement can happen in review.
