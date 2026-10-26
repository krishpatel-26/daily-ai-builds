# Identity and field mapping

## Record identity
Choose a source key and target key that represent the same stable entity identifier. A key should ideally be unique, non-empty, immutable and unaffected by formatting changes. Avoid names or email addresses as a primary identity where a stable customer ID is available.

## Field mapping
Map each source field to its destination counterpart. Names may differ (for example, source name → target full_name). Only mapped fields participate in value comparison. A good migration plan maps every field covered by the acceptance criteria.

## Duplicate and blank keys
Duplicate or blank keys make a one-to-one comparison ambiguous. The prototype reports them explicitly and uses the first row for the matching index; do not treat that first-row match as a final result for a duplicate key.

## Normalization
Trimming outer whitespace is a comparison-only option. Email case folding applies only to fields whose source or target field name contains “email”. The source/target text is never rewritten by normalization.