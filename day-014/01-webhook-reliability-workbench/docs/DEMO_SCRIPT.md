# 3-minute demo script

1. Click Load demo events. Point out delivered, queued, failed, and duplicate examples.
2. Select the failed invoice event and inspect its response, payload, and attempt timeline.
3. Explain why a 5xx may be retryable but a 400 usually needs payload or contract investigation.
4. Click Simulate retry to show a transient recovery in the mock workflow. Emphasize that no network request occurs.
5. Select the duplicate event and discuss receiver-side idempotency.
6. Paste a valid event into the validator and validate it.
7. Remove event_type or change data to an array and validate again to see actionable errors.
8. Export the event log and explain the observability fields a real system should retain.

Avoid claiming the prototype sends real webhooks or confirms a root cause.