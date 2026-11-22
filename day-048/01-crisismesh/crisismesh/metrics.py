def evaluate(scenario, result):
    incidents={x['id']:x for x in scenario['incidents']}
    assigned=result['assignments'];served_ids={a['incident_id'] for a in assigned}
    severe=[i for i in scenario['incidents'] if i['severity']>=4]
    served_people=sum(a['persons_capacity'] for a in assigned)
    total_people=sum(i['people'] for i in scenario['incidents'])
    return {'cases_total':len(incidents),'cases_assigned':len(assigned),'high_severity_cases':len(severe), 'high_severity_served':sum(x['id'] in served_ids for x in severe),'people_total':total_people,'response_capacity_people':served_people,'coverage_pct':round(100*len(assigned)/max(1,len(incidents)),1),'high_severity_coverage_pct':round(100*sum(x['id'] in served_ids for x in severe)/max(1,len(severe)),1),'mean_arrival_min':round(sum(x['arrival_min'] for x in assigned)/max(1,len(assigned)),2),'unserved_count':len(result['unserved'])}