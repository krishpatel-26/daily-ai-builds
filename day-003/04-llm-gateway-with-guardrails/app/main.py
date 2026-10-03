from fastapi import FastAPI,HTTPException
from .models import CompletionRequest,CompletionResponse
from .service import Gateway
app=FastAPI(title='LLM Gateway',version='1.0.0'); gateway=Gateway()
@app.get('/health')
def health(): return {'status':'ok','budget_remaining':gateway.budget-gateway.used}
@app.post('/v1/completions',response_model=CompletionResponse)
def completion(req:CompletionRequest):
 try:return gateway.complete(req)
 except RuntimeError as exc: raise HTTPException(429,str(exc)) from exc
