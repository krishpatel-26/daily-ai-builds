# Blocker playbook

Each blocker should have one accountable owner, severity, evidence, due date and next experiment. Use the smallest experiment that separates plausible causes.

## Severity guide
- Critical: deployment is stopped, data integrity or security is at immediate risk, or a core customer path is unusable.
- High: a major agreed integration path is blocked or security/reliability requirements are unmet.
- Medium: workaround exists but the rollout is riskier or incomplete.
- Low: minor issue or documentation gap that can be explicitly accepted.

## Working a blocker
1. State the observed symptom without guessing the cause.
2. Attach redacted evidence and a correlation ID.
3. Write the leading hypothesis and at least one plausible alternative in the timeline.
4. Agree on a bounded test, expected result and stop/rollback condition.
5. Assign owner and due date.
6. Capture outcome and confirm whether the blocker can be resolved.
7. If accepted rather than fixed, document the risk owner and expiration/review date externally.

The severity labels are team guidance, not a standardized industry scoring system.