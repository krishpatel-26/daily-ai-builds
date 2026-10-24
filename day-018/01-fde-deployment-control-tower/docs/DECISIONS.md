# Architecture decisions

## ADR-001: one workspace per deployment
Decision: use a self-contained local record with metadata, gates, blockers and events.
Why: customer delivery work needs lifecycle state, not only a one-time error report.
Trade-off: there is no multi-user sync or central audit backend.

## ADR-002: evidence gates rather than free-form status
Decision: checks have explicit status and evidence notes.
Why: a green status without proof is not sufficient for a meaningful handoff.
Trade-off: evidence notes are user-entered and cannot be independently verified by this tool.

## ADR-003: deterministic readiness model
Decision: transparent completion fraction and explicit blocker penalties.
Why: reviewers can explain why the score changed.
Trade-off: the model is not statistically calibrated and must not be used as an automatic release approval.

## ADR-004: local-first storage
Decision: localStorage and user-triggered exports, with no backend.
Why: no deployment setup and reduced accidental data transfer.
Trade-off: data is not encrypted, access-controlled, synchronized or backed up automatically.