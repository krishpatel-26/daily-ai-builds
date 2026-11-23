"""Hierarchical task decomposition and shortest-route task selection."""
from .world import ZONES
from .pathfinding import astar


def choose_task(state,pending,policy='nearest'):
    if policy not in ('nearest','ordered'):raise ValueError('Unknown planning strategy')
    options=[]
    for task in pending:
        pick=astar(state.position,state.objects[task.item],state.dynamic_obstacles)
        drop=astar(state.objects[task.item],ZONES[task.zone],state.dynamic_obstacles)
        if pick is None or drop is None:continue
        options.append((len(pick)+len(drop),task.id(),task,pick,drop))
    if not options:return None
    if policy=='ordered':
        for task in pending:
            for _,_,candidate,pick,drop in options:
                if candidate==task:return task,pick,drop
    _,_,task,pick,drop=min(options,key=lambda x:(x[0],x[1]))
    return task,pick,drop


def route_to(state,target):
    return astar(state.position,target,state.dynamic_obstacles)
