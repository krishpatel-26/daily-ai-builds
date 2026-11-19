import heapq
from .world import neighbors,valid
def distance(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
def astar(start,goal):
 if not valid(start) or not valid(goal):return []
 heap=[(distance(start,goal),0,start)];cost={start:0};prev={}
 while heap:
  _,g,p=heapq.heappop(heap)
  if g!=cost.get(p):continue
  if p==goal:
   path=[p]
   while p in prev:p=prev[p];path.append(p)
   return path[::-1]
  for q in neighbors(p):
   ng=g+1
   if ng<cost.get(q,10**9):cost[q]=ng;prev[q]=p;heapq.heappush(heap,(ng+distance(q,goal),ng,q))
 return []
