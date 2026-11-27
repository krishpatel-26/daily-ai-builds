from .propagate import propagate,closest
from .dynamics import impulse_prograde

def screen(scenario,step=20,horizon=10800,delta_v_m_s=0.):
    p=propagate(impulse_prograde(scenario['primary']['state'],delta_v_m_s),step,horizon)
    rows=[]
    for obj in scenario['objects']:
        trajectory=propagate(obj['state'],step,horizon)
        row={'object_id':obj['id'],'orbit_class':obj['class'],**closest(p,trajectory)}
        rows.append(row)
    return sorted(rows,key=lambda x:(x['min_separation_km'],x['object_id']))
