# Validation plan

## Manual functional checks
- Run default evaluation and inspect pass/fail/review counts.
- Switch among all five views.
- Edit a case, delete a case, and add a custom case.
- Export and re-import the dataset JSON.
- Inspect a trace and export it.
- Compare two prompts with different instruction coverage.
- Reset the demo and verify run history clears.
- Test on a narrow viewport and keyboard navigation.

## Model evaluation before real use
- Create a versioned, labeled evaluation dataset with edge cases.
- Define objective graders for structured output, source support, and policy compliance.
- Human-review a sample of grader decisions.
- Measure false positives and false negatives per check.
- Run repeated trials for nondeterministic outputs.
- Record model version, parameters, prompt hash, tools, retrieval configuration, latency, tokens, and errors.
- Compare results against an agreed release threshold.

## Not completed in this prototype
Automated browser tests, actual LLM calls, production tracing, provider-cost verification, and customer validation.