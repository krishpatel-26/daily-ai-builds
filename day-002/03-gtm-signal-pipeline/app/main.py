from datetime import datetime,timezone
from fastapi import FastAPI,HTTPException
from .models import Lead,Signal,ScoreResult
from .scoring import score
from .store import Store
app=FastAPI(title='GTM Signal Pipeline',version='1.0.0'); store=Store()
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/signals',response_model=ScoreResult)
def ingest(lead:Lead,signals:list[Signal]):
    value,tier,action=score(lead,signals); result=ScoreResult(lead_id=lead.id,score=value,tier=tier,recommended_action=action,updated_at=datetime.now(timezone.utc)); store.save(result); return result
@app.get('/v1/leads/{lead_id}',response_model=ScoreResult)
def get_lead(lead_id):
    row=store.get(lead_id)
    if not row: raise HTTPException(404,'lead not found')
    return ScoreResult(lead_id=row[0],score=row[1],tier=row[2],recommended_action=row[3],updated_at=datetime.fromisoformat(row[4]))