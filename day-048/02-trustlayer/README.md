# TrustLayer — Evidence-Verified AI Agent Runtime & Adversarial Evaluation

**Day 048/365 — Research Build 02.** A deterministic safety layer for simulated AI agent tool proposals. Python 3.11+, no external runtime packages.

## Features
- Server-side allowlist with forbidden action categories and resource namespaces.
- Evidence bindings to exact action/resource combinations.
- Trusted-source checks and evidence time-to-live expiration.
- Approval requirement for sensitive, otherwise permitted actions (simulated internal approval registry).
- Basic lexical prompt-injection indicator checks.
- Tamper-evident SHA-256 chained local decision audit log.
- Nine adversarial fixture proposals with an evaluation dashboard.
- 16 automated unit tests covering safeguards, approvals, evidence, and tampering.

## Run

```bash
python -m trustlayer.server
# In a second terminal:
python -m unittest discover -s tests -v
```

Open http://127.0.0.1:4201; demo JSON at GET /api/demo.

## Security limitations
No LLM calls or real tool execution. Lexical injection detection is incomplete; do not treat it as a guarantee against prompt injection. Evidence only checks structured binding and freshness, **not whether the claim is actually true**. The approval registry is a local simulation with no identity verification or payload binding; never use it for production authorization. The audit ledger is not cryptographically signed or externally anchored, and is not a substitute for secure audit storage. No authentication, persistent storage or production security validation.