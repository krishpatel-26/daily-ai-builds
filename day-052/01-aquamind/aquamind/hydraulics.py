"""Linear conductive analogy, intentionally not a physical pipe-flow solver."""
from .network import JUNCTIONS, PIPES, SOURCE_PRESSURE, RESERVOIR
from .linear import solve

def model(leak_node=None, leak_rate=0.0, closed_pipes=()):
    nodes={j.id:j for j in JUNCTIONS}
    if leak_node is not None and leak_node not in nodes:raise ValueError('Unknown leak node')
    if leak_rate<0 or leak_rate>20:raise ValueError('Leak rate must be 0..20')
    closed=set(closed_pipes)
    if not closed.issubset({p.id for p in PIPES}):raise ValueError('Unknown pipe ID')
    names=list(nodes)
    at={node:i for i,node in enumerate(names)}
    n=len(names); a=[[0.0]*n for _ in range(n)]
    b=[-nodes[name].demand-(leak_rate if name==leak_node else 0.0) for name in names]
    for p in PIPES:
        if p.id in closed:continue
        g=p.conductance
        if p.a!=RESERVOIR:a[at[p.a]][at[p.a]]+=g
        if p.b!=RESERVOIR:a[at[p.b]][at[p.b]]+=g
        if p.a==RESERVOIR:b[at[p.b]]+=g*SOURCE_PRESSURE
        elif p.b==RESERVOIR:b[at[p.a]]+=g*SOURCE_PRESSURE
        else:
            a[at[p.a]][at[p.b]]-=g
            a[at[p.b]][at[p.a]]-=g
    pressures=dict(zip(names,solve(a,b)))
    pressures[RESERVOIR]=SOURCE_PRESSURE
    flows={p.id:round(p.conductance*(pressures[p.a]-pressures[p.b]),6) if p.id not in closed else 0.0 for p in PIPES}
    return {'pressure':{k:round(v,6) for k,v in pressures.items()},'flow':flows,'source_supply':round(sum(-flows[p.id] if p.b==RESERVOIR else flows[p.id] for p in PIPES if RESERVOIR in (p.a,p.b)),6),
            'total_demand':round(sum(j.demand for j in JUNCTIONS)+leak_rate,6),'leak_node':leak_node,'leak_rate':leak_rate,'closed_pipes':sorted(closed)}

def residual_mass_balance(result):
    return result['source_supply']-result['total_demand']
