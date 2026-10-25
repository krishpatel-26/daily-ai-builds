# Threat model

## Assets
Customer endpoint paths, request metadata, payload examples, response bodies, request IDs and any accidental credentials.

## Risks
- A developer exports raw customer data.
- Pattern-based redaction misses a token format.
- A user interprets a mock PASS as proof of live API health.
- A malicious string in imported JSON is rendered as HTML.
- A user assumes the tool measures real latency or verifies auth.

## Safeguards
- No outbound network calls from the app; local mock simulation only.
- Escape user strings before HTML rendering and use textContent where possible.
- Mask common secret-like patterns in exported evidence.
- Explicitly label simulated latency and generated tests as drafts.
- Keep an allowlist of supported methods and validate scenario shape before running.

## Out of scope
This is not a secure vault, multi-tenant system, production proxy, live traffic recorder or certified incident-response tool. Treat the source and exports as untrusted, and review before sharing.