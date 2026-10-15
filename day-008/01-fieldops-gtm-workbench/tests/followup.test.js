import test from "node:test";import assert from "node:assert/strict";import {followupDraft} from "../src/followup.js";
const s={id:"1",account:"Northstar",type:"blocker",severity:"high",owner:"FDE",evidence:"Identifier mapping is undocumented",action:"Validate mapping with customer",due:"",stage:"open"};
test("draft includes account evidence and next step",()=>{const d=followupDraft(s);assert.match(d,/Northstar/);assert.match(d,/Identifier mapping is undocumented/);assert.match(d,/Validate mapping with customer/);assert.match(d,/INTERNAL REVIEW BEFORE SENDING/)});
test("completed signal cannot generate follow-up",()=>assert.throws(()=>followupDraft({...s,stage:"done"})));
