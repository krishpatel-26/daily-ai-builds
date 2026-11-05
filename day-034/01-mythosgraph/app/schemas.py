from typing import Literal,Optional
from pydantic import BaseModel,Field,ConfigDict
class EventInput(BaseModel):
 model_config=ConfigDict(extra="forbid")
 event_id:str=Field(min_length=3,max_length=80)
 event_type:Literal["conversation","combat","quest","discovery","trade","betrayal","gift"]
 actor_id:str
 target_id:Optional[str]=None
 summary:str=Field(min_length=5,max_length=500)
 importance:int=Field(default=5,ge=1,le=10)
 location:Optional[str]=None
 witnesses:list[str]=Field(default_factory=list)
 visibility:Literal["public","witnesses","private"]="witnesses"
class RecallRequest(BaseModel):
 character_id:str
 query:str=Field(min_length=2,max_length=300)
 limit:int=Field(default=8,ge=1,le=30)
class RelationshipInput(BaseModel):
 source_id:str
 target_id:str
 delta:int=Field(ge=-100,le=100)
 reason:str=Field(min_length=3,max_length=240)
class FactInput(BaseModel):
 fact_id:str
 subject:str
 predicate:str
 object:str
 source:str="canon"
 confidence:float=Field(default=1.0,ge=0,le=1)