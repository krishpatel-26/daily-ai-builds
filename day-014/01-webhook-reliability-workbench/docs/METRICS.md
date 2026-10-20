# Reliability metrics to measure

- Delivery success rate within the agreed delivery window
- Median and p95 delivery latency
- Retry attempts per successful event
- Percentage of events exhausting retries
- Dead-letter queue volume and oldest-event age
- Duplicate side-effect rate
- Payload validation failure rate by schema version
- Mean time from customer report to identified cause
- Percentage of incidents with an owner and verified resolution

Do not infer these metrics from the demo's synthetic sample counts. They require production-grade event timestamps and a defined measurement window.