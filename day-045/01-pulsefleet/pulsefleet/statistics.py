import math
def median(values):
 data=sorted(float(v) for v in values)
 if not data:return 0.0
 n=len(data);m=n//2
 return data[m] if n%2 else (data[m-1]+data[m])/2
def mad(values):
 if not values:return 0.0
 center=median(values);return median([abs(float(v)-center) for v in values])
def robust_z(value,baseline):
 if len(baseline)<4:return 0.0
 spread=mad(baseline)
 if spread==0:return 0.0 if value==median(baseline) else math.copysign(10.0,value-median(baseline))
 return 0.6745*(value-median(baseline))/spread
