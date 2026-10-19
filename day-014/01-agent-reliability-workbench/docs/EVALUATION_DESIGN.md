# Evaluation design

## Unit of evaluation
One case includes a user input, optional context, expected observable behavior, required checks, and severity.

## Result states
- Pass: all configured acceptance checks are supported by evidence.
- Fail: at least one objective requirement is violated.
- Review: automated or deterministic evidence is insufficient for an unambiguous verdict.

## Recommended real implementation
Keep graders modular. Use deterministic checks where possible (JSON schema, required fields, forbidden strings, citations resolving to source IDs). Use model-based graders only for properties that cannot be safely expressed as deterministic rules, then audit them against human labels.

## Aggregate scores
Always report per-category failures and confidence/coverage alongside the aggregate. Avoid hiding rare but high-impact policy failures inside an average.