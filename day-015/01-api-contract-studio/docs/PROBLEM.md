# Problem framing

Users: forward-deployed, integration, solutions, and API engineers validating customer integrations.

Job to be done: determine whether a payload matches the agreed rules, understand what changed between contract versions, and create reproducible edge cases.

Common failures include missing required fields, changed enums, mismatched types, untested boundaries, and confusing syntactic JSON validity with API compatibility.

Principles: explain violations by path, state supported rules, separate validation from diff heuristics, generate repeatable examples, and avoid live API calls by default.