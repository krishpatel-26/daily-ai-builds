from datetime import datetime
from pydantic import BaseModel,Field
class Lead(BaseModel):
    id:str=Field(min_length=2,max_length=100); company:str=Field(min_length=1,max_length=200); title:str=Field(min_length=1,max_length=120); employees:int=Field(ge=1,le=10000000)
class Signal(BaseModel): kind:str=Field(min_length=2,max_length=80); strength:float=Field(ge=0,le=1)
class ScoreResult(BaseModel): lead_id:str; score:float; tier:str; recommended_action:str; updated_at:datetime