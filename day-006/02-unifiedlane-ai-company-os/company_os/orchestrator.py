from dataclasses import dataclass
from typing import Any

from .audit import event_from_decision
from .models import AgentRole, Task
from .policy import authorize


KEYWORD_ROUTES: tuple[tuple[tuple[str, ...], AgentRole], ...] = (
    (("competitor", "market", "research", "source"), AgentRole.RESEARCH),
    (("strategy", "prioritize", "roadmap", "plan"), AgentRole.STRATEGY),
    (("post", "content", "copy", "campaign draft"), AgentRole.CONTENT),
    (("crm", "workflow", "schedule", "operation"), AgentRole.OPERATIONS),
    (("lead", "outreach", "prospect", "email"), AgentRole.OUTREACH),
    (("metric", "analytics", "performance", "report"), AgentRole.ANALYTICS),
)


def route_goal(goal: str) -> AgentRole:
    text = goal.casefold()
    for keywords, role in KEYWORD_ROUTES:
        if any(keyword in text for keyword in keywords):
            return role
    return AgentRole.STRATEGY


@dataclass
class Orchestrator:
    audit_events: list[dict[str, Any]]

    def __init__(self) -> None:
        self.audit_events = []

    def evaluate(self, task: Task) -> dict[str, Any]:
        decision = authorize(task)
        event = event_from_decision(decision)
        self.audit_events.append(event)

        if not decision.allowed:
            status = "denied"
        elif decision.requires_approval:
            status = "pending_approval"
        else:
            status = "ready"

        return {
            "task_id": task.task_id,
            "status": status,
            "agent": task.role.value,
            "action": task.action.value,
            "reason": decision.reason,
            "audit_event_id": event["event_id"],
        }

    def plan(self, goal: str) -> dict[str, str]:
        role = route_goal(goal)
        return {"goal": goal, "assigned_agent": role.value}
