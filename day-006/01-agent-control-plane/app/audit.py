from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from uuid import uuid4

@dataclass(frozen=True)
class DecisionAuditEvent:
    event_id: str
    timestamp: str
    task: str
    status: str
    route: str
    requires_approval: bool
    reasons: tuple[str, ...]

def from_decision(task: str, decision) -> DecisionAuditEvent:
    return DecisionAuditEvent(
        event_id=str(uuid4()),
        timestamp=datetime.now(timezone.utc).isoformat(),
        task=task,
        status=decision.status,
        route=decision.route,
        requires_approval=decision.requires_approval,
        reasons=decision.reasons,
    )

def serialize(event: DecisionAuditEvent) -> dict:
    payload = asdict(event)
    payload["reasons"] = list(event.reasons)
    return payload
