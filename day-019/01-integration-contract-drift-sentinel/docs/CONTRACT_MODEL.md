# Supported contract model

The tool accepts JSON objects shaped like a subset of OpenAPI 3.x.

Supported comparison inputs:
- paths and common HTTP methods
- operation parameters identified by name and location
- requestBody.required and content schemas
- response status codes and JSON response schemas
- components.schemas or legacy definitions
- schema type, properties, required, enum, format and additionalProperties

The payload validator supports:
- object, array, string, integer, number, boolean and null types
- required properties
- nested object properties and array items
- enum values
- additionalProperties=false
- local $ref references into components.schemas and definitions

References are not comprehensively resolved for diff context, and the code does not implement all OpenAPI constructs such as allOf/oneOf/anyOf, parameter serialization, content negotiation, security schemes, discriminator, external references or JSON Schema dialect differences. Unsupported features can lead to incomplete comparison results.