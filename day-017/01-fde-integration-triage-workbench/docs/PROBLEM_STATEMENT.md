# Problem statement

Forward Deployed Engineers often receive a mixture of application logs, configuration snippets and second-hand customer observations. A slow first investigation leads to repeated questions, ad hoc severity calls and handoffs without evidence.

This workbench gives the first-pass investigation a consistent structure: sanitize evidence, match known failure signatures, highlight risky configuration, sort by operational impact and export a concise handoff.

## Intended users
- FDEs and implementation engineers working across customer environments
- Solutions engineers helping with API integrations
- Support engineers investigating onboarding blockers

## Non-goals
It is not a replacement for platform observability, vendor documentation, security review or live validation. A heuristic signal is a starting point for a question, not proof of root cause.