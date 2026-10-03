from fastapi import FastAPI
from .engine import AutomationEngine
from .models import Event,Rule,RunResult
app=FastAPI(title='Event Driven AI Automation',version='1.0.0'); engine=AutomationEngine()
engine.add_rule(Rule(event_type='lead.created',action='qualify_lead',required_fields=['intent_score'])); engine.add_rule(Rule(event_type='lead.created',action='enrich_account',required_fields=['domain']))
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/rules')
def add_rule(rule:Rule): engine.add_rule(rule); return rule
@app.post('/events',response_model=RunResult)
def event(e:Event): return engine.process(e)
