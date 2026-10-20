# Webhook incident runbook

## When an event is reported missing
1. Confirm the event_id, event_type, and customer/account context.
2. Check whether the sender recorded a delivery attempt.
3. Inspect the receiver's response code and request logs.
4. Compare the actual payload with the agreed versioned contract.
5. Check if the event was already processed downstream before replaying.
6. Assign one owner and record the next checkpoint.
7. Send a customer-safe update only after facts are verified.

## Triage guide
- 400 / 422: inspect the payload and schema version.
- 401 / 403: confirm receiver authentication and secret rotation.
- 404: confirm endpoint path and environment.
- 409: inspect receiver idempotency or conflict rules.
- 429: respect Retry-After and reduce request pressure.
- 5xx / timeout: investigate receiver health, then retry within policy.

This is a starting runbook; actual response interpretation depends on the receiver's contract.