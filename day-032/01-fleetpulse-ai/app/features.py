"""Rolling telemetry features."""
from statistics import mean,median,pstdev

def _slope(values):
 n=len(values)
 if n<2:return 0.0
 xmean=(n-1)/2; ymean=mean(values)
 denom=sum((i-xmean)**2 for i in range(n)) or 1
 return sum((i-xmean)*(v-ymean) for i,v in enumerate(values))/denom

def rolling_features(rows,window=20):
 sample=rows[-window:]
 fields=("temperature","vibration","pressure","current","rpm")
 output={}
 for field in fields:
  vals=[float(r[field]) for r in sample]
  output[field]={"mean":round(mean(vals),4),"median":round(median(vals),4),"std":round(pstdev(vals),4),"slope":round(_slope(vals),5),"latest":vals[-1]}
 return {"sample_count":len(sample),"metrics":output,"runtime_hours":sample[-1]["runtime_hours"] if sample else 0}
