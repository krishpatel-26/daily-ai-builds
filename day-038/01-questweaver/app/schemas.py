from pydantic import BaseModel,Field,ConfigDict
class WorldState(BaseModel):
 model_config=ConfigDict(extra="forbid")
 player_reputation:float=Field(default=50,ge=0,le=100)
 village_trust:float=Field(default=50,ge=0,le=100)
 faction_tension:float=Field(default=20,ge=0,le=100)
 resource_supply:float=Field(default=70,ge=0,le=100)
 guard_readiness:float=Field(default=55,ge=0,le=100)
 npc_support:float=Field(default=45,ge=0,le=100)
 quest_access:float=Field(default=50,ge=0,le=100)
 regional_stability:float=Field(default=60,ge=0,le=100)
class PlanRequest(BaseModel):
 model_config=ConfigDict(extra="forbid")
 state:WorldState
 completed_quests:list[str]=Field(default_factory=list,max_length=100)
 limit:int=Field(default=5,ge=1,le=10)
class ValidateRequest(BaseModel):quest_id:str;completed_objectives:list[str]=Field(default_factory=list)