from .scenarios import make
from .screening import screen

def sweep(seeds=range(50,60),step=30):
    rows=[]
    for seed in seeds:
        s=make(seed);out=screen(s,step=step)
        rows.append({'seed':seed,'nearest':out[0]['object_id'],'nearest_km':out[0]['min_separation_km'],'flags':sum(r['illustrative_flag'] for r in out)})
    return {'cases':len(rows),'flagged_scenarios':sum(r['flags']>0 for r in rows),'near_object_counts':{name:sum(r['nearest']==name for r in rows) for name in sorted({r['nearest'] for r in rows})},'rows':rows}
