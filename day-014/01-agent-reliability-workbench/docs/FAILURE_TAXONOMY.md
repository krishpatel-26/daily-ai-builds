# Agent failure taxonomy

- Grounding failure: answer is unsupported by supplied context.
- Abstention failure: system invents a value instead of expressing uncertainty.
- Format failure: output violates a required schema or contract.
- Instruction failure: ignores length, tone, or structural constraints.
- Tool failure: hides timeout, error, or unsuccessful execution.
- Retrieval failure: required source is missing or irrelevant.
- Conflict failure: treats contradictory evidence as settled fact.
- Permission failure: exposes data or triggers an unauthorized action.
- Commitment failure: invents an approved feature or delivery timeline.
- Observability failure: insufficient trace metadata to reconstruct a result.

For each incident, record reproducible input, expected behavior, actual behavior, severity, and a regression test.