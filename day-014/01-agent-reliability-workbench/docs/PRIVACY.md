# Privacy and data handling

This prototype uses synthetic test cases and generated result metadata inside the browser. It does not make model-provider calls, upload inputs, or persist run history to a server.

Before adapting it to customer data:
- Remove unnecessary identifiers and redact sensitive fields.
- Establish a permitted data source and review process.
- Set access controls and retention / deletion rules.
- Avoid retaining secrets, credentials, or full tool payloads in traces.
- Document third-party model processing and regional requirements.
- Validate export handling and permissions.

A local-first UI is not a substitute for an approved production privacy architecture.