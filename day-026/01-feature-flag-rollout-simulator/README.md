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

## Release readiness checklist
- [ ] A named owner is accountable for the flag.
- [ ] The flag has a concise purpose and removal plan.
- [ ] The control and candidate cohorts are understood.
- [ ] Error and latency guardrails are defined before rollout.
- [ ] A tested fallback path exists.
- [ ] Monitoring covers dependencies as well as the changed service.
- [ ] Someone is available to respond during the rollout window.
- [ ] The flag has a review or retirement date.

## Verification matrix
| Scenario | Input condition | Expected result |
|---|---|---|
| Disabled flag | enabled = false | No user is exposed |
| Zero exposure | percentage = 0 | No user is exposed |
| Full exposure | percentage = 100 | Every bucket is included |
| Healthy metrics | Both metrics within limits | Continue through configured stages |
| Error breach | Error rate above limit | Stop and roll back |
| Latency breach | p95 above limit | Stop and roll back |
| Invalid schedule | Descending percentages | Reject configuration |
| Missing governance | Owner/purpose/review date absent | Flag marked for review |

## Simulation input contract
The `POST /api/simulate` endpoint accepts a JSON object with `steps` (ascending percentages), `errorRate`, `latencyP95`, `maxErrorRate`, and `maxLatencyP95`. The dashboard sends numeric values. Invalid JSON returns a client error; invalid rollout configuration is surfaced as an error response. The service is bound to loopback for local use and is not designed as a public API.

## Local security notes
The server binds to `127.0.0.1`, does not require credentials, and is intended for a developer workstation. Do not expose it to a public network or deploy it as-is. A production control plane would require authentication, authorization, CSRF protection where applicable, input validation, rate limiting, audit trails, secret management, and change approval policies.

## Production telemetry integration (design note)
A real rollout controller should consume time-windowed metrics from an observability backend rather than static form values. Each measurement should carry a service, environment, release identifier, cohort, time window, sample count, and source timestamp. The decision engine should reject stale or incomplete telemetry and make its evaluation window visible to operators. None of these integrations are implemented in this demo.

## Recommended audit event fields
For a production implementation, record a unique event ID, flag key, environment, previous and new exposure, actor identity, decision reason, evaluated metrics, threshold values, timestamp, and correlation/release ID. Keep audit records append-only and restrict access. The simulator does not persist audit events; this section describes a production hardening requirement.

## Feature flag lifecycle
Treat flags as temporary operational controls unless they are explicitly designed as permanent configuration. Create flags with an owner, purpose, creation date, review date, and removal condition. After full rollout, remove obsolete branching code and retire the flag. Periodically review stale flags because long-lived flags increase test combinations and operational complexity.

## Cohort analysis caveats
Stable bucketing supports consistent assignment, but it does not prove that cohorts are statistically comparable. Real experiments need sufficient sample size, exposure logging, exclusion rules, and analysis that accounts for repeated users and multiple metrics. Avoid interpreting a small synthetic sample as evidence of product impact. The sample users shown in the interface are illustrative only.

## Rollback versus recovery
Disabling a feature flag can stop new exposure, but it does not necessarily reverse database migrations, undo external side effects, or restore corrupted data. Design backward-compatible changes, reversible migrations where practical, and compensating actions for irreversible workflows. Validate recovery separately from the flag toggle. The simulator models exposure returning to zero, not full system recovery.

## Production hardening roadmap
Before adapting this concept into a real service, add a persistent flag store, authenticated role-based controls, approval workflows, real metrics adapters, stale-data detection, durable audit logging, alert routing, concurrency protection, and integration tests against a staging environment. Define failure behavior for the control plane itself; an unavailable rollout controller should not silently promote a release.

## Operator usability
Release controls should make state, risk, and next action clear without relying on color alone. Pair status colors with text labels, preserve keyboard access, announce state changes to assistive technology, and show units beside every metric. In a production interface, require confirmation for high-impact actions and display the target environment prominently before applying them.
