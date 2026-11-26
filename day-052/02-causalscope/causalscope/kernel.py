"""Known synthetic temporal response kernel used for simulation and matching."""
import math

def shape(delta):
    if delta<0:return 0.0
    return (1-math.exp(-delta/2.2))*math.exp(-max(0,delta-10)/28)

def effect(distance,t,start,lag=2,attenuation=.72):
    if distance<0:raise ValueError('negative distance')
    return (attenuation**distance)*shape(t-start-distance*lag)
