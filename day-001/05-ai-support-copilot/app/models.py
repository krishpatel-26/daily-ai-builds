from pydantic import BaseModel, Field

class Ticket(BaseModel):
    customer: str = Field(min_length=1, max_length=200)
    subject: str = Field(min_length=1, max_length=300)
    message: str = Field(min_length=1, max_length=5000)

class CopilotResponse(BaseModel):
    category: str
    confidence: float
    retrieved_articles: list[str]
    suggested_response: str
    should_escalate: bool
    escalation_reason: str | None = None
