# Architecture

Ranks research evidence using source quality, freshness, agreement, and provenance.

The core engine is intentionally dependency-light. External providers should be adapters around the deterministic core, never hidden inside business logic.
