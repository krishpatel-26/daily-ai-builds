# Edge-case matrix

| Area | Test input | Expected behavior |
| --- | --- | --- |
| Empty dataset | No cases configured | Show zero cases and no divide-by-zero errors |
| Empty context | Context omitted | Evaluation should require explicit handling, not silently fabricate evidence |
| Conflicting context | Two sources disagree | Require a conflict-aware answer or review |
| Malformed import | Invalid JSON | Reject and retain the current dataset |
| Partial import | Missing required case fields | Explain the validation failure |
| Duplicate ID | Two imported cases share an ID | Reject or normalize before storing in a production version |
| Very long input | Large prompt and context | Bound input size and report truncation explicitly |
| Tool timeout | Simulated timeout | Surface failed tool state; never imply success |
| Untrusted instruction | Context contains hostile instruction | Preserve application instruction hierarchy |
| Sensitive value | Credential appears in trace | Redact before persistence or export |
| Nondeterminism | Same case produces different answers | Use repeated trials and variance reporting |
| Grader disagreement | Human and model grader differ | Route to review and capture adjudication