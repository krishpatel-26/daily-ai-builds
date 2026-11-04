"""Validated API schemas."""
from typing import Optional
from pydantic import BaseModel, Field

class AssetCreate(BaseModel):
    asset_id:str=Field(min_length=2,max_length=40,pattern=r"^[A-Za-z0-9_-]+$")
    name:str=Field(min_length=2,max_length=100)
    asset_type:str=Field(default="rotating_equipment",max_length=60)
    location:str=Field(default="",max_length=100)
    criticality:str=Field(default="medium",pattern="^(low|medium|high|critical)$")
    temperature_limit:float=Field(default=85,gt=0,le=300)
    vibration_limit:float=Field(default=7.1,gt=0,le=100)
    pressure_min:float=Field(default=1,ge=0,le=10000)
    pressure_max:float=Field(default=10,gt=0,le=10000)

class TelemetryInput(BaseModel):
    timestamp:Optional[str]=Field(default=None,max_length=40)
    temperature:float=Field(ge=-50,le=500)
    vibration:float=Field(ge=0,le=500)
    pressure:float=Field(ge=0,le=50000)
    current:float=Field(ge=0,le=10000)
    rpm:float=Field(ge=0,le=100000)
    runtime_hours:float=Field(ge=0,le=10000000)

class WorkOrderInput(BaseModel):
    asset_id:str=Field(min_length=2,max_length=40)
    title:str=Field(min_length=3,max_length=150)
    priority:str=Field(default="medium",pattern="^(low|medium|high|critical)$")
    assigned_to:str=Field(default="",max_length=100)
    due_date:str=Field(default="",max_length=20)
    notes:str=Field(default="",max_length=2000)

class WorkOrderClose(BaseModel):
    resolution_notes:str=Field(min_length=3,max_length=2000)
