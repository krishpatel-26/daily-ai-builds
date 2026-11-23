"""Explicit synthetic ground-truth function for algorithm testing."""
import math
import random
from .domain import safe


def true_quality(candidate):
    t, s = candidate.temperature, candidate.speed
    primary = 23 * math.exp(-((t - 202) / 18) ** 2 - ((s - 53) / 16) ** 2)
    secondary = 12 * math.exp(-((t - 177) / 13) ** 2 - ((s - 32) / 11) ** 2)
    baseline = 65 - 0.006 * (t - 195) ** 2 - 0.006 * (s - 52) ** 2
    return round(baseline + primary + secondary, 4)


def measure(candidate, seed):
    if not safe(candidate):
        raise ValueError('Unsafe experiment parameters; experiment not performed')
    # Stable location+seed noise is comparable across optimization strategies.
    rng = random.Random(f'{seed}:{candidate.temperature}:{candidate.speed}')
    value = true_quality(candidate) + rng.gauss(0, 1.15)
    return round(value, 3)
