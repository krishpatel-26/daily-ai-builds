# Day 052 — ContractLens: API Change Impact Lab

ContractLens compares two OpenAPI JSON contracts, classifies compatibility changes, maps affected customer integrations, and builds an evidence-backed rollout handoff.

## Why it matters
A provider can deploy an apparently small API change that silently breaks a customer's integration: a route disappears, a field becomes required, an enum value is removed, or an authentication requirement changes. Forward-deployed and integration engineers need to know which consumers are affected before a release.

## Features
- Compare OpenAPI 3.0/3.1 JSON documents.
- Detect removed/added operations, changed parameters, request schemas, response schemas, enum values, security requirements and response codes.
- Classify findings as breaking, review, or non-breaking with evidence paths.
- Map changed operations to a synthetic customer integration registry.
- Generate a prioritized rollout checklist and Markdown/JSON reports.
- Include fixtures and deterministic regression tests.

## Run
Node.js 18+.

    npm test
    npm run serve

Open http://127.0.0.1:4173. No dependency installation is required.

## Scope
This prototype reads OpenAPI JSON only; YAML is not supported. It focuses on common HTTP operations and schema patterns, not the full OpenAPI specification or every JSON Schema dialect. It does not contact customer systems, infer undocumented dependencies, or guarantee source-code compatibility. Consumer mappings are synthetic and must be validated with integration owners.
