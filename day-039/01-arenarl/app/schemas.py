from pydantic import BaseModel,Field,ConfigDict
class TrainRequest(BaseModel):
 model_config=ConfigDict(extra="forbid")
 episodes:int=Field(default=120,ge=1,le=2000)
 seed:int=Field(default=17,ge=0,le=2**31-1)
 alpha:float=Field(default=.18,gt=0,le=1)
 gamma:float=Field(default=.92,ge=0,le=1)
 epsilon:float=Field(default=.25,ge=0,le=1)
class EvalRequest(BaseModel):
 episodes:int=Field(default=40,ge=1,le=500)
 seed:int=Field(default=101,ge=0,le=2**31-1)
 opponent:str=Field(default="heuristic",pattern="^(heuristic|random)$")