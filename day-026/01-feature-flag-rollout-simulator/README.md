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

## Rollout state model
The simulator models a simple sequence: configured → evaluating → promoted to the next exposure step, or rolled back when a guardrail is breached. The first failed step terminates the run; later percentages are not evaluated. This makes the decision trace easy to inspect and avoids treating a failed stage as permission to continue. The model is intentionally synchronous and deterministic so the same inputs produce the same decision.

## Cohort assignment
User assignment uses a deterministic string hash and maps the result into 100 buckets. A user therefore stays in the same bucket when the exposure percentage increases, which is the core property needed for sticky cohorts. This is a teaching implementation, not a cryptographic hash or a substitute for a mature experimentation platform. Avoid putting personal data into identifiers; use opaque stable IDs in real systems.

## Guardrail semantics
A stage passes only when both observed error rate and p95 latency are at or below their configured limits. A value equal to its limit passes; a value above the limit fails. The simulator uses a simple AND policy. Production systems may need additional signals such as saturation, availability, business conversion, queue depth, or dependency health, with clear ownership for each signal.

## Choosing thresholds
Set thresholds from a known baseline and service-level objectives rather than choosing convenient round numbers. Compare the candidate against a stable control cohort where possible. Account for sample size, traffic seasonality, and measurement delay. A short rollout window with too few requests can produce misleading confidence; do not promote solely because the simulator reports a pass.

## Operator playbook
1. Confirm the affected flag and current exposure.
2. Compare candidate metrics with the control and baseline.
3. If a release guardrail is breached, stop exposure growth.
4. Disable the flag or route traffic to the known-good path using the production platform's approved controls.
5. Record the decision, timestamp, owner, and evidence.
6. Verify recovery before attempting another rollout.

The dashboard's kill switch is a local demonstration only; it does not change an external flag.

## Incident rehearsal scenarios
**Error spike:** set error rate above its threshold and verify that the first rollout stage stops. **Latency regression:** set p95 latency above its limit and confirm the same rollback decision. **Healthy candidate:** keep both metrics below their limits and verify that all selected stages are evaluated. **Manual stop:** use the kill-switch control and confirm the displayed exposure returns to zero. Repeat rehearsals after changing thresholds.
