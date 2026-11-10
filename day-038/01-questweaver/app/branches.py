def choose(t,s):
 routes=[]
 fields={"trust":s.village_trust,"resources":s.resource_supply,"tension":s.faction_tension,"guards":s.guard_readiness,"reputation":s.player_reputation}
 for b in t["branches"]:
  value=fields[b["when"]];ok=value>=b["value"] if b["op"]=="gte" else value<b["value"]
  if ok:routes.append({"route":b["route"],"objective":b["objective"],"condition":f"{b['when']} {b['op']} {b['value']}","observed":value})
 return routes[:1]