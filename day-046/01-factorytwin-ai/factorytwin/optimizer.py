from dataclasses import replace
from .simulator import simulate
from .config import Config

def evaluate(config:Config=Config(),seeds=(11,22,33)):
 results=[]
 for policy,scale in [("reactive",1.0)]+[("preventive",x) for x in (.5,.75,1.0,1.25,1.5)]:
  trials=[simulate(replace(config,seed=seed),policy,scale) for seed in seeds]
  results.append({"policy":policy,"interval_scale":scale,"mean_completed":round(sum(x["completed"] for x in trials)/len(trials),2),"mean_cost":round(sum(x["estimated_cost"] for x in trials)/len(trials),2),"mean_downtime":round(sum(x["downtime_minutes"] for x in trials)/len(trials),2)})
 return sorted(results,key=lambda x:(x["mean_cost"],-x["mean_completed"]))
