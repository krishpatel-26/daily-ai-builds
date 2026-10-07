def choose(candidates: list[dict]) -> dict | None:
    if not candidates:
        return None
    return min(candidates, key=lambda item: (item.get('cost', 0), item.get('latency', 0)))
