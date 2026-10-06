from app.engine import IncidentEngine
from app.models import Alert, IncidentRequest

def test_critical_incident_generates_approved_boundary():
    req = IncidentRequest(title='API outage', recent_deploy=True, alerts=[Alert(service='api',metric='error_rate',value=8,threshold=2,message='5xx spike')])
    plan = IncidentEngine().analyze(req)
    assert plan.severity == 'critical'
    assert plan.actions
    assert all(a.requires_approval for a in plan.actions)

def test_low_signal_stays_low():
    req = IncidentRequest(title='Minor latency', alerts=[Alert(service='worker',metric='latency',value=105,threshold=100,message='small deviation')])
    assert IncidentEngine().analyze(req).severity == 'low'
