def summarize(result):
 c=result["changes"]
 return {"most_affected":c[:3],"improved":[x for x in c if x["delta"]>0],"declined":[x for x in c if x["delta"]<0],"net_absolute_change":round(sum(abs(x["delta"]) for x in c),2)}