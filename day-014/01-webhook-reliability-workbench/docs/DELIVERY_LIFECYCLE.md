# Delivery lifecycle

A typical production lifecycle is:

1. Accept an event from a trusted publisher.
2. Validate envelope, signature, timestamp, and event schema.
3. Store the event durably before acknowledging receipt.
4. Dispatch a delivery attempt to the configured receiver.
5. Record status, response category, latency, and attempt number.
6. Retry transient failures according to a bounded policy.
7. Route exhausted or non-retryable events to a dead-letter queue.
8. Expose evidence and an approved replay workflow to operators.

The current workbench demonstrates this lifecycle visually with synthetic state only. It does not implement durable queues or actual HTTP dispatch.