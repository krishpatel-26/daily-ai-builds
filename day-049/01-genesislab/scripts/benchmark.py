"""Emit a reproducible adaptive-vs-random baseline report."""
import json
from genesislab.benchmark import benchmark
if __name__=='__main__':print(json.dumps(benchmark(range(8),14),indent=2))
