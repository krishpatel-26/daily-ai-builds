from typing import Literal
from pydantic import BaseModel,Field,ConfigDict
class ActionProposal(BaseModel):
 model_config=ConfigDict(extra="forbid")
 agent_id:str;action:Literal["move","gather","guard","attack","rest","trade"];target:str|None=None;destination:list[int]|None=None;priority:int=Field(default=1,ge=1,le=5)
class TurnRequest(BaseModel):steps:int=Field(default=1,ge=1,le=10)
class PolicyRequest(BaseModel):agent_id:str;policy:Literal["balanced","aggressive","defensive","economist"]