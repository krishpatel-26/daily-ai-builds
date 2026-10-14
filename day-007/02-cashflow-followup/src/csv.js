const FIELDS = ["client","number","amount","issueDate","dueDate","status"];
export function escapeCell(value) { const s = String(value ?? ""); return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g,'""') + '"' : s; }
export function toCSV(invoices) { return [FIELDS.join(","), ...invoices.map(row=>FIELDS.map(key=>escapeCell(row[key])).join(","))].join("\r\n"); }
export function parseCSV(text) {
  const rows=[]; let row=[], cell="", quoted=false;
  for(let i=0;i<text.length;i++){const ch=text[i];
    if(quoted){if(ch==='"'&&text[i+1]==='"'){cell+='"';i++;}else if(ch==='"')quoted=false;else cell+=ch;}
    else if(ch==='"'&&cell==="")quoted=true;
    else if(ch===","){row.push(cell);cell="";}
    else if(ch==="\n"){row.push(cell.replace(/\r$/,""));if(row.some(v=>v!==""))rows.push(row);row=[];cell="";}
    else cell+=ch;
  }
  if(quoted) throw new Error("CSV contains an unclosed quoted field.");
  row.push(cell.replace(/\r$/,""));if(row.some(v=>v!==""))rows.push(row);
  if(!rows.length) return [];
  const header=rows.shift().map(v=>v.trim());
  const missing=FIELDS.filter(f=>!header.includes(f));
  if(missing.length) throw new Error("CSV is missing columns: "+missing.join(", "));
  return rows.map((cells,index)=>Object.fromEntries(FIELDS.map(field=>[field,cells[header.indexOf(field)] ?? ""])).valueOf()).map((r,index)=>({...r,amount:Number(r.amount),id:`import-${Date.now()}-${index}`}));
}
export const CSV_FIELDS = FIELDS;
