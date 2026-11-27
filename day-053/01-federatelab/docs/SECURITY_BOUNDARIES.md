# Security boundaries

This simulator is **not** secure federated learning: no authenticated participants, transport encryption, differential privacy, secure multiparty computation, trusted execution environment or private aggregation is implemented. The orchestration process has access to each individual update. It does not prevent membership inference or model inversion. Never upload private real-world training data.
