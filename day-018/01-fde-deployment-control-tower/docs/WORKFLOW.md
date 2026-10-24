# Standard FDE workflow

1. Open a workspace for one customer and integration. Set environment, owner, target date and measurable success criteria.
2. Complete discovery before promising a delivery date or a go-live.
3. Test connectivity from the same network/runtime context the integration will use.
4. Validate auth identity and minimum scopes without putting secrets in evidence notes.
5. Test contract mapping with synthetic payloads, including required fields, nulls, duplicates and negative cases.
6. Establish bounded timeouts/retries, correlation IDs, monitoring and escalation.
7. Review TLS, webhook trust, data retention and permissions.
8. Run the customer's UAT against acceptance criteria; record the result, not just the meeting.
9. Assign each blocker one owner, one due date and one next experiment.
10. Recalculate readiness after each checkpoint, record decisions and prepare the customer handoff.
11. The accountable release owner makes and records the final go/no-go decision.
12. Monitor the agreed post-launch window and capture actual outcomes.

When a test fails, record expected versus observed behavior, timestamp, request ID and a safe reproduction. Don't silently turn a failed check into N/A.