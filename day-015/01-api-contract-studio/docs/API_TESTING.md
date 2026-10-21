# API testing workflow

1. Confirm the API provider and contract version.
2. Capture valid and representative invalid examples.
3. Test types, required fields, enums, bounds, and nested objects.
4. Compare released and proposed schemas.
5. Review likely impact with consumer owners.
6. Turn confirmed expectations into automated tests.
7. Run them in a sandbox before production.
8. Store schemas and results with integration documentation.

Syntax-valid JSON is only the first step; tests must capture the actual behavior the integration depends on.