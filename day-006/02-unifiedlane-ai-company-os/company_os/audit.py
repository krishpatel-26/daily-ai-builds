from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .models import Decision


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    timestamp: str
    task_id: str
    role: str
    action: str
    allowed: bool
    requires_approval: bool
    reason: str


def event_from_decision(decision: Decision) -> dict[str, Any]:
    event = AuditEvent(
        event_id=str(uuid4()),
        timestamp=datetime.now(timezone.utc).isoformat(),
        task_id=decision.task_id,
        role=decision.role.value,
        action=decision.action.value,
        allowed=decision.allowed,
        requires_approval=decision.requires_approval,
        reason=decision.reason,
    )
    return asdict(event)
