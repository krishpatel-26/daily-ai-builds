# FDE Deployment Control Tower — Day 018

A local-first customer deployment workspace for Forward Deployed Engineers. Track an integration from discovery through go-live, manage evidence-backed readiness gates, assign blockers, keep a decision timeline and export a customer handoff.

## Why this is different
Day 017 triaged a log/config snapshot. This system tracks the deployment lifecycle and the evidence needed to make a go/no-go decision. It turns scattered checks into a shared operating record.

## Run
Requirements: Node.js 18+. No npm dependencies.

    npm start

Open http://127.0.0.1:4173. Run built-in core tests with npm test and syntax checks with npm run check.

## Workflow
1. Load the demo workspace or create a customer integration record.
2. Fill in customer, owner, environment, target date and success criteria.
3. Move through eight deployment gates: discovery, connectivity, authentication, API contract, observability, security, UAT and rollback.
4. Mark each check pass/fail/not applicable/to do and attach evidence notes.
5. Register blockers with severity, owner and due date.
6. Review readiness score, evidence gaps and the recommended next actions.
7. Export a JSON workspace, a Markdown customer handoff or a verification runbook.

## Privacy and scope
All workspace state is stored in browser localStorage. No customer systems are called and no backend receives the data. Secret-like patterns are masked in report outputs, but redaction is heuristic, not guaranteed. Do not paste credentials or confidential production material.

The readiness score is an explainable checklist indicator, not a probability of success or a substitute for actual validation. This is a prototype, not a certified deployment gate.