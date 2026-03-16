# Current Journey (Today)

## Persona in focus

- Researcher with spreadsheet data, limited DB modeling background.

## Current flow

1. Prepare spreadsheet in expected multi-sheet template format.
2. Fill metadata tables with specific names/columns.
3. Run tool (GUI or CLI).
4. Resolve validation errors (PK/FK, metadata, template structure).
5. Re-run checks until valid.
6. Convert to SQLite + ERD + PDF + metadata JSON.

## Main friction points

## 1) Front-loaded modeling burden

- Users must understand relational structure before first success.
- Practical effect: delayed value, early frustration.

## 2) Validation as a gate

- Many errors are surfaced after preparation work is done.
- Error recovery can feel technical and iterative.

## 3) Metadata complexity

- Metadata is represented as internal tables.
- Users must map conceptual metadata into schema cells.

## 4) Tool mental model mismatch

- Researchers think in projects, samples, measurements.
- Tool asks for tables, keys, references, constraints.

## 5) Success appears late

- User only sees final outputs after compliance is reached.
- Limited sense of incremental progress.

## Observable symptoms

- First-run failures are likely for non-expert users.
- Repeated check/fix cycles before conversion.
- Potential abandonment before first complete output.

## Opportunity statement

Convert the experience from:

- "Build a compliant schema first, then convert"

to:

- "Bring your data, get guided to publishable outputs"
