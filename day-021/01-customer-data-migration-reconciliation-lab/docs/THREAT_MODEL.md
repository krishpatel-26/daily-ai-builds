# Threat model

## Assets
Customer records, identifiers, personal data, migration status and field values.

## Risks
- Accidentally exporting data to an unauthorized recipient
- Choosing a non-unique key that hides record collisions
- Leaving fields unmapped and assuming full reconciliation
- Normalization masking a significant difference
- Reading a successful comparison as complete business acceptance
- Importing malformed CSV that is interpreted incorrectly

## Safeguards
- No external requests or target-system mutation
- Explicit key selection and source-to-target field mappings
- Visible duplicate, blank-key and mismatch findings
- Scope and normalization included in report metadata
- File size limit and strict header validation
- Clear limitations and manual review requirement

## Out of scope
Encryption at rest, access control, certified anonymization, database change execution and a formal data-governance workflow.