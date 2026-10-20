# Day 014 — Webhook Reliability Workbench

A static, local-first sandbox for debugging event-driven customer integrations. It provides a sample event inbox, payload contract checks, simulated delivery attempts, retry/replay controls, attempt timelines, and JSON export.

## Why this exists
During an integration rollout, a customer may report that a record did not arrive, a webhook returned an error, or a duplicate event caused confusion. Engineers need to inspect the event, validate its contract, understand attempt history, and choose a safe next action.

## Features
- Synthetic event inbox with failed, delivered, queued, and duplicate examples
- Search and status filters
- Payload inspection and required-field/type validation
- Retry and replay simulation with visible attempt history
- Basic idempotency warnings for duplicate event IDs in the current workspace
- Create a local test event and export the event log as JSON
- No API key, backend, or network delivery required

## Run locally
Open index.html in a modern browser. No build step or server is needed.

## Payload contract
Required: event_id (non-empty string), event_type (non-empty string), created_at (parseable timestamp string), data (object). These are baseline checks only, not a full schema registry or business validation.

## Important limitations
This prototype does not call a real webhook endpoint, sign requests, persist server-side state, or prove receiver-side idempotency. Retry/replay actions are simulations. Real delivery needs authentication, endpoint configuration, durable storage, backoff, bounded retries, dead-letter handling, and tests against a controlled receiver.