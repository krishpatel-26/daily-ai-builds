# Schema comparison

The diff checks root-level properties and flags property additions/removals, newly required fields, type changes, enum changes, numeric bounds, and string-length bounds.

A removed field or newly required field can be breaking, depending on request/response direction and actual consumer behavior. A diff is a review aid, not proof of compatibility.