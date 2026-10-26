# Limitations

- CSV parsing covers common quoted CSV, not every locale, encoding or dialect.
- Reconciliation indexes the first occurrence of a duplicate key; duplicates remain findings and make the match ambiguous.
- Matching uses a single selected key; composite keys are not supported.
- Only mapped fields are compared.
- Normalization supports outer whitespace and email case-folding only.
- Null, blank, literal "NULL" and missing cell semantics are not configurable.
- Report findings can contain actual values; no complete PII redaction exists.
- Data is read-only; the app does not connect to databases or make repairs.
- Score is a prioritization heuristic, not a statistical quality metric.

Use the tool to identify review work, then validate using the customer-approved source of truth, migration logs and business acceptance criteria.