# Incident triage runbook

1. Confirm the incident window and use a sanitized log export.
2. Load a JSON array or JSON Lines (JSONL) with timestamps, severity, service, message, and request IDs where available.
3. Review severity counts, grouped findings, time bounds, and supporting events.
4. Correlate request IDs with your approved logging/tracing platform.
5. Check deployments, configuration changes, dependency status, and service-owner runbooks.
6. Export JSON or Markdown for handoff.
7. Ask the service owner to validate the hypothesis and record remediation and recovery evidence.

## Guardrails
- Pattern matches are leads, not proof of root cause.
- Never paste credentials, tokens, payment data, or personal information into this demo.
- Never replay production events solely because a recommendation suggests checking retries.
- Preserve original logs and investigate in approved observability systems.

## Limitations
Rule-based heuristics only; no LLM, alerting, authentication, database, durable audit history, or production integrations. Use sanitized synthetic logs and keep this prototype on loopback.
