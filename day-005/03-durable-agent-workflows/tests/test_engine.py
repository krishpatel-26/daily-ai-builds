# Durable Agent Workflow Engine — tests/test_engine.py

This component implements checkpointed workflows with retry, idempotency, and recovery.

Design rules:
- deterministic local behavior
- explicit contracts
- bounded state
- explainable decisions
- testable failure paths
