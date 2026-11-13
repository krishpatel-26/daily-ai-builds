from pydantic import BaseModel,Field,ConfigDict
class TrainRequest(BaseModel):
 model_config=ConfigDict(extra="forbid")
 updates:int=Field(80,ge=1,le=1000);seed:int=Field(7,ge=0);learning_rate:float=Field(.0003,gt=0,le=.01);epochs:int=Field(4,ge=1,le=20)
class EvalRequest(BaseModel):episodes:int=Field(30,ge=1,le=500);seed:int=Field(100,ge=0)