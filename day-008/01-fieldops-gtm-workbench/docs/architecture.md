# Architecture

Static ES-module app; no build step or server.
- `app.js`: UI events, filtering, rendering, import/export.
- `src/domain.js`: validation, scoring, summary and account brief.
- `src/storage.js`: guarded local storage.
- `src/followup.js`: deterministic follow-up draft.
- `src/demo-data.js`: synthetic example signals.
- `tests/`: Node built-in test runner.

The app uses explicit rules and local text templates; no external AI API is called.
