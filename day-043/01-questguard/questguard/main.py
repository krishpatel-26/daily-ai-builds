from fastapi import FastAPI; from questguard.models import TurnRequest; from questguard.simulator import world,cases; from questguard.guard import inspect; from questguard.executor import execute; from questguard.metrics import summarize; from questguard.audit import AuditLog
app=FastAPI(title="QuestGuard",version="0.1.0"); audit=AuditLog()
@app.get("/api/health")
def health():return {"status":"ok"}
@app.get("/api/demo")
def demo():
 s=world();rows=[inspect(s,p) for p in cases()]
 for r in rows:audit.append(r)
 return {"world":s.model_dump(),"results":rows,"metrics":summarize(rows)}
@app.post("/api/validate")
def validate(req:TurnRequest):
 r=inspect(req.state,req.proposal);audit.append(r);return r
@app.post("/api/execute")
def run(req:TurnRequest):return execute(req.state,req.proposal)
@app.get("/api/audit")
def logs(limit:int=50):return audit.list(limit)