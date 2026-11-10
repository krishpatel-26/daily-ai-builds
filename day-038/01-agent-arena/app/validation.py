def validate(action,state):
 aid=action["agent_id"]
 if aid not in state["agents"]:return False,"unknown_agent"
 a=state["agents"][aid]
 if not a["alive"]:return False,"agent_eliminated"
 kind=action["action"]
 if kind in ("move","attack") and a["energy"]<2:return False,"insufficient_energy"
 if kind=="attack":
  if action.get("target") not in state["agents"]:return False,"unknown_target"
  t=state["agents"][action["target"]]
  if not t["alive"]:return False,"target_eliminated"
  if t["team"]==a["team"]:return False,"friendly_fire_blocked"
 if kind=="gather" and not any(v>0 for v in state["resources"].values()):return False,"no_resources"
 if kind=="trade" and state["resources"]["food"]<1:return False,"insufficient_trade_stock"
 if kind=="move":
  d=action.get("destination")
  if not d or len(d)!=2 or any(not isinstance(x,int) or x<0 or x>7 for x in d):return False,"invalid_destination"
 return True,"validated"