# FDE Integration Triage Workbench — Day 017

A local-first workbench for Forward Deployed Engineers investigating customer integration failures. Paste customer-safe logs and an environment/config JSON object; the app redacts common secrets, applies transparent diagnostic rules, prioritizes blockers, and creates a handoff report.

## Run locally
Requirements: Node.js 18+ (no npm dependencies).

    npm start

Then open http://localhost:4173. Alternatively, open index.html directly in a browser; the local server is recommended.

## Use
1. Click Load sample to inspect the demo case.
2. Replace the sample logs and config with sanitized customer evidence.
3. Click Analyze evidence.
4. Review severity, rule IDs, evidence and suggested actions.
5. Export JSON or a Markdown handoff.

## Scope
- Browser-side analysis only. No customer endpoint is called.
- Secret-like values are redacted from displayed evidence and exports.
- Rule-based heuristic triage, not an AI root-cause oracle.
- It does not execute commands, inspect a customer's cloud, or validate credentials against a live service.

## Quality
Run npm test for built-in Node tests and see tests/MANUAL_TESTS.md for the browser workflow. Keep raw logs out of public repositories and remove personal data before sharing evidence.

## Status
Prototype; validate findings against your actual integration and platform documentation before acting.