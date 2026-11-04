# Industrial Connector Roadmap

Potential read-only ingestion adapters:
- MQTT broker subscription with topic allowlists and QoS configuration.
- OPC UA client with certificate validation and explicit node mapping.
- CSV batch import with schema validation and timestamp normalization.
- Edge gateway spool-and-forward with backpressure and idempotency keys.

Any live connector requires network segmentation, credential management, monitoring, data provenance, and a separate industrial cybersecurity assessment. Never implement write/actuation controls in this prototype.