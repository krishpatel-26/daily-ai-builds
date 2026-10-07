from dataclasses import dataclass

@dataclass(frozen=True)
class Checkpoint:
    workflow_id: str
    step: str
    attempt: int
    completed: bool
