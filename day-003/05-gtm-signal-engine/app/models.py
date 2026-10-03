from datetime import datetime
from pydantic import BaseModel,Field
class Activity(BaseModel):
 account_id:str=Field(min_length=1,max_length=100)
 event:str=Field(min_length=2,max_length=100)
 weight:float=Field(default=1,ge=0,le=10)
 occurred_at:datetime
class Signal(BaseModel):
 account_id:str
 score:float
 reasons:list[str]
 recommended_action:str
class ScoreRequest(BaseModel):
 activities:list[Activity]=Field(min_length=1,max_length=200)
