def route(task: str) -> str:
    text = task.lower()
    if any(word in text for word in ("research", "analyze", "compare")):
        return "research-agent"
    if any(word in text for word in ("sales", "lead", "account")):
        return "gtm-agent"
    return "general-agent"
