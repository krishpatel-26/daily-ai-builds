# Delivery observability

## Fields worth recording
- event_id and correlation_id
- event_type and schema version
- destination identifier, with secrets excluded
- attempt number and retry reason
- enqueue, attempt-start, and completion timestamps
- elapsed duration
- HTTP response category and sanitized error summary
- next retry time or terminal disposition
- replay operator and replay reason

## Useful views
- Failure rate by destination and event type
- Delivery latency percentiles
- Retry volume and exhausted attempts
- Age and size of the dead-letter queue
- Duplicate detections
- Events approaching their delivery deadline

Avoid logging full sensitive payloads by default. The current prototype shows example timeline messages only, not real telemetry or operational SLOs.