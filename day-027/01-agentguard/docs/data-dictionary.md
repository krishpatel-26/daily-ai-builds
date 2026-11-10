# Data dictionary

- request_id: unique identifier for the evaluated proposal.
- actor: caller-supplied agent identity string (untrusted in this demo).
- role: caller-supplied role label (must be replaced by trusted identity claims).
- action: requested operation.
- resource_type/resource_id: target object descriptor.
- status: allowed, denied, pending_approval, approved, or rejected.
- risk: policy-assigned risk tier.
- reasons: human-readable explanation for the decision.
- audit: append-only by application convention, not tamper-proof storage.
