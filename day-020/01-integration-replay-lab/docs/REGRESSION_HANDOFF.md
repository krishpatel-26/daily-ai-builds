# Regression handoff

A useful handoff should include:
- Brief symptom statement and affected operation
- Environment/version and correlation ID, sanitized where needed
- Minimal request shape and the observed response
- Explicit assertions that fail before the fix
- Expected post-fix outcome and negative-path behavior
- Generated test file or scenario pack
- Reproduction steps and safe test data
- Owner, PR/issue reference and validation result
- Residual risks and conditions that were not tested

Before sharing, remove secrets and customer PII. The tool's masks are only an initial guard; inspect the artifact manually.