def apply(action,state):
 a=state["agents"][action["agent_id"]];kind=action["action"];out={"agent":a["id"],"action":kind,"result":"success"}
 if kind=="move":
  a["x"],a["y"]=action["destination"];a["energy"]-=2;out["position"]=[a["x"],a["y"]]
 elif kind=="gather":
  resource=max(state["resources"],key=state["resources"].get)
  if state["resources"][resource]>0:state["resources"][resource]-=1;a["energy"]=max(0,a["energy"]-1);state["scores"][a["team"]]+=1;out["resource"]=resource
  else:out["result"]="no_resource"
 elif kind=="guard":a["energy"]=max(0,a["energy"]-1);out["guarding"]=True
 elif kind=="attack":
  t=state["agents"][action["target"]];t["hp"]=max(0,t["hp"]-3);a["energy"]-=2
  if t["hp"]==0:t["alive"]=False;state["scores"][a["team"]]+=3
  out.update({"target":t["id"],"target_hp":t["hp"]})
 elif kind=="rest":a["energy"]=min(10,a["energy"]+3);a["hp"]=min(10,a["hp"]+1)
 elif kind=="trade":state["resources"]["food"]-=1;state["resources"]["wood"]+=1;out["exchange"]="1 food for 1 wood"
 return out