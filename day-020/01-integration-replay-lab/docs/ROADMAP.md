# Roadmap

## MVP hardening
- Add import/export version migration and schema validation for every assertion type.
- Add redaction fixtures for cookies, JWTs, custom auth headers, phone numbers and internal hosts.
- Improve array-index JSON paths and header normalization.
- Add deterministic snapshot tests for each export and documented error behavior.
- Validate the generated test draft in a temporary project during CI.

## Next iteration
- Build import adapters for HAR, sanitized cURL and Postman collection files.
- Generate runnable tests for selected stacks (Node, Python pytest) with assertion parity.
- Add correlation between scenarios, retries and idempotency workflows.
- Attach evidence artifact references, owner and reproduction notes to each scenario.

## Future
- Optional connectors to approved observability/test systems with explicit read-only permissions.
- Team-managed scenario libraries with access control, retention and audit logs.
- Measure repro quality by how often a scenario reliably triggers a labeled bug.
- Never send captured traffic to a remote replay service without explicit opt-in and a reviewable data boundary.