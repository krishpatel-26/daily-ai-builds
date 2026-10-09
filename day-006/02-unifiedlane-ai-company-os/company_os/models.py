from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class AgentRole(StrEnum):
    RESEARCH = "research"
    STRATEGY = "strategy"
    CONTENT = "content"
    OPERATIONS = "operations"
    OUTREACH = "outreach"
    ANALYTICS = "analytics"


class Action(StrEnum):
    READ_RESEARCH = "read:research"
    READ_ANALYTICS = "read:analytics"
    WRITE_CONTENT = "write:content"
    UPDATE_CRM = "write:crm"
    SEND_OUTREACH = "send:outreach"
    RUN_WORKFLOW = "run:workflow"
    APPROVE_ACTION = "approve:action"


@dataclass(frozen=True)
class Task:
    task_id: str
    goal: str
    role: AgentRole
    action: Action
    risk: str = "low"
    requires_external_side_effect: bool = False
    context: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Decision:
    allowed: bool
    requires_approval: bool
    reason: str
    task_id: str
    role: AgentRole
    action: Action
