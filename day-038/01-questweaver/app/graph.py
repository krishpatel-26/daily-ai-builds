from .templates import TEMPLATES
def quest_graph(t):
 nodes=[o["id"] for o in t["objectives"]]
 edges=[{"from":nodes[i],"to":nodes[i+1]} for i in range(len(nodes)-1)]
 return {"nodes":nodes,"edges":edges}
def topological_order(g):
 deps={n:set() for n in g["nodes"]}
 for e in g["edges"]:
  if e["from"] not in deps or e["to"] not in deps:raise ValueError("Edge references unknown objective")
  deps[e["to"]].add(e["from"])
 order=[]
 while deps:
  ready=sorted(n for n,d in deps.items() if not d)
  if not ready:raise ValueError("Quest objective graph contains a cycle")
  order.extend(ready)
  for n in ready:deps.pop(n)
  for d in deps.values():d.difference_update(ready)
 return order
def catalog():return [{"id":t["id"],"title":t["title"],"theme":t["theme"],"graph":quest_graph(t)} for t in TEMPLATES]