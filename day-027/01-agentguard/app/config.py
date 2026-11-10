from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
    service_name: str = "AgentGuard"
    environment: str = "development"
    max_audit_rows: int = 100
settings = Settings()
