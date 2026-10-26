const test=require('node:test');
const assert=require('node:assert/strict');
const {spawn}=require('node:child_process');
const C=require('../src/core');

const source='id,name,email,status\nA-1,Avery,a@example.test,active\nA-2,Jordan,j@example.test,pending';
const target='id,full_name,email,status\nA-1,Avery,a@example.test,active\nA-3,Sam,s@example.test,active';
const baseMap=[{source:'name',target:'full_name'},{source:'email',target:'email'},{source:'status',target:'status'}];

test('parses simple CSV and returns row/column counts',()=>{
 const p=C.parseCsv(source);
 assert.deepEqual(p.headers,['id','name','email','status']);
 assert.equal(p.rowCount,2);
 assert.equal(p.records[0].id,'A-1');
 assert.equal(p.records[0].__row,2);
});

test('parses quoted commas, escaped quotes and embedded newlines',()=>{
 const p=C.parseCsv('id,notes\nA-1,"hello, world"\nA-2,"said ""yes"""\nA-3,"line one\nline two"');
 assert.equal(p.records[0].notes,'hello, world');
 assert.equal(p.records[1].notes,'said "yes"');
 assert.equal(p.records[2].notes,'line one\nline two');
});

test('strips UTF-8 BOM and handles CRLF endings',()=>{
 const p=C.parseCsv('\uFEFFid,name\r\n1,Avery\r\n2,Sam\r\n');
 assert.equal(p.rowCount,2);
 assert.equal(p.records[1].name,'Sam');
});

test('rejects duplicate and blank headers',()=>{
 assert.throws(()=>C.parseCsv('id,id\n1,2'),/Duplicate CSV header/);
 assert.throws(()=>C.parseCsv('id,,name\n1,2,3'),/header.*blank/i);
});

test('rejects unterminated quotes and rows with extra non-empty cells',()=>{
 assert.throws(()=>C.parseCsv('id,name\n1,"Avery'),/inside a quoted field/);
 assert.throws(()=>C.parseCsv('id,name\n1,Avery,extra'),/more cells/);
});

test('detects missing and extra records',()=>{
 const r=C.reconcile(source,target,{sourceKey:'id',targetKey:'id',mappings:baseMap,trim:true,lowercaseEmail:true});
 assert.equal(r.missingRecords.length,1);
 assert.equal(r.missingRecords[0].key,'A-2');
 assert.equal(r.extraRecords.length,1);
 assert.equal(r.extraRecords[0].key,'A-3');
 assert.equal(r.mismatchCount,0);
 assert.equal(r.status,'REVIEW REQUIRED');
});

test('maps different source and target column names',()=>{
 const r=C.reconcile('id,name\n1,Avery','key,display_name\n1,Avery',{sourceKey:'id',targetKey:'key',mappings:[{source:'name',target:'display_name'}]});
 assert.equal(r.matchedCount,1);
 assert.equal(r.mismatchCount,0);
 assert.equal(r.status,'RECONCILED');
});

test('detects duplicate identities and blank keys on both sides',()=>{
 const r=C.reconcile('id,value\n1,a\n1,b\n,c','key,value\n1,a\n1,b\n,d',{sourceKey:'id',targetKey:'key',mappings:[{source:'value',target:'value'}]});
 assert.equal(r.sourceDuplicates.length,1);
 assert.equal(r.targetDuplicates.length,1);
 assert.equal(r.blankSourceRows.length,1);
 assert.equal(r.blankTargetRows.length,1);
 assert.ok(r.findings.filter(f=>f.type==='duplicate').length>=4);
});

test('trimming and email case folding are comparison-only',()=>{
 const s='id,email,name\n1,AVERY@EXAMPLE.TEST," Avery "';
 const t='id,email,display_name\n1,avery@example.test,Avery';
 const r=C.reconcile(s,t,{sourceKey:'id',targetKey:'id',mappings:[{source:'email',target:'email'},{source:'name',target:'display_name'}],trim:true,lowercaseEmail:true});
 assert.equal(r.mismatchCount,0);
 assert.equal(s.includes('" Avery "'),true);
});

