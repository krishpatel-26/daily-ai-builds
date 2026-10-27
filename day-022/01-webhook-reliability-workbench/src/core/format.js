export function formatRelativeAge(timestamp, now = Date.now()) {
  const value = Date.parse(timestamp); if (Number.isNaN(value)) return "unknown";
  const minutes = Math.max(0, Math.floor((now - value) / 60000));
  if (minutes < 1) return "just now"; if (minutes < 60) return minutes + "m ago";
  const hours = Math.floor(minutes / 60); if (hours < 24) return hours + "h ago";
  return Math.floor(hours / 24) + "d ago";
}
export function formatDuration(ms) {
  const value = Math.max(0, Number(ms) || 0); if (value < 1000) return Math.round(value) + " ms";
  if (value < 60000) return (value / 1000).toFixed(1) + " s"; return (value / 60000).toFixed(1) + " min";
}
export function toMarkdownCell(value) { return String(value ?? "").replace(/\|/g, "\\|").replace(/[\r\n]+/g, " ").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
export function safeFileName(value) { return String(value ?? "export").toLowerCase().replace(/[^a-z0-9-]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 64) || "export"; }
