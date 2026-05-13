# AGENTS.md

## Project overview
This repository contains “Enhancing FAIRness / Ss2db”, a Python app that converts a spreadsheet template (one sheet per table) into a documented SQLite database with metadata JSON and ERD + PDF documentation.

## Entry points
- `app.py`: main entry; runs CLI when args are provided, GUI otherwise. Also configures logging and PyInstaller runtime paths.
- `cli.py`: CLI workflow (validation, extraction, SQLite creation, ERD, PDF generation).
- `gui.py`: Tkinter-based GUI wired through `src/gui` MVC classes.

## Core modules and flow
- `src/extraction`: validates template spreadsheets and extracts data (`GetSpreadsheetData` in `src/extraction/retrieve_data.py`).
- `src/dbcreate`: builds SQLite schema + inserts data + ERD blob (`src/dbcreate/dbcreate.py`, `src/dbcreate/erd_create.py`).
- `src/doccreate`: generates PDF documentation from template HTML/CSS (`src/doccreate/pdf_create.py`).
- `src/utils`: shared helpers for IO, GUI utilities, PDF formatting, extraction helpers.
- `conf/config.py`: loads `conf/template_conf.json` and defines template constants.

## Configuration and templates
- `conf/template_conf.json`: spreadsheet template definition (table names, column names, metadata tables).
- `conf/dc_meta_terms.json`, `conf/metadata_properties.json`: metadata term definitions and properties.
- `src/templates/doc.html` and `src/templates/doc.css`: PDF documentation templates.

## Tooling
- Dependency and environment management via `uv` (configured through `mise.toml`).
- Dependencies are defined in `pyproject.toml` (no `requirements.txt`).
- Build backend: `hatchling`.
- Run Python through uv (example: `uv run python --version`).
- Prefer `mise` tasks for common workflows (`mise run`, `mise test`, `mise lint`, `mise format`, `mise type-check`) instead of ad-hoc `uv run ...` commands when an equivalent task exists.

## Git workflow
- Always work on a non-`main` branch for any change (code, docs, or config).
- Keep `main` clean and use focused topic branches for PRs.
- For every completed unit of work: commit changes, push the branch, and open a PR for review.
- When merging PRs, use squash merges and delete the source branch after merge.

## Data and fixtures
- `data/`: sample spreadsheets for testing and demos.
- `data/images/`: sample images referenced by spreadsheet image columns.

## Setup (mise + uv)
```bash
mise setup
```

External dependencies used by optional features:
- Graphviz / PyGraphviz: improves ERD rendering (see README for OS-specific install steps).
- wkhtmltopdf: required by PDF generation (`pdfkit`).

## Run
```bash
mise run
```
CLI usage (runs when arguments are passed):
```bash
uv run python app.py /absolute/path/to/spreadsheet.xlsx -o /absolute/output/dir
```

## Tests
Tests are `unittest`-based.
1. Create `tests/conf.json` with absolute image paths (see README for expected format).
2. Run:
```bash
mise test
```

## Build
PyInstaller build instructions are documented in `README.md` (Linux and Windows examples).
