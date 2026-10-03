from fastapi import FastAPI
from .models import ResearchRequest,ResearchReport
from .orchestrator import ResearchOrchestrator
app=FastAPI(title='Agentic Research Pipeline',version='1.0.0'); engine=ResearchOrchestrator()
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/research',response_model=ResearchReport)
def research(req:ResearchRequest): return engine.run(req)
