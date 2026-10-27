import { classifyFailure } from "./triage.js";
import { retryDecision, buildRetrySchedule } from "./retry-policy.js";
import { findDuplicateKeys } from "./idempotency.js";
import { summarizeHealth } from "./health-score.js";
import { toMarkdownCell } from "./format.js";
export function buildIncidentReport(events, generatedAt = new Date().toISOString()) {
  const list = Array.isArray(events) ? events : []; const duplicateKeys = findDuplicateKeys(list); const health = summarizeHealth(list);
  const rows = list.map((event) => {
    const triage = classifyFailure(event); const retry = retryDecision(event);
    return { eventId:event.id, eventType:event.eventType, customer:event.customer, endpoint:event.endpoint, attempt:event.attempt, status:event.status, failureType:event.failureType ?? "none", triageCategory:triage.category, severity:triage.severity, suggestedAction:triage.action, retryAllowedByDemoPolicy:retry.retry, retryReason:retry.reason, retrySchedule:retry.retry ? buildRetrySchedule(event.createdAt).slice(0,3) : [] };
  });
  return { schemaVersion:"1.0", generatedAt, scope:"synthetic-local-demo", disclaimer:"Heuristic evidence bundle. Validate provider semantics and downstream side effects before acting.", summary:health, duplicateIdempotencyKeys:duplicateKeys, deliveries:rows };
}
export function reportToMarkdown(report) {
  const rows = report.deliveries.map((item) => "| " + [item.eventId,item.customer,item.status,item.severity,item.triageCategory,item.suggestedAction].map(toMarkdownCell).join(" | ") + " |");
  return [
    "# Webhook incident handoff","", "- Generated: " + report.generatedAt, "- Scope: " + report.scope,
    "- Attempts reviewed: " + report.summary.total, "- Delivery success rate: " + report.summary.successRate + "%",
    "- Failed / dead-letter: " + report.summary.failed, "", "> " + report.disclaimer, "",
    "## Delivery evidence","", "| Event ID | Customer | State | Severity | Category | Suggested action |", "|---|---|---|---|---|---|", ...rows, "",
    "## Duplicate idempotency keys","",
    ...(report.duplicateIdempotencyKeys.length ? report.duplicateIdempotencyKeys.map((item) => "- " + toMarkdownCell(item.key) + " appears " + item.count + " times: " + item.eventIds.join(", ")) : ["None detected in the supplied sample."]),
    "", "## Required human checks","", "- Confirm receiver response and request ID in provider logs.", "- Check downstream side effects before any replay.", "- Confirm idempotency key and provider retry semantics.", "- Record owner and next review time in the customer incident ticket.", ""
  ].join("\n");
}
