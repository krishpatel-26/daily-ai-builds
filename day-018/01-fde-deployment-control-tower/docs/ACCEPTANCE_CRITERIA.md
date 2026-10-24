# Acceptance criteria

- [ ] Workspace starts blank and persists in localStorage.
- [ ] Demo case shows a blocked deployment with three synthetic open blockers.
- [ ] All eight deployment gates render with three checks each.
- [ ] Each check accepts To do, Pass, Fail or N/A and a free-text evidence note.
- [ ] Pass without evidence is counted as an evidence gap.
- [ ] Required failed checks or a critical open blocker yield NO-GO.
- [ ] Closing the last blocker recalculates the risk metrics and records a timeline entry.
- [ ] Blocker owner and severity changes persist after refresh.
- [ ] Timeline updates appear newest first.
- [ ] Handoff and runbook exports include gate states, evidence gaps and blockers.
- [ ] Secret-like patterns are masked in generated reports.
- [ ] A user can clear/restart through New workspace after confirming.
- [ ] Core unit tests cover readiness, blocker lifecycle, normalization and redaction.

Acceptance demonstrates product behavior, not the truth of any customer-provided evidence.