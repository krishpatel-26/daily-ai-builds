# Architecture

- `index.html`: editors, report, diff viewer, and test pack.
- `styles.css`: responsive interface.
- `app.js`: parser, selected-rule validator, schema diff, case generator, and downloads.
- `fixtures/`: synthetic contract and payload examples.
- `docs/`: assumptions, safety, release, and design notes.
- `templates/`: reusable contract review note.
- `tests/`: manual QA checklist.

This is a static browser application. No backend, database, API key, or network delivery is required. A production tool should use a maintained full JSON Schema validator.