from app.planner import build_plan
def test_planner_selects_specialists():
    assert [s.agent for s in build_plan('research competitors and build a lead api').steps]==['research','gtm','api']
def test_default_plan():
    assert build_plan('hello').steps[0].agent=='research'