import test from "node:test";import assert from "node:assert/strict";import {toCSV,parseCSV} from "../src/csv.js";
const data=[{id:"1",client:'Acme, "North"',number:"INV-1",amount:125.5,issueDate:"2026-10-01",dueDate:"2026-10-10",status:"unpaid"}];
test("round trips commas and quotes",()=>{const parsed=parseCSV(toCSV(data));assert.equal(parsed[0].client,data[0].client);assert.equal(parsed[0].amount,125.5)});
test("rejects missing required columns",()=>assert.throws(()=>parseCSV("client,amount\nA,10")));
test("handles empty file",()=>assert.deepEqual(parseCSV(""),[]));
