from typing import Literal
from pydantic import BaseModel,Field,ConfigDict
class SocialAction(BaseModel):
 model_config=ConfigDict(extra="forbid")
 actor_id:str;target_id:str;action:Literal["help","gift","keep_promise","lie","betray","threaten","insult","defend"];intensity:int=Field(default=1,ge=1,le=5);context:str=Field(default="",max_length=240)
class RumourInput(BaseModel):
 source_id:str;subject_id:str;claim:str=Field(min_length=5,max_length=240);confidence:float=Field(default=.6,ge=0,le=1);audience:list[str]=Field(default_factory=list)
class TickInput(BaseModel):steps:int=Field(default=1,ge=1,le=10)