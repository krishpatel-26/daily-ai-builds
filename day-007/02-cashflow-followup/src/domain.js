export function normalizeInvoice(input, now = new Date()) {
  const client = String(input.client ?? "").trim();
  const number = String(input.number ?? "").trim();
  const amount = Number(input.amount);
  const issueDate = String(input.issueDate ?? "");
  const dueDate = String(input.dueDate ?? "");
  if (!client || !number) throw new Error("Client and invoice number are required.");
  if (!Number.isFinite(amount) || amount <= 0) throw new Error("Amount must be greater than zero.");
  if (!isDate(issueDate) || !isDate(dueDate)) throw new Error("Valid issue and due dates are required.");
  if (dueDate < issueDate) throw new Error("Due date cannot be before issue date.");
  return { id: String(input.id || createId()), client, number, amount: roundMoney(amount), issueDate, dueDate, status: input.status === "paid" ? "paid" : "unpaid", createdAt: input.createdAt || now.toISOString() };
}
export function isDate(value) { return /^\d{4}-\d{2}-\d{2}$/.test(value) && !Number.isNaN(Date.parse(value + "T00:00:00Z")); }
export function daysBetween(from, to) { return Math.floor((Date.parse(to + "T00:00:00Z") - Date.parse(from + "T00:00:00Z")) / 86400000); }
export function getInvoiceState(invoice, today = new Date().toISOString().slice(0,10)) {
  if (invoice.status === "paid") return { key:"paid", label:"Paid", daysOverdue:0 };
  const delta = daysBetween(today, invoice.dueDate);
  if (delta < 0) return { key:"overdue", label:`Overdue ${Math.abs(delta)}d`, daysOverdue:Math.abs(delta) };
  if (delta <= 7) return { key:"due", label:delta === 0 ? "Due today" : `Due in ${delta}d`, daysOverdue:0 };
  return { key:"open", label:"Upcoming", daysOverdue:0 };
}
export function priorityScore(invoice, today) {
  const state = getInvoiceState(invoice, today);
  if (state.key === "paid") return -1;
  const lateness = state.daysOverdue * 100;
  const amount = Math.min(invoice.amount / 100, 999);
  const dueSoon = state.key === "due" ? 50 : 0;
  return lateness + amount + dueSoon;
}
export function summarize(invoices, today) {
  const unpaid = invoices.filter(i => i.status !== "paid");
  const overdue = unpaid.filter(i => getInvoiceState(i, today).key === "overdue");
  const due = unpaid.filter(i => getInvoiceState(i, today).key === "due");
  return { outstanding:roundMoney(unpaid.reduce((sum,i)=>sum+i.amount,0)), overdueCount:overdue.length, dueSoonCount:due.length, followupCount:overdue.length, paidCount:invoices.length-unpaid.length };
}
export function roundMoney(n) { return Math.round((Number(n) + Number.EPSILON) * 100) / 100; }
function createId() { return globalThis.crypto?.randomUUID?.() ?? `inv-${Date.now()}-${Math.random().toString(16).slice(2)}`; }
