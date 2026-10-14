# Architecture

Static ES-module frontend, no backend dependency.

- `app.js`: DOM events, view rendering, and orchestration.
- `src/domain.js`: validation, invoice state, prioritization, and summaries.
- `src/storage.js`: guarded local-storage read/write.
- `src/csv.js`: CSV serialization and parsing.
- `src/reminders.js`: deterministic reminder copy.
- `src/demo-data.js`: synthetic records.
- `tests/`: Node built-in test runner.

Domain helpers are separated from DOM rendering so business rules can be tested independently.