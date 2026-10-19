"""Command-line interface for the deterministic evaluation harness."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .runner import evaluate_dataset, load_dataset


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run deterministic checks over an LLM evaluation JSONL dataset.")
    parser.add_argument("--dataset", required=True, help="Path to JSON Lines dataset.")
    parser.add_argument("--output", help="Optional path to write a JSON report.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        cases = load_dataset(args.dataset)
        report = evaluate_dataset(cases)
    except (OSError, ValueError) as exc:
        print(f"Evaluation could not run: {exc}", file=sys.stderr)
        return 2
    serialized = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        destination = Path(args.output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(serialized + "\n", encoding="utf-8")
    print(f"Cases: {report['case_count']} | Pass: {report['passed']} | Fail: {report['failed']} | Pass rate: {report['pass_rate']:.1%}")
    if args.output:
        print(f"Report written to {args.output}")
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
