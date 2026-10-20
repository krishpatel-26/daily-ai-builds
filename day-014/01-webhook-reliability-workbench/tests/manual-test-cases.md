# Manual QA checklist

- [ ] Open index.html; empty state is visible.
- [ ] Load demo events; inbox contains multiple statuses and stats update.
- [ ] Search by event ID, event type, and customer.
- [ ] Filter Failed, Queued, Delivered, and Duplicate statuses.
- [ ] Select each event and inspect payload and timeline.
- [ ] Retry the transient HTTP 500 event; confirm the mock recovery is recorded.
- [ ] Retry the HTTP 400 event; confirm it remains failed and explains the payload issue.
- [ ] Replay an event with an already delivered event ID; confirm a duplicate warning.
- [ ] Create a test event; verify it appears in the inbox.
- [ ] Validate a structurally valid payload.
- [ ] Validate malformed JSON and a missing required field.
- [ ] Format valid JSON and clear the validator.
- [ ] Export the event log and parse the resulting JSON.
- [ ] Test keyboard selection and a narrow viewport.
- [ ] Confirm the UI states that retries and replays are simulated and no network request is made.