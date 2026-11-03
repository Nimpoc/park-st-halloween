/* Pure data functions shared by the page and validation tests. */
(function(root){
'use strict';
const minute=t=>{const [h,m]=t.split(':').map(Number);return h*60+m};
const total=r=>r.sourceTotal??r.estimate??null;
const sum=r=>r.intervals?.length?r.intervals.reduce((n,p)=>n+p.count,0):null;
const approximate=r=>!!r.sourceApproximate||(r.sourceTotal==null&&r.estimate!=null);
function validate(r){
 if(!r||!Number.isInteger(r.year)||r.year<1900||r.year>2200)throw Error('Choose a year between 1900 and 2200.');
 for(const k of ['sourceTotal','estimate','computedInterpretation'])if(r[k]!=null&&(!Number.isSafeInteger(r[k])||r[k]<0||r[k]>1000000))throw Error('Totals must be whole numbers from 0 to 1,000,000, or blank.');
 if(typeof r.sourceApproximate!=='boolean')throw Error('Choose a total precision.');
 if(!['high','medium','low','unknown'].includes(r.confidence))throw Error('Choose a source review status.');
 for(const k of ['notes','handwrittenWeather'])if(typeof r[k]!=='string'||r[k].length>30000)throw Error('Weather or notes are too long or missing.');
 if(!Array.isArray(r.intervals)||r.intervals.length>300)throw Error('Use at most 300 time intervals.');
 let end=-1;
 for(const p of r.intervals){if(!p||!/^([01]\d|2[0-3]):[0-5]\d$/.test(p.time)||!Number.isInteger(p.minutes)||p.minutes<1||p.minutes>1440||!Number.isSafeInteger(p.count)||p.count<0||p.count>1000000)throw Error('Each time needs a valid start, positive duration, and whole visitor count.');const t=minute(p.time);if(t<end||t+p.minutes>1440)throw Error('Time intervals must be in order, without overlaps, and end before midnight.');end=t+p.minutes;}
 if(r.sourceImages!=null&&(!Array.isArray(r.sourceImages)||r.sourceImages.length>20||r.sourceImages.some(i=>!i||typeof i.name!=='string'||typeof i.src!=='string'||!(/^(data:image\/(jpeg|png|webp);base64,|sources\/[a-zA-Z0-9_.-]+$)/.test(i.src)))))throw Error('Sheet pictures must be JPEG, PNG or WebP images.');
 return r;
}
function validateOverrides(value){if(!value||typeof value!=='object'||Array.isArray(value)||Object.keys(value).length>301)throw Error('This is not a valid notebook backup.');const out={};for(const[k,r]of Object.entries(value)){validate(r);if(String(r.year)!==k)throw Error('A year does not match its record.');out[k]=r;}return out;}
function readBackup(data){if(!data||![1,2].includes(data.schemaVersion))throw Error('This backup format is not recognized.');return validateOverrides(data.overrides);}
function csvParse(text){const rows=[];let row=[],field='',quote=false;for(let i=0;i<text.length;i++){const c=text[i];if(c==='"'){if(quote&&text[i+1]==='"'){field+='"';i++;}else quote=!quote;}else if(c===','&&!quote){row.push(field);field='';}else if((c==='\n'||c==='\r')&&!quote){if(c==='\r'&&text[i+1]==='\n')i++;row.push(field);if(row.some(x=>x.trim()))rows.push(row);row=[];field='';}else field+=c;}if(quote)throw Error('An opening quote in the CSV has no closing quote.');row.push(field);if(row.some(x=>x.trim()))rows.push(row);return rows;}
function csvRecords(text,getRecord){const rows=csvParse(text.replace(/^\uFEFF/,''));if(rows.length<2)throw Error('The CSV needs a header and at least one count.');const head=rows.shift().map(s=>s.trim().toLowerCase());if(!['year','time','count'].every(k=>head.includes(k)))throw Error('CSV columns must include year, time and count.');const grouped={};for(const row of rows){const get=k=>row[head.indexOf(k)]?.trim();const year=Number(get('year'));if(!get('year')||!get('time')||!get('count'))throw Error('Every CSV row needs a year, time and count.');(grouped[year]??=[]).push({time:get('time'),count:Number(get('count')),minutes:get('minutes')?Number(get('minutes')):15});}const out={};for(const[y,intervals]of Object.entries(grouped)){const r={...getRecord(Number(y)),intervals};validate(r);out[y]=r;}return out;}
function segments(r,mode){const result=[];let current=[],end=null,acc=0;for(const p of r.intervals){const start=minute(p.time);if(end!==null&&start!==end){if(current.length)result.push(current);current=[];}if(mode==='cumulative'){if(!current.length)current.push({x:start,y:acc});acc+=p.count;current.push({x:start+p.minutes,y:acc});}else{current.push({x:start,y:p.count*15/p.minutes},{x:start+p.minutes,y:p.count*15/p.minutes});}end=start+p.minutes;}if(current.length)result.push(current);return result;}
const api={minute,total,sum,approximate,validate,validateOverrides,readBackup,csvRecords,segments};root.PorchModel=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
