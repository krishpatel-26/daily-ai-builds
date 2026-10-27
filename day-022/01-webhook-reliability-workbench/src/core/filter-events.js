export function filterEvents(events, options = {}) {
  const status = options.status ?? "all"; const query = String(options.query ?? "").trim().toLowerCase();
  return (events ?? []).filter((event) => {
    const statusMatch = status === "all" || event.status === status;
    const haystack = [event.id, event.eventType, event.customer, event.endpoint, event.failureType, event.idempotencyKey].join(" ").toLowerCase();
    return statusMatch && (!query || haystack.includes(query));
  }).slice().sort((a, b) => Date.parse(b.createdAt) - Date.parse(a.createdAt));
}
