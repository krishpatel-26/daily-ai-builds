# Threat model

## Assets
Business records, credentials, customer data, workflow integrity, audit records.

## Threats
- Prompt injection causes an agent to propose an unsafe action.
- Agent requests an action outside its role.
- Stale resource state causes an invalid update.
- Sensitive values are smuggled through payload fields.
- Reviewer identity is spoofed in the demo.
- Audit database is modified by a local attacker.

## Controls in this prototype
Role/action allowlists, restricted payload keys, state preconditions, approval queue, audit trail.

## Limitations
No authentication, no signed reviewer identity, no tenant isolation, no encrypted database, no external policy provider, and no production execution adapter. Do not expose this demo publicly or use it as a production authorization service.
