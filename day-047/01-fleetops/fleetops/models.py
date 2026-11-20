from dataclasses import dataclass, field

@dataclass
class Robot:
    id: str
    position: tuple[int, int]
    battery: float = 80.0
    status: str = 'idle'
    task_id: str | None = None
    route: list[tuple[int, int]] = field(default_factory=list)
    completed: int = 0
    distance: int = 0
    faults: int = 0
    blocked_steps: int = 0
    fault_until: int = 0

@dataclass
class Task:
    id: str
    goal: tuple[int, int]
    priority: int
    due: int
    status: str = 'queued'
    robot_id: str | None = None
    assigned_at: int | None = None
    completed_at: int | None = None
