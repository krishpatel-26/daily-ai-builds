# Architecture decisions

## ADR-001: local mock simulation instead of network replay
Decision: run scenario assertions only against mockResponse embedded in JSON.
Reason: makes the prototype deterministic, free to run and safe to demo without customer credentials or network access.
Trade-off: it doesn't reproduce provider-specific runtime behavior automatically.

## ADR-002: explicit assertions
Decision: users define status, field, header, value and simulated latency checks.
Reason: a teammate can inspect precisely why a case passed or failed.
Trade-off: only the documented assertion subset is supported.

## ADR-003: generated test file is a draft artifact
Decision: export Node.js node:test source without writing into any customer repo.
Reason: the user reviews, adapts and executes it in a proper test environment.
Trade-off: test generation does not close the loop on CI by itself.

## ADR-004: local-first data boundary
Decision: no backend, telemetry or outbound HTTP calls.
Reason: keep the first reproduction workflow safe and dependency-free.
Trade-off: no collaboration, shared storage or authenticated audit trail.