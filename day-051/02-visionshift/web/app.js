const $=s=>document.querySelector(s),names={baseline:'NO NEW LABELS',random:'RANDOM',uncertainty:'UNCERTAINTY',diversity:'DIVERSITY'};
fetch('/api/report').then(r=>r.json()).then(d=>{
const e=d.example,b=d.benchmark;$('#stats').innerHTML=[['SHIFTED BASELINE F1',e.shifted_baseline.f1],['STABLE BASELINE F1',e.stable_baseline.f1],['LABEL BUDGET',e.budget],['BENCHMARK SEEDS',b.random.trials]].map(([k,v])=>`<div class="stat"><small>${k}</small><strong>${v}</strong></div>`).join('');
const highest=Math.max(.01,...Object.values(b).map(x=>x.mean_f1));
$('#methods').innerHTML=Object.entries(b).map(([k,v])=>`<div class="method"><b>${names[k]}</b><div class="meter"><i style="width:${100*v.mean_f1/highest}%"></i></div><strong>${v.mean_f1}</strong></div>`).join('');
const max=Math.max(.01,...Object.values(e.feature_psi));$('#drift').innerHTML=Object.entries(e.feature_psi).map(([k,v])=>`<div class="drift"><b>${k.toUpperCase()}</b><div class="meter"><i style="width:${100*v/max}%"></i></div><strong>${v}</strong></div>`).join('');
$('#review').innerHTML=e.review_candidates.map(x=>`<div class="sample"><strong>${x.id.split('-').slice(-1)}</strong><small>VECTOR ${x.features.map(f=>f.toFixed(1)).join(' · ')}</small><span>${Math.round(x.uncertainty*100)}% uncertainty</span></div>`).join('')
}).catch(e=>{$('#stats').textContent='Experiment unavailable: '+e.message});
