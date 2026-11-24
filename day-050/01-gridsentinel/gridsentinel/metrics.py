
def compare_strategies(rows):
    baseline=next(x for x in rows if x['strategy']=='baseline')
    return [{**x,'delta_served_percentage_points':round(x['mean_served_pct']-baseline['mean_served_pct'],2),
             'delta_critical_unserved':round(x['mean_critical_unserved']-baseline['mean_critical_unserved'],2)} for x in rows]
