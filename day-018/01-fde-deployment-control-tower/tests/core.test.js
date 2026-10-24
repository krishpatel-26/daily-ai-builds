const test = require('node:test');
const assert = require('node:assert/strict');
const C = require('../src/core');

function markAll(w,status='pass',withEvidence=true) {
  for (const gate of w.gates) {
    for (const check of gate.checks) {
      C.setCheck(w,gate.id,check.id,status,withEvidence?'Synthetic test evidence recorded for '+gate.id+'/'+check.id+'.':'');
    }
  }
}
function completeContext(w) {
  w.meta.customer='Example Customer';
  w.meta.integration='CRM sync';
  w.meta.owner='FDE';
  w.meta.successCriteria='100 synthetic records sync without duplicates';
}

test('workspace creates eight gates and 24 required checks',()=>{
  const w=C.createWorkspace();
  assert.equal(w.gates.length,8);
  assert.equal(w.gates.reduce((sum,g)=>sum+g.checks.length,0),24);
  assert.equal(C.evaluateWorkspace(w).totalChecks,24);
  assert.equal(C.evaluateWorkspace(w).completeGates,0);
});

test('a failed required check creates a NO-GO recommendation',()=>{
  const w=C.createWorkspace();
  C.setCheck(w,'authentication','scopes','fail','API returned 403 for the required write scope.');
  const r=C.evaluateWorkspace(w);
  assert.equal(r.failedChecks,1);
  assert.equal(r.decision,'NO-GO');
  assert.equal(r.decisionStatus,'blocked');
});

test('pass without evidence is still an evidence gap',()=>{
  const w=C.createWorkspace();
  C.setCheck(w,'discovery','stakeholders','pass','');
  const r=C.evaluateWorkspace(w);
  assert.equal(r.evidenceGaps,1);
  assert.notEqual(r.decision,'GO-TO-REVIEW');
});

test('complete evidence-backed checklist reaches reviewable state, not automatic approval',()=>{
  const w=C.createWorkspace();
  markAll(w,'pass',true);
  completeContext(w);
  const r=C.evaluateWorkspace(w);
  assert.equal(r.score,100);
  assert.equal(r.satisfiedChecks,24);
  assert.equal(r.evidenceGaps,0);
  assert.equal(r.canGo,true);
  assert.equal(r.decision,'GO-TO-REVIEW');
  assert.notEqual(r.decision,'APPROVED');
});

test('critical blocker forces NO-GO even when every checklist passes',()=>{
  const w=C.createWorkspace();
  markAll(w,'pass',true);
  completeContext(w);
  const b=C.addBlocker(w,{title:'Data integrity concern',severity:'critical',description:'Duplicate records observed.',owner:'Platform owner'});
  assert.equal(C.evaluateWorkspace(w).decision,'NO-GO');
  C.updateBlocker(w,b.id,{status:'resolved'});
  assert.equal(C.evaluateWorkspace(w).openBlockers,0);
  assert.equal(C.evaluateWorkspace(w).decision,'GO-TO-REVIEW');
});

test('blocker resolution is recorded in timeline',()=>{
  const w=C.createWorkspace();
  const b=C.addBlocker(w,{title:'Timeout too low',severity:'high'});
  C.updateBlocker(w,b.id,{status:'resolved'});
  assert.ok(w.events.some(e=>e.text.includes('Blocker resolved: Timeout too low')));
});

test('secret-like data is masked in redaction output',()=>{
  const input='Authorization: Bearer abc.def.ghi api_key=sk_live_A1B2C3 user person@example.com';
  const output=C.redactText(input);
  assert.match(output,/REDACTED_TOKEN/);
  assert.match(output,/REDACTED_API_KEY/);
  assert.match(output,/REDACTED_EMAIL/);
  assert.doesNotMatch(output,/sk_live_A1B2C3/);
  assert.doesNotMatch(output,/person@example.com/);
});

test('handoff and runbook include deployment state and next steps',()=>{
  const w=C.createWorkspace({customer:'Example Co',integration:'Invoice sync'});
  C.setCheck(w,'connectivity','network','fail','DNS resolution timed out.');
  const handoff=C.buildHandoff(w);
  const runbook=C.buildRunbook(w);
  assert.match(handoff,/Example Co/);
  assert.match(handoff,/NO-GO/);
  assert.match(handoff,/Evidence gaps/);
  assert.match(runbook,/NOT DONE|FAILED|EVIDENCE GAP/);
});

test('normalization rejects unknown gate IDs and normalizes check statuses',()=>{
  const normalized=C.normalizeWorkspace({meta:{customer:'Example'},gates:[{id:'intruder',checks:[{id:'x',status:'approved'}]}],blockers:[{id:'b',title:'T',severity:'planet',status:'unrecognized'}]});
  assert.equal(normalized.gates.length,8);
  assert.ok(normalized.gates.every(g=>g.id!=='intruder'));
  assert.equal(normalized.blockers[0].severity,'medium');
  assert.equal(normalized.blockers[0].status,'open');
});