def grounding_ratio(supported: int, total: int) -> float:
    return round(supported / total, 3) if total else 0.0
