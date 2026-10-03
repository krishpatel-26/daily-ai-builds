import logging
from .guardrails import inspect
from .router import ModelRouter
from .models import CompletionRequest,CompletionResponse
log=logging.getLogger(__name__)
class Gateway:
 def __init__(self,budget=10000): self.router=ModelRouter(); self.budget=budget; self.used=0
 def complete(self,req):
  allowed,_=inspect(req.prompt)
  if not allowed:return CompletionResponse(provider='policy',model='blocked',text='Request blocked by input guardrail.',input_tokens=0,output_tokens=0,estimated_cost=0,blocked=True)
  inp=len(req.prompt.split())
  if self.used+inp+req.max_tokens>self.budget: raise RuntimeError('token budget exceeded')
  p=self.router.route(req.task); text=p.complete(req.prompt,req.max_tokens); out=len(text.split()); self.used+=inp+out; cost=round((inp+out)*0.000001,8); log.info('completion provider=%s input=%d output=%d',p.name,inp,out); return CompletionResponse(provider=p.name,model=p.model,text=text,input_tokens=inp,output_tokens=out,estimated_cost=cost)
