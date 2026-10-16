# Day 009 — FDE Discovery Copilot

A local-first prototype for turning discovery-call notes into evidence-linked signals, suggested actions, and a human-reviewed follow-up draft.

## Why build this?

Forward-deployed engineers often hear implementation details, workflow friction, security dependencies, success criteria, and product requests in the same customer conversation. GTM and account teams need a clear handoff, but a generic summary can lose the evidence behind the next action.

This prototype keeps each candidate signal connected to the sentence that triggered it.

## Features

- Paste notes or load a synthetic sample account.
- Detect six candidate categories: implementation blocker, adoption friction, success criterion, expansion signal, security/delivery risk, and product feedback.
- Display the exact evidence sentence and matched keywords.
- Generate suggested next actions with proposed owners.
- Create a follow-up email draft with no automatic sending.
- Copy a brief or export JSON.
- Works as a static page without a server or API key.

## Run locally

Open `index.html` in a modern browser. The app uses ES modules and browser APIs; if your browser blocks local modules, run a static server from this directory:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Important limitations

This is a keyword-based heuristic, not an LLM and not a validated classifier. One sentence can trigger multiple categories; terms can be ambiguous; confidence is a rough UI indicator, not a calibrated probability. All suggested actions and owners require human review. The app does not persist notes to a database, call external APIs, or send messages. Avoid pasting sensitive customer information into a prototype.

## Validation checklist

- [ ] Test notes with no matching terms.
- [ ] Test one sentence that triggers multiple categories.
- [ ] Test empty and very short notes.
- [ ] Verify exported JSON contains evidence and matched terms.
- [ ] Review follow-up draft for unsupported commitments.
- [ ] Validate the categories with FDEs and customer-facing GTM teams.
- [ ] Add unit tests and accessibility checks before broader use.

## Build thesis

The value of an FDE workflow is not just summarizing a conversation. It is preserving the path from customer evidence → technical blocker or business signal → accountable next action → verified outcome.
