import numpy as np
def summarize(history):
 if not history:return {"updates":0}
 recent=history[-min(10,len(history)):]; return {"updates":len(history),"recent_mean_reward":round(float(np.mean([x["episode_reward"] for x in recent])),4),"recent_success_rate":round(float(np.mean([x["success"] for x in recent])),3),"actor_loss":history[-1]["actor_loss"],"critic_loss":history[-1]["critic_loss"],"mean_edges":round(float(np.mean([x["mean_edges"] for x in recent])),3)}