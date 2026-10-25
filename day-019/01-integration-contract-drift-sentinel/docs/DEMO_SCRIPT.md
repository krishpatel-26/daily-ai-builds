# Demo script

## 0:00 — State the problem
“An API contract can change independently of a customer integration. The goal is to discover compatibility risk before rollout.”

## 0:30 — Load sample contracts
Click Load sample contracts. Show the baseline and candidate versions.

## 1:00 — Explain detected drift
Highlight the removed GET operation, the newly required X-Region and Idempotency-Key headers, the new required region property and the closed request schema. Distinguish those breaking changes from the added enum value and response status.

## 2:00 — Validate a baseline payload
Leave the payload target on Proposed V2 and click Validate payload. Show missing region and legacy_code rejected by the new contract. Switch to Current V1 and validate again.

## 3:00 — Review generated tests
Explain how each diff creates a regression-test idea. The plan is exported but not executed by the prototype.

## 4:00 — Close honestly
“The Sentinel is a rules-based compatibility assistant for a supported OpenAPI subset. It doesn't call the provider API or claim full OpenAPI/JSON Schema coverage.”