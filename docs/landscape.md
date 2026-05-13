# Project Landscape

This note positions `Enhancing FAIRness / Ss2db` in the existing tooling ecosystem.
It is intentionally practical: where overlap exists, where this project is different, and how to communicate that to users and contributors.

## Problem Space

Researchers often begin with spreadsheets. Publishing those datasets in a reusable, machine-actionable way usually requires:

1. Converting tabular data to a structured database format.
2. Generating dataset metadata in a standardized schema.
3. Producing human-readable technical documentation (schema + data dictionary).

Most tools cover only one part of that workflow.

## Adjacent Tool Categories

| Category | Typical tools | Strong at | Gap relative to this project |
| --- | --- | --- | --- |
| ETL / data transformation | dbt, Airbyte, Talend | Pipeline automation and transformations | Usually assumes engineering-first sources, not spreadsheet-template authoring with FAIR metadata capture |
| ERD / schema visualization | Graphviz-based tools, SchemaSpy, DBeaver | Diagramming existing schemas | Does not create FAIR metadata JSON or end-to-end dataset documentation from spreadsheet input |
| Data catalog / governance | CKAN, DataHub, Amundsen | Dataset discovery and governance at scale | Heavyweight for small teams; not optimized for local spreadsheet-to-database conversion workflows |
| Scientific metadata tooling | Frictionless, DataCite integrations, domain repositories | Metadata schema validation and publication support | Often does not include relational SQLite creation + ERD + PDF generation as one local workflow |

## What This Project Is

`Ss2db` is best understood as a **research-data packaging workflow** with a spreadsheet-first interface.

It converts a constrained spreadsheet template into:

- a normalized SQLite database,
- machine-readable metadata JSON,
- ERD artifacts,
- PDF technical documentation.

This is not primarily a pipeline orchestrator or enterprise data catalog.

## Why This Niche Matters

- Many contributors to research datasets are comfortable with spreadsheets, not code-first pipelines.
- Reproducible packaging improves FAIR outcomes without requiring a full platform migration.
- A local, low-infrastructure workflow is easier to adopt in small labs and project teams.

## Positioning Statement (Draft)

`Enhancing FAIRness / Ss2db` is a spreadsheet-first research-data packaging tool that turns template-driven tables into a documented SQLite dataset package with FAIR-oriented metadata and schema artifacts.

## Scope Boundaries

To keep the project focused and reviewable, avoid reframing it as:

- a full data catalog,
- a general-purpose ETL platform,
- a replacement for institutional repository systems.

The value is in the bridge from researcher-authored spreadsheets to portable, reusable dataset packages.

## Related Decision Record

See `docs/adr/002-project-positioning.md` for the formal project decision based on this analysis.
