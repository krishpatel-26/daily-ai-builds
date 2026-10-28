# Architecture and algorithm assumptions

## Data flow
1. User chooses a synthetic traffic scenario and a local quota policy.
2. The simulator processes requests in timestamp order while preserving original row order for display.
3. Each algorithm receives fresh per-run state scoped by client ID and route.
4. The dashboard presents accepted/rejected outcomes and heuristic reset/retry estimates.
5. The report builder exports per-request evidence and an explicit simulation disclaimer.

## Algorithms
- Fixed window: a counter resets on aligned window boundaries.
- Sliding window: retains requests whose timestamps are inside the rolling interval.
- Token bucket: starts with capacity equal to limit and replenishes uniformly across the time window.
- Request cost can represent weighted units, although sample traffic uses one unit per request.

These are educational models. Production algorithms differ in precision, storage, race behavior, fairness and provider-specific semantics.
