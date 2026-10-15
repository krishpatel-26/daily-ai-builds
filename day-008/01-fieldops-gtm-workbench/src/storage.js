const KEY="fieldops-workbench:v1";
export function loadSignals(storage=globalThis.localStorage){try{const v=JSON.parse(storage?.getItem(KEY)||"[]");return Array.isArray(v)?v:[]}catch{return []}}
export function saveSignals(signals,storage=globalThis.localStorage){try{storage?.setItem(KEY,JSON.stringify(signals));return {ok:true}}catch{return {ok:false}}}
export function clearSignals(storage=globalThis.localStorage){try{storage?.removeItem(KEY);return true}catch{return false}}
