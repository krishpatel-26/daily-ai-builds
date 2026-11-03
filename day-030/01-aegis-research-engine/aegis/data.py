"""Deterministic synthetic benchmark and controlled distribution shifts."""
from __future__ import annotations

import hashlib
import random
import re

DOCUMENTS = [
    ("d01", "BM25 ranks documents using term frequency and inverse document frequency with length normalization."),
    ("d02", "TF IDF represents documents as weighted term vectors and compares query similarity using cosine distance."),
    ("d03", "Hybrid retrieval combines lexical ranking signals to balance exact matching and term weighting."),
    ("d04", "Bootstrap confidence intervals estimate uncertainty by repeatedly resampling observations with replacement."),
    ("d05", "Paired randomization tests compare two systems on identical examples to assess metric differences."),
    ("d06", "Mean reciprocal rank rewards systems that place the first relevant result near the top."),
    ("d07", "Normalized discounted cumulative gain evaluates graded relevance while discounting lower ranked results."),
    ("d08", "Recall measures the fraction of all relevant documents recovered within a result set."),
    ("d09", "Precision measures the fraction of retrieved documents that are relevant."),
    ("d10", "Distribution shift occurs when evaluation inputs differ from the data conditions used during development."),
    ("d11", "Typographical noise changes token spelling and can reduce exact lexical matching performance."),
    ("d12", "Ablation studies remove one component at a time to estimate its contribution to system performance."),
    ("d13", "A reproducibility manifest records code version, configuration, random seed, and dataset fingerprint."),
    ("d14", "A benchmark should include representative queries, relevance judgments, and documented limitations."),
    ("d15", "Statistical significance does not automatically imply a practically meaningful improvement."),
    ("d16", "Latency and computational cost are important dimensions alongside retrieval relevance."),
    ("d17", "A reranker can reorder retrieved candidates using a more expressive relevance model."),
    ("d18", "Dense retrieval maps queries and passages into embedding vectors for semantic similarity search."),
    ("d19", "Data leakage occurs when information from evaluation data influences model development."),
    ("d20", "Human relevance judgments provide a reference for evaluating information retrieval systems."),
]

QUERIES = [
    ("q01", "How does BM25 score documents?", ["d01"]),
    ("q02", "Explain TF IDF vector similarity", ["d02"]),
    ("q03", "What is hybrid lexical retrieval?", ["d03"]),
    ("q04", "How do bootstrap confidence intervals work?", ["d04"]),
    ("q05", "How can paired systems be statistically compared?", ["d05"]),
    ("q06", "What does mean reciprocal rank measure?", ["d06"]),
    ("q07", "Explain normalized discounted cumulative gain", ["d07"]),
    ("q08", "How is retrieval recall calculated?", ["d08"]),
    ("q09", "Define precision in search results", ["d09"]),
    ("q10", "What is distribution shift in evaluation?", ["d10"]),
    ("q11", "How do typos affect lexical search?", ["d11"]),
    ("q12", "Why perform ablation studies?", ["d12"]),
    ("q13", "What belongs in a reproducibility manifest?", ["d13"]),
    ("q14", "What makes a useful benchmark?", ["d14"]),
    ("q15", "Difference between statistical and practical significance", ["d15"]),
    ("q16", "Why measure retrieval latency and cost?", ["d16"]),
    ("q17", "What is a retrieval reranker?", ["d17"]),
    ("q18", "How does dense retrieval work?", ["d18"]),
    ("q19", "Explain data leakage in machine learning", ["d19"]),
    ("q20", "Why do search benchmarks need human judgments?", ["d20"]),
]

def fingerprint() -> str:
    payload = repr((DOCUMENTS, QUERIES)).encode()
    return hashlib.sha256(payload).hexdigest()

def _typo(word: str, rng: random.Random) -> str:
    if len(word) < 5 or not word.isalpha():
        return word
    i = rng.randrange(1, len(word) - 1)
    return word[:i] + word[i + 1] + word[i] + word[i + 2:]

def build_scenarios(seed: int = 42):
    rng = random.Random(seed)
    base = [(qid, query, list(rel)) for qid, query, rel in QUERIES]
    typo = []
    for qid, query, rel in base:
        words = query.split()
        candidates = [i for i, w in enumerate(words) if len(w) >= 5]
        if candidates:
            idx = rng.choice(candidates)
            words[idx] = _typo(words[idx], rng)
        typo.append((qid, " ".join(words), rel))
    paraphrase_map = {
        "How does": "In what way does", "Explain": "Describe",
        "What is": "Can you define", "Why": "For what reason",
        "How can": "What method can",
    }
    paraphrase = []
    for qid, query, rel in base:
        altered = query
        for old, new in paraphrase_map.items():
            if altered.startswith(old):
                altered = new + altered[len(old):]
                break
        paraphrase.append((qid, altered, rel))
    distractor_docs = list(DOCUMENTS) + [
        ("x01", "A practical guide to gardening soil, irrigation, and plant growth."),
        ("x02", "A recipe for sourdough bread with flour, water, and fermentation."),
        ("x03", "A travel guide describing train stations and city attractions."),
    ]
    return {
        "clean": (list(DOCUMENTS), base),
        "typo": (list(DOCUMENTS), typo),
        "paraphrase_proxy": (list(DOCUMENTS), paraphrase),
        "distractor_heavy": (distractor_docs, base),
    }
