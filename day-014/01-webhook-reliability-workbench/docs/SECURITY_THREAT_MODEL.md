# Webhook security threat model

## Assets
Customer event payloads, integration configuration, signing secrets, delivery logs, and downstream business actions.

## Threats
- Forged events sent to a public receiver
- Replay of old signed requests
- Duplicate delivery causing repeated side effects
- Sensitive data leaking into logs or exported files
- Payloads triggering unexpected business logic
- Secrets exposed in client-side code

## Mitigations for a real implementation
- Verify signatures with server-side secrets and compare timestamps against a replay window.
- Use HTTPS, authentication, rate limits, payload-size limits, and schema validation.
- Redact sensitive fields from logs and define retention policy.
- Keep secret material out of browser JavaScript and Git.
- Deduplicate by stable event ID and record operator replay actions.
- Restrict access to event contents and exports.

This static prototype contains no real credentials and does not implement signature verification.