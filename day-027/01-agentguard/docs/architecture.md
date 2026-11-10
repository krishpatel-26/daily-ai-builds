# Architecture

1. Agent submits a typed action proposal.
2. Policy engine checks role/resource/action allowlists.
3. Sensitive payload keys are rejected.
4. Expected-state preconditions are checked against supplied current state.
5. Decision is persisted with an audit event.
6. Human reviewer may approve or reject pending actions.

The prototype deliberately does not execute external actions. A production adapter should sit after approval and must independently re-check identity, permissions, resource state, and idempotency.
