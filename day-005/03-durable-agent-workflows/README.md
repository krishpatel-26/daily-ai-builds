# Durable Agent Workflow Engine

Adds checkpointed workflow execution with retry, idempotency, and recovery semantics.

## Architecture
request → validation → deterministic policy → core engine → decision → audit

## Design goals
- Explicit contracts
- Deterministic local fallback
- Testable components
- Bounded state
- Explainable decisions

## Status
Day 005 — foundational implementation.
