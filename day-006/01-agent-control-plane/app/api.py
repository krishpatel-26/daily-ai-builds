from .engine import evaluate
from .models import AgentRequest

def handle(task: str, risk: float = 0.0, metadata: dict[str, str] | None = None):
    return evaluate(AgentRequest(task=task, risk=risk, metadata=metadata or {}))
