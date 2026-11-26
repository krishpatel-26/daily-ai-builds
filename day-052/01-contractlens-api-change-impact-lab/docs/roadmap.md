# Roadmap

## Compatibility coverage
- Resolve internal $ref safely with cycle/depth limits.
- Parse YAML and OpenAPI 3.1 JSON Schema dialects.
- Merge path-level and operation-level parameters.
- Compare security requirements, request content types, response headers, response media types and nested schemas.
- Support configurable compatibility rules per SDK language and consumer.

## Customer impact
- Replace synthetic consumer registry with an owner-approved service catalog.
- Add repository and generated SDK dependency mappings.
- Add customer-specific usage evidence from API gateway telemetry.
- Track migration status, owners, due dates and exceptions.

## Release workflow
- Add baseline/candidate approval, exception sign-off and audit history.
- Connect to CI as a non-blocking check, then introduce policy gates after false-positive evaluation.
- Produce machine-readable SARIF or GitHub Check annotations.
- Add real consumer contract tests in an isolated staging environment.
