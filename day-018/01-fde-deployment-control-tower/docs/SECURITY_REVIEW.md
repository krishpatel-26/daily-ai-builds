# Security review checklist

- [ ] No secrets or live customer payloads are stored in the repo or demo fixtures.
- [ ] Test token/API-key/email masking with the actual input formats used by the team.
- [ ] Confirm TLS verification remains enabled in the integration runtime.
- [ ] Confirm webhook signature, timestamp and replay checks for every inbound event.
- [ ] Confirm credentials are held in the approved secret manager, not workspace notes.
- [ ] Confirm least-privilege scopes and scheduled rotation ownership.
- [ ] Confirm data minimization, retention and access boundaries for logs and exports.
- [ ] Review exported handoff material before sending it outside the project team.

The Control Tower can record evidence of a review; it cannot replace a security review or certify that the checks passed.