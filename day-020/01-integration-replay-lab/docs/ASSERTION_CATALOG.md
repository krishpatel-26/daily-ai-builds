# Assertion catalog

- status: expected HTTP status code.
- requiredJsonPaths: every named path must exist; null is considered present, while undefined/missing is absent.
- forbiddenJsonPaths: each named path must be absent.
- headersEqual: case-insensitive header name lookup, exact string value comparison.
- maxLatencyMs: checks the mock's declared latencyMs metadata against a budget. It does not time actual processing.
- bodyEquals: compares the selected JSON value with strict JSON serialization equality.

Assertion results include a stable assertion ID, label, pass/fail, expected value and observed value.

Limitations: header normalization handles names but not full HTTP semantics; JSON equality is order-sensitive for object serialization; dot paths cannot express keys containing dots or array indexing. Avoid relying on unsupported semantics in release decisions.