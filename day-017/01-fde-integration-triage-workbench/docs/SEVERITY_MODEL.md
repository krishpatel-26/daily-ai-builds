# Severity model

- Critical: a likely complete blocker or high-impact connectivity/authentication failure that warrants immediate validation.
- High: a major integration/security/reliability issue likely to block or degrade a rollout.
- Medium: meaningful risk requiring review and a specific mitigation.
- Info: preventive documentation or observability gap.

Readiness score starts at 100 and applies penalties of 32, 18, 8 and 2 points per critical, high, medium and low finding, respectively, clamped at zero. This is a prioritization cue, not a calibrated probability.

Labels:
- BLOCKED when any critical/high item exists
- NEEDS REVIEW when no critical/high item exists but medium items remain
- READY TO REVIEW otherwise

“Ready to review” does not mean production validated.