from app.config import LIMITS
from app.features import summarize
def score(rows):
 f=summarize(rows);p={}
 for k,(lo,hi) in LIMITS.items():
  v=f[k]["latest"];p[k]=round(min(1,max(0,(lo-v)/(hi-lo),(v-hi)/(hi-lo))*2.5),4)
 return round(sum(p.values())/len(p),4),p,f