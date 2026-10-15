# Acceptance criteria

- User can create a signal with account, type, severity, evidence, owner, and next action.
- Missing required fields are rejected.
- Queue filters by blocker, high priority, open, and completed.
- Priority is deterministic and documented.
- Selecting a signal creates an account brief containing evidence and next action.
- Follow-up draft includes the evidence and action, with explicit human-review language.
- Completed signals cannot create follow-up drafts.
- JSON export/import works for a list of signals.
- Records persist locally after reload.
- Demo records are labeled synthetic.
