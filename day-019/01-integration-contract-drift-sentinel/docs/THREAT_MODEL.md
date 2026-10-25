# Threat model

## Assets
API contract details, request/response examples, customer-specific field names, internal endpoint paths and regression test payloads.

## Risks and safeguards
- Accidental sharing: processing is local; review all exported artifacts.
- Misleading compatibility claims: every report states the supported-subset limitation; treat findings as heuristics.
- HTML injection through contract text: UI renders user-controlled strings with textContent or escaped HTML.
- Malformed inputs: JSON parsing is guarded and error messages are displayed without continuing analysis.
- Overconfident rollout decision: output is a recommendation, not a release approval.
- Sensitive examples: use synthetic payloads and never commit real customer data.

## Out of scope
This prototype is not an API gateway, secrets vault, vulnerability scanner, certified policy engine or autonomous deployment gate.