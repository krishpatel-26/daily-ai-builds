# Roadmap

## Harden the prototype
- Add table-driven automated tests for each rule and redaction pattern.
- Add a redaction review panel with reversible per-line approval before export.
- Improve secret detection while documenting false-positive/false-negative limits.
- Separate rule definitions from implementation and make the catalog versioned.
- Add sample cases for OAuth, webhooks, database connectivity, queue lag and schema drift.

## Next iteration
- Add structured JSONL parsing, request-ID correlation and log time-window filters.
- Compare expected vs observed API contracts using imported OpenAPI schemas.
- Generate a customer-facing update with owner, ETA, confidence and next checkpoint.
- Support configurable severity policy per integration type.

## Future
- Optional, explicit connectors to approved observability tools with narrow read-only scope.
- Authenticated workspaces with controlled retention and audited exports.
- Evaluation dataset measuring detection precision/recall against labeled incidents.