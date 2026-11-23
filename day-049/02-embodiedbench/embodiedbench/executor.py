"""Authoritative, validated state transitions."""
from .policy import validate


def execute(state,action,target=None):
    allowed,code=validate(state,action,target)
    if not allowed:return {'ok':False,'code':code}
    if action=='move':
        state.position=target;state.battery-=1
    elif action=='pick':
        state.carrying=target
    elif action=='place':
        state.completed.append(state.carrying)
        del state.objects[state.carrying]
        state.carrying=None
    return {'ok':True,'code':'EXECUTED'}
