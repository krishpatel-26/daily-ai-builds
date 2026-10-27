export function normalizeText(value) { return String(value ?? "").trim(); }
export function normalizeHeaderName(value) { return normalizeText(value).toLowerCase().replace(/[^a-z0-9-]/g, ""); }
export function normalizeEventId(value) { return normalizeText(value).replace(/\s+/g, ""); }
export function normalizeEndpoint(value) {
  try { const url = new URL(String(value)); url.hash = ""; return url.toString().replace(/\/$/, ""); }
  catch { return ""; }
}
