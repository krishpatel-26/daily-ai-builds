# Architecture decisions

## ADR-001: local-first static prototype
Decision: use a no-dependency browser UI and local Node server.
Reason: keep the first demo easy to run and avoid shipping customer diagnostic evidence to a backend.
Trade-off: no multi-user collaboration or persistence.

## ADR-002: explainable rules before LLM reasoning
Decision: start with transparent pattern/config rules.
Reason: initial remediation should be traceable to evidence and testable.
Trade-off: coverage is limited; the app can miss novel errors and trigger on irrelevant text.

## ADR-003: redaction before evidence rendering
Decision: apply common-pattern redaction to visible finding evidence and exports.
Reason: reduce accidental leakage in handoffs.
Trade-off: heuristics do not eliminate all sensitive data; original input remains in the text fields.

## ADR-004: readiness score is a heuristic
Decision: simple fixed penalty score.
Reason: make prioritization visible in the demo.
Trade-off: score is not calibrated against historical deployment outcomes and must not be used as a release gate.