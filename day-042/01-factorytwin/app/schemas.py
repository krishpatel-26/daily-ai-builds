from pydantic import BaseModel,Field
class SensorPoint(BaseModel):
 machine_id:str
 timestamp:int=Field(ge=0)
 temperature:float
 vibration:float=Field(ge=0)
 current:float=Field(ge=0)
 pressure:float=Field(gt=0)
 throughput:float=Field(ge=0)
class WorkOrder(BaseModel):
 machine_id:str
 task:str
 duration_hours:float=Field(gt=0,le=72)
 priority:int=Field(ge=1,le=5)
class ScheduleRequest(BaseModel):
 available_hours:float=Field(default=8,gt=0,le=24)