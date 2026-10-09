# UnifiedLane AI Company OS

A reference implementation of a multi-agent operating layer for business workflows. One orchestrator coordinates specialized agents while enforcing explicit roles, least-privilege tool access, audit events, human approval gates, and recoverable task state.

## Architecture

```text
Business Request
      |
      v
Orchestrator / Control Plane ---- Policy + Role Permissions
      |                                  |
      v                                  v
Research | Strategy | Content | Operations | Outreach | Analytics
      |                                  |
      +---------- Shared Services -------+
                 Memory / Knowledge / Tools
      |
      v
Audit Events + Observability + Human Approval + Outputs
```

## Included in this MVP

- Role-based capabilities and least-privilege authorization.
- Task routing to six specialist agent roles.
- Risk-aware approval gates for external or sensitive actions.
- Structured audit events for allow/deny/approval decisions.
- Simple in-memory orchestration so the policy model is easy to inspect.
- Tests for routing, permissions, and approval requirements.

## Quick start

Requires Python 3.11+.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest
```

Run a demo:

```bash
python examples/demo.py
```

## Example policy

An outreach agent may draft a message, but sending it is classified as an external action and requires explicit approval. The analytics agent can read performance data but cannot modify CRM records. Agents should never receive broad credentials simply because another agent needs them.

## Production hardening roadmap

1. Replace in-memory state with PostgreSQL and durable workflow checkpoints.
2. Add a queue and idempotency keys for retries and duplicate delivery protection.
3. Integrate identity-aware secrets, sandboxed tools, and per-tenant policy enforcement.
4. Add OpenTelemetry traces, token/cost budgets, rate limits, and SLO dashboards.
5. Add approval UI, policy versioning, retention controls, and adversarial evaluations.

This repository is an architecture/MVP reference, not a fully autonomous production deployment. External integrations and real model calls are intentionally stubbed.
