(() => {
  'use strict';
  const C = window.DeploymentTowerCore;
  const $ = id => document.getElementById(id);
  const STORE = 'fieldops-deployment-tower-v1';
  let workspace = null;
  function esc(value) { return String(value == null ? '' : value).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;'); }
  function toast(message) { const n=$('toast'); n.textContent=message; n.classList.remove('hidden'); clearTimeout(toast.timer); toast.timer=setTimeout(()=>n.classList.add('hidden'),3200); }
  function save() { workspace.updatedAt=new Date().toISOString(); try { localStorage.setItem(STORE,JSON.stringify(workspace)); $('savedIndicator').innerHTML='<i></i> SAVED LOCALLY'; } catch { $('savedIndicator').textContent='LOCAL SAVE FAILED'; toast('Browser storage is unavailable. Export the workspace JSON to keep a copy.'); } }
  function log(type,text) { C.addEvent(workspace,type,text); save(); }
  function loadStored() { try { const raw=localStorage.getItem(STORE); if(raw){workspace=C.normalizeWorkspace(JSON.parse(raw));return;} } catch {} workspace=C.createWorkspace(); save(); }
  function fillProject() { const m=workspace.meta; $('customerName').value=m.customer; $('integrationName').value=m.integration; $('environment').value=m.environment||'Staging'; $('ownerName').value=m.owner; $('targetDate').value=m.targetDate; $('successCriteria').value=m.successCriteria; }
  function stateOptions(current) { return C.STATUS.map(s=>'<option value="'+s+'"'+(s===current?' selected':'')+'>'+({todo:'Not done',pass:'Pass',fail:'Fail',na:'N/A'}[s])+'</option>').join(''); }
  function gateHtml(gate,index) {
    const r=C.getGateStatus(gate);
    let html='<article class="gate-card gate-'+r.status+'" data-gate="'+esc(gate.id)+'"><div class="gate-head"><span class="gate-number">'+String(index+1).padStart(2,'0')+'</span><div class="gate-title-wrap"><div class="gate-title-row"><h3 class="gate-title">'+esc(gate.name)+'</h3><span class="gate-state '+r.status+'">'+r.label+'</span></div><p class="gate-summary">'+esc(gate.summary)+'</p></div></div><div class="gate-progress"><i style="width:'+r.progress+'%"></i></div><div class="gate-checks">';
    gate.checks.forEach(check=>{html+='<div class="check-row" data-check="'+esc(check.id)+'"><div class="check-main"><div class="check-title">'+esc(check.title)+(check.required?'<span class="check-required">REQUIRED</span>':'')+'</div><textarea data-check-evidence placeholder="Evidence: test result, timestamp, request ID, ticket…">'+esc(check.evidence)+'</textarea></div><select data-check-status aria-label="Status for '+esc(check.title)+'">'+stateOptions(check.status)+'</select></div>';});
    html+='</div><div class="gate-footer"><small>'+r.passed+'/'+r.total+' checks satisfied · '+r.evidenceGaps+' evidence gaps</small><button class="button secondary" data-save-gate="'+esc(gate.id)+'">Save checkpoint ✓</button></div></article>';
    return html;
  }
  function renderGates() { $('gatesGrid').innerHTML=workspace.gates.map(gateHtml).join(''); }
  function renderMetrics() {
    const r=C.evaluateWorkspace(workspace);
    $('readinessScore').textContent=r.score; $('readinessTrack').firstElementChild.style.width=r.score+'%';
    $('readinessCaption').textContent=r.decision==='GO-TO-REVIEW'?'All required checks evidenced; accountable owner still approves.':r.failedChecks+' failed check(s) · '+r.openBlockers+' open blocker(s)';
    $('gatesComplete').textContent=r.completeGates+'/'+r.totalGates; $('gatesCaption').textContent=r.blockedGates+' blocked · '+r.evidenceGaps+' evidence gap(s)';
    $('gateMiniBars').innerHTML=r.gateResults.map(g=>'<i class="'+(g.status==='ready'?'done':g.status==='blocked'?'blocked':'')+'" title="'+esc(g.gate.short+': '+g.label)+'"></i>').join('');
    $('openBlockers').textContent=r.openBlockers; $('criticalBlockers').textContent=r.criticalBlockers+' critical';
    $('blockerCaption').textContent=r.openBlockers?'Assign owners and close the highest-impact items.':'No unresolved blockers recorded.';
    $('evidenceGaps').textContent=r.evidenceGaps+r.metaGaps.length; $('evidenceCaption').textContent=r.metaGaps.length?'Missing project context: '+r.metaGaps.join(', '):'Check evidence notes before relying on a pass state.';
    $('blockerSummary').textContent=r.openBlockers+' OPEN';
    $('decisionTag').textContent=r.decision; $('decisionTag').className='decision-tag '+r.decisionStatus;
    $('decisionHeadline').textContent=r.headline; $('decisionDescription').textContent=r.description;
    const reasons=[];
    if(r.criticalBlockers)reasons.push('Resolve '+r.criticalBlockers+' critical blocker(s) before proceeding.');
    if(r.failedChecks)reasons.push(r.failedChecks+' required check(s) are explicitly marked failed.');
    if(r.evidenceGaps)reasons.push(r.evidenceGaps+' passed/failed check(s) need evidence notes.');
    if(r.openBlockers&&!r.criticalBlockers)reasons.push(r.openBlockers+' open blocker(s) still need resolution or explicit acceptance.');
    if(r.metaGaps.length)reasons.push('Complete project context: '+r.metaGaps.join(', ')+'.');
    if(!reasons.length)reasons.push('Record the final accountable go/no-go decision and the post-launch monitoring window.');
    $('decisionReasons').innerHTML=reasons.slice(0,4).map((t,i)=>'<div class="reason-row '+(r.canGo?'good':'')+'"><i></i><span>'+esc(t)+'</span></div>').join('');
  }
  function renderBlockers() {
    const list=$('blockersList'); const sorted=workspace.blockers.slice().sort((a,b)=>(a.status===b.status?({critical:0,high:1,medium:2,low:3}[a.severity]-{critical:0,high:1,medium:2,low:3}[b.severity]):a.status==='open'?-1:1));
    if(!sorted.length){list.innerHTML='<div class="empty-inline">No blockers registered. Add a risk when an integration issue has an owner and next action.</div>';return;}
    list.innerHTML=sorted.map(b=>'<article class="blocker-card" data-blocker="'+esc(b.id)+'"><div class="blocker-top"><span class="blocker-severity sev-'+esc(b.severity)+'">'+esc(b.severity.toUpperCase())+'</span><div class="blocker-info"><h4 class="blocker-title">'+esc(b.title)+'</h4><p class="blocker-desc">'+esc(C.redactText(b.description))+'</p><div class="blocker-meta"><span>'+esc(b.gateId?workspace.gates.find(g=>g.id===b.gateId)?.short||b.gateId:'UNASSIGNED GATE')+'</span><span>DUE '+esc(b.dueDate||'NOT SET')+'</span><span>'+esc(b.status.toUpperCase())+'</span></div></div></div><div class="blocker-controls"><input data-blocker-owner value="'+esc(b.owner)+'" maxlength="80" aria-label="Owner" placeholder="Assign owner"><select data-blocker-severity aria-label="Severity"><option value="critical"'+(b.severity==='critical'?' selected':'')+'>Critical</option><option value="high"'+(b.severity==='high'?' selected':'')+'>High</option><option value="medium"'+(b.severity==='medium'?' selected':'')+'>Medium</option><option value="low"'+(b.severity==='low'?' selected':'')+'>Low</option></select><button data-save-blocker="'+esc(b.id)+'">Save</button><button class="resolve" data-toggle-blocker="'+esc(b.id)+'">'+(b.status==='open'?'Resolve':'Reopen')+'</button></div></article>').join('');
  }
  function renderTimeline() {
    const list=$('timelineList'); const events=workspace.events.slice(0,14);
    if(!events.length){list.innerHTML='<div class="empty-inline">No events recorded yet.</div>';return;}
    list.innerHTML=events.map(e=>{const date=new Date(e.createdAt);const t=Number.isNaN(date.getTime())?'—':date.toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'});return '<div class="timeline-item"><time class="timeline-time">'+esc(t)+'</time><div class="timeline-event '+esc(e.type)+'"><strong>'+esc(e.type==='decision'?'Decision':e.type==='test'?'Test result':e.type==='customer'?'Customer update':e.type==='blocker'?'Blocker':'Update')+'</strong><span class="event-type">'+esc(e.type.toUpperCase())+'</span><p>'+esc(C.redactText(e.text))+'</p></div></div>';}).join('');
  }
  function renderAll() { renderGates(); renderMetrics(); renderBlockers(); renderTimeline(); }
  function download(name,content,type) { const blob=new Blob([content],{type}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download=name; document.body.append(a); a.click(); a.remove(); setTimeout(()=>URL.revokeObjectURL(url),500); }
  function exportSafeWorkspace() { const copy=JSON.parse(JSON.stringify(workspace)); const mapText=v=>typeof v==='string'?C.redactText(v):v; copy.meta=Object.fromEntries(Object.entries(copy.meta).map(([k,v])=>[k,mapText(v)])); copy.blockers=copy.blockers.map(b=>({...b,title:mapText(b.title),description:mapText(b.description),owner:mapText(b.owner)})); copy.gates=copy.gates.map(g=>({...g,checks:g.checks.map(c=>({...c,evidence:mapText(c.evidence)}))})); copy.events=copy.events.map(e=>({...e,text:mapText(e.text)})); return copy; }
  $('projectForm').addEventListener('submit',event=>{event.preventDefault();const previous=JSON.stringify(workspace.meta);workspace.meta={customer:$('customerName').value.trim(),integration:$('integrationName').value.trim(),environment:$('environment').value,owner:$('ownerName').value.trim(),targetDate:$('targetDate').value,successCriteria:$('successCriteria').value.trim()};if(JSON.stringify(workspace.meta)!==previous)log('update','Deployment context saved for '+(workspace.meta.customer||'unnamed customer')+' / '+(workspace.meta.integration||'unnamed integration')+'.');save();renderMetrics();$('projectMessage').textContent='Deployment context saved in this browser.';toast('Deployment context saved.');});
  $('loadDemoBtn').addEventListener('click',()=>{workspace=C.createDemoWorkspace();fillProject();save();renderAll();$('projectMessage').textContent='Demo case loaded; all customer and event data is synthetic.';toast('Demo workspace loaded.');});
  $('newWorkspaceBtn').addEventListener('click',()=>{if(!confirm('Start a new workspace? Export the current deployment first if you need to keep it.'))return;workspace=C.createWorkspace();fillProject();save();renderAll();$('projectMessage').textContent='New blank workspace created.';toast('New workspace created.');});
  $('gatesGrid').addEventListener('click',event=>{const btn=event.target.closest('[data-save-gate]');if(!btn)return;const id=btn.dataset.saveGate;const gate=workspace.gates.find(g=>g.id===id);const card=btn.closest('[data-gate]');card.querySelectorAll('[data-check]').forEach(row=>{C.setCheck(workspace,id,row.dataset.check,row.querySelector('[data-check-status]').value,row.querySelector('[data-check-evidence]').value);});const result=C.getGateStatus(gate);log(result.status==='ready'?'test':result.status==='blocked'?'decision':'update','Checkpoint saved: '+gate.name+' — '+result.label+' ('+result.passed+'/'+result.total+' satisfied; '+result.evidenceGaps+' evidence gaps).');save();renderAll();toast(gate.name+' checkpoint saved.');});
  $('blockerForm').addEventListener('submit',event=>{event.preventDefault();try{const b=C.addBlocker(workspace,{title:$('blockerTitle').value,description:$('blockerDescription').value,severity:$('blockerSeverity').value,owner:$('blockerOwner').value,dueDate:$('blockerDue').value,gateId:$('blockerGate').value});$('blockerForm').reset();save();renderAll();toast('Blocker registered: '+b.title);}catch(e){toast(e.message);}});
  $('blockersList').addEventListener('click',event=>{const saveBtn=event.target.closest('[data-save-blocker]');const toggleBtn=event.target.closest('[data-toggle-blocker]');if(!saveBtn&&!toggleBtn)return;const id=(saveBtn||toggleBtn).dataset.saveBlocker||(toggleBtn&&toggleBtn.dataset.toggleBlocker);const card=(saveBtn||toggleBtn).closest('[data-blocker]');const b=workspace.blockers.find(x=>x.id===id);if(!b)return;if(saveBtn){C.updateBlocker(workspace,id,{owner:card.querySelector('[data-blocker-owner]').value,severity:card.querySelector('[data-blocker-severity]').value});C.addEvent(workspace,'update','Blocker ownership/severity updated: '+b.title);toast('Blocker updated.');}else{C.updateBlocker(workspace,id,{status:b.status==='open'?'resolved':'open'});toast(b.status==='resolved'?'Blocker resolved.':'Blocker reopened.');}save();renderAll();});
  $('blockersList').addEventListener('change',event=>{const sev=event.target.closest('[data-blocker-severity]');if(!sev)return;const card=sev.closest('[data-blocker]');const b=workspace.blockers.find(x=>x.id===card.dataset.blocker);if(b){b.severity=sev.value;save();renderMetrics();}});
  $('eventForm').addEventListener('submit',event=>{event.preventDefault();try{log($('eventType').value,$('eventText').value);$('eventText').value='';renderTimeline();toast('Timeline entry recorded.');}catch(e){toast(e.message);}});
  $('exportHandoffBtn').addEventListener('click',()=>download('customer-deployment-handoff.md',C.buildHandoff(exportSafeWorkspace()),'text/markdown'));
  $('exportRunbookBtn').addEventListener('click',()=>download('deployment-next-step-runbook.md',C.buildRunbook(exportSafeWorkspace()),'text/markdown'));
  $('exportJsonBtn').addEventListener('click',()=>download('fde-deployment-workspace.json',JSON.stringify(exportSafeWorkspace(),null,2),'application/json'));
  function setupGateSelect(){ $('blockerGate').innerHTML='<option value="">Unassigned</option>'+C.GATES.map(g=>'<option value="'+esc(g.id)+'">'+esc(g.short)+'</option>').join(''); }
  loadStored(); setupGateSelect(); fillProject(); renderAll();
})();