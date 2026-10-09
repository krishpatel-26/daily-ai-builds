# Architecture and operating model

## Control plane
The orchestrator routes goals and evaluates each requested action against a role permission map. A policy decision is produced before the task is considered ready. Sensitive actions become `pending_approval`; disallowed actions become `denied`.

## Agent roles
| Role | Intended responsibilities | Example permissions |
|---|---|---|
| Research | Web, document, and competitor research | Read research |
| Strategy | Planning and prioritization | Read research and analytics |
| Content | Drafting content and assets | Read research, write content |
| Operations | Internal workflow execution | Run workflows, read analytics |
| Outreach | Lead management and communication | Read research, CRM updates, outreach |
| Analytics | Metrics and reporting | Read analytics and research |

Permissions are intentionally narrow. Real tool adapters must independently enforce the same boundary; a prompt saying “do not do this” is not a security control.

## Shared services
- Memory platform: scoped short- and long-term context.
- Knowledge base: approved internal documents and data.
- Tool integration layer: API adapters with per-agent credentials.
- Security and access control: authorization, audit events, secrets, and tenant boundaries.

## Reliability and sustainability
Production deployments should persist workflow state, use idempotent jobs, retry transient failures with backoff, support checkpoint/recovery, enforce usage budgets, and expose latency/error/cost metrics. This starter keeps state in memory to make the core policy behavior explicit.

## Human oversight
Require human approval for external side effects, sensitive changes, and high-risk actions. Approval should be bound to the exact action payload, actor, policy version, and expiry; any payload change should invalidate approval.
