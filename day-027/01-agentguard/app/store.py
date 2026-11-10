import json, sqlite3
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path("agentguard.db")

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect() as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS requests (
          request_id TEXT PRIMARY KEY, created_at TEXT NOT NULL, actor TEXT NOT NULL,
          role TEXT NOT NULL, action TEXT NOT NULL, resource_type TEXT NOT NULL,
          resource_id TEXT NOT NULL, proposal_json TEXT NOT NULL, status TEXT NOT NULL,
          risk TEXT NOT NULL, reasons_json TEXT NOT NULL, requires_approval INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS audit (
          id INTEGER PRIMARY KEY AUTOINCREMENT, request_id TEXT NOT NULL,
          timestamp TEXT NOT NULL, event TEXT NOT NULL, details_json TEXT NOT NULL
        );
        """)
def now():
    return datetime.now(timezone.utc).isoformat()
def record_request(proposal, decision):
    with connect() as db:
        db.execute("INSERT INTO requests VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
          (decision.request_id, now(), proposal.actor, proposal.role, proposal.action,
           proposal.resource_type, proposal.resource_id, proposal.model_dump_json(),
           decision.status, decision.risk.value, json.dumps(decision.reasons),
           int(decision.requires_approval)))
        add_audit(db, decision.request_id, "evaluated", {"status": decision.status, "risk": decision.risk.value})
def add_audit(db, request_id, event, details):
    db.execute("INSERT INTO audit(request_id,timestamp,event,details_json) VALUES (?,?,?,?)",
               (request_id, now(), event, json.dumps(details)))
def list_rows(table, limit=100):
    if table not in {"requests", "audit"}: raise ValueError("Unsupported table")
    with connect() as db:
        return [dict(r) for r in db.execute(f"SELECT * FROM {table} ORDER BY 1 DESC LIMIT ?", (limit,))]
def get_request(request_id):
    with connect() as db:
        row = db.execute("SELECT * FROM requests WHERE request_id=?", (request_id,)).fetchone()
        return dict(row) if row else None
def set_status(request_id, status, reviewer, note):
    with connect() as db:
        row = db.execute("SELECT status FROM requests WHERE request_id=?", (request_id,)).fetchone()
        if not row: return False
        if row["status"] != "pending_approval": raise ValueError("Request is not awaiting approval")
        db.execute("UPDATE requests SET status=? WHERE request_id=?", (status, request_id))
        add_audit(db, request_id, status, {"reviewer": reviewer, "note": note})
        return True
