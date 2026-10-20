# Acceptance criteria

- The user can load synthetic event examples.
- The event inbox supports search and status filtering.
- Selecting an event exposes its payload and attempt timeline.
- The payload validator checks the required envelope and reports problems.
- Retry and replay actions are visibly marked as simulated.
- Duplicate event IDs trigger an idempotency warning in the workspace.
- A user can create a local test event.
- The event log can be exported as JSON.
- The README explains limitations and local run instructions.
- UI wording does not imply actual network delivery or a confirmed root cause.