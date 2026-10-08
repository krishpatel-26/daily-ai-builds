# Architecture

The control plane sits above individual agent implementations.

```text
REQUEST
  ↓
POLICY GATE
  ↓
ROUTER
  ↓
AGENT
  ↓
EVALUATION
  ↓
OBSERVABILITY
  ↓
HUMAN APPROVAL (when required)
```

The core is deterministic and provider-agnostic so external LLMs can be added behind adapters without moving governance into prompts.
