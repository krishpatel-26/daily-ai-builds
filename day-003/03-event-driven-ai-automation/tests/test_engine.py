from app.engine import AutomationEngine
from app.models import Event,Rule
def test_idempotency(tmp_path):
 e=AutomationEngine(str(tmp_path/'a.db')); e.add_rule(Rule(event_type='lead.created',action='qualify_lead',required_fields=['intent_score'])); x=Event(idempotency_key='abc',type='lead.created',payload={'intent_score':90}); first=e.process(x); second=e.process(x); assert first.status=='completed' and second.status=='duplicate' and first.actions==['qualify_lead']
