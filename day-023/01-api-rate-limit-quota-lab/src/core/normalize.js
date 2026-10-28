export function normalizeText(value) { return String(value ?? "").trim(); }
export function normalizeRoute(value) {
  const raw = normalizeText(value);
  if (!raw.startsWith("/")) return "";
  const path = raw.split("?")[0].replace(/\/{2,}/g, "/");
  return path.length > 1 ? path.replace(/\/$/, "") : path;
}
export function normalizeClientId(value) { return normalizeText(value).toLowerCase().replace(/[^a-z0-9._-]/g, ""); }
export function normalizeRequestId(value) { return normalizeText(value).replace(/\s+/g, ""); }
