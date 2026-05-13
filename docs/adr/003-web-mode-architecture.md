# ADR 003: Introduce CLI `serve` subcommand for local-first web mode

- Status: Proposed
- Date: 2026-05-13
- Owners: Project maintainers
- Related: docs/adr/002-project-positioning.md

## Context

The current application offers a CLI and a native desktop GUI. The native GUI has platform-specific friction and limits UI evolution speed. The project needs a path that preserves automation-friendly CLI usage while improving portability and enabling a richer user experience.

## Decision

Introduce a `serve` subcommand as the web entrypoint.

- `ss2db serve` starts a local HTTP server for browser-based interaction.
- The same server process can run in containerized environments for team/service usage.
- Existing conversion capabilities remain available through CLI commands.

Web mode will use an async job model and a local-first default posture:

- default bind host: `127.0.0.1`
- configurable host/port for containerized deployment

## Alternatives considered

- Keep native GUI and incrementally improve Tkinter UX.
- Replace native GUI directly with a hosted-only web service.
- Add a global `--web` flag instead of a dedicated subcommand.

## Consequences

- Clear command separation avoids growing global CLI flag complexity.
- The web stack becomes the primary UX evolution surface.
- The project maintains scriptable CLI workflows while gaining browser-based interaction.
- Runtime concerns (server lifecycle, job queue/state, artifact storage) become first-class responsibilities.

## Why upstream should want this

This approach improves cross-platform usability and contributor velocity without removing CLI automation workflows that existing users depend on.

## Migration and compatibility

- No breaking change to existing CLI conversion flow is required for initial rollout.
- Native GUI can remain temporarily during transition and be deprecated after feature parity milestones.
