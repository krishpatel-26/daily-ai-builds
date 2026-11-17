from collections import Counter
def fleet_report(health):
 counts=Counter(x.status for x in health)
 return {"fleet_size":len(health),"status_counts":dict(counts),"average_health":round(sum(x.health_score for x in health)/len(health),1) if health else 0,"inspection_queue":[x.to_dict() for x in sorted(health,key=lambda x:(x.health_score,x.robot_id)) if x.status=="inspect"],"robots":[x.to_dict() for x in health]}
