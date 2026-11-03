"""Transparent lexical retrieval baselines."""
from __future__ import annotations

import math
import re
from collections import Counter

TOKEN_RE = re.compile(r"[a-z0-9]+")

def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())

def _idf(term: str, docs: list[list[str]]) -> float:
    df = sum(term in set(doc) for doc in docs)
    return math.log(1 + (len(docs) - df + 0.5) / (df + 0.5))

def bm25(query: str, documents: list[tuple[str, str]], k: int = 5, k1: float = 1.5, b: float = 0.75):
    token_docs = [tokenize(text) for _, text in documents]
    avg_len = sum(map(len, token_docs)) / max(1, len(token_docs))
    qterms = tokenize(query)
    scored = []
    for (doc_id, _), tokens in zip(documents, token_docs):
        counts = Counter(tokens)
        score = 0.0
        for term in qterms:
            if not counts[term]:
                continue
            idf = _idf(term, token_docs)
            denom = counts[term] + k1 * (1 - b + b * len(tokens) / max(avg_len, 1))
            score += idf * counts[term] * (k1 + 1) / denom
        scored.append((doc_id, score))
    return [doc for doc, _ in sorted(scored, key=lambda x: (-x[1], x[0]))[:k]]

def tfidf(query: str, documents: list[tuple[str, str]], k: int = 5):
    token_docs = [tokenize(text) for _, text in documents]
    vocab = set(tokenize(query))
    for tokens in token_docs:
        vocab.update(tokens)
    n = max(1, len(token_docs))
    idf = {term: math.log(1 + n / (1 + sum(term in set(d) for d in token_docs))) for term in vocab}
    def vector(tokens):
        counts = Counter(tokens)
        return {t: (1 + math.log(c)) * idf[t] for t, c in counts.items() if c and t in idf}
    qv = vector(tokenize(query))
    qnorm = math.sqrt(sum(v*v for v in qv.values())) or 1.0
    scored = []
    for (doc_id, _), tokens in zip(documents, token_docs):
        dv = vector(tokens)
        dnorm = math.sqrt(sum(v*v for v in dv.values())) or 1.0
        score = sum(qv.get(t, 0) * v for t, v in dv.items()) / (qnorm * dnorm)
        scored.append((doc_id, score))
    return [doc for doc, _ in sorted(scored, key=lambda x: (-x[1], x[0]))[:k]]

def retrieve(method: str, query: str, documents: list[tuple[str, str]], k: int = 5, hybrid_weight: float = 0.5):
    if method == "bm25":
        return bm25(query, documents, k)
    if method == "tfidf":
        return tfidf(query, documents, k)
    if method != "hybrid":
        raise ValueError(f"Unknown retrieval method: {method}")
    # Reciprocal-rank fusion avoids mixing incomparable raw score scales.
    left, right = bm25(query, documents, len(documents)), tfidf(query, documents, len(documents))
    scores = {}
    for rank, doc in enumerate(left, 1):
        scores[doc] = scores.get(doc, 0) + hybrid_weight / (60 + rank)
    for rank, doc in enumerate(right, 1):
        scores[doc] = scores.get(doc, 0) + (1 - hybrid_weight) / (60 + rank)
    return [doc for doc, _ in sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:k]]
