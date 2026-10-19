# Lightweight threat model

## Assets
Prompts, evaluation data, model outputs, traces, provider metadata, and exported reports.

## Threats
- Sensitive user data leaks through logs or exports.
- A manipulated context attempts to override system instructions.
- A misleading grader result is interpreted as proof of correctness.
- Model/provider errors are mistaken for valid answers.
- Prompt versions cannot be reproduced after a release.
- Trace fields accidentally contain API keys or credentials.

## Mitigations for a production version
- Redact sensitive values before traces are persisted.
- Separate trusted instruction layers from retrieved/untrusted context.
- Apply deterministic checks where possible and human review to ambiguous results.
- Record provider errors and distinguish them from grader failures.
- Hash immutable prompts and version datasets.
- Keep API keys server-side and restrict access to exports.

The current prototype makes no external calls and uses synthetic records, but it is not a production security implementation.