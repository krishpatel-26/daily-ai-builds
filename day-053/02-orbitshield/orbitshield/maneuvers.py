from .screening import screen
CANDIDATES=(-2.,-1.,-.5,0.,.5,1.,2.)

def compare(scenario,step=20,horizon=10800):
    candidates=[]
    for delta in CANDIDATES:
        findings=screen(scenario,step,horizon,delta)
        worst=min(f['min_separation_km'] for f in findings)
        # Explicitly illustrative objective: reward worst-case miss distance, small impulse penalty.
        score=worst-.10*abs(delta)
        candidates.append({'delta_v_m_s':delta,'worst_miss_km':worst,'flagged_objects':sum(f['illustrative_flag'] for f in findings),'synthetic_score':round(score,4)})
    return {'scenarios':candidates,'highest_simulated_score':max(candidates,key=lambda r:(r['synthetic_score'],-abs(r['delta_v_m_s']))) ,'warning':'Maneuver candidates are educational, not flight recommendations.'}
