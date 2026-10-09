from app.audit import from_decision, serialize
from app.engine import evaluate
from app.models import AgentRequest

def test_audit_event_preserves_policy_decision():
    decision = evaluate(AgentRequest("research competitor landscape", risk=0.7))
    event = from_decision("research competitor landscape", decision)
    payload = serialize(event)
    assert payload["status"] == "review"
    assert payload["requires_approval"] is True
    assert payload["route"] == "research-agent"
    assert payload["event_id"] and payload["timestamp"]
