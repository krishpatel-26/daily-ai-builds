from typing import Literal
from pydantic import BaseModel, Field
Severity=Literal['low','medium','high','critical']
class Alert(BaseModel):
    service:str=Field(min_length=1,max_length=100); metric:str=Field(min_length=1,max_length=100); value:float; threshold:float; message:str=Field(min_length=3,max_length=1000)
class IncidentRequest(BaseModel):
    title:str=Field(min_length=3,max_length=200); alerts:list[Alert]=Field(min_length=1,max_length=50); recent_deploy:bool=False
class Evidence(BaseModel):
    id:str|None=None; agent:str; finding:str; confidence:float=Field(ge=0,le=1)
class Action(BaseModel):
    priority:int=Field(ge=1,le=10); action:str; reason:str; requires_approval:bool=True
class IncidentPlan(BaseModel):
    incident_id:str|None=None; title:str; severity:Severity; score:int; evidence:list[Evidence]; actions:list[Action]; rationale:str; approval_required:bool=True; decision:Literal['pending','approved','rejected']='pending'
class ApprovalRequest(BaseModel):
    actor:str=Field(min_length=2,max_length=100); decision:Literal['approved','rejected']; comment:str=Field(default='',max_length=1000)
class AuditResponse(BaseModel):
    incident_id:str; events:list[dict]
