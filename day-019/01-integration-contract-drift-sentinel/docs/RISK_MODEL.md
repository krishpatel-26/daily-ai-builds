# Risk and release recommendation

The Sentinel derives a prioritization score from detected changes; it is not a statistical probability.

- Breaking changes produce a risk score of at least 65.
- Higher-severity breaking changes increase the score, capped at 100.
- Semantic-review findings produce a lower non-zero score.
- Only additive changes or no detected material differences result in a zero score in this simple model.

Recommendation states:
- BREAKING CHANGES: operation-level removal or multiple detected breaks
- REVIEW REQUIRED: one or more breaking changes need a migration/compatibility decision
- SEMANTIC REVIEW: changes need human interpretation
- COMPATIBLE: no likely break under supported rules

A compatible label does not prove real-world compatibility. A contract may contain undocumented behavior, authentication changes, rate-limit changes or semantics that are not represented in schema structure.