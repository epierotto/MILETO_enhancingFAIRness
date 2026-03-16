# Experiment: Onboarding MVP for researcher-first flow

## ID
experiment-001

## Objective

Validate that a guided onboarding layer can improve first-run success for novice users without changing the core conversion engine.

## Hypothesis

If users receive guided pre-conversion support (assistant steps + actionable fixes + metadata wizard), then they will complete successful conversions faster and with fewer error loops than in the current flow.

## Scope (MVP)

In scope:

- Guided pre-check step in GUI that summarizes readiness.
- Action-oriented validation messages for top recurring failures.
- Minimal metadata wizard for required fields only.
- Progress states: `Imported -> Needs attention -> Ready -> Converted`.

Out of scope:

- Full schema inference engine.
- Deep automation of relationship modeling.
- CLI workflow redesign.
- Any changes to output artifact formats.

## Variant design

- Baseline (A): current workflow.
- MVP (B): current workflow + onboarding assistant layer.

## Target users

- Primary: researchers with limited DB modeling experience.
- Secondary: data stewards validating novice-prepared spreadsheets.

## Tasks users perform during test

1. Import a realistic spreadsheet with common issues.
2. Resolve surfaced issues until conversion is enabled.
3. Provide minimum required metadata.
4. Generate outputs.

## Success metrics

Primary:

- Time to first successful conversion (median).
- First-run completion rate.

Secondary:

- Number of validation loops per session.
- Number of unresolved blocking errors.
- User-reported clarity of next action (1-5 scale).

Guardrails:

- Output correctness remains unchanged vs baseline.
- No increase in critical conversion failures.

## Success thresholds

- >= 25% reduction in median time to first successful conversion.
- >= 20% increase in first-run completion rate.
- >= 30% reduction in validation loops for novice users.

## Instrumentation plan

Track events:

- `file_imported`
- `readiness_summary_viewed`
- `validation_issue_opened`
- `fix_action_applied`
- `metadata_wizard_started`
- `metadata_wizard_completed`
- `conversion_started`
- `conversion_succeeded`
- `conversion_failed`

Track properties:

- issue type/category,
- step duration,
- session outcome,
- user role (researcher/steward),
- mode (baseline/mvp).

## Risks and mitigations

- Risk: users distrust automatic suggestions.
  - Mitigation: show confidence + allow easy override.
- Risk: too much UX chrome increases complexity.
  - Mitigation: keep wizard minimal and optional where safe.
- Risk: insufficient sample size for reliable conclusions.
  - Mitigation: run repeated sessions with representative fixtures.

## Execution plan

1. Define and prepare test fixture spreadsheets (easy/medium/hard).
2. Implement MVP UI layer behind a feature flag.
3. Run internal pilot sessions.
4. Collect metrics and qualitative notes.
5. Compare A/B outcomes and decide promote/iterate/stop.

## Decision rule

- Promote to implementation roadmap if at least 2 of 3 primary/secondary threshold groups are met and guardrails hold.
- Otherwise iterate once on UX copy and step flow, then retest.

## Ownership

- Product lead: defines acceptance and prioritization.
- UX lead: interaction design and clarity testing.
- Engineering lead: MVP feasibility and instrumentation.
