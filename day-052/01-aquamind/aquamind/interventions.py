from .hydraulics import model

def compare_pipe_isolation(leak_node='J-07',leak_rate=4.5):
    initial=model(leak_node,leak_rate)
    from .network import PIPES
    scenarios=[]
    for pipe in PIPES:
        try:
            result=model(leak_node,leak_rate,closed_pipes=(pipe.id,))
        except ValueError:
            scenarios.append({'pipe':pipe.id,'feasible':False,'reason':'network disconnected'});continue
        worst=min(v for k,v in result['pressure'].items() if k!='SOURCE')
        scenarios.append({'pipe':pipe.id,'feasible':True,'minimum_pressure':round(worst,2),
                          'source_supply':result['source_supply'],
                          'pressure_change_min':round(worst-min(v for k,v in initial['pressure'].items() if k!='SOURCE'),2)})
    return sorted(scenarios,key=lambda r:(not r['feasible'],-r.get('minimum_pressure',-100)))
