# Token Cost Observatory — Day 028/365

A zero-dependency Node.js dashboard for understanding LLM token usage, estimated API spend, model/project attribution, budget health, and basic spend alerts.

## Features
- Estimate input/output token costs using an editable model pricing map
- Aggregate spend by model, project, and event date
- Track input, output, and total tokens
- Configure a monthly USD budget
- Alert at 80% and 100% budget consumption
- Flag a latest-day spend spike above 2× the previous daily average
- Identify events for models without configured pricing
- Ingest additional usage events through an HTTP API or dashboard form

## Run locally
Requires Node.js 20 or newer. No third-party packages are required.

```bash
npm test
npm run check
npm start
```

Open http://127.0.0.1:4178.

## API
- `GET /api/analytics` — summary, model/project/day breakdowns, alerts
- `GET /api/events` — current in-memory events
- `POST /api/events` — add one event or an array of events
- `POST /api/budget` — set `{"monthlyBudget":100}`

Example event:
```json
{
  "project": "support-agent",
  "provider": "openai",
  "model": "gpt-4.1-mini",
  "inputTokens": 12000,
  "outputTokens": 2500
}
```

## Pricing assumptions
Rates are illustrative USD per one million tokens and are defined in `src/analytics.js`. Update them to match the exact provider, model version, region, cached-input rules, and effective pricing contract before using the estimates for financial decisions.

## Important limitations
This is a local prototype, not a billing system. Usage events and budget settings are held in memory and reset on restart. It does not connect to provider billing APIs, account for every provider's pricing dimensions, persist data, authenticate callers, or provide production-grade anomaly detection. The spend-spike detector is a simple daily comparison, not a statistical forecasting model. Never expose the local ingestion API publicly without authentication and validation hardening.

## Suggested next steps
- Add provider-specific pricing catalogs and effective dates
- Persist events in PostgreSQL or SQLite
- Add tenant isolation, API keys, and audit logs
- Add time-window anomaly detection and budget forecasting
- Connect provider usage exports and billing APIs

**Daily AI Builds:** one practical engineering build at a time.