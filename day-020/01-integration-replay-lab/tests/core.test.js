const test=require('node:test');
const assert=require('node:assert/strict');
const vm=require('node:vm');
const C=require('../src/core');

test('sample pack is valid and contains three scenarios',()=>{
 const pack=C.samplePack();
 assert.deepEqual(C.validateScenario(pack),[]);
 assert.equal(pack.scenarios.length,3);
});

test('sample replay deterministically returns one failing case and two passing cases',()=>{
 const run=C.runAll(C.samplePack());
 assert.equal(run.status,'FAIL');
 assert.equal(run.scenarioCount,3);
 assert.equal(run.failed,1);
 assert.equal(run.passed,2);
 assert.equal(run.externalRequests,0);
 assert.deepEqual(run.results.map(r=>r.status),['FAIL','PASS','PASS']);
});

test('failure output identifies expected and observed status values',()=>{
 const r=C.runScenario(C.samplePack().scenarios[0]);
 assert.equal(r.firstFailure.id,'status');
 assert.equal(r.firstFailure.expected,'201');
 assert.equal(r.firstFailure.observed,'400');
 assert.ok(r.failedAssertions>=2);
});

test('required JSON paths, headers and max latency are asserted',()=>{
 const scenario={id:'checks',title:'Check assertion types',method:'GET',path:'/mock/x',
  mockResponse:{status:200,headers:{'Content-Type':'application/json'},body:{data:{id:'x'}},latencyMs:150},
  assertions:{status:200,requiredJsonPaths:['data.id','data.name'],headersEqual:{'content-type':'application/json'},maxLatencyMs:100}};
 const r=C.runScenario(scenario);
 assert.equal(r.status,'FAIL');
 assert.ok(r.checks.some(c=>c.id==='required:data.name'&&!c.passed));
 assert.ok(r.checks.some(c=>c.id==='header:content-type'&&c.passed));
 assert.ok(r.checks.some(c=>c.id==='latency'&&!c.passed));
});

test('scenario validation rejects duplicate IDs, invalid methods and paths',()=>{
 const p=C.samplePack();
 p.scenarios[1].id=p.scenarios[0].id;
 p.scenarios[2].method='BREW';
 p.scenarios[2].path='v1/no-leading-slash';
 const errors=C.validateScenario(p);
 assert.ok(errors.some(e=>e.includes('duplicate id')));
 assert.ok(errors.some(e=>e.includes('unsupported HTTP method')));
 assert.ok(errors.some(e=>e.includes('path must start with /')));
});

test('invalid JSON request body in string form is rejected',()=>{
 const p=C.samplePack();
 p.scenarios[0].request.body='{"unterminated":';
 assert.ok(C.validateScenario(p).some(e=>e.includes('JSON is invalid')));
});

test('redaction masks bearer tokens, secret assignments, provider keys and email',()=>{
 const source='Authorization: Bearer abc123 api_key=hidden-secret sk_live_DEMO123 person@example.test';
 const out=C.redactText(source);
 assert.doesNotMatch(out,/Bearer abc123/);
 assert.doesNotMatch(out,/api_key=hidden-secret/);
 assert.doesNotMatch(out,/sk_live_DEMO123/);
 assert.doesNotMatch(out,/person@example.test/);
 assert.match(out,/REDACTED/);
});

test('sanitizer recursively redacts strings without mutating input',()=>{
 const original={nested:{token:'Bearer liveabc123'},mail:'person@example.test'};
 const clean=C.sanitize(original);
 assert.equal(original.mail,'person@example.test');
 assert.doesNotMatch(JSON.stringify(clean),/person@example\.test/);
 assert.doesNotMatch(JSON.stringify(clean),/Bearer liveabc123/);
});

test('handoff includes local-only boundary and failed assertion details',()=>{
 const pack=C.samplePack();
 const run=C.runAll(pack);
 const report=C.buildHandoff(pack,run);
 assert.match(report,/Integration Replay Handoff/);
 assert.match(report,/External requests: 0/);
 assert.match(report,/FAIL — Create customer/);
 assert.match(report,/expected 201/);
});

test('generated regression-test draft parses as JavaScript',()=>{
 const pack=C.samplePack();
 const source=C.generateNodeTest(pack);
 assert.doesNotMatch(source,/person@example\.com/);
 assert.doesNotThrow(()=>new vm.Script(source));
 assert.match(source,/node:test/);
});

test('no assertion rules gives a deterministic passing replay',()=>{
 const r=C.runScenario({id:'no-assert',title:'No assertions',method:'GET',path:'/health',mockResponse:{status:204,body:null,headers:{},latencyMs:0},assertions:{}});
 assert.equal(r.status,'PASS');
 assert.equal(r.totalAssertions,0);
});
