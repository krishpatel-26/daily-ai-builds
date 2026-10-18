# Manual test checklist

- [ ] Load synthetic telemetry; metrics and sensor list appear.
- [ ] Confirm synthetic dataset yields candidate gap and spike events.
- [ ] Change expected interval; gap count updates.
- [ ] Change spike threshold; spike count updates.
- [ ] Filter sensor cards to a single stream.
- [ ] Select a trace and inspect plotted samples.
- [ ] Upload valid CSV with timestamp,sensor,value header.
- [ ] Upload CSV missing a required header; verify validation error.
- [ ] Upload CSV containing invalid timestamps and values; invalid rows are ignored.
- [ ] Export JSON and Markdown; confirm report includes settings and limitations.
- [ ] Test empty file, one-row file, constant stream, and narrow viewport.
- [ ] Compare every detected event against expected labeled faults before relying on the detector.