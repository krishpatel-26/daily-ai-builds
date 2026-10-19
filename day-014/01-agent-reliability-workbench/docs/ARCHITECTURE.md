# Architecture

The prototype is a static browser app.

- `index.html`: navigation, evaluation summary, case editor, history, trace inspector, prompt comparison.
- `styles.css`: responsive UI and visual status language.
- `app.js`: synthetic dataset, heuristic/demo run generation, rendering, imports and exports.
- `docs/`: assumptions, evaluation design, threat model, and next steps.
- `tests/`: manual validation plan and example evaluation cases.

There is no backend, model provider, database, authentication, telemetry upload, or persisted run storage. Demo trace metadata is generated locally.