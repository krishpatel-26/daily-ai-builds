# Security and responsible research

AEGIS runs locally and uses only bundled synthetic data. It does not execute user-provided code, make network requests, or call external model APIs.

Before using real data:
- Remove personal or confidential information.
- Verify dataset licenses and permissions.
- Treat retrieved text as untrusted input.
- Do not interpret benchmark scores as safety certification.
- Record dataset provenance and evaluation changes.
- Review dependencies and pin versions if dependencies are introduced.

The current prototype is not a security evaluation framework and does not validate model behavior beyond the stated retrieval metrics.
