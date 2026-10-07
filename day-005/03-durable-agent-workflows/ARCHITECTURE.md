# Durable Agent Workflow Engine — ARCHITECTURE.md

This component implements checkpointed workflows with retry, idempotency, and recovery.

Design rules:
- deterministic local behavior
- explicit contracts
- bounded state
- explainable decisions
- testable failure paths
