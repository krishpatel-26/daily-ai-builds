def score_candidate(validation,base,world):
 if not validation["valid"]:return {"score":0.0,"eligible":False,"reasons":["Validation failed."]}
 reasons=["All targets are registered.","World prerequisites are satisfied."]
 if world["flags"].get("goblin_threat"):reasons.append("Active threat increases relevance.")
 if world["flags"].get("herb_shortage"):reasons.append("Current shortage increases relevance.")
 return {"score":round(min(base,1.0),3),"eligible":True,"reasons":reasons}