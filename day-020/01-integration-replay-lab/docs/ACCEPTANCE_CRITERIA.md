# Acceptance criteria

- [ ] npm start serves the UI on 127.0.0.1:4173.
- [ ] Load sample populates three scenarios and runs them.
- [ ] The create-customer case fails the status and required response-path assertions.
- [ ] The happy-path read case passes all configured assertions.
- [ ] The throttling case verifies status 429 and Retry-After: 30.
- [ ] Scenario validation rejects duplicate IDs, unsupported methods and paths not starting with slash.
- [ ] Filters show all, failed and passed scenarios correctly.
- [ ] Invalid JSON shows an actionable message.
- [ ] Handoff and JSON exports mask common secret patterns.
- [ ] Generated Node.js test output parses as JavaScript.
- [ ] Unit tests and server tests pass.
- [ ] Browser manual test plan has been run before claiming wider release readiness.

This checklist defines tests to execute; checked items need observed evidence.