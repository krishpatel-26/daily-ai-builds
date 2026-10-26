# Demo script

## 0:00 — Introduce the problem
“A migration can be green operationally and still lose or alter data. This tool compares the result, not just the job status.”

## 0:30 — Load sample migration
Click Load sample migration. Explain that the source intentionally contains a duplicate key and a record missing from the target; the target also contains a target-only record.

## 1:15 — Review mapping
Show source name mapped to target full_name, and email case folding normalizing one example without rewriting the input.

## 2:00 — Run the comparison
Show coverage, duplicate keys, missing/extra counts and the status field mismatch for C-003.

## 3:00 — Inspect one difference
Explain the key, source/target values and recommended next investigation. Filters help focus by category.

## 4:00 — Export report
Add a reviewer and notes, export the Markdown report, and explain why only mapped fields are in scope.

## 4:45 — Close honestly
“This is a local CSV reconciliation prototype. It never writes to a customer system, and its report is one piece of migration sign-off evidence, not automatic approval.”