test('whitespace differences remain when trim normalization is disabled',()=>{
 const r=C.reconcile('id,name\n1," Avery "','id,display_name\n1,Avery',{sourceKey:'id',targetKey:'id',mappings:[{source:'name',target:'display_name'}],trim:false,lowercaseEmail:false});
 assert.equal(r.mismatchCount,1);
});

test('rejects invalid keys and empty mappings',()=>{
 assert.throws(()=>C.reconcile(source,target,{sourceKey:'missing',targetKey:'id',mappings:baseMap}),/Source key does not exist/);
 assert.throws(()=>C.reconcile(source,target,{sourceKey:'id',targetKey:'id',mappings:[]}),/at least one valid/);
});

test('sample data intentionally shows duplicate, missing, extra and mismatch issues',()=>{
 const s=C.sampleData();
 const r=C.reconcile(s.source,s.target,{sourceKey:'customer_id',targetKey:'customer_id',mappings:s.mappings,trim:true,lowercaseEmail:true});
 assert.equal(r.sourceDuplicates.length,1);
 assert.equal(r.missingRecords.length,1);
 assert.equal(r.extraRecords.length,1);
 assert.ok(r.mismatchCount>=1);
 assert.equal(r.status,'REVIEW REQUIRED');
});

test('report includes comparison scope and reviewer notes',()=>{
 const r=C.reconcile(source,target,{sourceKey:'id',targetKey:'id',mappings:baseMap});
 const report=C.buildReport(r,{project:'Synthetic CRM Migration',reviewer:'FDE',notes:'Test handoff'});
 assert.match(report,/Customer Data Migration Reconciliation Report/);
 assert.match(report,/Synthetic CRM Migration/);
 assert.match(report,/Missing from target: 1/);
 assert.match(report,/Field mappings/);
 assert.match(report,/Test handoff/);
 assert.ok(report.includes('\n'));
});

test('identical mapped data returns reconciled with score 100',()=>{
 const r=C.reconcile('id,name\n1,Avery\n2,Sam','id,display_name\n1,Avery\n2,Sam',{sourceKey:'id',targetKey:'id',mappings:[{source:'name',target:'display_name'}]});
 assert.equal(r.status,'RECONCILED');
 assert.equal(r.score,100);
 assert.equal(r.recordCoverage,100);
});

async function startServer(t){
 const port=5300+Math.floor(Math.random()*500);
 const child=spawn(process.execPath,['scripts/serve.js'],{cwd:process.cwd(),env:{...process.env,PORT:String(port)},stdio:['ignore','pipe','pipe']});
 let output='';
 child.stdout.on('data',chunk=>output+=chunk.toString());
 t.after(()=>child.kill());
 let response;
 for(let i=0;i<50;i++){try{response=await fetch('http://127.0.0.1:'+port+'/');break;}catch{await new Promise(resolve=>setTimeout(resolve,60));}}
 assert.ok(response,'static server failed to start: '+output);
 return{port,home:response};
}

test('serves dashboard and JavaScript with restrictive response headers',async t=>{
 const {port,home}=await startServer(t);
 assert.equal(home.status,200);
 assert.match(home.headers.get('content-type'),/text\/html/);
 assert.match(home.headers.get('content-security-policy'),/default-src 'self'/);
 assert.match(await home.text(),/Migration Reconciliation Lab/);
 const asset=await fetch('http://127.0.0.1:'+port+'/src/core.js');
 assert.equal(asset.status,200);
 assert.match(await asset.text(),/function reconcile/);
});

test('returns 404 for missing asset and does not serve paths outside root',async t=>{
 const {port}=await startServer(t);
 assert.equal((await fetch('http://127.0.0.1:'+port+'/no-such-file')).status,404);
 const traversal=await fetch('http://127.0.0.1:'+port+'/%2e%2e/%2e%2e/etc/passwd');
 assert.notEqual(traversal.status,200);
});
