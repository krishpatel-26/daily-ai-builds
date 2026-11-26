# Compatibility classification matrix

| Change | Default classification | Why it matters |
|---|---|---|
| Existing method/path removed | Breaking | Consumers can no longer call the operation |
| New optional method/path | Safe / additive | Existing request behavior is unchanged |
| New required request property | Breaking | Existing payloads can fail validation |
| Request property removed | Breaking | Existing clients may still send it |
| Request property type changed | Breaking | Serialization or validation may fail |
| Optional parameter becomes required | Breaking | Existing clients may omit it |
| Parameter removed | Breaking | Existing generated clients may still send it |
| Numeric maximum narrowed | Review | Previously valid values can now be rejected |
| Enum member removed | Breaking | Client values or returned values may no longer be supported |
| Response property removed | Review | Strict consumers may depend on it; others may ignore it |
| Operation ID changed | Review | Generated SDK method names may change |
| Documented response code removed | Review | Consumers may handle the code explicitly |

This is an explicit project heuristic, not a universal compatibility standard. Language SDK generators, validators, gateways, and runtime behavior differ. Check the receiver contract and actual clients before release.
