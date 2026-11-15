import numpy as np
FIELDS=["temperature","vibration","current","pressure","throughput"]
def summarize(rows):
 o={}
 for k in FIELDS:
  a=np.array([getattr(x,k) for x in rows],float);o[k]={"mean":round(float(a.mean()),3),"std":round(float(a.std()),3),"min":round(float(a.min()),3),"max":round(float(a.max()),3),"latest":round(float(a[-1]),3),"slope":round(float(np.polyfit(np.arange(len(a)),a,1)[0]),5)}
 return o