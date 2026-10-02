import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv('APP_ENV', 'development')
    log_level: str = os.getenv('LOG_LEVEL', 'INFO')
    top_k: int = int(os.getenv('KNOWLEDGE_TOP_K', '3'))
    llm_provider: str = os.getenv('LLM_PROVIDER', 'mock')

settings = Settings()
