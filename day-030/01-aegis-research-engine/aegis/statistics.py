"""Small-sample statistical utilities; no external dependencies."""
import random
import math

def mean(values):
    values = list(values)
    return sum(values) / len(values) if values else 0.0

def bootstrap_ci(values, samples=1000, confidence=0.95, seed=42):
    values = list(values)
    if not values:
        return {"mean": 0.0, "lower": 0.0, "upper": 0.0}
    if samples < 1 or not 0 < confidence < 1:
        raise ValueError("invalid bootstrap configuration")
    rng = random.Random(seed)
    estimates = sorted(mean(rng.choices(values, k=len(values))) for _ in range(samples))
    alpha = (1 - confidence) / 2
    lo = max(0, min(len(estimates)-1, math.floor(alpha * samples)))
    hi = max(0, min(len(estimates)-1, math.ceil((1-alpha) * samples)-1))
    return {"mean": mean(values), "lower": estimates[lo], "upper": estimates[hi]}

def paired_randomization(a, b, samples=5000, seed=42):
    """Two-sided paired sign-flip test on per-query metric differences."""
    if len(a) != len(b) or not a:
        raise ValueError("paired samples must be non-empty and equal length")
    diffs = [x-y for x, y in zip(a, b)]
    observed = abs(mean(diffs))
    rng = random.Random(seed)
    extreme = 0
    for _ in range(samples):
        permuted = [d if rng.random() < 0.5 else -d for d in diffs]
        if abs(mean(permuted)) >= observed - 1e-15:
            extreme += 1
    return {"mean_difference": mean(diffs), "p_value": (extreme + 1) / (samples + 1), "permutations": samples}
