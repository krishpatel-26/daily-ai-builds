from dataclasses import asdict
from .network import demo_network,validate
from .dispatch import evaluate


def run(failed_line=None,strategy='baseline'):
    network=demo_network();validate(network)
    allowed={'baseline','backup','reinforce','combined'}
    if strategy not in allowed:
        raise ValueError('Unknown scenario strategy')
    if failed_line and failed_line not in {l.id for l in network.lines}:
        raise ValueError('Unknown line ID')
    return {
        'network':{'nodes':[asdict(n) for n in network.nodes],'lines':[asdict(l) for l in network.lines]},
        'result':evaluate(network,failed_lines=[failed_line] if failed_line else [],
                          backup=strategy in ('backup','combined'),reinforced=strategy in ('reinforce','combined')),
        'strategy':strategy,
        'assumptions':'Static topology, lossless DC flow, proportional generation dispatch, priority-aware capacity shedding.'
    }


def compare_outages():
    network=demo_network()
    results=[]
    for strategy in ('baseline','backup','reinforce','combined'):
        cases=[evaluate(network,(l.id,),strategy in ('backup','combined'),strategy in ('reinforce','combined')) for l in network.lines]
        results.append({'strategy':strategy,'outages':len(cases),
                        'mean_served_pct':round(sum(x['served_pct'] for x in cases)/len(cases),2),
                        'mean_critical_unserved':round(sum(x['critical_unserved'] for x in cases)/len(cases),2),
                        'overload_scenarios':sum(bool(x['overloaded_lines']) for x in cases),
                        'min_served_pct':min(x['served_pct'] for x in cases)})
    return results
