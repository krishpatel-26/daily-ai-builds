from .world import demo,OBSTACLES,WIDTH,HEIGHT
from .allocator import assign
from .planner import plan_routes,simulate_traffic
def run():
 robots,tasks=demo();assignments,unassigned=assign(robots,tasks);routes=plan_routes(robots,assignments);traffic=simulate_traffic(routes)
 return {"width":WIDTH,"height":HEIGHT,"obstacles":[list(p) for p in sorted(OBSTACLES)],"assignments":{rid:[t.id for t in ts] for rid,ts in assignments.items()},"unassigned":[t.id for t in unassigned],"routes":{rid:[list(p) for p in path] for rid,path in routes.items()},"traffic":traffic,"tasks":len(tasks),"note":"Discrete research simulation; not a complete collision-free MAPF solver."}
