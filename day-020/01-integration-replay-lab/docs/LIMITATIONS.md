# Limitations

- This runner simulates response objects; it does not send a request to localhost or a real API.
- latencyMs is scenario metadata, not wall-clock timing.
- Authentication, authorization, TLS, DNS, rate limits and network behavior can only be modeled as fixture data here.
- Basic JSON path support is dot-separated object traversal; it doesn't implement full JSONPath or array indexing.
- The JSON validator covers scenario shape, not a complete JSON Schema dialect.
- Redaction patterns are incomplete.
- Generated Node.js tests may require hand-editing for unusual data, test frameworks or project conventions.
- Local browser source and exported files are not encrypted or access-controlled.

Use this as a reproducibility and handoff workbench, not as a production replay gateway or release certification system.