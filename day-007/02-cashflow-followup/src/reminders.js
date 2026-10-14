import { getInvoiceState } from "./domain.js";
const money = n => new Intl.NumberFormat("en-IN",{style:"currency",currency:"INR",maximumFractionDigits:2}).format(n);
export function draftReminder(invoice, today = new Date().toISOString().slice(0,10)) {
  const state=getInvoiceState(invoice,today);
  if(state.key==="paid") throw new Error("Paid invoices do not need a reminder.");
  const greeting=invoice.client.trim().split(/\s+/)[0] || "there";
  const urgency=state.key==="overdue" ? `our records show invoice ${invoice.number} is ${state.daysOverdue} day(s) past its due date` : state.key==="due" ? `invoice ${invoice.number} is due ${invoice.dueDate===today?"today":"on "+invoice.dueDate}` : `invoice ${invoice.number} is scheduled for ${invoice.dueDate}`;
  return `Subject: Follow-up on invoice ${invoice.number}\n\nHi ${greeting},\n\nI hope you're doing well. I'm checking in about ${urgency}, for ${money(invoice.amount)}.\n\nCould you let me know the expected payment date, or tell me if you need another copy of the invoice?\n\nThanks for your time,\n[Your name]`;
}
