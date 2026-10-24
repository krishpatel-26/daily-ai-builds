# Risk model

The dashboard score is a navigation aid, not a statistical estimate.

## Calculation
1. Start with the fraction of required checks marked Pass or N/A, multiplied by 100.
2. Subtract points for open blockers: Critical 18, High 10, Medium 4, Low 1.
3. Clamp the result to 0–100.
4. Count checks marked Pass/Fail without evidence as evidence gaps.

## Decision state
- NO-GO: any critical open blocker or required failed check.
- CONDITIONAL: blockers, evidence gaps or missing project context remain.
- GO-TO-REVIEW: all required checks pass or are N/A, evidence is attached, blockers are closed and key project context is complete.

The “GO-TO-REVIEW” label deliberately does not mean “approved to launch.” Final approval belongs to the designated release owner.