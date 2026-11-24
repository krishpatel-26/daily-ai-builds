from .linear import solve_linear


def dc_flow(nodes, lines, injections):
    """Lossless DC load flow, single balanced island; values in model power units."""
    ids=sorted(nodes)
    if not ids:
        return {}
    if abs(sum(injections.get(n,0.0) for n in ids))>1e-6:
        raise ValueError('Power injections must balance for an island')
    if len(ids)==1:
        return {}
    idx={name:i for i,name in enumerate(ids)}
    b=[[0.0]*len(ids) for _ in ids]
    for l in lines:
        i,j=idx[l.start],idx[l.end];v=1/l.reactance
        b[i][i]+=v;b[j][j]+=v;b[i][j]-=v;b[j][i]-=v
    # Slack angle at first node is zero; solve remaining N-1 angles.
    theta=[0.0]+solve_linear([row[1:] for row in b[1:]], [injections.get(k,0.0) for k in ids[1:]])
    return {l.id:(theta[idx[l.start]]-theta[idx[l.end]])/l.reactance for l in lines}
