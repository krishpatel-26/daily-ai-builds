"""Research report rendering and artifact persistence."""
from __future__ import annotations
import json
from pathlib import Path

def render_markdown(result):
    lines = [
        "# AEGIS Research Report", "",
        f"- Dataset SHA-256: `{result['manifest']['dataset_sha256']}`",
        f"- Seed: {result['manifest']['seed']} | K: {result['manifest']['k']}",
        f"- Runtime: {result['manifest']['runtime_seconds']} seconds", "",
        "## Aggregate retrieval quality", "",
        "| Scenario | Method | Precision@K | Recall@K | MRR | nDCG@K |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for scenario, methods in result["results"].items():
        for method, metrics in methods.items():
            vals = [metrics[m]["mean"] for m in ("precision", "recall", "mrr", "ndcg")]
            lines.append(f"| {scenario} | {method} | " + " | ".join(f"{v:.3f}" for v in vals) + " |")
    lines += ["", "## Paired comparison: hybrid vs BM25", "",
              "Positive mean difference favors hybrid. P-values are exploratory and should not be interpreted without considering benchmark design and multiple comparisons.", ""]
    for scenario, metrics in result["comparisons_hybrid_vs_bm25"].items():
        lines.append(f"### {scenario}")
        for metric, test in metrics.items():
            lines.append(f"- {metric}: Δ={test['mean_difference']:.4f}, p={test['p_value']:.4f}")
        lines.append("")
    lines += [
        "## Limitations", "",
        "- Synthetic benchmark with one primary relevant document per query.",
        "- Stress transformations are deterministic proxies, not representative real-world distribution shifts.",
        "- Lexical baselines only; no embeddings, neural reranker, or generative model.",
        "- Bootstrap intervals do not account for benchmark construction bias.",
        "- Paired tests are exploratory; multiple-comparison correction is not applied.",
        "- No claim of production readiness or general superiority is supported by this benchmark.", "",
    ]
    return "\n".join(lines)

def write_artifacts(result, output_dir="artifacts"):
    root = Path(output_dir)
    root.mkdir(parents=True, exist_ok=True)
    (root / "results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (root / "research_report.md").write_text(render_markdown(result), encoding="utf-8")
    return str(root.resolve())
