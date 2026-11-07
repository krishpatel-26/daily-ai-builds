from .config import MAX_SCORE,MIN_SCORE
AXES=("trust","fear","loyalty","rivalry")
def key(a,b):return a+"->"+b
def ensure(s,a,b):
 k=key(a,b)
 if k not in s["relationships"]:s["relationships"][k]={"source":a,"target":b,**{x:0 for x in AXES}}
 return s["relationships"][k]
def clamp(v):return max(MIN_SCORE,min(MAX_SCORE,int(v)))
def apply_delta(s,a,b,d):
 r=ensure(s,a,b)
 for k,v in d.items():
  if k in AXES:r[k]=clamp(r[k]+v)
 return dict(r)
def get(s,a,b):return dict(s["relationships"].get(key(a,b),{"source":a,"target":b,**{x:0 for x in AXES}}))