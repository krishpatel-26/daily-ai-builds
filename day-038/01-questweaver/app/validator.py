def validate_template(t):
 errors=[];ids=[o["id"] for o in t.get("objectives",[])]
 if len(ids)!=len(set(ids)):errors.append("Duplicate objective identifiers")
 if not ids:errors.append("Quest must contain objectives")
 for b in t.get("branches",[]):
  if b.get("objective") not in ids:errors.append("Branch references unknown objective")
  if b.get("op") not in ("gte","lt"):errors.append("Unsupported branch operator")
 return not errors,errors
def validate_progress(t,completed):
 valid,errors=validate_template(t)
 known={o["id"] for o in t["objectives"]}
 unknown=set(completed)-known
 if unknown:errors.append("Unknown completed objectives: "+", ".join(sorted(unknown)))
 return {"valid":valid and not unknown,"errors":errors,"completed":sorted(set(completed)&known),"remaining":[o for o in t["objectives"] if o["id"] not in completed]}