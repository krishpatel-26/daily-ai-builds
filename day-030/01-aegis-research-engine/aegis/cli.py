"""Command-line interface."""
import argparse
import json
from .experiment import run_experiment
from .report import write_artifacts, render_markdown

def main():
    parser = argparse.ArgumentParser(prog="aegis", description="Reproducible AI retrieval research engine")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="run controlled benchmark")
    run.add_argument("--seed", type=int, default=42)
    run.add_argument("--bootstrap", type=int, default=500)
    run.add_argument("--k", type=int, default=5)
    run.add_argument("--hybrid-weight", type=float, default=0.5)
    run.add_argument("--output", default="artifacts")
    args = parser.parse_args()
    if args.bootstrap < 1 or args.k < 1 or not 0 <= args.hybrid_weight <= 1:
        parser.error("bootstrap and k must be positive; hybrid-weight must be in [0, 1]")
    result = run_experiment(args.seed, args.bootstrap, args.k, args.hybrid_weight)
    path = write_artifacts(result, args.output)
    print(render_markdown(result))
    print(f"\nArtifacts written to: {path}")

if __name__ == "__main__":
    main()
