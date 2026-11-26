"""Directed dependency links point from a cause service to its consumers."""
from collections import deque
SERVICES=('database','cache','queue','identity','checkout','catalog','gateway','frontend')
EDGES=(('database','identity'),('database','checkout'),('cache','catalog'),('queue','checkout'),('identity','gateway'),('checkout','gateway'),('catalog','gateway'),('gateway','frontend'))
LAYOUT={'database':(.08,.22),'cache':(.08,.52),'queue':(.08,.82),'identity':(.40,.14),'checkout':(.40,.52),'catalog':(.40,.86),'gateway':(.72,.50),'frontend':(.94,.50)}

def downstream_hops(root):
    if root not in SERVICES:raise ValueError('Unknown root service')
    dist={root:0};queue=deque([root])
    while queue:
        u=queue.popleft()
        for a,b in EDGES:
            if a==u and b not in dist:dist[b]=dist[u]+1;queue.append(b)
    return dist

def topology():
    return {'services':[{'id':s,'x':LAYOUT[s][0],'y':LAYOUT[s][1]} for s in SERVICES],
            'dependencies':[{'upstream':a,'downstream':b} for a,b in EDGES],
            'note':'Synthetic dependency model; an arrow means an upstream failure can propagate downstream.'}
