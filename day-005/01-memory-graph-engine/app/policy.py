BLOCK_THRESHOLD = 0.90
REVIEW_THRESHOLD = 0.60

def classify(score: float) -> str:
    if score >= BLOCK_THRESHOLD:
        return "blocked"
    if score >= REVIEW_THRESHOLD:
        return "review"
    return "allowed"
