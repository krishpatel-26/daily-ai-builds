# Integration Contract Drift Sentinel — Day 019

A local-first FDE workbench for comparing API contract revisions before a customer deployment. It detects likely breaking changes, validates sample payloads against the newer request schema, generates regression-test ideas and exports an evidence-backed rollout-risk review.

## Why it matters
A customer can have a green integration today and still break after a provider changes a contract. The Sentinel compares contract versions before rollout, classifies the impact and turns each finding into a testable action.

## Run
Requirements: Node.js 18+. No npm runtime dependencies.

    npm start

Open http://127.0.0.1:4173. Run core tests with npm test and syntax checks with npm run check.

## Try it
1. Click Load sample contracts.
2. Click Analyze contract drift.
3. Review the breaking/additive change list and compatibility recommendation.
4. Validate the included sample payload against the new request schema.
5. Export the Markdown review and generated regression-test plan.

## Scope
- Supports an OpenAPI-style JSON subset with paths, methods, parameters, request bodies, responses and component schemas.
- Compares schema properties, required fields, types, enums, operation parameters and response codes.
- Validates basic JSON types, required properties, enums, nested properties and additionalProperties=false.
- Generates test ideas; it does not execute tests against a live API.
- No customer endpoints are called; contracts and payloads remain in the browser. No analytics or backend.

## Limitations
This is a prototype and its compatibility rules are heuristic. It doesn't implement the full OpenAPI or JSON Schema specifications, resolve every schema reference, or infer every semantic change. Validate the findings against the provider's documented contract and actual integration tests.