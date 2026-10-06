import hashlib,json,sqlite3
from datetime import datetime,timezone
from .config import settings
from .models import Evidence,IncidentPlan
class AuditStore:
    def __init__(self,path=None):
        self.path=path or settings.audit_db_path
        with sqlite3.connect(self.path) as db:
            db.execute("CREATE TABLE IF NOT EXISTS audit_events(id INTEGER PRIMARY KEY AUTOINCREMENT,incident_id TEXT,event TEXT,actor TEXT,payload TEXT,created_at TEXT)")
    def record(self,incident_id,event,actor,payload):
        with sqlite3.connect(self.path) as db:
            db.execute("INSERT INTO audit_events(incident_id,event,actor,payload,created_at) VALUES(?,?,?,?,?)",(incident_id,event,actor,json.dumps(payload),datetime.now(timezone.utc).isoformat())); db.commit()
    def events(self,incident_id):
        with sqlite3.connect(self.path) as db: rows=db.execute("SELECT event,actor,payload,created_at FROM audit_events WHERE incident_id=? ORDER BY id",(incident_id,)).fetchall()
        return [{"event":e,"actor":a,"payload":json.loads(p),"created_at":t} for e,a,p,t in rows]
def evidence_id(e:Evidence)->str:
    return hashlib.sha256(f"{e.agent}|{e.finding}|{e.confidence}".encode()).hexdigest()[:16]
def apply_governance(plan:IncidentPlan)->IncidentPlan:
    evidence=[e.model_copy(update={"id":evidence_id(e)}) for e in plan.evidence]
    approval=plan.severity in {"critical","high"} or any(e.confidence<settings.min_evidence_confidence for e in evidence)
    actions=[a.model_copy(update={"requires_approval":approval}) for a in plan.actions]
    return plan.model_copy(update={"evidence":evidence,"actions":actions,"approval_required":approval})
