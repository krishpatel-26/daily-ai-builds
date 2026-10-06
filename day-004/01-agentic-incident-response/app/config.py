from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    incident_provider:str='local'
    max_evidence:int=12
    min_evidence_confidence:float=.70
    audit_db_path:str='incident_audit.db'
    log_level:str='INFO'
    model_config={'env_file':'.env','extra':'ignore'}
settings=Settings()
