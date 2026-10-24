# Manual test plan

1. Run npm start and open http://127.0.0.1:4173.
2. Click Load demo. Verify 8 gates, 3 blockers and a NO-GO decision appear.
3. Open Authentication and inspect the failed scope check and evidence note.
4. Change a check to Pass but leave its evidence blank. Save the checkpoint and confirm an evidence gap remains.
5. Add a sentence of evidence and save again; confirm the gap count changes.
6. Resolve a blocker, then reopen it. Confirm the timeline records both actions and the metrics update.
7. Change the blocker owner/severity and save.
8. Record a Decision, Test result and Customer update in the timeline.
9. Export customer handoff, runbook and workspace JSON; confirm the exports download and contain current state.
10. Use synthetic token/email values in notes and inspect output masking. Do not treat this as a complete redaction guarantee.
11. Start a new workspace and confirm the current workspace data remains only if exported first.
12. Refresh the page and confirm localStorage restores the current workspace.
13. Check layout at a narrow viewport and keyboard-operate the controls.
14. Run npm run check and npm test; capture full output as evidence for this revision.