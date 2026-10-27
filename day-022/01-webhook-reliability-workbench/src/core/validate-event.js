import { normalizeText, normalizeEndpoint } from "./normalize.js";
export function validateEvent(event) {
  const errors = [];
  if (!event || typeof event !== "object" || Array.isArray(event)) return { valid: false, errors: ["Event must be an object."] };
  if (!normalizeText(event.id)) errors.push("Missing event id.");
  if (!normalizeText(event.eventType)) errors.push("Missing event type.");
  if (!normalizeText(event.customer)) errors.push("Missing customer or workspace.");
  if (!normalizeEndpoint(event.endpoint)) errors.push("Endpoint must be a valid absolute URL.");
  if (!Number.isInteger(event.attempt) || event.attempt < 1) errors.push("Attempt must be a positive integer.");
  if (!["delivered", "failed", "retrying", "dead-letter"].includes(event.status)) errors.push("Unsupported delivery status.");
  if (!event.createdAt || Number.isNaN(Date.parse(event.createdAt))) errors.push("createdAt must be a valid timestamp.");
  return { valid: errors.length === 0, errors };
}
