from pydantic import BaseModel, Field
class ApprovalRequest(BaseModel):
    decision: str
    reviewer: str = Field(min_length=1, max_length=80)
    note: str = Field(default="", max_length=500)
