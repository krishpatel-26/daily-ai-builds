# Problem statement

Customer integrations often depend on an API contract that changes independently of the implementation. An upstream service can add required fields, remove an operation, tighten validation or change a type. The customer may discover the break only after a deploy has reached staging or production.

The Sentinel provides a pre-deployment review: compare the baseline and candidate contract, explain likely compatibility impact, validate a sample payload and produce a regression-test plan.

## Target users
- Forward Deployed Engineers and implementation engineers
- Solutions engineers supporting customer integrations
- API owners managing versioned contracts
- Support engineers preparing customer migrations

## Non-goals
This prototype does not call a live API, infer business semantics not present in the supplied documents, execute generated tests or approve releases automatically. Its output is a prioritized review artifact, not a guarantee.