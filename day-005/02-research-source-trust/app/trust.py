def trust_score(quality: float, freshness: float, agreement: float) -> float:
    values = [max(0.0, min(1.0, x)) for x in (quality, freshness, agreement)]
    return round(sum(values) / len(values), 3)
