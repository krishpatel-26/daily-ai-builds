from dataclasses import replace
from .graph import components
from .powerflow import dc_flow


def allocate_island(nodes):
    total_gen=sum(x.generation_capacity for x in nodes)
    served={n.id:0.0 for n in nodes}
    remaining=total_gen
    # Explicit protection of critical infrastructure in capacity deficit.
    for n in sorted(nodes,key=lambda n:(-n.criticality,n.id)):
        amount=min(remaining,n.demand)
        served[n.id]=amount
        remaining-=amount
    consumed=sum(served.values())
    generation={n.id:(n.generation_capacity/total_gen*consumed if total_gen else 0.0) for n in nodes}
    return served,generation


def evaluate(network, failed_lines=(), backup=False, reinforced=False):
    active=[]
    for l in network.lines:
        if l.id not in failed_lines:
            active.append(replace(l,limit=l.limit*1.5 if reinforced and l.id in ('L05','L09','L10') else l.limit))
    nodes=list(network.nodes)
    if backup:
        nodes=[replace(n,generation_capacity=n.generation_capacity+(24 if n.id in ('HOSPITAL','WATER') else 0)) for n in nodes]
    lookup={n.id:n for n in nodes}
    served={};generation={};flows={};islands=components(lookup,active)
    for component in islands:
        island_nodes=[lookup[x] for x in component]
        s,g=allocate_island(island_nodes)
        served.update(s);generation.update(g)
        edge=[l for l in active if l.start in component and l.end in component]
        injection={x:g[x]-s[x] for x in component}
        flows.update(dc_flow(component,edge,injection))
    utilization={l.id:round(abs(flows[l.id])/l.limit,4) for l in active}
    overloaded=[name for name,val in utilization.items() if val>1+1e-6]
    total=sum(x.demand for x in nodes)
    unserved={n.id:round(n.demand-served[n.id],4) for n in nodes}
    critical_unserved=round(sum(unserved[n.id] for n in nodes if n.criticality>=4),4)
    return {'failed_lines':list(failed_lines),'backup':backup,'reinforced':reinforced,
            'islands':[list(c) for c in islands], 'served':{k:round(v,4) for k,v in served.items()},
            'generation':{k:round(v,4) for k,v in generation.items()},
            'unserved':unserved,'total_demand':round(total,3),'served_load':round(sum(served.values()),3),
            'served_pct':round(100*sum(served.values())/total,2) if total else 100.0,
            'critical_unserved':critical_unserved,'flows':{k:round(v,3) for k,v in flows.items()},
            'utilization':utilization,'overloaded_lines':overloaded,
            'max_line_utilization':round(max(utilization.values(),default=0),3),
            'warning':'DC approximation; overloaded lines are flagged, not automatically tripped or resolved.'}
