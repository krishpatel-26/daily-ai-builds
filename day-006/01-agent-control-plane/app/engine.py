from .models import AgentDecision, AgentRequest
from .policy import decide
from .routing import route

def evaluate(request: AgentRequest) -> AgentDecision:
    status, approval = decide(request.risk)
    selected = route(request.task) if status != "blocked" else "none"
    reasons = (f"risk={request.risk:.2f}", f"route={selected}")
    return AgentDecision(status, selected, approval, reasons)
