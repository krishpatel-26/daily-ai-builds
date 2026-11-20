from .grid import astar, CHARGERS

def nearest_charger(position):
    paths=[astar(position,c) for c in CHARGERS]
    return min((p for p in paths if p),key=len)

def choose_assignment(robot, tasks, tick):
    options=[]
    for t in tasks:
        if t.status != 'queued':
            continue
        path=astar(robot.position,t.goal)
        if not path or robot.battery < len(path)+12:
            continue
        urgency = max(0, tick + len(path) - t.due)
        score = len(path)*2 - t.priority*6 + urgency*2
        options.append((score,t.id,t,path))
    return min(options,key=lambda o:(o[0],o[1]))[2:] if options else None
