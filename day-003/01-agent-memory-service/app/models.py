from datetime import datetime
from pydantic import BaseModel, Field
class MemoryCreate(BaseModel):
    user_id:str=Field(min_length=1,max_length=100)
    agent_id:str=Field(min_length=1,max_length=100)
    content:str=Field(min_length=3,max_length=4000)
    kind:str=Field(default='fact',pattern='^(fact|preference|event|instruction)$')
    importance:float=Field(default=.5,ge=0,le=1)
class Memory(MemoryCreate):
    id:int
    created_at:datetime
