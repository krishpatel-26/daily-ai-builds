from dataclasses import replace
from .config import Experiment
from .simulator import simulate

def demand_sensitivity(demands=(60,90,120),seed=47):
    data=[]
    for demand in demands:
        exp=replace(Experiment(),demand=demand)
        for policy in ('reactive','periodic','condition_based'):
            r=simulate(policy,seed,exp)
            data.append({'demand':demand,'policy':policy,'units':r['units_produced'],'late_units':r['late_units'],'cost':r['estimated_cost']})
    return data
