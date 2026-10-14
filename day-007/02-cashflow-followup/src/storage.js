const KEY = "cashflow-planner:v1";
export function loadInvoices(storage = globalThis.localStorage) {
  try { const raw = storage?.getItem(KEY); if (!raw) return []; const parsed = JSON.parse(raw); return Array.isArray(parsed) ? parsed : []; }
  catch { return []; }
}
export function saveInvoices(invoices, storage = globalThis.localStorage) {
  try { storage?.setItem(KEY, JSON.stringify(invoices)); return { ok:true }; }
  catch (error) { return { ok:false, reason:error?.name === "QuotaExceededError" ? "storage_full" : "storage_unavailable" }; }
}
export function clearInvoices(storage = globalThis.localStorage) { try { storage?.removeItem(KEY); return true; } catch { return false; } }
export const STORAGE_KEY = KEY;
