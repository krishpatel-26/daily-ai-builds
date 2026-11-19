from .astar import astar

def plan_routes(robots,assignments):
 routes={}
 for r in robots:
  current=r.position;route=[current]
  for task in assignments.get(r.id,[]):
   leg=astar(current,task.goal)
   if not leg:continue
   route.extend(leg[1:]);current=task.goal
  routes[r.id]=route
 return routes

def simulate_traffic(routes,max_ticks=250):
 positions={rid:path[0] for rid,path in routes.items() if path};indexes={rid:0 for rid in positions};frames=[dict(positions)];waits=0
 for tick in range(max_ticks):
  proposed={rid:(routes[rid][min(indexes[rid]+1,len(routes[rid])-1)]) for rid in positions}
  occupied=set(positions.values());next_positions=dict(positions)
  for rid in sorted(positions):
   target=proposed[rid]
   if target==positions[rid]:continue
   if target in next_positions.values() or target in occupied:
    waits+=1;continue
   next_positions[rid]=target;indexes[rid]+=1
  positions=next_positions;frames.append(dict(positions))
  if all(indexes[rid]==len(routes[rid])-1 for rid in positions):break
 return {"ticks":len(frames)-1,"waits":waits,"completed_routes":sum(indexes[rid]==len(routes[rid])-1 for rid in positions),"robots":len(positions),"frames":frames}
