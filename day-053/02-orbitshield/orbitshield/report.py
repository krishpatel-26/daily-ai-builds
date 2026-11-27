from .scenarios import make
from .screening import screen
from .maneuvers import compare
from .benchmark import sweep

def build(seed=53,step=20):
    if not 1<=step<=120:raise ValueError('step must be 1..120 seconds')
    s=make(seed)
    return {'project':'OrbitShield','inputs':{'seed':seed,'step_seconds':step,'horizon_seconds':10800,'two_body_planar':True},'primary':{'id':s['primary']['id'],'altitude_km':550},'screening':screen(s,step),'maneuvers':compare(s,step),'benchmark':sweep(),'disclaimer':'Two-body synthetic planar simulation, with no ephemeris or covariance. Not for spacecraft operations.'}
