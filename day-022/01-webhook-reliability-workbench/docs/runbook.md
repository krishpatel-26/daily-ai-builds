# Webhook delivery incident runbook

Checklist for a field engineer coordinating a customer integration incident.

## 1. Stabilize and scope
- Record affected workspace, endpoint, event IDs, time window and provider request IDs.
- Estimate customer impact and separate delayed events from permanently rejected events.
- Check receiver logs using request IDs and UTC timestamps.
- Preserve evidence before manually replaying anything.

## 2. Classify the failure

| Symptom | First action | Retry posture |
|---|---|---|
| Timeout / 5xx | Check receiver health and response path | Bounded retry if side effects are protected |
| 429 | Respect Retry-After and lower concurrency | Retry after indicated delay |
| 401 / 403 | Verify credential, scope, secret rotation and access | Fix configuration first |
| 400 / 422 | Compare payload against accepted schema | Do not replay unchanged |
| 404 | Confirm endpoint and route version | Correct destination first |
| Dead letter | Find last concrete error and accountable owner | Explicit review before replay |

## 3. Prevent duplicate side effects
- Confirm which idempotency key is used by sender and receiver.
- Check if an earlier attempt completed downstream work.
- For payments, orders, provisioning and account changes, verify business-state effects before replay.
- Prefer operator-approved replay with an audit record over a blind loop.

## 4. Retry safely
- Use bounded exponential backoff with jitter in production.
- Respect Retry-After and destination rate limits.
- Cap attempts and route exhausted events to a dead-letter workflow.
- Keep workers idempotent and watch retry amplification during outages.

## 5. Handoff
Include impact, affected endpoints, event/request IDs, failure classification, mitigation, owner, next update and go/no-go recommendation. Redact secrets, authorization headers, personal data and payment details.

## Demo limitation
The workbench uses local heuristics on synthetic data. It does not call provider APIs, validate a provider's exact signature scheme or prove replay is safe in a specific integration.
