import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from .models import ActionProposal
from .engine import evaluate
from . import store
from .ui import DASHBOARD

@asynccontextmanager
async def lifespan(app: FastAPI):
    store.init_db()
    yield

app = FastAPI(title="AgentGuard", version="0.1.0", lifespan=lifespan)

@app.get("/", response_class=HTMLResponse)
def home():
    return DASHBOARD

@app.get("/health")
def health():
    return {"status": "ok", "service": "agentguard"}

@app.post("/api/evaluate")
def evaluate_action(proposal: ActionProposal):
    decision = evaluate(proposal)
    store.record_request(proposal, decision)
    return decision

@app.get("/api/requests")
def requests():
    rows = store.list_rows("requests")
    for row in rows:
        row["reasons"] = json.loads(row.pop("reasons_json"))
        row.pop("proposal_json", None)
    return rows

@app.get("/api/approvals")
def approvals():
    return [r for r in requests() if r["status"] == "pending_approval"]

@app.post("/api/approvals/{request_id}")
def approval(request_id: str, body: dict):
    decision = body.get("decision")
    if decision not in {"approved", "rejected"}:
        raise HTTPException(400, "decision must be approved or rejected")
    try:
        changed = store.set_status(request_id, decision, str(body.get("reviewer", "reviewer")),
                                   str(body.get("note", "")))
    except ValueError as exc:
        raise HTTPException(409, str(exc))
    if not changed: raise HTTPException(404, "request not found")
    return {"request_id": request_id, "status": decision}

@app.get("/api/audit")
def audit():
    rows = store.list_rows("audit")
    for row in rows: row["details"] = json.loads(row.pop("details_json"))
    return rows
