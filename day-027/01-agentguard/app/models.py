from enum import Enum
from typing import Any
from pydantic import BaseModel, Field

class Risk(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ActionProposal(BaseModel):
    actor: str = Field(min_length=1, max_length=80)
    role: str = Field(min_length=1, max_length=40)
    action: str = Field(min_length=1, max_length=80)
    resource_type: str = Field(min_length=1, max_length=60)
    resource_id: str = Field(min_length=1, max_length=120)
    payload: dict[str, Any] = Field(default_factory=dict)
    current_state: dict[str, Any] = Field(default_factory=dict)
    expected_state: dict[str, Any] = Field(default_factory=dict)
    idempotency_key: str | None = Field(default=None, max_length=120)

class Decision(BaseModel):
    request_id: str
    status: str
    risk: Risk
    reasons: list[str]
    requires_approval: bool
