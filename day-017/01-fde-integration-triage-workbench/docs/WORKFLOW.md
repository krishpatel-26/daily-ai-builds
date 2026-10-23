# FDE triage workflow

1. Establish scope: customer, tenant, target environment, integration path, expected outcome and last known successful run.
2. Request a time-bounded, minimum evidence set: relevant log excerpt, request ID, timestamp/timezone, HTTP status and sanitized config.
3. Paste only sanitized evidence into the workbench.
4. Review redacted evidence first and remove any confidential material that escaped masking.
5. Analyze and group findings by severity, evidence and rule ID.
6. Validate the top hypothesis against live telemetry, vendor documentation and customer context.
7. Agree on one low-risk experiment with an owner and rollback/stop condition.
8. Record expected versus observed result and whether the hypothesis was confirmed.
9. Export the handoff note, review it manually and share only through approved channels.
10. Re-run after the change and capture evidence of recovery.

Never ask customers to paste production secrets into chat or a diagnostic form. Never treat a heuristic finding as authorization to change a production system.