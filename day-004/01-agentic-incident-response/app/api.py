import logging
from fastapi import FastAPI
from .engine import IncidentEngine
from .models import IncidentPlan, IncidentRequest

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
app = FastAPI(title='Agentic Incident Response Engine', version='1.0.0')
engine = IncidentEngine()

@app.get('/health')
def health(): return {'status':'ok'}

@app.post('/v1/incidents/analyze', response_model=IncidentPlan)
def analyze(req: IncidentRequest): return engine.analyze(req)
