from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    incident_provider: str = 'local'
    max_evidence: int = 12
    log_level: str = 'INFO'
    model_config = {'env_file': '.env', 'extra': 'ignore'}

settings = Settings()
