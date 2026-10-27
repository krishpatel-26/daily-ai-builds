export function countBy(events, selector) {
  const counts = Object.create(null); for (const item of events ?? []) { const key = String(selector(item) ?? "unknown"); counts[key] = (counts[key] ?? 0) + 1; } return counts;
}
export function failureBreakdown(events) { return countBy((events ?? []).filter((event) => event.status !== "delivered"), (event) => event.failureType ?? "unknown"); }
export function attemptStats(events) {
  const values = (events ?? []).map((event) => Number(event.attempt)).filter(Number.isFinite);
  if (!values.length) return { min: 0, max: 0, average: 0 };
  const sum = values.reduce((total, value) => total + value, 0);
  return { min: Math.min(...values), max: Math.max(...values), average: Math.round(sum / values.length * 100) / 100 };
}
