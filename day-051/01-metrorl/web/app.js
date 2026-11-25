const $=s=>document.querySelector(s),labels={fixed_time:'FIXED TIME',max_pressure:'MAX PRESSURE',q_learning:'Q-LEARNING'};
const numeral=v=>Number(v).toLocaleString(undefined,{maximumFractionDigits:2});
fetch('/api/report').then(r=>r.json()).then(d=>{
const b=d.comparison, t=d.training;
$('#stats').innerHTML=[['TRAINING EPISODES',t.episodes],['LEARNED STATES',t.states_learned],['INTERSECTIONS',3],['EVALUATION SEEDS',b.q_learning.exits.n]].map(([k,v])=>`<div class="stat"><small>${k}</small><strong>${numeral(v)}</strong></div>`).join('');
const max=Math.max(...Object.values(b).map(x=>x.exits.mean));
$('#policies').innerHTML=Object.entries(b).map(([key,value])=>`<div class="policy"><div><b>${labels[key]}</b><small>Queue ${value.mean_queue.mean}</small></div><div class="meter"><i style="width:${100*value.exits.mean/Math.max(1,max)}%"></i></div><strong>${numeral(value.exits.mean)}</strong></div>`).join('');
const names=['fixed_time','max_pressure','q_learning'];const traces=names.map(n=>d.examples[n].trace);const length=Math.min(...traces.map(x=>x.length));const every=Math.max(1,Math.ceil(length/35));const values=traces.flat().map(v=>v.total_queue);const high=Math.max(1,...values);
$('#chart').innerHTML=Array.from({length:Math.ceil(length/every)},(_,i)=>`<div class="barstack">${names.map((name,k)=>`<i class="${'abc'[k]}" title="${labels[name]}: ${traces[k][i*every].total_queue}" style="height:${Math.max(2,100*traces[k][i*every].total_queue/high)}%"></i>`).join('')}</div>`).join('');
$('#training').innerHTML=[['EPISODES',t.episodes],['STATES VISITED',t.states_learned],['EARLY QUEUE',t.first_20_episode_mean_queue],['LATE QUEUE',t.last_20_episode_mean_queue]].map(([k,v])=>`<div><small>${k}</small><strong>${numeral(v)}</strong></div>`).join('')
}).catch(e=>{$('#stats').textContent='Simulation unavailable: '+e.message});
