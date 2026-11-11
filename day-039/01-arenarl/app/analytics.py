def summarize(history):
 if not history:return {"episodes":0,"blue_win_rate":0,"red_win_rate":0,"draw_rate":0,"rolling_blue_reward":[]}
 n=len(history);wins={k:sum(x["winner"]==k for x in history)/n for k in ("blue","red","draw")};window=max(1,min(20,n//5 or 1));rolling=[]
 for i in range(0,n,window):
  chunk=history[i:i+window];rolling.append({"from":i+1,"to":i+len(chunk),"blue_reward":round(sum(x["blue_reward"] for x in chunk)/len(chunk),3)})
 return {"episodes":n,"blue_win_rate":round(wins["blue"],3),"red_win_rate":round(wins["red"],3),"draw_rate":round(wins["draw"],3),"rolling_blue_reward":rolling,"last_episode":history[-1]}