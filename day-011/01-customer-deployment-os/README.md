# Day 011 — Customer Deployment OS

A local-first FDE workspace connecting customer-reported signals, implementation readiness, proposed next steps, and a shareable handoff brief.

## Features
- Account, target launch date, owner, and stage
- Signal capture with evidence, type, priority, and suggested owner
- Signal resolution workflow
- Eight readiness checks with critical gates
- Heuristic completion score and launch plan
- Customer handoff brief
- Browser-local state and JSON/Markdown exports
- Synthetic demo account; no automatic messages

## Run
Open index.html in a modern browser. No build step or API key is needed.

## Limitations
The readiness score is a checklist completion ratio, not a verified launch-success probability. A checked item does not prove evidence is correct. This is a static prototype with no authentication, shared database, LLM provider, CRM integration, or multi-user sync. Use only synthetic or non-sensitive information.

See tests/manual-test-cases.md. Browser QA and automated tests still need to be run before real customer use.