# Error taxonomy

| Category | Example | Next step |
| --- | --- | --- |
| Parse | Malformed JSON | Fix syntax |
| Required | Missing email | Inspect payload construction |
| Type | String supplied for integer | Align producer and contract |
| Enum | Unsupported plan | Confirm allowed values/version |
| Bounds | Value over maximum | Check business constraint |
| Format | Invalid email shape | Confirm format rule |
| Compatibility | Removed field | Review actual consumers |
| Unsupported | Keyword not implemented | Use a full validator |

A mismatch does not automatically identify which team or system caused it.