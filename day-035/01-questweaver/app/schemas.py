from typing import Literal,Optional
from pydantic import BaseModel,Field,ConfigDict
class Objective(BaseModel):
 model_config=ConfigDict(extra="forbid")
 objective_id:str
 kind:Literal["visit","collect","talk","defeat","deliver","discover","activate"]
 target_id:str
 description:str=Field(min_length=3,max_length=240)
 required_count:int=Field(default=1,ge=1,le=20)
class QuestProposal(BaseModel):
 model_config=ConfigDict(extra="forbid")
 quest_id:str=Field(min_length=3,max_length=80)
 title:str=Field(min_length=3,max_length=100)
 giver_id:str
 summary:str=Field(min_length=10,max_length=500)
 objectives:list[Objective]=Field(min_length=1,max_length=8)
 prerequisites:list[str]=Field(default_factory=list)
 reward_item:Optional[str]=None
 reward_xp:int=Field(default=0,ge=0,le=10000)
 narrative_reason:str=Field(default="",max_length=500)
class QuestRequest(BaseModel):
 player_id:str="player"
 tone:Literal["mystery","urgent","exploration","social"]="mystery"
 max_results:int=Field(default=3,ge=1,le=10)