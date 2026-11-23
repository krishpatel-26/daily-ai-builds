"""Expected-improvement acquisition for maximum quality."""
import math
from .gp import GaussianProcess


def expected_improvement(mean, std, incumbent, exploration=0.35):
    if std <= 1e-12:
        return max(0, mean - incumbent - exploration)
    advantage = mean - incumbent - exploration
    z = advantage / std
    cdf = 0.5 * (1 + math.erf(z / math.sqrt(2)))
    pdf = math.exp(-0.5 * z*z) / math.sqrt(2*math.pi)
    return max(0, advantage * cdf + std * pdf)


def propose(pool, observed):
    if not observed:
        raise ValueError('At least one measurement required')
    known = {c for c, _ in observed}
    options = [c for c in pool if c not in known]
    if not options:
        return None, None
    model = GaussianProcess([c for c,_ in observed], [y for _,y in observed])
    incumbent = max(y for _,y in observed)
    ranked = []
    for c in options:
        mean,std = model.predict(c)
        ranked.append((expected_improvement(mean,std,incumbent),std,-c.temperature,-c.speed,c))
    _,std,_,_,winner = max(ranked)
    mean,_ = model.predict(winner)
    return winner, {'predicted_quality':round(mean,3),'uncertainty':round(std,3),
                    'expected_improvement':round(expected_improvement(mean,std,incumbent),4)}
