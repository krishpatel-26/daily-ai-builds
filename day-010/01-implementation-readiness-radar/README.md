# Day 010 — Implementation Readiness Radar

A local-first checklist and launch-planning workspace for Forward-Deployed Engineering and GTM teams.

## Problem
Customer implementations often look green in a status meeting while access, integration, security, data, adoption, or support dependencies remain unresolved. Teams need a shared view of evidence and ownership before promising a launch date.

## Features
- 12 weighted readiness checks across discovery, ownership, technical setup, security, data, adoption, operations, validation, and GTM handoff.
- Transparent readiness score and completion coverage.
- Priority blocker view with suggested owners.
- Target launch date tracking.
- Exportable JSON assessment and Markdown launch plan.
- Synthetic demo account; no server, API key, or automatic external messages.

## Run
Open index.html in a modern browser. If local browser policies restrict scripts, run python -m http.server 8000 from this folder and open http://localhost:8000.

## Scoring
Each checklist item contributes a documented weight. Score = completed item weights divided by total item weights. The score is a workflow heuristic, not a probability of success. Security, integration, access, and acceptance gaps are highlighted as critical blockers.

## Limitations
The prototype does not verify whether evidence is genuine, integrate with a CRM, persist to a shared database, or notify owners. A checked item is an assertion by the user. Review the checklist with customer stakeholders and do not treat the score as a substitute for engineering sign-off.

## Build thesis
A launch date should be the consequence of verified readiness, not the starting assumption. Connect customer evidence to technical dependencies, accountable owners, and a customer-approved go/no-go decision.