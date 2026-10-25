# Problem statement

An FDE often receives a vague report: “the API is failing.” The original request may be unavailable, the customer environment is inaccessible, and a teammate cannot consistently recreate the bug. Without a deterministic repro, teams repeat discovery work and risk making changes based on an untested guess.

Integration Replay Lab packages a sanitized request shape, a local mock response and explicit assertions into a reusable scenario. It runs deterministic checks without sending traffic outside the browser, points to the first mismatch and exports a regression-test handoff.

## Intended users
- Forward Deployed Engineers and implementation engineers
- Solutions engineers debugging customer API integrations
- Support engineers preparing minimal repros
- API teams creating contract regression fixtures

## Non-goals
It is not a network proxy, packet capture, credential validator, production traffic replay system or live API client. Mock results help reproduce logic and expectations; they do not prove live provider behavior.