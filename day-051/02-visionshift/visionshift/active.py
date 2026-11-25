"""Oracle labeling in synthetic data only; scores on a held-out test set."""
import random

def select(pool,model,budget=50,strategy='uncertainty',seed=51):
    if not 0<=budget<=len(pool):raise ValueError('label budget outside pool bounds')
    if strategy=='random':return random.Random(seed).sample(pool,budget)
    if strategy=='uncertainty':
        return sorted(pool,key=lambda r:(abs(model.predict_proba(r.x)-.5),r.id))[:budget]
    if strategy=='diversity':
        if not budget:return []
        # Greedy farthest-first in standardized synthetic feature space.
        ordered=sorted(pool,key=lambda r:r.id)
        selected=[max(ordered,key=lambda r:(sum(x*x for x in r.x),r.id))]
        candidates=[r for r in ordered if r.id!=selected[0].id]
        while len(selected)<budget:
            def score(row):return min(sum((a-b)**2 for a,b in zip(row.x,chosen.x)) for chosen in selected)
            nxt=max(candidates,key=lambda r:(score(r),r.id));selected.append(nxt);candidates.remove(nxt)
        return selected
    raise ValueError('unknown active learning strategy')
