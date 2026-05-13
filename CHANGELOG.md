# Changelog

All notable changes to this project are documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning where practical.

## [Unreleased]

### Added
- Research and product-direction workspace under `workstreams/researcher-first-redesign/` with:
  - strategy README,
  - collaboration guide (`AGENTS.md`),
  - current/future user journeys,
  - product direction decision note,
  - onboarding MVP experiment plan.
- Top-level `AGENTS.md` for contributor and automation context.
- `mise` task entries for `lint`, `format`, and `type-check`.

### Changed
- Tooling migrated from `requirements.txt` flow to `uv` + `mise` workflow.
- `mise` test task now runs pytest and exports JUnit XML to `reports/unit_tests.xml`.
- `uv` version pin in `mise.toml` set to `0.10.9` to avoid breakage from unpinned updates.

### Removed
- `requirements.txt` in favor of `pyproject.toml` + `uv.lock` dependency management.

## [1.1.0-beta]

### Added
- Spreadsheet-to-SQLite conversion workflow with metadata extraction.
- ERD generation and PDF documentation support.
- GUI workflow for spreadsheet validation, metadata editing, and conversion.
