# Architecture

The prototype is a static browser application with no runtime dependencies. scripts/serve.js serves committed files from the project root on loopback only. The dashboard loads src/core.js as a browser global and app.js as the UI layer.

## State
A workspace contains:
- meta: customer, integration, environment, owner, date and success criteria
- gates: eight stable gate IDs with required checks, status, evidence text and update timestamps
- blockers: severity, owner, due date, linked gate, open/resolved lifecycle
- events: append-only-style decision/update timeline entries

State is stored in browser localStorage. JSON export is the user's portable backup; Markdown exports are generated client-side.

## Decision calculation
The core counts completed, failed and evidence-gap checks; applies explicit blocker penalties; and labels the state NO-GO, CONDITIONAL or GO-TO-REVIEW. The formula and limitations are documented in config/risk-model.json.

## Trust boundaries
There is no backend or network integration. HTML rendering escapes user-controlled values; report text passes through heuristic secret masking. Redaction is not complete or guaranteed.