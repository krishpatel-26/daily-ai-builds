# Architecture

Telemetry flows through validation and grouping, then robust/rule-based detection. Findings feed a heuristic health index and inspection queue. A standard-library HTTP server exposes read-only JSON and a static dashboard. Synthetic data is deterministic for repeatable demos.
