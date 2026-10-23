# Five-minute demo script

## 0:00 — Frame the problem
“An FDE gets logs, config fragments and an unclear customer symptom. The challenge is turning that evidence into the safest next experiment.”

## 0:45 — Load sample evidence
Click Load sample case. Point out the synthetic 401, 429, timeout and missing-field messages, then show the intentionally risky example configuration.

## 1:45 — Explain a finding
Open the highest-severity finding. Show the stable rule ID, redacted evidence and the suggested action. Explain that a 401 and 429 are separate signals and need different fixes.

## 2:45 — Show data hygiene
Review Redaction preview. Explain that patterns mask common secrets but do not guarantee complete anonymization.

## 3:30 — Prepare the handoff
Switch severity filters, then export JSON and a Markdown handoff note. Review the suggested owner and next action.

## 4:30 — Close honestly
“This is a local, rule-based prototype. It does not call the customer API, confirm credentials, or prove production readiness. Its goal is to standardize the first ten minutes of investigation.”