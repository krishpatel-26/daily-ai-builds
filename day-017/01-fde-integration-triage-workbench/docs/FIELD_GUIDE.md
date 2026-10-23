# Field guide: asking for good evidence

Ask for the smallest evidence package that can separate likely causes.

## For an HTTP integration
- Target environment and region
- Exact timestamp and timezone
- Request/correlation ID
- Endpoint path with query parameters removed if they contain customer data
- HTTP status and sanitized error body
- API version and auth method (never the credential)
- A minimal redacted payload and schema validation error
- Last known successful request

## For a webhook
- Provider event ID and timestamp
- Delivery status and retry history
- Signature-validation result, but never signing secret
- Whether raw request bytes were preserved for verification
- Replay-window and idempotency behavior

## Communication pattern
“Based on these logs, our leading hypothesis is X because of signal Y. Let's run test Z in staging. Success looks like A; if it fails, we'll capture request ID B and route to owner C.”

State the confidence and alternative hypothesis. Do not say “root cause confirmed” until the evidence supports it.