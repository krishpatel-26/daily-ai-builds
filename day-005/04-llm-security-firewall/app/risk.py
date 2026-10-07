def risk_score(text: str) -> float:
    markers = ("ignore previous", "system prompt", "exfiltrate")
    hits = sum(m in text.lower() for m in markers)
    return min(1.0, hits / len(markers))
