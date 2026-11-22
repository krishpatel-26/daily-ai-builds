from .routing import route

def eligible(team, incident, flood):
    if incident['kind']=='medical' and team['kind'] not in ('ambulance','boat'):return False
    if incident['kind']=='evacuation' and team['kind']=='truck' and flood>1:return False
    return True

def dispatch(scenario, policy='risk_aware'):
    if policy not in ('risk_aware','shortest'):raise ValueError('unsupported dispatch policy')
    jobs=sorted(scenario['incidents'],key=lambda x:(-x['severity'],-x['people'],x['id']))
    available=list(scenario['teams']); assignments=[];unserved=[]
    for incident in jobs:
        candidates=[]
        for team in available:
            flood=scenario['water'][incident['y']][incident['x']]
            if not eligible(team,incident,flood):continue
            option=route(scenario['water'],scenario['base'],(incident['x'],incident['y']),team['max_water'],policy)
            if not option or option['steps']*2>team['range_units']:continue
            travel=option['cost']/team['speed']
            capacity=min(incident['people'],team['capacity'])
            score=travel+3*(incident['people']-capacity)
            candidates.append((score,team['id'],team,option,travel,capacity))
        if not candidates:
            unserved.append({'incident_id':incident['id'],'reason':'no compatible available response team / safe route'});continue
        _,_,team,path,travel,capacity=min(candidates,key=lambda x:(x[0],x[1]))
        assignments.append({'incident_id':incident['id'],'severity':incident['severity'],'kind':incident['kind'],'people':incident['people'],'team_id':team['id'],'arrival_min':round(travel,2),'persons_capacity':capacity,'route':path['path'],'route_cost':path['cost']})
        available.remove(team)
    return {'assignments':assignments,'unserved':unserved, 'available_teams':[x['id'] for x in available]}