import logging
from fastapi import FastAPI,HTTPException
from .engine import IncidentEngine
from .governance import AuditStore
from .models import ApprovalRequest,AuditResponse,IncidentPlan,IncidentRequest
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')
app=FastAPI(title='Agentic Incident Response Engine',version='1.1.0'); engine=IncidentEngine(); audit=AuditStore()
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/incidents/analyze',response_model=IncidentPlan)
def analyze(req:IncidentRequest):
    plan=engine.analyze(req); audit.record(plan.incident_id,'plan_created','system',plan.model_dump()); return plan
@app.post('/v1/incidents/{incident_id}/approval',response_model=IncidentPlan)
def decide(incident_id:str,request:ApprovalRequest):
    events=audit.events(incident_id)
    if not events: raise HTTPException(404,'incident not found')
    plan=events[0]['payload']
    if plan.get('decision')!='pending': raise HTTPException(409,'incident already decided')
    plan['decision']=request.decision; audit.record(incident_id,'approval_decision',request.actor,{'decision':request.decision,'comment':request.comment})
    return IncidentPlan.model_validate(plan)
@app.get('/v1/incidents/{incident_id}/audit',response_model=AuditResponse)
def audit_log(incident_id:str):
    events=audit.events(incident_id)
    if not events: raise HTTPException(404,'incident not found')
    return AuditResponse(incident_id=incident_id,events=events)
