from app.engine import evaluate
from app.models import Request

def test_engine_returns_explainable_decision():
    result = evaluate(Request("hello"))
    assert result.status == "allowed"
    assert result.reasons

def test_engine_bounds_score():
    result = evaluate(Request("x" * 5000))
    assert 0 <= result.score <= 1
