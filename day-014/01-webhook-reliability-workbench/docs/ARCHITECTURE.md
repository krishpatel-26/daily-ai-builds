# Architecture

The workbench is a static browser application.

- index.html defines the event inbox, inspection view, validator, and runbook.
- styles.css provides the responsive dark UI.
- app.js owns synthetic fixtures, filtering, payload checks, event history, simulated retry/replay, and exports.
- fixtures/ contains standalone payload examples.
- docs/ records the assumptions, operational guidance, and validation plan.
- tests/manual-test-cases.md defines the current manual QA checklist.

No server, database, network requests, real signing, endpoint delivery, or external notifications are implemented. The event array exists in the current page session and resets on reload. Export files are created only when a user clicks export.

## Future service boundary
A production architecture would separate ingestion, durable event storage, delivery workers, retry scheduling, receiver response capture, dead-letter queues, and the operator UI. Secrets and signing keys must stay server-side.