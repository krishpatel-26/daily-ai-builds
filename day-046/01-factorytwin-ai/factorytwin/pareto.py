def pareto_front(candidates):
 return [a for a in candidates if not any((b["mean_cost"]<=a["mean_cost"] and b["mean_completed"]>=a["mean_completed"]) and (b["mean_cost"]<a["mean_cost"] or b["mean_completed"]>a["mean_completed"]) for b in candidates)]
