import test from "node:test";import assert from "node:assert/strict";import {draftReminder} from "../src/reminders.js";
const invoice={client:"Mango Tree Cafe",number:"INV-1043",amount:7800,dueDate:"2026-10-10",status:"unpaid"};
test("creates a polite reminder with invoice details",()=>{const text=draftReminder(invoice,"2026-10-14");assert.match(text,/Mango Tree Cafe/);assert.match(text,/INV-1043/);assert.match(text,/7,800/);assert.match(text,/Subject:/)});
test("does not draft for paid invoices",()=>assert.throws(()=>draftReminder({...invoice,status:"paid"},"2026-10-14")));
