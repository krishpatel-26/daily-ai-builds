# Roadmap

## Prototype delivered
- Synthetic event inbox with delivery statuses
- Basic envelope validation
- Search and filters
- Simulated retry and replay
- Attempt timeline and JSON export

## Next engineering steps
1. Add a local mock receiver with deterministic 2xx, 4xx, 429, 5xx, and timeout scenarios.
2. Add event-type-specific JSON Schemas and version checks.
3. Implement automated unit tests for validation, filtering, retry bounds, and idempotency warnings.
4. Add a backend with durable event storage and a retry queue.
5. Add signature verification, secret management, and receiver-side idempotency.
6. Add dead-letter queue workflows, audit trails, access controls, and telemetry.
7. Test under duplicate events, out-of-order delivery, slow receivers, and burst traffic.

All future items are proposals, not current capabilities.