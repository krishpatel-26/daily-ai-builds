from pydantic import BaseModel, Field
from typing import Literal

class WorkflowRequest(BaseModel):
    request: str = Field(min_length=5, max_length=4000)

class PlanStep(BaseModel):
    id: str
    agent: Literal['research','data','gtm','api']
    objective: str

class WorkflowPlan(BaseModel):
    steps: list[PlanStep]

class StepResult(BaseModel):
    step_id: str
    agent: str
    output: str
    status: Literal['completed','failed']

class WorkflowResult(BaseModel):
    workflow_id: str
    plan: WorkflowPlan
    results: list[StepResult]
    status: Literal['completed','partial']
