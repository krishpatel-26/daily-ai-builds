import time,uuid,logging
from .actions import ActionRegistry
from .models import Event,RunResult
from .store import EventStore
log=logging.getLogger(__name__)
class AutomationEngine:
 def __init__(self,path='automation.db'): self.store=EventStore(path); self.actions=ActionRegistry(); self.rules=[]
 def add_rule(self,rule): self.rules.append(rule)
 def process(self,event):
  eid=str(uuid.uuid4())
  if self.store.seen(event.idempotency_key): return RunResult(event_id=eid,status='duplicate',actions=[],attempts=0)
  self.store.mark(event.idempotency_key,eid); actions=[]; errors=[]; attempts=0
  for rule in [r for r in self.rules if r.event_type==event.type]:
   if any(k not in event.payload for k in rule.required_fields): continue
   for attempt in range(1,rule.max_attempts+1):
    attempts=max(attempts,attempt)
    try:self.actions.run(rule.action,event.payload); self.store.audit(eid,rule.action,'success'); actions.append(rule.action); break
    except Exception as exc: errors.append(f'{rule.action}: {exc}'); self.store.audit(eid,rule.action,'failed',str(exc)); time.sleep(.01*2**(attempt-1))
  log.info('event_processed id=%s actions=%d',eid,len(actions)); return RunResult(event_id=eid,status='completed' if not errors else 'completed_with_errors',actions=actions,attempts=attempts,errors=errors)
