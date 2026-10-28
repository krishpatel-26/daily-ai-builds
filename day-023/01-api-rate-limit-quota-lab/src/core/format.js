export function formatMs(value){
 const ms=Math.max(0,Number(value)||0);
 if(ms<1000)return Math.round(ms)+" ms";
 if(ms<60000)return (ms/1000).toFixed(ms%1000===0?0:1)+" s";
 return (ms/60000).toFixed(1)+" min";
}
export function percent(numerator,denominator){return denominator?Math.round(Number(numerator)/Number(denominator)*100)+"%":"0%";}
export function safeFileName(value){return String(value??"export").toLowerCase().replace(/[^a-z0-9._-]+/g,"-").replace(/^-+|-+$/g,"").slice(0,100)||"export";}
