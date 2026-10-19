# Trace schema proposal

A production trace record should include:

- trace_id and run_id
- timestamp and duration_ms
- prompt_version and prompt_hash
- model_provider, model_id, and generation parameters
- input token count and output token count
- retrieved source IDs and tool names
- tool-call status and bounded error messages
- output artifact location or redacted output
- deterministic grader outputs
- human review status and reviewer note

Do not put secrets, authentication tokens, or unnecessary personal data into traces. Define a retention policy before collecting real customer inputs.