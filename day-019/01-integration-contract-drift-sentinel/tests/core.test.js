const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const C=require('../src/core');
const fixture=name=>JSON.parse(fs.readFileSync(path.join(__dirname,'..','fixtures',name),'utf8'));
const v1=()=>fixture('customer-api-v1.openapi.json');
const v2=()=>fixture('customer-api-v2.openapi.json');

test('detects removed operation as a critical breaking change',()=>{
 const result=C.compareContracts(v1(),v2());
 const item=result.changes.find(c=>c.title==='An API operation was removed');
 assert.ok(item);
 assert.equal(item.severity,'critical');
 assert.equal(item.classification,'breaking');
 assert.match(item.path,/GET \/v1\/customers\/\{id\}/);
});

test('detects newly required request property and required parameters',()=>{
 const result=C.compareContracts(v1(),v2());
 assert.ok(result.changes.some(c=>c.title==='A new required property was added'&&c.path.includes('region')));
 assert.ok(result.changes.some(c=>c.title==='A required parameter was added'&&c.path.includes('Idempotency-Key')));
 assert.ok(result.changes.some(c=>c.title==='An optional parameter became required'&&c.path.includes('X-Region')));
});

test('classifies an added enum value as additive',()=>{
 const result=C.compareContracts(v1(),v2());
 assert.ok(result.changes.some(c=>c.title==='Allowed enum values were added'&&c.classification==='additive'));
});

test('baseline fixture passes old request schema',()=>{
 const payload=fs.readFileSync(path.join(__dirname,'..','fixtures','customer-create-v1-valid.json'),'utf8');
 const result=C.validatePayload(v1(),'POST /v1/customers',payload);
 assert.equal(result.valid,true,JSON.stringify(result.issues));
});

test('baseline payload fails candidate contract with missing and unknown fields',()=>{
 const payload=fs.readFileSync(path.join(__dirname,'..','fixtures','customer-create-v2-breaking.json'),'utf8');
 const result=C.validatePayload(v2(),'POST /v1/customers',payload);
 assert.equal(result.valid,false);
 assert.ok(result.issues.some(i=>i.path==='$.region'));
 assert.ok(result.issues.some(i=>i.path==='$.legacy_code'));
});

test('candidate fixture passes candidate request schema',()=>{
 const payload=fs.readFileSync(path.join(__dirname,'..','fixtures','customer-create-v2-valid.json'),'utf8');
 const result=C.validatePayload(v2(),'POST /v1/customers',payload);
 assert.equal(result.valid,true,JSON.stringify(result.issues));
});

test('invalid JSON input fails clearly',()=>{
 const result=C.validatePayload(v2(),'POST /v1/customers','{"name":');
 assert.equal(result.valid,false);
 assert.match(result.issues[0].message,/invalid/i);
});

test('report includes summary, recommendation and test plan',()=>{
 const result=C.compareContracts(v1(),v2());
 const report=C.buildReport('', '', result);
 assert.match(report,/Integration Contract Drift Review/);
 assert.match(report,/Recommendation: BREAKING CHANGES/);
 assert.match(report,/Regression test plan/);
 assert.ok(result.regressionTests.length>0);
});

test('no-drift contracts return no changes',()=>{
 const contract=v1();
 const result=C.compareContracts(contract,JSON.parse(JSON.stringify(contract)));
 assert.equal(result.counts.total,0);
 assert.equal(result.status,'COMPATIBLE');
 assert.equal(result.riskScore,0);
});