"""Policy and hazard scenario comparisons."""
from .simulator import Simulator


def compare(limit=200):
    result=[]
    for policy in ('nearest','ordered'):
        for fault in (False,True):
            metrics=Simulator(policy,fault,limit).run()['metrics']
            result.append({'policy':policy,'dynamic_obstacle':fault,**metrics})
    return result
