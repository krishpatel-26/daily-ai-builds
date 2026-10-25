# Five-minute demo script

## 0:00 — State the problem
“When an integration fails, the slowest step is often getting a reproducible example everyone agrees on.”

## 0:40 — Load synthetic scenarios
Click Load sample. Explain that the first case expects 201 but the mock returns a 400 validation error; the second is a healthy read; the third checks Retry-After on a 429 response.

## 1:30 — Run all replays
Show the PASS/FAIL summary. Expand the first scenario and point to the exact status and missing-response-field assertions.

## 2:15 — Change one expectation
Edit the create scenario's mock response or expected status. Run again to show the difference between expected and observed behavior. The mock is local and deterministic.

## 3:00 — Export the handoff
Export the Markdown handoff and standalone Node test draft. Explain that generated tests are drafts and must be reviewed and run in a real test repository.

## 4:15 — Close honestly
“This tool never calls a customer API. It structures a reproducible local scenario and supports regression planning; it is not proof of actual production behavior.”