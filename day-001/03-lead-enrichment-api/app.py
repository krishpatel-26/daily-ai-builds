from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Lead Enrichment API")

class Lead(BaseModel):
    name: str
    email: EmailStr
    company: str
    employees: int
    industry: str

@app.post("/qualify")
def qualify(lead: Lead):
    score = 0
    if lead.employees >= 50:
        score += 30
    if lead.employees >= 200:
        score += 20
    if lead.industry.lower() in {"saas", "fintech", "ai", "software"}:
        score += 30
    if "@" in str(lead.email):
        score += 20

    tier = "high" if score >= 70 else "medium" if score >= 40 else "low"
    action = {
        "high": "Route to sales immediately",
        "medium": "Enroll in personalized nurture",
        "low": "Add to automated education sequence",
    }[tier]

    return {
        "lead": lead.model_dump(),
        "score": score,
        "tier": tier,
        "recommended_next_action": action,
    }
