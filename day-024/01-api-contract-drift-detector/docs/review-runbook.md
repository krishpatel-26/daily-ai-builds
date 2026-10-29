# API contract review runbook

1. Use the last released specification as the baseline.
2. Compare it with the proposed candidate JSON contract.
3. Inspect each reported path and validate the change with consumer teams.
4. Run contract and integration tests before release.
5. Record API owner approval, versioning decisions, and deprecation communication.

## Limitations
This is a dependency-free structural JSON diff, not a complete OpenAPI semantic validator. It does not resolve references or model request/response direction. Review results manually; do not use this prototype alone as a production deployment gate.
