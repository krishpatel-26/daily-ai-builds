# Deployment readiness checklist

## Before customer rollout
- [ ] Validate endpoint and API version in the intended environment.
- [ ] Confirm identity and minimum scopes with the customer platform owner.
- [ ] Confirm network/DNS/VPN and certificate trust from the runtime location.
- [ ] Confirm API schema, required fields and a sanitized passing fixture.
- [ ] Set bounded timeouts and an error-aware retry policy.
- [ ] Verify webhook signature checks and idempotency behavior.
- [ ] Test negative paths for invalid credentials, throttling and transient 5xx errors.
- [ ] Document dashboards, alerts, request IDs and escalation owners.
- [ ] Confirm rollback/disable switch and customer change window.
- [ ] Record an explicit owner and go/no-go decision.

The workbench can help organize evidence. It cannot certify that these checks have actually passed.