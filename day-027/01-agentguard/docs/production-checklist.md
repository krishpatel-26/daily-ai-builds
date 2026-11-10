# Production hardening checklist

- [ ] Authenticate actors and reviewers with an identity provider.
- [ ] Derive roles from trusted claims; never trust caller-supplied roles.
- [ ] Store policies in a versioned policy service.
- [ ] Bind state checks to authoritative resource reads.
- [ ] Add tenant isolation and database access controls.
- [ ] Sign approval events and enforce separation of duties.
- [ ] Add idempotency enforcement and replay protection.
- [ ] Encrypt audit data and define retention.
- [ ] Add rate limits, request size limits, and alerting.
- [ ] Execute actions only through narrowly scoped service identities.
- [ ] Run security review and integration tests before production.
