"""Dataset loading and evaluation report creation."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .graders import grade_output


def load_dataset(path: str | Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    seen: set[str] = set()
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                case = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}: {exc.msg}") from exc
            for field in ("id", "input", "output", "checks"):
                if field not in case:
                    raise ValueError(f"Line {line_number} is missing required field: {field}")
            case_id = str(case["id"])
            if case_id in seen:
                raise ValueError(f"Duplicate case id on line {line_number}: {case_id}")
            if not isinstance(case["checks"], dict):
                raise ValueError(f"Checks must be an object on line {line_number}")
            seen.add(case_id)
            cases.append(case)
    return cases


def evaluate_dataset(cases: list[dict[str, Any]]) -> dict[str, Any]:
    results = []
    for case in cases:
        checks = grade_output(str(case["output"]), case["checks"])
        failed = [check for check in checks if not check["passed"]]
        results.append({
            "id": str(case["id"]),
            "category": case.get("category", "Uncategorized"),
            "severity": case.get("severity", "medium"),
            "status": "pass" if checks and not failed else "fail",
            "input": case["input"],
            "output": case["output"],
            "checks": checks,
            "failed_checks": len(failed),
        })
    total = len(results)
    passed = sum(row["status"] == "pass" for row in results)
    failed = total - passed
    categories: dict[str, dict[str, int]] = {}
    for row in results:
        cat = str(row["category"])
        counts = categories.setdefault(cat, {"total": 0, "pass": 0, "fail": 0})
        counts["total"] += 1
        counts[row["status"]] += 1
    return {
        "schema_version": "1.0",
        "case_count": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": round(passed / total, 4) if total else 0.0,
        "category_summary": categories,
        "results": results,
        "limitations": [
            "These are deterministic surface checks, not a semantic truth detector.",
            "A pass means only that the configured checks passed.",
            "Review dataset quality and grader false positives/negatives before release.",
        ],
    }
