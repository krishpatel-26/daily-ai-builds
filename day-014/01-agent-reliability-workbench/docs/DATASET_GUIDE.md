# Dataset guide

A useful evaluation dataset should reflect real product risks, not only easy examples.

For each case, store:
- Stable case identifier
- Product scenario and risk category
- Input and context
- Expected observable behavior
- Required deterministic checks
- Severity and rationale
- Dataset version and author
- Review history

Include normal cases, edge cases, missing context, conflicting sources, tool errors, prompt injection attempts where relevant, and boundary conditions. Use synthetic or explicitly approved, redacted examples. Keep a held-out set to reduce overfitting to the test suite.