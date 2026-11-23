"""Small exact Gaussian-process regressor using Cholesky, no NumPy dependency."""
import math
from .domain import scaled

AMPLITUDE = 16.0
LENGTH_SCALE = 0.29
NOISE_VARIANCE = 1.3**2
PRIOR_MEAN = 67.0


def kernel(a, b):
    x, y = scaled(a), scaled(b)
    squared = sum((p - q)**2 for p, q in zip(x, y))
    return AMPLITUDE**2 * math.exp(-squared / (2 * LENGTH_SCALE**2))


def cholesky(matrix):
    n = len(matrix)
    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            value = matrix[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                if value <= 0:
                    raise ValueError('Covariance matrix not positive definite')
                lower[i][j] = math.sqrt(value)
            else:
                lower[i][j] = value / lower[j][j]
    return lower


def forward(lower, vector):
    x = []
    for i, row in enumerate(lower):
        x.append((vector[i] - sum(row[j] * x[j] for j in range(i))) / row[i])
    return x


def backward(lower, vector):
    n = len(lower)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (vector[i] - sum(lower[j][i] * x[j] for j in range(i + 1, n))) / lower[i][i]
    return x


class GaussianProcess:
    def __init__(self, candidates, observations):
        if len(candidates) != len(observations):
            raise ValueError('Training inputs and measurements differ in length')
        self.points = list(candidates)
        self.values = list(observations)
        self.lower = None
        self.alpha = None
        if candidates:
            matrix = [[kernel(a,b) + (NOISE_VARIANCE+1e-7 if i == j else 0.0)
                       for j,b in enumerate(candidates)] for i,a in enumerate(candidates)]
            self.lower = cholesky(matrix)
            centered = [value - PRIOR_MEAN for value in observations]
            self.alpha = backward(self.lower, forward(self.lower, centered))

    def predict(self, point):
        if not self.points:
            return PRIOR_MEAN, AMPLITUDE
        covariance = [kernel(p, point) for p in self.points]
        mean = PRIOR_MEAN + sum(a * v for a, v in zip(covariance, self.alpha))
        vector = forward(self.lower, covariance)
        variance = max(0.0, kernel(point,point) - sum(v*v for v in vector))
        return mean, math.sqrt(variance)
