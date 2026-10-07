from .models import Decision, Request
from .policy import classify

def evaluate(request: Request) -> Decision:
    score = min(1.0, len(request.value) / 1000)
    status = classify(score)
    return Decision(status=status, score=round(score, 3), reasons=(f"input_length={len(request.value)}",))
