import math
from .constants import MU,R_EARTH

def circular_state(altitude_km,phase_deg=0.0):
    if not 150<=altitude_km<=2000:raise ValueError('altitude must be 150..2000 km')
    angle=math.radians(phase_deg);radius=R_EARTH+altitude_km;v=math.sqrt(MU/radius)
    return (radius*math.cos(angle),radius*math.sin(angle),-v*math.sin(angle),v*math.cos(angle))

def derivative(s):
    x,y,vx,vy=s;r=math.hypot(x,y)
    if r<=R_EARTH:raise ValueError('invalid/impact state')
    acceleration=-MU/(r*r*r)
    return (vx,vy,acceleration*x,acceleration*y)

def rk4(s,dt):
    if dt<=0 or dt>120:raise ValueError('time step must be >0 and <=120 sec')
    k1=derivative(s)
    k2=derivative(tuple(s[i]+dt*k1[i]/2 for i in range(4)))
    k3=derivative(tuple(s[i]+dt*k2[i]/2 for i in range(4)))
    k4=derivative(tuple(s[i]+dt*k3[i] for i in range(4)))
    return tuple(s[i]+dt*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(4))

def specific_energy(s):
    return (s[2]**2+s[3]**2)/2-MU/math.hypot(s[0],s[1])

def impulse_prograde(s,delta_v_m_s):
    if abs(delta_v_m_s)>2.00001:raise ValueError('illustrative delta-v limited to ±2 m/s')
    speed=math.hypot(s[2],s[3]);d=delta_v_m_s/1000.0
    return (s[0],s[1],s[2]+d*s[2]/speed,s[3]+d*s[3]/speed)
