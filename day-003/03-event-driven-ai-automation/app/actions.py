class ActionRegistry:
 def __init__(self): self.actions={'qualify_lead':self.qualify,'create_followup':self.followup,'enrich_account':self.enrich}
 def run(self,name,payload):
  if name not in self.actions: raise ValueError(f'unknown action: {name}')
  return self.actions[name](payload)
 def qualify(self,p): return {'tier':'hot' if p.get('intent_score',0)>=80 else 'warm' if p.get('intent_score',0)>=50 else 'cold'}
 def followup(self,p): return {'task':'follow_up','owner':p.get('owner','unassigned')}
 def enrich(self,p): return {'enriched':True,'domain':p.get('domain','unknown')}
