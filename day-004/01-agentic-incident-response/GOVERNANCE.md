# AI Governance & Human Approval

This iteration adds a governance boundary around incident recommendations.

- Every specialist finding receives a deterministic evidence ID for lineage.
- Critical/high incidents always require human approval.
- Lower-severity incidents require approval when evidence confidence is below the policy threshold.
- Actions remain recommendations; no infrastructure changes are executed automatically.
- SQLite records plan creation and approval/rejection decisions with actor, timestamp, and payload.

API flow:
1. POST /v1/incidents/analyze
2. POST /v1/incidents/{incident_id}/approval
3. GET /v1/incidents/{incident_id}/audit

For financial-services deployment, the next layer should add identity-backed RBAC, immutable external audit storage, policy-as-code, separation of duties, and signed evidence/artifact references.
