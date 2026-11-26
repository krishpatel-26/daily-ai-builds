# API contract change rollout runbook

## Before implementation
- Agree on the candidate contract and versioning policy with API owners.
- Identify all consumers, including undocumented integrations, batch jobs and internal services.
- Validate the consumer registry with named integration owners; this demo registry is synthetic.
- Decide whether the change can be made additive or needs a migration window.

## Before release
- Run ContractLens against the current production contract and candidate contract.
- Review every breaking and review-level finding with an engineer.
- Generate consumer-specific contract tests from actual request/response examples.
- Notify affected customer owners with dates, migration notes and support channels.
- Provide a compatibility window or versioned alternative when required.

## During rollout
- Deploy additive server support before migrating clients when feasible.
- Monitor operation-level errors, validation failures and client version distribution.
- Keep rollback criteria measurable and assign a release decision owner.
- Do not equate a clean static diff with runtime compatibility.

## After rollout
- Re-run consumer tests against the released endpoint.
- Confirm each affected consumer owner has validated their integration.
- Remove deprecated behavior only after the agreed migration window and approvals.
- Archive the approved contract, report, exceptions and sign-off record.
