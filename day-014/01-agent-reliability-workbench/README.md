# Day 014 — Agent Reliability Workbench

A local-first prototype for evaluating LLM workflow behavior, inspecting per-case traces, comparing prompt instructions, and keeping a repeatable regression dataset.

## Features
- Eight synthetic evaluation cases spanning grounding, uncertainty, formatting, safety, instruction-following, tool failure, conflicting sources, and unsupported commitments.
- Pass/fail/review labels with per-case explanations.
- Run history with timestamps, prompt version, illustrative latency, and approximate token counts.
- Trace inspector showing synthetic pipeline steps.
- Editable test cases and JSON import/export.
- Prompt instruction risk comparison.
- JSON run/trace export and CSV-free browser-only operation.

## Run
Open `index.html` in a modern browser. No build step, server, API key, or external model call is required.

## Important interpretation
This build is a UI and evaluation-workflow prototype. Its demo outcomes and latencies are synthetic; it does not execute an LLM. The prompt comparison checks for certain words and is not a benchmark. To become a real evaluation platform, replace the synthetic runner with a provider adapter, version exact prompts, build a labeled dataset, define per-check graders, add repeatable runs and statistical reporting, and instrument real latency/cost/error traces.

## Limitations
Passing a keyword rule is not equivalent to answer correctness. Human review is needed for ambiguous results. The current in-memory run history resets on refresh and is not sent to a database. No real customer data is included.