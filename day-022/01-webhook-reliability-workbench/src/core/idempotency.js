import { normalizeText } from "./normalize.js";
export function getIdempotencyKey(event) { return normalizeText(event?.idempotencyKey || event?.id); }
export function findDuplicateKeys(events) {
  const groups = new Map();
  for (const event of events ?? []) {
    const key = getIdempotencyKey(event); if (!key) continue;
    const group = groups.get(key) ?? []; group.push(event); groups.set(key, group);
  }
  return [...groups.entries()].filter(([, group]) => group.length > 1).map(([key, group]) => ({ key, count: group.length, eventIds: group.map((item) => item.id) }));
}
export function hasPriorSuccessfulDelivery(events, event) {
  const key = getIdempotencyKey(event); if (!key) return false;
  return (events ?? []).some((candidate) => candidate.id !== event.id && getIdempotencyKey(candidate) === key && candidate.status === "delivered");
}
