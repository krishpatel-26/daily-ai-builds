# Design decision log

## Static first
Decision: use plain HTML, CSS, and JavaScript.
Reason: keep the demo easy to run without build tools, provider keys, or backend setup.

## Make outcomes simulated
Decision: retry and replay update local state rather than making HTTP calls.
Reason: safe, reproducible demonstrations without contacting real customer endpoints.

## Validate the envelope, not every business schema
Decision: check required fields and basic types only.
Reason: show useful baseline validation while making the absence of per-event schemas explicit.

## Treat duplicate detection as a warning
Decision: warn on repeated IDs in the local workspace.
Reason: true idempotency must be enforced by a durable receiver-side store and cannot be guaranteed by a browser list.

## Keep operator guidance close to the event
Decision: show a recommended next step and attempt history in the inspection pane.
Reason: the target workflow is diagnosis and evidence collection, not just displaying a status badge.