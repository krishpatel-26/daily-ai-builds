# Roadmap

## MVP hardening
- Complete the manual acceptance checklist on Windows/macOS/Linux browsers.
- Add evidence attachment/import with size limits and explicit review before export.
- Add an evidence freshness field and warn when critical checks rely on stale artifacts.
- Test redaction against labeled synthetic credentials and document detection limits.
- Add controlled import of an existing workspace JSON file.

## Next iteration
- Add customer-specific gate templates and versioned acceptance criteria.
- Add dependency mapping so a blocker can identify downstream gates it blocks.
- Add structured test result objects with expected/observed result and artifact reference.
- Add release review signatures and decision-maker/decision-time fields.
- Add Markdown/CSV evidence export and a changelog diff between checkpoints.

## Future
- Optional connectors to approved ticketing and observability tools with read-only scopes.
- Team collaboration with access control, audit logs, retention policy and encrypted storage.
- Measure whether the readiness score predicts delayed rollouts using a labeled historical dataset.
- Never claim readiness scoring is calibrated until the evaluation has been done.