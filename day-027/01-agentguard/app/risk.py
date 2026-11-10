from .models import Risk
WEIGHTS = {Risk.LOW: 10, Risk.MEDIUM: 35, Risk.HIGH: 70, Risk.CRITICAL: 100}
def risk_score(risk: Risk) -> int:
    return WEIGHTS[risk]
