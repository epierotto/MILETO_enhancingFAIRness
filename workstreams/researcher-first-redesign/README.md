# Researcher-First Redesign Workstream

This workspace is dedicated to rethinking the product approach before implementation.

## Why this exists

Current concern:

- The tool can feel like it asks researchers to pre-learn database and RDM practices.
- Users may need to build a compliant relational spreadsheet first, then run conversion.
- This can shift effort to users instead of reducing their effort.

This workstream focuses on a **researcher-first** direction: start from real-world, messy data and guide users to publishable outputs with less upfront schema work.

## Problem framing

The app currently excels at:

- enforcing template consistency,
- validating PK/FK and metadata structure,
- generating standardized outputs (SQLite, ERD, PDF, metadata JSON).

But it may underperform on:

- low-friction onboarding for non-DB users,
- progressive guidance from messy spreadsheets,
- minimizing conceptual load (PK/FK, normalization, metadata schema internals).

## Target outcomes

- Reduce researcher cognitive load.
- Preserve output quality and FAIR alignment.
- Shift from hard-gate validation to guided correction.

## Product principles

1. **Messy-first input**
   - Accept imperfect spreadsheets and infer structure where possible.
2. **Guided repair over rejection**
   - Provide clear suggestions and assisted fixes.
3. **Progressive disclosure**
   - Basic mode hides DB jargon; advanced mode enables full control.
4. **Metadata by interview**
   - Collect key metadata through guided prompts and generate internal tables.
5. **Publish-first UX**
   - Keep focus on outputs users need, not internal schema concepts.

## Suggested roadmap

### Phase 0: Discovery and alignment

- Capture user personas and jobs-to-be-done.
- Map current user journey and drop-off points.
- Define success metrics (time-to-first-success, error resolution rate).

### Phase 1: Quick wins

- Rewrite error messages as action-oriented fixes.
- Add inline remediation hints in GUI.
- Introduce a guided metadata wizard for common required terms.

### Phase 2: Assisted modeling

- Auto-suggest probable PK/FK candidates.
- Surface relationship suggestions and confidence.
- Add one-click data cleaning helpers for common issues.

### Phase 3: Experience redesign

- Add beginner/advanced modes.
- Replace metadata table editing with form-first flow (table edit still available in advanced mode).
- Build a step-by-step conversion assistant.

## Deliverables in this folder

- Problem statements
- User journeys and friction maps
- Product decisions and trade-off notes
- Experiment proposals and validation criteria
- Implementation handoff notes (when approved)

## Open questions to resolve

- Which user segment is primary: researchers, data stewards, or both?
- Which outputs are essential in first-run success?
- How much automatic inference is acceptable before trust drops?
- What is the minimum metadata required for practical FAIR gains?

## Working convention

- Treat this folder as strategy/design-first.
- No direct production code changes from here.
- Promote ideas into implementation only after explicit decisions.
