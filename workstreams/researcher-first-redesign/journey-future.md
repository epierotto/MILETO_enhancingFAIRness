# Future Journey (Researcher-First)

## Persona in focus

- Researcher with real-world spreadsheet data, minimal DB/RDM specialization.

## Target flow

1. Import spreadsheet as-is (no strict pre-template requirement).
2. Tool profiles sheets and suggests likely entities, identifiers, and links.
3. User confirms or edits suggestions through guided steps.
4. Tool highlights issues with fix-first actions (not only error messages).
5. Metadata wizard collects essential context in plain language.
6. User previews outputs and publishes package.

## Experience principles in practice

## 1) Start from user reality

- Accept imperfect structure and infer where possible.
- Do not require full schema literacy to begin.

## 2) Replace rejection with assistance

- For each issue, provide:
  - what happened,
  - why it matters,
  - one-click or guided fix options.

## 3) Progressive complexity

- Beginner mode: natural-language labels and guided defaults.
- Advanced mode: full PK/FK/type controls and table-level editing.

## 4) Metadata interview

- Ask short, domain-friendly questions.
- Generate metadata tables/JSON behind the scenes.

## 5) Earlier value

- Show partial progress and preview artifacts before final conversion.
- Keep users oriented with clear completion states.

## MVP version of this future journey

- Keep existing converter internals.
- Add a pre-check assistant layer in GUI.
- Add action-oriented validation messages.
- Add minimal metadata wizard for required terms.

## Success criteria

- Faster time to first successful conversion.
- Lower first-run error rate.
- Fewer repeated check/fix loops.
- Higher completion rate for novice users.
