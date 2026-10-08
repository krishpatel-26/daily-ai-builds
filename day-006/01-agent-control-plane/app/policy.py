REVIEW_THRESHOLD = 0.60
BLOCK_THRESHOLD = 0.90

def decide(risk: float) -> tuple[str, bool]:
    risk = max(0.0, min(1.0, risk))
    if risk >= BLOCK_THRESHOLD:
        return "blocked", True
    if risk >= REVIEW_THRESHOLD:
        return "review", True
    return "allowed", False
