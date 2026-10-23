# Diagnostic rule catalog

The app includes heuristics for authentication failures (401), authorization (403), throttling (429), upstream 5xx errors, timeouts, DNS/connection failures, schema validation (400/422), CORS, TLS issues, retry activity and webhook signature failures. Config checks flag HTTP URLs, low configured timeouts, a small retry budget, disabled webhook signature checks, missing endpoint/auth fields and disabled TLS verification.

Each rule carries a stable ID, severity, explanation, next action, suggested owner and redacted evidence. Duplicate occurrences of a rule are grouped into one finding.

Pattern matches can be false positives. For example, a log may include 401 as an unrelated identifier or mention CORS in a successful diagnostic. Verify the matching line and request context before changing production settings.