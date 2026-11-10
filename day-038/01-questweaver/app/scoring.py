def score(t,s):
 checks=[("village_trust","min_trust",1),("faction_tension","max_tension",-1),("player_reputation","min_reputation",1),("resource_supply","min_resources",1)]
 score=float(t["priority"]);reasons=[]
 for field,rule,direction in checks:
  value=getattr(s,field);threshold=t[rule]
  passed=value>=threshold if direction==1 else value<=threshold
  if passed:score+=2;reasons.append(f"{field} {value:g} meets {rule} {threshold}")
  else:score-=3;reasons.append(f"{field} {value:g} does not meet {rule} {threshold}")
 return round(score,2),reasons