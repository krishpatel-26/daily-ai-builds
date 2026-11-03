"""Experiment runner with per-query traces and reproducibility metadata."""
from __future__ import annotations

import platform
import sys
import time
from .data import build_scenarios, fingerprint
from .metrics import score_query
from .retrieval import retrieve
from .statistics import bootstrap_ci, paired_randomization, mean

METHODS = ("bm25", "tfidf", "hybrid")
METRICS = ("precision", "recall", "mrr", "ndcg")

def run_experiment(seed=42, bootstrap_samples=500, k=5, hybrid_weight=0.5):
    started = time.perf_counter()
    scenarios = build_scenarios(seed)
    results, traces = {}, {}
    for scenario, (documents, queries) in scenarios.items():
        results[scenario], traces[scenario] = {}, {}
        for method in METHODS:
            rows = []
            for qid, query, relevant in queries:
                ranking = retrieve(method, query, documents, k, hybrid_weight)
                rows.append({"query_id": qid, **score_query(ranking, relevant, k), "ranking": ranking})
            traces[scenario][method] = rows
            results[scenario][method] = {
                metric: bootstrap_ci([r[metric] for r in rows], bootstrap_samples, seed=seed + i)
                for i, metric in enumerate(METRICS)
            }
    comparisons = {}
    for scenario in scenarios:
        comparisons[scenario] = {}
        for metric in METRICS:
            comparisons[scenario][metric] = paired_randomization(
                [r[metric] for r in traces[scenario]["hybrid"]],
                [r[metric] for r in traces[scenario]["bm25"]],
                samples=max(1000, bootstrap_samples * 4), seed=seed + 99,
            )
    elapsed = time.perf_counter() - started
    return {
        "manifest": {
            "engine": "AEGIS", "version": "0.1.0", "seed": seed, "k": k,
            "hybrid_weight": hybrid_weight, "bootstrap_samples": bootstrap_samples,
            "dataset_sha256": fingerprint(), "python": sys.version.split()[0],
            "platform": platform.platform(), "runtime_seconds": round(elapsed, 6),
        },
        "results": results, "comparisons_hybrid_vs_bm25": comparisons,
        "traces": traces,
    }
