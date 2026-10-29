# API security review runbook

1. Use a trusted, sanitized OpenAPI JSON document.
2. Review each rule ID and JSON path.
3. Validate authentication requirements with the API owner; public endpoints may be intentional.
4. Confirm fixes with authorized dynamic and integration tests.
5. Assign remediation owners and document accepted risks.

Static heuristics can produce false positives and miss business-logic and runtime flaws. This is not a penetration test or compliance certification.
