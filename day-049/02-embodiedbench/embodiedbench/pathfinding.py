"""A* with an authoritative obstacle map."""
import heapq
from .world import WALLS,valid


def astar(start,goal,obstacles=None):
    blocked = WALLS | (obstacles or set())
    if not valid(start,blocked) or not valid(goal,blocked):return None
    dist=lambda p:abs(p[0]-goal[0])+abs(p[1]-goal[1])
    queue=[(dist(start),0,start)]
    cost={start:0};parent={}
    while queue:
        _,g,here=heapq.heappop(queue)
        if g!=cost.get(here):continue
        if here==goal:
            path=[here]
            while here in parent:
                here=parent[here];path.append(here)
            return path[::-1]
        for new in ((here[0]+1,here[1]),(here[0]-1,here[1]),
                    (here[0],here[1]+1),(here[0],here[1]-1)):
            if not valid(new,blocked):continue
            ng=g+1
            if ng<cost.get(new,10**9):
                parent[new]=here;cost[new]=ng
                heapq.heappush(queue,(ng+dist(new),ng,new))
    return None
