# Lightweight threat model

## Assets
Assessment status, customer name, launch date, exported files.

## Trust boundaries
The current prototype runs in a browser tab. Exported files leave the browser only through an explicit user action.

## Risks
- Sensitive details included in exports or screenshots.
- A misleading score is shared as an official approval.
- A user marks a prerequisite complete without evidence.
- A future integration exposes customer data to unauthorized users.

## Mitigations
- Use synthetic data for demos.
- Clearly label scores as heuristic.
- Keep external delivery out of scope.
- Require authentication, authorization, audit logs, and retention policies before a multi-user deployment.