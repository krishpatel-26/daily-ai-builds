from app.engine import evaluate
from app.models import AgentRequest

def test_low_risk_routes_without_approval():
    result = evaluate(AgentRequest("research competitors", risk=0.2))
    assert result.status == "allowed"
    assert result.route == "research-agent"
    assert not result.requires_approval

def test_medium_risk_requires_approval():
    result = evaluate(AgentRequest("send account outreach", risk=0.7))
    assert result.status == "review"
    assert result.requires_approval

def test_high_risk_is_blocked():
    result = evaluate(AgentRequest("execute destructive action", risk=0.95))
    assert result.status == "blocked"
    assert result.route == "none"
