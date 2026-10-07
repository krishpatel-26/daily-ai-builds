from .engine import evaluate
from .models import Request

def handle(value: str, metadata: dict[str, str] | None = None):
    return evaluate(Request(value=value, metadata=metadata or {}))
