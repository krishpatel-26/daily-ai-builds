from .topology import downstream_hops
from .signals import aggregate

def evidence_trace(timeline,root):
    hops=downstream_hops(root);sig=aggregate(timeline)
    out=[]
    for service,distance in sorted(hops.items(),key=lambda x:(x[1],x[0])):
        peaks=sorted(enumerate(sig[service]),key=lambda x:-x[1])
        tick,val=peaks[0]
        out.append({'service':service,'graph_hops':distance,'strongest_signal_tick':tick,
                    'peak_combined_z':round(val,2),'interpretation':'Correlated synthetic downstream signal; not causal proof'})
    return out
