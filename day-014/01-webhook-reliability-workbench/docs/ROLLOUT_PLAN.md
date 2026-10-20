# Rollout plan

## Phase 1 — Contract and receiver tests
Agree on event schema, response semantics, authentication, idempotency, and retention.

## Phase 2 — Controlled sandbox
Use synthetic events against a non-production receiver. Inject timeouts, 4xx/5xx responses, malformed payloads, and duplicate IDs.

## Phase 3 — Observability
Add correlation IDs, sanitized attempt logs, retry dashboards, and dead-letter ownership.

## Phase 4 — Limited production
Enable a small event subset with rate limits, alerts, rollback steps, and a named incident owner.

## Phase 5 — Review
Compare observed delivery performance with agreed SLOs; review false positives, replay safety, and support burden before broadening rollout.

The browser prototype alone is not suitable for live customer events.