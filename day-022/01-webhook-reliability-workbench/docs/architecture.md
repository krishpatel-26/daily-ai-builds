# Architecture and operational boundaries

## Data flow
1. Browser loads synthetic attempts from the sample module.
2. A memory-only store holds current demo state.
3. Pure helpers validate envelopes, group idempotency keys, calculate retry suggestions, classify failures and summarize the visible sample.
4. UI renders the selected attempt and exposes a local-only simulated retry.
5. Export produces a Markdown handoff with an explicit heuristic disclaimer.

## Reliability choices
- Retry calculations are deterministic and bounded for testability.
- Likely permanent failures (authentication, authorization and payload validation) are not automatically retried by the sample policy.
- Duplicate idempotency keys are evidence, not proof of duplicate business effects.
- There are no runtime dependencies and state is held in memory.
- HMAC helper signs the exact raw text passed to it; provider-specific parsing and verification rules still need implementation.

## Production gaps
A real implementation needs provider-specific inbound HTTP handling, signature verification before JSON parsing, timestamp/replay-window checks, durable inbox and idempotency tables, transactional side-effect protection, bounded queue retries, Retry-After handling, dead-letter access controls, metrics/alerts, audit logs, secrets management and end-to-end tests against a controlled receiver.

Health scores, failure classifications and retry recommendations are rule-based heuristics, not guarantees.
