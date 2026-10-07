def build_sequence(tier: str) -> list[str]:
    return {"hot":["research","personalize","outreach"],"warm":["enrich","personalize","outreach"],"cold":["enrich","nurture"]}.get(tier,["enrich"])
