# Roadmap

## Phase 1 — Current static prototype
- Synthetic regression dataset
- Pass/fail/review summary
- Editable cases and JSON import/export
- Illustrative run history and trace inspection
- Prompt text risk comparison

## Phase 2 — Real provider adapter
- Explicit provider interface and timeout handling
- Store exact prompt/template version
- Record actual model IDs, request IDs, latency, tokens, and errors
- Add schema checks and grounded citation checks
- Keep provider keys server-side

## Phase 3 — Evaluation quality
- Labeled examples reviewed by domain experts
- Model-based graders calibrated against human labels
- Repeat trials and confidence intervals
- Category and severity-level regression gates
- Baseline-versus-candidate comparison

## Phase 4 — Team operations
- Authenticated workspace and access control
- Persistent database and run retention policy
- CI-triggered evaluation in pull requests
- Alerting on configured regressions
- Exportable review and approval record

No later-phase capability should be described as already implemented.