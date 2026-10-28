# Day 023 — AI Incident Triage Workbench

A local-first engineering prototype that groups structured application logs into prioritized findings, retains bounded supporting evidence, and generates incident handoff reports. This version uses deterministic rules, not an LLM, so results are reproducible and logs stay local.

## Features
- JSON array and JSON Lines input
- Common field alias normalization
- Pattern-based detection of authentication failures, timeouts, rate limits, server errors, data integrity problems, and resource pressure
- Grouped findings, severity ranking, request-ID coverage, and up to five evidence records per group
- JSON API and Markdown report generation
- Node.js built-ins only; no API keys or external dependencies

## Quick start
Requires Node.js 20+.

```bash
npm test
npm run check
npm start
```

Open http://127.0.0.1:4173. API health: GET /api/health. Analyze: POST /api/analyze with JSON body `{"input":"{\\"message\\":\\"upstream timeout\\"}"}`.

## Structure
- `src/triage.js` — parsing, classification, grouping, report generation
- `src/server.js` — local HTTP API
- `tests/triage.test.js` — Node built-in test suite
- `samples/sample-logs.jsonl` — synthetic records
- `docs/incident-runbook.md` — human-led investigation workflow

## Safety and limitations
The server binds to 127.0.0.1 by default. Request bodies are limited to 5 MB and each analysis to 10,000 records. This demo has no authentication, persistence, redaction, telemetry, or production integrations. Do not expose it to a public network or submit sensitive logs. Findings are heuristic hypotheses, not confirmed root causes. It does not execute remediation or retry events.

## Roadmap
Add configurable secret/PII redaction, approved log-source adapters, persistent cases with access controls, rule versioning, integration tests, and optional evidence-grounded LLM summaries requiring human review.

MIT License.
