from .simulator import simulate
from .statistics import summary,paired_delta

DEFAULT_SEEDS=(11,23,37,50,71,89,101,143,181,211)

def compare_policies(seeds=DEFAULT_SEEDS,days=70,disrupted=True):
    seeds=tuple(seeds)
    if not seeds:raise ValueError('At least one seed needed')
    samples={p:[simulate(p,seed,days,disrupted)['metrics'] for seed in seeds] for p in ('lean','diversified','resilient')}
    lean_cost=[x['estimated_cost'] for x in samples['lean']]
    results=[]
    for name,rows in samples.items():
        results.append({'policy':name,'cost':summary([x['estimated_cost'] for x in rows]),
                        'fill_rate':summary([x['fill_rate_pct'] for x in rows]),
                        'lost_sales':summary([x['lost_sales_units'] for x in rows]),
                        'paired_cost_delta_vs_lean':paired_delta([x['estimated_cost'] for x in rows],lean_cost)})
    return results

def pareto(results):
    # Simultaneously minimize cost and maximize fill rate.
    return [a['policy'] for a in results if not any(b['policy']!=a['policy'] and b['cost']['mean']<=a['cost']['mean'] and b['fill_rate']['mean']>=a['fill_rate']['mean'] and (b['cost']['mean']<a['cost']['mean'] or b['fill_rate']['mean']>a['fill_rate']['mean']) for b in results)]
