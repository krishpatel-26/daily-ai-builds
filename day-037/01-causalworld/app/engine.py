from .model import VARIABLES,EQUATIONS,DESCRIPTIONS
from .graph import topological_order,parents
def simulate(interventions=None):
 interventions=interventions or {};unknown=set(interventions)-set(VARIABLES)
 if unknown:raise ValueError("Unknown intervention variables: "+", ".join(sorted(unknown)))
 s=dict(VARIABLES)
 for k,v in interventions.items():s[k]=round(max(0,min(100,float(v))),2)
 for v in topological_order():
  if v not in interventions and v in EQUATIONS:s[v]=round(max(0,min(100,EQUATIONS[v][1](s))),2)
 return s
def compare(interventions):
 base=simulate();alt=simulate(interventions);changes=[]
 for k in VARIABLES:
  d=round(alt[k]-base[k],2)
  if abs(d)>.001:changes.append({"variable":k,"description":DESCRIPTIONS[k],"baseline":base[k],"counterfactual":alt[k],"delta":d,"direction":"increase" if d>0 else "decrease"})
 changes.sort(key=lambda x:abs(x["delta"]),reverse=True)
 return {"baseline":base,"counterfactual":alt,"interventions":interventions,"changes":changes,"changed_count":len(changes)}
def explain(v):
 if v not in VARIABLES:raise ValueError("Unknown variable: "+v)
 paths=[]
 def walk(n,path):
  ps=parents(n)
  if not ps:paths.append(list(reversed(path+[n])))
  else:
   for p in ps:walk(p,path+[n])
 walk(v,[])
 return {"variable":v,"description":DESCRIPTIONS[v],"parents":parents(v),"root_paths":paths}