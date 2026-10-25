# Integration Replay Lab — Day 020

A local-first FDE tool for turning sanitized customer API failures into repeatable mock scenarios, observable assertion results and regression-test artifacts.

## What problem it solves
A customer says “the integration fails,” but the team cannot reliably reproduce it. The Replay Lab packages a request shape, expected outcome and observed/mock response into a deterministic scenario. It runs assertions entirely locally, highlights the first mismatch and generates a test handoff.

## Run
Requirements: Node.js 18+. No runtime dependencies.

    npm start

Open http://127.0.0.1:4173. Run tests with npm test and syntax checks with npm run check.

## Demo workflow
1. Click Load sample scenarios.
2. Click Run all replays.
3. Inspect PASS/FAIL per case and the exact assertion that failed.
4. Edit the scenario JSON to model another request/response.
5. Export a redacted incident handoff or generated Node.js regression test plan.

## Safety boundary
This prototype is a deterministic local simulator, not a live network replay proxy. It never sends requests to a customer API or external endpoint. Responses come from the scenario's local mockResponse object.

## Scope and caveats
- Checks status, basic JSON paths, response headers and latency budgets against synthetic mock results.
- It does not validate authentication against a real provider, measure real latency or prove production behavior.
- Secret masking is heuristic. Review exports before sharing and use synthetic or pre-redacted evidence.
- Generated tests are artifacts for review; they are not automatically committed to or executed in a customer repository.