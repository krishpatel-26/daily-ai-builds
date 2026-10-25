# Payload validation scope

The validator finds an operation's JSON request schema and supports local refs under components.schemas or definitions. It checks primitive types, required fields, nested properties, array items, enum values and additionalProperties=false.

It intentionally does not validate:
- string format such as email or date-time
- numeric min/max, string pattern/length or array cardinality
- allOf, oneOf, anyOf, not, dependent schemas or conditional keywords
- parameter serialization, auth headers, response bodies or real server behavior
- external $ref URLs

A payload that passes means only that it passed the implemented subset. It does not mean the request will succeed against the actual API.