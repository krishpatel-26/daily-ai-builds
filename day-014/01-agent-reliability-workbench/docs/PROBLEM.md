# Problem framing

LLM prototypes often look convincing in a happy-path demo but regress after a prompt change, fail under missing context, mishandle tool errors, or make claims not supported by supplied evidence.

## Primary user
An applied AI engineer or team responsible for shipping an LLM-powered workflow.

## Job to be done
Before releasing a prompt or agent change, run a repeatable set of cases, inspect failures, compare versions, and record what changed.

## Desired operating principle
Treat prompts, model configuration, tools, context, and graders as versioned software artifacts. Avoid a single aggregate score without traceability to the underlying examples.