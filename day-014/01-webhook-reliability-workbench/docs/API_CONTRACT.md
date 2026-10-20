# Future API contract sketch

This describes a possible server API; these endpoints are not implemented in the static prototype.

## POST /v1/events
Accept an event envelope, verify its sender, validate schema and size, persist it durably, then return an event receipt.

Possible success: 202 Accepted with event_id and current processing state.
Possible errors: 400 invalid envelope, 401 invalid authentication, 413 payload too large, 422 schema violation, 429 rate limited.

## GET /v1/events/{event_id}
Return status, attempts, sanitized response details, and the next scheduled retry time.

## POST /v1/events/{event_id}/replay
Require an authenticated operator, an explicit replay reason, and idempotency checks. Record who replayed the event and when.

## Contract requirements
Version the API, define pagination and rate limits, redact secrets, and document error response shape. Never expose receiver credentials or signing keys to the browser.