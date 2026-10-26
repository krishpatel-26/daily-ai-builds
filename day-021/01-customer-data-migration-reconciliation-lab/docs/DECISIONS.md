# Architecture decisions

## ADR-001: local-first, read-only analysis
Decision: parse the user's source and target CSV text in the browser.
Reason: no credentials, deployments or data-upload backend are required.
Trade-off: no team collaboration or encrypted persistence.

## ADR-002: explicit mappings
Decision: compare fields only when the user maps them.
Reason: source and target schemas frequently name fields differently; implicit fuzzy mapping could create false confidence.
Trade-off: unmapped fields are outside the result's scope.

## ADR-003: normalization is opt-in
Decision: support trim and email case-folding as explicit options.
Reason: silent coercion can hide important data differences.
Trade-off: users must define canonical semantics for dates, numbers, nulls and domain-specific fields.

## ADR-004: findings before auto-fixes
Decision: report mismatches and recommended investigation rather than mutate records.
Reason: reconciliation evidence should not directly modify customer data.
Trade-off: remediation must happen in the approved migration pipeline.