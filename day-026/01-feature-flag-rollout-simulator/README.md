# ReleasePilot — Feature Flag Rollout Simulator

**Day 026 of Daily AI Builds.** A local-first progressive-delivery workbench for rehearsing staged feature exposure and rollback decisions.

## What it does
- Simulates staged rollout percentages (1%, 5%, 25%, 50%, 100%).
- Evaluates candidate error-rate and p95-latency guardrails at each stage.
- Stops at the first breached threshold and models exposure returning to 0%.
- Demonstrates deterministic, sticky user bucketing.
- Includes a simulated kill switch and a release-governance checklist.

## Run locally
Requires Node.js 20+ and no third-party dependencies.

```bash
npm test
npm run check
npm start
```

Open http://127.0.0.1:4176.

## Example scenarios
- **Healthy:** error rate 0.8%, p95 latency 280 ms, thresholds 2% and 500 ms.
- **Error regression:** set error rate to 3% to trigger rollback.
- **Latency regression:** set p95 latency to 650 ms to trigger rollback.
- **Emergency:** select Trigger kill switch to rehearse a manual stop.

## Architecture
- `src/rollout.js`: deterministic bucketing, guardrail evaluation, rollout simulation, flag lifecycle checks.
- `src/server.js`: Node.js built-in HTTP server and simulation endpoint.
- `app.js`, `index.html`, `styles.css`: interactive dashboard.
- `tests/rollout.test.js`: Node's built-in test runner.

## Important limitations
This is an educational simulator using synthetic metrics. It does not connect to production traffic, manage real feature flags, collect telemetry, or perform an actual rollback. A production rollout system needs authenticated controls, durable audit logs, real observability integrations, access policies, tested fallback paths, and ownership/lifecycle governance.

## Design principle
Deployment and release are separate decisions. Increase exposure only when evidence supports it, and define rollback criteria before the rollout begins.

Further reading: [Vercel — Feature flags](https://vercel.com/i/feature-flagging) · [GO Feature Flag — Rollouts](https://gofeatureflag.org/product/rollouts)
