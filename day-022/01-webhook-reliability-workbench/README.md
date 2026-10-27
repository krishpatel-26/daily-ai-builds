# Day 022 — Webhook Reliability Workbench

A local-first browser workbench for debugging webhook delivery failures and producing evidence-backed customer handoffs.

## Features
- Inspect deterministic sample webhook delivery attempts.
- Validate event envelope shape and identifiers.
- Group attempts by idempotency key and flag duplicate candidates.
- Estimate bounded exponential retry schedules.
- Classify failures into actionable triage categories.
- Filter attempts and review per-event timelines.
- Export a Markdown incident handoff and JSON evidence bundle.
- Show delivery health metrics with visible caveats.

## Run locally
Requirements: Node.js 18 or newer.

    npm test
    npm run serve

Open http://localhost:4173. No package install or build step is required.

## Demo boundaries
All attempts are synthetic. Replay changes in-memory demo state only; no HTTP requests are sent, no user payload is persisted, and no queue/database/provider API is connected. HMAC helper is educational and not provider-specific signature middleware. Scores and failure classifications are heuristics, not ground truth. Review downstream side effects before a real replay.

## Structure
- src/app.js: UI wiring and local simulation.
- src/core/: pure validation, idempotency, retry, triage, metrics and report helpers.
- src/data/: synthetic scenarios.
- tests/: dependency-free Node test suite.
- docs/runbook.md: incident response checklist.
- docs/architecture.md: design and limitations.

## Production hardening
Add provider-specific signature middleware, durable inbox/outbox storage, transactional idempotency, bounded queue workers, dead-letter ownership, structured telemetry, secrets rotation, rate limits, replay authorization and integration tests against a test endpoint.
