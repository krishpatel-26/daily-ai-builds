# Troubleshooting guide

## Payload validator rejects JSON
Check quotes, commas, brackets, and required envelope fields. Ensure created_at is a parseable timestamp and data is an object rather than null or an array.

## Event appears failed
Inspect the displayed mock response and attempt history. A local failure is only an example, not the status of a real destination.

## Retry does not resolve the event
In this prototype, outcomes are simulated. A real integration should inspect receiver logs and use retry policy rather than clicking replay repeatedly.

## A duplicate warning appears
Compare event_id and verify receiver-side idempotency. Do not assume a duplicate is harmless without checking downstream effects.

## CSV or payload import is unavailable
This prototype takes JSON in the validator and uses its built-in event fixtures. It does not include an HTTP receiver or production event ingestion.