def fixed_time(states,tick,cycle=7):
    return [(tick//cycle)%2]*len(states)

def max_pressure(states,tick):
    actions=[]
    for ns,ew,phase,emergency in states:
        # Coarse state bins, so this is an illustrative queue-pressure policy.
        if emergency: actions.append(emergency-1)
        else: actions.append(0 if ns>ew else 1 if ew>ns else phase)
    return actions

class QPolicy:
    def __init__(self,table=None):self.table=table if table is not None else {}
    def values(self,state):return self.table.get(tuple(state),[0.,0.])
    def act(self,states,tick):
        return [int(self.values(state)[1]>self.values(state)[0]) for state in states]
