# Day 023 — API Rate Limit & Quota Lab

A local-first engineering lab for comparing rate-limiting algorithms, understanding HTTP 429 responses, and producing quota incident handoffs.

## Features
- Fixed-window, sliding-window and token-bucket rate limiting.
- Deterministic traffic replay against configurable policies.
- HTTP 429 decisions, remaining quota and estimated Retry-After.
- Per-route metrics, burst behavior and client impact.
- Filterable request ledger with JSON/Markdown export.
- Guardrails for invalid or unsafe policy configuration.

## Run locally
Requirements: Node.js 18 or newer.

    npm test
    npm run serve

Open http://localhost:4173. No package installation or build step is needed.

## Demo boundaries
This lab processes synthetic traffic only. It does not call external APIs, change provider quotas, or enforce limits on live services. Simulated Retry-After is an estimate, not a provider guarantee. Real deployments need distributed atomic state, clock-skew handling, retry budgets, trusted client identity, and provider-specific response headers.
