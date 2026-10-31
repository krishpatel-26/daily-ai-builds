# SLO Sentinel — Reliability & Error Budget Analyzer

**Day 027 of Daily AI Builds.** A local-first SRE workbench that calculates observed availability, error-budget consumption, burn rate, and release recommendations from aggregate request counts.

## Run locally
Requires Node.js 20+ and no third-party packages.
```bash
npm test
npm run check
npm start
```
Open http://127.0.0.1:4177.

## Inputs
- Availability target (strictly between 0% and 100%)
- Total requests in the measurement window
- Failed requests in the same window
- Measurement window in days

## Metrics
- Observed availability = 1 − failed requests / total requests
- Allowed failure rate = 1 − SLO target
- Error budget consumed = observed failures / allowed failures for the measured request volume
- Burn rate = observed failure rate / allowed failure rate
- Recommendation bands: healthy, warning, high burn, exhausted budget

## Important interpretation
This is a simplified aggregate model. It assumes the supplied request counts are representative of the SLI measurement window. It does not calculate multi-window alerting, time-series burn rates, latency-based SLIs, or statistical confidence. The displayed projected budget duration is a simple extrapolation, not a forecast. Real SRE practice should define SLIs carefully, evaluate short and long windows, consider traffic volume and user impact, and align release policy with service objectives.

## Limitations and safety
No telemetry is collected and no external service is contacted. The API binds to loopback for local use. This is an educational decision-support tool, not an observability platform or an automated production release gate.

## Architecture
- `src/slo.js`: validation and SLO/error-budget calculations.
- `src/server.js`: Node built-in HTTP server.
- `app.js`, `index.html`, `styles.css`: browser dashboard.
- `tests/slo.test.js`: Node built-in tests.
