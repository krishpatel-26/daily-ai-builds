from .astar import astar
def assign(robots,tasks):
 pending=list(tasks);result={r.id:[] for r in robots};positions={r.id:r.position for r in robots}
 while pending:
  options=[]
  for r in robots:
   for task in pending:
    route=astar(positions[r.id],task.goal)
    if route:options.append((len(route),r.id,task.id,task))
  if not options:break
  _,rid,_,task=min(options,key=lambda x:(x[0],x[1],x[2]));result[rid].append(task);positions[rid]=task.goal;pending.remove(task)
 return result,pending
