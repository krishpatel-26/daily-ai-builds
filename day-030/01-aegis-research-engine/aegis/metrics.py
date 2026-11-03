"""Information retrieval metrics with explicit edge-case behavior."""
import math

def precision_at_k(ranked, relevant, k=5):
    if k <= 0:
        raise ValueError("k must be positive")
    return sum(d in set(relevant) for d in ranked[:k]) / k

def recall_at_k(ranked, relevant, k=5):
    relevant = set(relevant)
    if k <= 0:
        raise ValueError("k must be positive")
    return sum(d in relevant for d in ranked[:k]) / len(relevant) if relevant else 0.0

def reciprocal_rank(ranked, relevant):
    relevant = set(relevant)
    return next((1.0 / i for i, d in enumerate(ranked, 1) if d in relevant), 0.0)

def ndcg_at_k(ranked, relevant, k=5):
    relevant = set(relevant)
    dcg = sum((1.0 if d in relevant else 0.0) / math.log2(i + 1) for i, d in enumerate(ranked[:k], 1))
    ideal = sum(1.0 / math.log2(i + 1) for i in range(1, min(len(relevant), k) + 1))
    return dcg / ideal if ideal else 0.0

def score_query(ranked, relevant, k=5):
    return {
        "precision": precision_at_k(ranked, relevant, k),
        "recall": recall_at_k(ranked, relevant, k),
        "mrr": reciprocal_rank(ranked, relevant),
        "ndcg": ndcg_at_k(ranked, relevant, k),
    }
