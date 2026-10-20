# Idempotency and safe replay

A webhook sender may deliver the same event more than once because acknowledgements can be lost after the receiver has already committed the side effect.

## Recommended receiver pattern
- Require a stable event_id.
- Store processed event IDs with a uniqueness constraint.
- Process the event and record its outcome in one transaction where feasible.
- Return a consistent acknowledgement for a previously processed event.
- Make downstream side effects idempotent or use a durable outbox.
- Keep an audit record of manual replays and the operator who initiated them.

## What this prototype does
It warns when an event ID duplicates an already delivered event in the local workspace. This is only a UI-level illustration. It does not guarantee exactly-once processing, which cannot be inferred from the browser's local list.