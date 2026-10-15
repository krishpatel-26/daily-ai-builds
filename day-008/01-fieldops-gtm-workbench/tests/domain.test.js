import test from "node:test";import assert from "node:assert/strict";import {normalizeSignal,scoreSignal,priorityLabel,summarize,accountBrief} from "../src/domain.js";
const base={account:"Acme",type:"blocker",severity:"high",owner:"FDE",evidence:"Webhook contract mismatch observed",action:"Reproduce and validate mapping",due:"",stage:"open"};
test("normalizes valid customer signal",()=>{const s=normalizeSignal(base);assert.equal(s.account,"Acme");assert.ok(s.id)});
test("requires evidence, owner and next action",()=>{assert.throws(()=>normalizeSignal({...base,evidence:" "}));assert.throws(()=>normalizeSignal({...base,owner:""}));assert.throws(()=>normalizeSignal({...base,action:""}))});
test("rejects invalid type and severity",()=>{assert.throws(()=>normalizeSignal({...base,type:"guess"}));assert.throws(()=>normalizeSignal({...base,severity:"critical"}))});
test("blocker priority is transparent and high",()=>{assert.ok(scoreSignal(base)>=80);assert.match(priorityLabel(base),/Urgent/)});
test("completed signal has zero score",()=>{assert.equal(scoreSignal({...base,stage:"done"}),0)});
test("summary counts open blockers and completed signals",()=>{const x=summarize([base,{...base,id:"done",stage:"done"}]);assert.equal(x.open,1);assert.equal(x.blockers,1);assert.equal(x.done,1)});
test("account brief retains evidence and action",()=>{const b=accountBrief(base);assert.match(b,/Webhook contract mismatch observed/);assert.match(b,/Reproduce and validate mapping/)});
