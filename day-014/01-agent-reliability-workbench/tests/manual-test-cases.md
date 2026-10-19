# Manual test checklist

## Navigation and overview
- [ ] Load the app; confirm no JavaScript errors in the browser console.
- [ ] Switch through all five navigation views.
- [ ] Run evaluation and verify cases evaluated equals the current dataset size.
- [ ] Confirm pass, fail, and review counts sum to the number of evaluated cases.

## Cases and dataset
- [ ] Add a custom test case and verify it appears.
- [ ] Edit a case name and expected behavior.
- [ ] Delete a case and verify totals update on the next run.
- [ ] Export test dataset JSON and import it again.
- [ ] Import malformed JSON and verify a clear validation error.

## Runs and traces
- [ ] Run twice; confirm history contains two separate run IDs.
- [ ] Select a trace and verify each step is shown.
- [ ] Export a trace JSON.
- [ ] Export full run history JSON.

## Prompt comparison and layout
- [ ] Compare prompts with explicit and absent uncertainty instructions.
- [ ] Confirm the UI labels comparison as a textual heuristic.
- [ ] Test keyboard access, focus visibility, and narrow mobile width.

## Data integrity
- [ ] Confirm the demo does not call an LLM provider or transmit test content.
- [ ] Confirm latency/token values are labeled illustrative.
- [ ] Confirm generated status is not described as validated model accuracy.