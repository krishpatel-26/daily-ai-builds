# Day 012 — Autonomous GTM Signal Engine

A local-first prospect qualification workbench with inspectable scoring rules, deduplication, suppression controls, and human-reviewed outreach drafts.

## Features
- Add prospect records with company size, role, intent, and stack-fit inputs.
- Apply a transparent 100-point heuristic score.
- Explain every score component.
- Detect duplicate company domains.
- Maintain opt-out / suppression status and prevent draft generation for suppressed records.
- Filter and search records.
- Generate editable drafts grounded in the entered fields.
- Export CSV with qualification scores and reasons.
- Synthetic demo data; no external enrichment, CRM connection, scraping, or automatic sending.

## Run
Open index.html in a modern browser. State is stored in browser localStorage.

## Scoring
Company size: 20 points; intent: 0–35; stack match: 0–25; role keywords: 0–20. A score of 60 or above is labeled qualified unless suppressed. This is an illustrative heuristic, not a validated buyer-intent model.

## Limitations and safeguards
The demo does not verify identity, company facts, legal basis, or actual consent. The opt-out field is a local suppression flag only. Verify recipient expectations, applicable rules, accuracy, and suppression status before any manual outreach. It does not send messages.