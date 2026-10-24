# Release checklist

- [ ] Node.js 18+ works on target developer machines.
- [ ] npm run check completes with no syntax errors.
- [ ] npm test passes all core unit tests.
- [ ] Sample workspace loads and demonstrates a NO-GO state for unresolved critical failures.
- [ ] Saving a gate persists check status and evidence notes.
- [ ] Pass/fail checks without evidence show evidence gaps.
- [ ] Blocker owner, severity and status can be updated.
- [ ] Resolving and reopening blockers records timeline events.
- [ ] JSON and Markdown exports contain redacted evidence.
- [ ] Invalid imported workspace data normalizes to the known gate model.
- [ ] No customer endpoint or analytics request is made.
- [ ] Manual browser checks are completed at desktop and mobile widths.
- [ ] Review the privacy warning and risk-score limitations before wider use.

Do not label the app production-ready until browser-level acceptance has been performed.