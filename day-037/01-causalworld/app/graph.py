from .model import VARIABLES,EQUATIONS
def parents(v):return EQUATIONS.get(v,("",None))[0].split()
def graph():return {v:parents(v) for v in VARIABLES}
def topological_order():
 deps={v:set(parents(v)) for v in VARIABLES};order=[]
 while deps:
  ready=sorted(v for v,d in deps.items() if not d)
  if not ready:raise ValueError("Causal graph contains a cycle")
  order.extend(ready)
  for v in ready:deps.pop(v)
  for d in deps.values():d.difference_update(ready)
 return order
def validate_graph():
 for v,ps in graph().items():
  if set(ps)-set(VARIABLES):raise ValueError("Unknown causal parent")
 return {"acyclic":True,"variables":len(VARIABLES),"edges":sum(map(len,graph().values())),"order":topological_order()}