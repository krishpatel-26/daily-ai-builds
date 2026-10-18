# Readiness scoring model

The score is the sum of weights for completed checklist items divided by the sum of all item weights, multiplied by 100 and rounded to the nearest integer.

| Category | Example evidence |
| --- | --- |
| Discovery | Agreed scope and measurable success criteria |
| Ownership | Customer owner and escalation path |
| Technical | Access provisioned; end-to-end integration tested |
| Risk | Security and compliance approval |
| Data | Mapping and sample records validated |
| Adoption | Workflow mapped and training scheduled |
| Operations | Monitoring and rollback plan |
| Validation | Customer acceptance test |
| GTM | Support handoff and status shared |

The UI labels readiness as a review state, not an automatic launch approval. Technical, security, integration, and acceptance gaps remain critical regardless of the overall score.

The weights are design assumptions and must be calibrated with implementation teams before operational use.