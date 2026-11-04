# Architecture

Telemetry ingestion → validation → SQLite time-ordered storage → rolling feature extraction → robust anomaly indicators + configured operating limits → explainable health assessment → fleet summary / alerts / work orders / exports.

The prototype uses a deterministic rule-based scoring model. Statistical signals remain visible; no LLM is used to make maintenance decisions.