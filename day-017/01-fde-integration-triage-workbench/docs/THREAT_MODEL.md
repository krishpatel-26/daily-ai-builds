# Threat model

## Protected assets
Customer log content, tenant identifiers, personal data, credentials, endpoint metadata and deployment history.

## Risks and controls
- Accidental evidence sharing: inputs are processed client-side; no application API receives them.
- Credential leakage in reports: common secret-like patterns are masked before display/export.
- Redaction misses: show a privacy warning and require user review; patterns are heuristic.
- Misleading diagnosis: findings expose rule ID and matched evidence; the app states that matches are not proof.
- Unsafe remediation: suggestions emphasize least privilege, proper certificate validation and bounded retries.
- Risky configuration recommendations: low timeout/retry checks are flagged as heuristics, not hard standards.

## Out of scope
This is not a secure secret vault, SIEM, customer-system scanner, certified compliance product or automated remediation agent.