def allowed(tool: str, allowlist: set[str]) -> bool:
    return tool in allowlist
