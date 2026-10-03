from fastapi import FastAPI
from .models import WorkflowRequest,WorkflowResult
from .runtime import execute
app=FastAPI(title='Agent Workflow Orchestrator',version='1.0.0')
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/workflows',response_model=WorkflowResult)
def create_workflow(request:WorkflowRequest): return execute(request)
