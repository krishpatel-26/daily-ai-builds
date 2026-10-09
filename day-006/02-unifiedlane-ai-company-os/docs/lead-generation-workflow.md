# Concrete workflow: B2B lead generation with human approval

## Scenario
A company wants to identify promising B2B prospects, prioritize them, prepare tailored first-touch messages, and let a human review every message before anything is sent.

## Workflow
1. **Research input** — demo prospect records include company, website, industry, team-size band, public business signal, and contact role.
2. **Qualification** — a transparent illustrative scoring function assigns a 0–100 score and tier, with reasons. It is a demo heuristic, not a validated predictive model.
3. **Personalization** — creates an outreach draft using the provided context; it does not invent quantified results or claim a prior relationship.
4. **Policy gate** — all drafts remain `pending_approval`; the workflow explicitly reports `messages_sent: 0`.
5. **Human review** — an identified reviewer can approve a pending draft. Approval does not itself send the message.
6. **Delivery adapter (future)** — a separately authorized integration should re-check consent, suppression lists, rate limits, data handling, and approval freshness before sending.
7. **Feedback loop (future)** — store delivery outcomes and replies, then evaluate campaign performance before changing scoring or prompts.

## Run it

```bash
pip install -e ".[dev]"
python examples/lead_generation_demo.py
pytest
```

The example uses fictional companies and reserved `.example` domains. It performs no web research, does not connect to a CRM, and sends no emails.

## Production requirements
- Use authorized, policy-compliant data sources and respect applicable privacy and outreach rules.
- Apply tenant isolation, secrets management, access checks, and audit logging at each tool boundary.
- Keep human approval bound to the exact recipient, subject, body, and expiry; edits invalidate prior approval.
- Use durable workflow state, retries with idempotency, budget/rate limits, observability, and a documented retention policy.
- Measure qualification quality and campaign outcomes before claiming business impact.
