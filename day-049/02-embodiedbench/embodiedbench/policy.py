"""Deterministic world-state action gates."""
from .world import valid,WALLS,ZONES


def validate(state, action, target=None):
    if action=='move':
        if target is None or abs(state.position[0]-target[0])+abs(state.position[1]-target[1])!=1:
            return False,'INVALID_STEP'
        if not valid(target,WALLS|state.dynamic_obstacles):return False,'BLOCKED_CELL'
        if state.battery<1:return False,'LOW_BATTERY'
        return True,'VALID'
    if action=='pick':
        if state.carrying:return False,'GRIPPER_OCCUPIED'
        if target not in state.objects:return False,'UNKNOWN_OBJECT'
        if state.objects[target]!=state.position:return False,'OBJECT_NOT_AT_ROBOT'
        return True,'VALID'
    if action=='place':
        if not state.carrying:return False,'NOT_HOLDING'
        if target not in ZONES:return False,'UNKNOWN_ZONE'
        if state.position!=ZONES[target]:return False,'WRONG_DESTINATION'
        return True,'VALID'
    return False,'ACTION_NOT_ALLOWED'
