DASHBOARD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AgentGuard</title><style>
:root{color-scheme:dark;--bg:#0b1020;--panel:#121b31;--line:#263552;--blue:#78aaff;--muted:#9aabc7}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 80% 0,#172b50,var(--bg) 48%);color:#edf3ff;font:15px Inter,system-ui}
main{max-width:1120px;margin:36px auto;padding:0 22px}.top{display:flex;justify-content:space-between;align-items:center;gap:16px}
h1{font-size:32px;margin:0}.sub{color:var(--muted);margin:8px 0 24px}.pill{border:1px solid #31507e;color:#9dc2ff;padding:8px 12px;border-radius:99px}
.grid{display:grid;grid-template-columns:1.1fr .9fr;gap:18px}.card{background:#111a2e;border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:0 16px 50px #0003}
h2{font-size:17px;margin:0 0 16px}.row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
input,select,textarea{width:100%;background:#0b1325;color:white;border:1px solid #30415f;border-radius:9px;padding:11px;margin:5px 0 12px}
label{font-size:12px;color:var(--muted)}button{background:#4c8cff;color:#071326;border:0;border-radius:9px;padding:11px 16px;font-weight:700;cursor:pointer}
pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#091122;padding:14px;border-radius:10px;color:#c9dcff;min-height:90px}
.stats{display:flex;gap:10px;margin:18px 0}.stat{flex:1;background:#0b1427;border:1px solid var(--line);padding:14px;border-radius:12px}.stat b{display:block;font-size:24px;color:var(--blue)}
table{width:100%;border-collapse:collapse;font-size:13px}td,th{text-align:left;padding:10px;border-bottom:1px solid var(--line)}th{color:var(--muted)}
@media(max-width:760px){.grid{grid-template-columns:1fr}.top{align-items:flex-start;flex-direction:column}}
</style></head><body><main>
<div class="top"><div><h1>◈ AgentGuard</h1><p class="sub">Policy enforcement for AI agents · local demo</p></div><span class="pill">DETERMINISTIC CONTROL PLANE</span></div>
<div class="stats"><div class="stat"><b id="total">0</b>Requests</div><div class="stat"><b id="pending">0</b>Awaiting approval</div><div class="stat"><b id="denied">0</b>Denied</div></div>
<div class="grid"><section class="card"><h2>Evaluate an agent action</h2>
<form id="form"><div class="row"><div><label>Actor</label><input name="actor" value="agent-007"></div><div><label>Role</label><select name="role"><option>support_agent</option><option>finance_agent</option><option>admin</option></select></div></div>
<div class="row"><div><label>Resource type</label><select name="resource_type"><option>ticket</option><option>customer</option><option>invoice</option></select></div><div><label>Action</label><select name="action"><option>read</option><option>tag</option><option>assign</option><option>update_contact</option><option>draft</option><option>export</option><option>close</option><option>delete</option></select></div></div>
<div class="row"><div><label>Resource ID</label><input name="resource_id" value="CASE-1042"></div><div><label>Payload note</label><input name="note" value="routine workflow"></div></div>
<button>Evaluate action</button></form><h2 style="margin-top:18px">Decision</h2><pre id="result">Submit a proposal to see the policy decision.</pre></section>
<section class="card"><h2>Pending approvals</h2><div id="approval-list">Loading…</div><h2 style="margin-top:22px">Recent audit events</h2><div id="audit-list">Loading…</div></section></div>
</main><script>
const $=s=>document.querySelector(s);
async function refresh(){const [r,a,l]=await Promise.all([fetch('/api/requests').then(x=>x.json()),fetch('/api/approvals').then(x=>x.json()),fetch('/api/audit').then(x=>x.json())]);
$('#total').textContent=r.length;$('#pending').textContent=a.length;$('#denied').textContent=r.filter(x=>x.status==='denied').length;
$('#approval-list').innerHTML=a.length?a.map(x=>'<p><b>'+x.action+'</b> · '+x.resource_type+'/'+x.resource_id+'<br><button onclick="review(\''+x.request_id+'\',\'approved\')">Approve</button> <button onclick="review(\''+x.request_id+'\',\'rejected\')">Reject</button></p>').join(''):'<p>No pending approvals.</p>';
$('#audit-list').innerHTML=l.slice(0,5).map(x=>'<p>'+x.event+' · '+x.timestamp+'</p>').join('')||'No events yet.'}
async function review(id,decision){await fetch('/api/approvals/'+id,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({decision,reviewer:'dashboard-user'})});refresh()}
$('#form').addEventListener('submit',async e=>{e.preventDefault();const f=new FormData(e.target);const body={actor:f.get('actor'),role:f.get('role'),action:f.get('action'),resource_type:f.get('resource_type'),resource_id:f.get('resource_id'),payload:{note:f.get('note')}};const res=await fetch('/api/evaluate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});$('#result').textContent=JSON.stringify(await res.json(),null,2);refresh()});refresh();
</script></body></html>"""
