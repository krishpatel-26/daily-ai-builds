from pydantic import BaseModel,Field
from typing import Any
class Event(BaseModel):
 idempotency_key:str=Field(min_length=3,max_length=120); type:str=Field(min_length=3,max_length=100); payload:dict[str,Any]={}
class Rule(BaseModel):
 event_type:str; action:str; required_fields:list[str]=[]; max_attempts:int=Field(default=3,ge=1,le=5)
class RunResult(BaseModel):
 event_id:str; status:str; actions:list[str]; attempts:int; errors:list[str]=[]
