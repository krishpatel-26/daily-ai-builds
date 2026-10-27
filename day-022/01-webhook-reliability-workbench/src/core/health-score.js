export function summarizeHealth(events) {
  const list = Array.isArray(events) ? events : []; const total = list.length;
  const delivered = list.filter((event) => event.status === "delivered").length;
  const failed = list.filter((event) => ["failed", "dead-letter"].includes(event.status)).length;
  const retrying = list.filter((event) => event.status === "retrying").length;
  const deadLetter = list.filter((event) => event.status === "dead-letter").length;
  const invalid = list.filter((event) => !event.id || !event.endpoint || !event.idempotencyKey).length;
  const successRate = total ? Math.round(delivered / total * 100) : 0;
  return { total, delivered, failed, retrying, deadLetter, invalid, successRate, healthScore: total ? Math.max(0, Math.min(100, Math.round(successRate - deadLetter * 8 - invalid * 5))) : 0, note: "Heuristic summary of the visible sample, not a provider-confirmed delivery metric." };
}
