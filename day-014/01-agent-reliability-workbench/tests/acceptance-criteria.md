# Acceptance criteria

- The interface loads without a bundler or API key.
- A fixed set of synthetic cases can be evaluated.
- Each run records a unique ID, time, prompt-version label, and per-case result.
- Per-case result includes a status and human-readable note.
- Users can inspect step-by-step synthetic traces.
- The case dataset can be edited and exported/imported as JSON.
- The run history and selected trace can be exported.
- Prompt comparison identifies textual risk-instruction coverage and labels itself heuristic.
- Limitations clearly state that no model is actually invoked.
- Mobile layout remains usable without horizontal page overflow.

Acceptance here describes intended manual verification; it is not a claim that every criterion has already passed browser QA.