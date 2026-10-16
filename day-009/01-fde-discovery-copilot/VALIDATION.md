# Validation plan

## Hypotheses
1. Linking each signal to its source sentence makes customer handoffs easier to audit.
2. Suggested actions are more useful when they include a proposed owner and explicit review requirement.
3. A follow-up draft reduces blank-page work without turning unverified assumptions into commitments.

## Manual test cases
- Empty notes: should ask the user to add more context.
- Notes shorter than 25 characters: should show a validation message.
- Notes with no known keywords: should show an empty-match state rather than inventing signals.
- Notes mentioning an API blocker and a security review: should show evidence for both categories.
- Product feature request: follow-up must say the capability needs confirmation rather than promise delivery.
- Export: JSON should include the raw matched evidence, categories, heuristic method, and caveat.

## Risks and mitigations
- False positives: show matched terms and source sentence.
- False negatives: state that unmatched notes still need human review.
- Overconfidence: label the score as heuristic and avoid presenting it as a calibrated probability.
- Accidental customer commitments: generated drafts explicitly require review and are never sent automatically.
- Sensitive data: keep processing in-browser and remind users to remove sensitive information.

## Not yet done
Automated tests, accessibility audit, cross-browser testing, customer interviews, and any production security review.