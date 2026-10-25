# Change classification policy

## Breaking
A likely incompatibility for existing callers or consumers:
- an operation or response status is removed
- a required request parameter is added or optionality is tightened
- a new required property is added
- a property, enum value or shared schema is removed
- a schema type changes
- unknown properties become disallowed

## Additive
A change that is commonly compatible but still deserves a test:
- a new operation or optional property/parameter appears
- a response status or enum value is added
- a shared schema is introduced

## Review
A potentially meaningful semantic change that the supported rules cannot safely label as breaking or additive, such as a format change or a previously required field becoming optional.

Classification depends on whether a schema represents requests, responses or shared models. The MVP's generic shared-schema comparison is intentionally conservative and can flag a response-side change as breaking even when a particular client would tolerate it. Always validate findings against the provider's compatibility policy and actual consumer behavior.