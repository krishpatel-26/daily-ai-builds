"""Simple, inspectable graders for candidate LLM outputs.

These graders measure explicitly configured surface properties. They do not
prove semantic correctness, factual truth, or policy compliance.
"""
from __future__ import annotations

import json
import re
from typing import Any


def _normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def grade_output(output: str, checks: dict[str, Any]) -> list[dict[str, Any]]:
    """Evaluate a string against a mapping of deterministic check definitions.

    Supported checks: contains_all, contains_any, forbid_any, max_bullets,
    valid_json_keys, requires_uncertainty, requires_conflict.
    """
    if not isinstance(output, str):
        output = str(output)
    result: list[dict[str, Any]] = []
    text = _normalized(output)

    def add(name: str, passed: bool, detail: str) -> None:
        result.append({"check": name, "passed": bool(passed), "detail": detail})

    for term in checks.get("contains_all", []):
        ok = _normalized(str(term)) in text
        add("contains_all:" + str(term), ok,
            "Required phrase found." if ok else "Required phrase missing.")
    any_terms = checks.get("contains_any", [])
    if any_terms:
        found = [str(t) for t in any_terms if _normalized(str(t)) in text]
        add("contains_any", bool(found),
            "Matched: " + ", ".join(found) if found else "No accepted phrase found.")
    forbidden = checks.get("forbid_any", [])
    found_forbidden = [str(t) for t in forbidden if _normalized(str(t)) in text]
    if forbidden:
        add("forbid_any", not found_forbidden,
            "Forbidden phrase(s): " + ", ".join(found_forbidden) if found_forbidden
            else "No configured forbidden phrases found.")
    if "max_bullets" in checks:
        bullets = sum(1 for line in output.splitlines()
                      if re.match(r"^\s*(?:[-*•]|\d+[.)])\s+", line))
        limit = int(checks["max_bullets"])
        add("max_bullets", bullets <= limit,
            f"Found {bullets} bullet(s); maximum allowed is {limit}.")
    if "valid_json_keys" in checks:
        try:
            parsed = json.loads(output)
            required = list(checks["valid_json_keys"])
            missing = [key for key in required if key not in parsed]
            ok = isinstance(parsed, dict) and not missing
            add("valid_json_keys", ok,
                "Required keys present." if ok else
                ("Missing keys: " + ", ".join(missing) if isinstance(parsed, dict)
                 else "JSON root must be an object."))
        except (json.JSONDecodeError, TypeError):
            add("valid_json_keys", False, "Output is not valid JSON.")
    if checks.get("requires_uncertainty"):
        phrases = checks.get("uncertainty_phrases", [
            "not provided", "cannot determine", "insufficient information",
            "do not have enough information", "isn't available in the context",
        ])
        found = [p for p in phrases if _normalized(p) in text]
        add("requires_uncertainty", bool(found),
            "Uncertainty phrase detected." if found else
            "No configured uncertainty phrase detected.")
    if checks.get("requires_conflict"):
        phrases = checks.get("conflict_phrases", [
            "conflict", "contradict", "disagree", "cannot determine which",
        ])
        found = [p for p in phrases if _normalized(p) in text]
        add("requires_conflict", bool(found),
            "Conflict acknowledgement detected." if found else
            "No configured conflict acknowledgement detected.")
    if not checks:
        add("manual_review", False, "No deterministic checks configured.")
    return result
