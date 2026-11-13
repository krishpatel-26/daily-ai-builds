def summary(h):
 if not h:return {"updates":0}
 x=h[-min(10,len(h)):];return {"updates":len(h),"recent_reward":round(sum(a["mean_reward"] for a in x)/len(x),4),"actor_loss":h[-1]["actor_loss"],"critic_loss":h[-1]["critic_loss"]}