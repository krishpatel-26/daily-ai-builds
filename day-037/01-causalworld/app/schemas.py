from pydantic import BaseModel,Field,ConfigDict
class Intervention(BaseModel):
 model_config=ConfigDict(extra="forbid")
 variable:str=Field(min_length=1,max_length=64)
 value:float=Field(ge=0,le=100)
class ScenarioRequest(BaseModel):
 model_config=ConfigDict(extra="forbid")
 name:str=Field(default="What if?",max_length=80)
 interventions:list[Intervention]=Field(min_length=1,max_length=8)
class CompareRequest(BaseModel):scenarios:list[ScenarioRequest]=Field(min_length=1,max_length=8)