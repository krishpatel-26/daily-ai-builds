# Architecture

Turns agent memories into typed entities and relationships for explainable retrieval.

The core engine is intentionally dependency-light. External providers should be adapters around the deterministic core, never hidden inside business logic.
