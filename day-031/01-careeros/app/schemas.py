"""Validated API request and response schemas."""
from typing import Optional
from pydantic import BaseModel, Field

class ProfileInput(BaseModel):
    name: str = Field(default="Your name", max_length=100)
    target_role: str = Field(default="AI Engineer", max_length=120)
    experience_level: str = Field(default="Entry level", max_length=40)
    location: str = Field(default="", max_length=100)
    resume_text: str = Field(default="", max_length=30000)
    skills: list[str] = Field(default_factory=list, max_length=100)

class ResumeInput(BaseModel):
    text: str = Field(min_length=20, max_length=30000)

class AnalyzeInput(BaseModel):
    target_role: Optional[str] = Field(default=None, max_length=120)

class RoadmapUpdate(BaseModel):
    status: str = Field(pattern="^(todo|in_progress|done)$")

class ApplicationInput(BaseModel):
    company: str = Field(min_length=1, max_length=120)
    role: str = Field(min_length=1, max_length=120)
    location: str = Field(default="", max_length=100)
    stage: str = Field(default="Saved", pattern="^(Saved|Applied|Assessment|Interview|Offer|Rejected)$")
    url: str = Field(default="", max_length=500)
    follow_up_date: str = Field(default="", max_length=20)
    notes: str = Field(default="", max_length=2000)

class ApplicationUpdate(BaseModel):
    stage: Optional[str] = Field(default=None, pattern="^(Saved|Applied|Assessment|Interview|Offer|Rejected)$")
    follow_up_date: Optional[str] = Field(default=None, max_length=20)
    notes: Optional[str] = Field(default=None, max_length=2000)
