from dataclasses import dataclass, field

@dataclass(frozen=True)
class AgentRequest:
    task: str
    risk: float = 0.0
    metadata: dict[str, str] = field(default_factory=dict)

@dataclass(frozen=True)
class AgentDecision:
    status: str
    route: str
    requires_approval: bool
    reasons: tuple[str, ...] = ()
