# Integration observability expectations

For every integration path, capture:
- Stable request/correlation ID propagated across system boundaries
- Timestamp and timezone with environment/build/API version
- Success/failure count and status/error category
- Latency distribution, not only average latency
- Bounded retry count, backoff and idempotency behavior
- Queue depth/lag and delivery age where applicable
- Webhook delivery attempts and signature validation result
- A dashboard, alert threshold, escalation owner and customer communication route

Avoid logging credentials or full sensitive payloads. A useful error log lets an engineer correlate the failed operation without disclosing customer data.