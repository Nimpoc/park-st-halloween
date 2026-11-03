/* Three presentations, one notebook and one set of interactions. */
(function(){
'use strict';
const root=document.documentElement,button=document.getElementById('style-switcher'),dialog=document.getElementById('style-dialog');
const labels={almanac:'Almanac',compact:'Fieldwork',glass:'Liquid Glass'};
function updateLabel(){const theme=root.dataset.theme||'almanac';document.getElementById('current-style').textContent=labels[theme];document.title=theme==='almanac'?'After dark on Park Street':labels[theme]+' · Park Street Halloween';document.querySelectorAll('[data-style-choice]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.styleChoice===theme));}
function applyStyle(theme){if(!Object.hasOwn(labels,theme))return;root.dataset.theme=theme;try{localStorage.setItem('park-street.style',theme);}catch(e){}const url=new URL(location.href);url.searchParams.set('style',theme);history.replaceState(null,'',url);updateLabel();updateSystemAppearance();window.dispatchEvent(new Event('resize'));document.dispatchEvent(new CustomEvent('porch:stylechange',{detail:{theme}}));}
function updateSystemAppearance(){const dark=matchMedia('(prefers-color-scheme: dark)').matches;document.querySelector('meta[name="theme-color"]').content=dark?'#15191d':root.dataset.theme==='compact'?'#f5f7f6':root.dataset.theme==='glass'?'#eef2f7':'#f6f2e9';document.getElementById('appearance-status').textContent='Follows your device · '+(dark?'Dark':'Light');window.dispatchEvent(new Event('resize'));}
button.onclick=()=>{updateLabel();updateSystemAppearance();dialog.showModal();button.setAttribute('aria-expanded','true');};
document.getElementById('close-style').onclick=()=>dialog.close();
dialog.addEventListener('close',()=>{button.setAttribute('aria-expanded','false');button.focus();});
dialog.addEventListener('click',e=>{if(e.target===dialog){const rect=dialog.getBoundingClientRect();if(e.clientX<rect.left||e.clientX>rect.right||e.clientY<rect.top||e.clientY>rect.bottom)dialog.close();}});
document.querySelectorAll('[data-style-choice]').forEach(b=>b.onclick=()=>{applyStyle(b.dataset.styleChoice);dialog.close();});
matchMedia('(prefers-color-scheme: dark)').addEventListener('change',updateSystemAppearance);
updateLabel();updateSystemAppearance();
})();
