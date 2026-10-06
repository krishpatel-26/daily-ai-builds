from app.engine import IncidentEngine
from app.governance import AuditStore, evidence_id
from app.models import Alert, IncidentRequest

def test_critical_plan_requires_approval_and_has_lineage():
    req=IncidentRequest(title='Payments outage',recent_deploy=True,alerts=[Alert(service='payments',metric='error_rate',value=8,threshold=2,message='5xx spike')])
    plan=IncidentEngine().analyze(req)
    assert plan.approval_required is True
    assert plan.evidence[0].id == evidence_id(plan.evidence[0])
    assert all(a.requires_approval for a in plan.actions)

def test_audit_store_round_trip(tmp_path):
    store=AuditStore(str(tmp_path/'audit.db'))
    store.record('inc-1','plan_created','system',{'score':87})
    assert store.events('inc-1')[0]['payload']['score']==87
