export function retryAfterSeconds(retryAfterMs){
 const value=Number(retryAfterMs);
 if(!Number.isFinite(value)||value<=0)return 0;
 return Math.ceil(value/1000);
}
export function formatRetryAfter(retryAfterMs){return retryAfterSeconds(retryAfterMs)+"s";}
export function parseRetryAfter(value,nowMs=Date.now()){
 const text=String(value??"").trim();if(!text)return null;
 if(/^\d+(?:\.\d+)?$/.test(text))return Math.max(0,Math.ceil(Number(text)*1000));
 const date=Date.parse(text);if(Number.isNaN(date))return null;
 return Math.max(0,date-Number(nowMs));
}
