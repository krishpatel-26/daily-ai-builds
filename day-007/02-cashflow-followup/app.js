import {normalizeInvoice,getInvoiceState,priorityScore,summarize} from "./src/domain.js";
import {loadInvoices,saveInvoices,clearInvoices} from "./src/storage.js";
import {toCSV,parseCSV} from "./src/csv.js";
import {draftReminder} from "./src/reminders.js";
import {DEMO_INVOICES} from "./src/demo-data.js";
const $=id=>document.getElementById(id);
let invoices=loadInvoices(), activeDraft="", toastTimer;
const today=()=>new Date().toISOString().slice(0,10);
const money=n=>new Intl.NumberFormat("en-IN",{style:"currency",currency:"INR",maximumFractionDigits:0}).format(n);
function toast(msg){const el=$("toast");el.textContent=msg;el.classList.add("show");clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.classList.remove("show"),2400)}
function persist(){const result=saveInvoices(invoices);if(!result.ok)toast("Could not save locally. Export a backup.");}
function esc(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function render(){
 const summary=summarize(invoices,today());
 $("outstandingMetric").textContent=money(summary.outstanding);$("overdueMetric").textContent=summary.overdueCount;$("weekMetric").textContent=summary.dueSoonCount;$("followupMetric").textContent=summary.followupCount;
 const q=$("searchInput").value.trim().toLowerCase(),filter=$("statusFilter").value,sort=$("sortFilter").value;
 let rows=invoices.filter(i=>(i.client+" "+i.number).toLowerCase().includes(q));
 rows=rows.filter(i=>filter==="all"||getInvoiceState(i,today()).key===filter||(filter==="paid"&&i.status==="paid")||(filter==="open"&&getInvoiceState(i,today()).key==="open"));
 rows.sort((a,b)=>sort==="due"?a.dueDate.localeCompare(b.dueDate):sort==="amount"?b.amount-a.amount:sort==="client"?a.client.localeCompare(b.client):priorityScore(b,today())-priorityScore(a,today()));
 $("recordCount").textContent=rows.length+" invoice"+(rows.length===1?"":"s");
 $("invoiceRows").innerHTML=rows.map(i=>{const s=getInvoiceState(i,today());return `<tr><td><div class="client-name">${esc(i.client)}</div><div class="subtext">${esc(i.number)}</div></td><td>${esc(i.dueDate)}</td><td><span class="status status-${s.key}">${esc(s.label)}</span></td><td class="money">${money(i.amount)}</td><td><button class="action-btn" data-action="draft" data-id="${esc(i.id)}">${i.status==="paid"?"View invoice":"Draft reminder"}</button></td><td><div class="more-actions"><button class="action-btn" data-action="edit" data-id="${esc(i.id)}" aria-label="Edit ${esc(i.number)}">Edit</button><button class="action-btn" data-action="toggle" data-id="${esc(i.id)}">${i.status==="paid"?"Reopen":"Mark paid"}</button></div></td></tr>`}).join("");
 $("emptyState").classList.toggle("visible",rows.length===0);
}
function openForm(invoice){$("invoiceForm").reset();$("editId").value=invoice?.id||"";$("dialogTitle").textContent=invoice?"Edit invoice":"Add invoice";$("clientInput").value=invoice?.client||"";$("numberInput").value=invoice?.number||"";$("amountInput").value=invoice?.amount??"";$("issueInput").value=invoice?.issueDate||today();$("dueInput").value=invoice?.dueDate||today();$("statusInput").value=invoice?.status||"unpaid";$("invoiceDialog").showModal()}
function closeForm(){$("invoiceDialog").close()}
$("addBtn").onclick=()=>openForm();$("emptyAddBtn").onclick=()=>openForm();$("closeDialog").onclick=closeForm;$("cancelDialog").onclick=closeForm;
$("invoiceForm").addEventListener("submit",e=>{e.preventDefault();try{const id=$("editId").value;const row=normalizeInvoice({id,client:$("clientInput").value,number:$("numberInput").value,amount:$("amountInput").value,issueDate:$("issueInput").value,dueDate:$("dueInput").value,status:$("statusInput").value});const duplicate=invoices.some(i=>i.number.toLowerCase()===row.number.toLowerCase()&&i.id!==id);if(duplicate)throw new Error("That invoice number already exists.");invoices=id?invoices.map(i=>i.id===id?row:i):[row,...invoices];persist();render();closeForm();toast("Invoice saved.");}catch(err){toast(err.message)}});
["searchInput","statusFilter","sortFilter"].forEach(id=>$(id).addEventListener(id==="searchInput"?"input":"change",render));
$("invoiceRows").addEventListener("click",e=>{const b=e.target.closest("button[data-action]");if(!b)return;const i=invoices.find(x=>x.id===b.dataset.id);if(!i)return;
 if(b.dataset.action==="edit")openForm(i);
 if(b.dataset.action==="toggle"){i.status=i.status==="paid"?"unpaid":"paid";persist();render();toast(i.status==="paid"?"Marked as paid.":"Invoice reopened.");}
 if(b.dataset.action==="draft"){if(i.status==="paid"){toast("This invoice is already marked paid.");return}activeDraft=draftReminder(i,today());$("draftBox").textContent=activeDraft;$("copyDraftBtn").disabled=false;toast("Reminder draft ready to review.");}
});
$("copyDraftBtn").onclick=async()=>{try{await navigator.clipboard.writeText(activeDraft);toast("Reminder copied.");}catch{const area=document.createElement("textarea");area.value=activeDraft;document.body.append(area);area.select();document.execCommand("copy");area.remove();toast("Reminder copied.");}};
$("exportBtn").onclick=()=>download("cashflow-invoices.csv",toCSV(invoices),"text/csv;charset=utf-8;");
function download(name,content,type){const blob=new Blob([content],{type}),url=URL.createObjectURL(blob),a=document.createElement("a");a.href=url;a.download=name;a.click();URL.revokeObjectURL(url);toast("Export ready.");}
$("importFile").addEventListener("change",async e=>{const file=e.target.files?.[0];if(!file)return;try{const parsed=parseCSV(await file.text());const valid=parsed.map(i=>normalizeInvoice(i));const seen=new Set(invoices.map(i=>i.number.toLowerCase()));const fresh=valid.filter(i=>!seen.has(i.number.toLowerCase()));invoices=[...fresh,...invoices];persist();render();toast(`Imported ${fresh.length} new invoice(s).`)}catch(err){toast("Import failed: "+err.message)}finally{e.target.value=""}});
$("loadDemoBtn").onclick=()=>{const seen=new Set(invoices.map(i=>i.number));invoices=[...invoices,...DEMO_INVOICES.filter(i=>!seen.has(i.number))];persist();render();toast("Demo records added. Sample data is illustrative.");};
$("clearBtn").onclick=()=>{if(!confirm("Delete all invoices stored in this browser? Export a backup first if needed."))return;invoices=[];clearInvoices();activeDraft="";$("draftBox").textContent="Select “Draft reminder” on an invoice to create a message.";$("copyDraftBtn").disabled=true;render();toast("Local records cleared.");};
render();
