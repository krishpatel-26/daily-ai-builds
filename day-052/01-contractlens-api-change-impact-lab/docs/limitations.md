# Limitations and interpretation

- JSON input only; YAML and remote URL fetching are not supported.
- Supports a subset of OpenAPI 3.0/3.1 patterns, not the complete specification.
- Does not resolve local or remote $ref pointers.
- Compares operations by exact HTTP method and path string; equivalent templated paths are not canonicalized.
- Parameter comparison is operation-level only; path-level inherited parameters are not merged.
- Inspects application/json request bodies and the first sorted 2xx application/json response schema only.
- Does not fully compare nested array item schemas, oneOf/anyOf/allOf, nullable, readOnly/writeOnly, security schemes, callbacks, webhooks, headers, content negotiation, or discriminator behavior.
- Consumer registry is synthetic unless explicitly replaced with a verified inventory.
- Severity is a review heuristic and may produce false positives or miss client-specific breakage.
- A report does not prove source or runtime compatibility and cannot replace consumer contract tests.
