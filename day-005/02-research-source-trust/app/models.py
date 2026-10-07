from dataclasses import dataclass, field

@dataclass(frozen=True)
class Request:
    value: str
    metadata: dict[str, str] = field(default_factory=dict)

@dataclass(frozen=True)
class Decision:
    status: str
    score: float
    reasons: tuple[str, ...] = ()
