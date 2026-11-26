# ContractLens architecture

## Analysis flow
1. Parse two OpenAPI JSON documents and enumerate HTTP operations.
2. Match operations by method and path.
3. Compare parameters, request schemas, representative JSON response schemas, and documented response codes.
4. Classify findings as breaking, review or safe.
5. Match findings to the synthetic consumer registry by exact operation key.
6. Build priority-ranked rollout actions and export an evidence report.

## Compatibility assumptions
- Removing an operation is breaking.
- Adding an optional operation is generally additive.
- Newly required request fields/parameters and changed types are breaking.
- Narrowed numeric limits and operation ID changes require review.
- Removing response fields is marked review because strictness differs by generated client.
- Only JSON request bodies and the first 2xx JSON response schema are inspected.

## Trust boundaries
The app parses untrusted JSON in the browser, imposes a 2 MB per-file limit, performs no network calls after loading the static fixtures, and never modifies an API server. Consumer mappings are synthetic. The report is supporting evidence, not a compatibility guarantee.
