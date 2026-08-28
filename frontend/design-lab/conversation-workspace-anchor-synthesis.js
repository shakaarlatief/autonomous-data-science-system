const root = document.documentElement;
const compositionSelect = document.querySelector('#composition-select');
const depthSelect = document.querySelector('#depth-select');
const expandHome = document.querySelector('#expand-home');
const closeX5 = document.querySelector('#close-x5');
const threadList = document.querySelector('#thread-list');
const archiveList = document.querySelector('#archive-list');
const title = document.querySelector('#conversation-title');
const subtitle = document.querySelector('#conversation-subtitle');
const scopePill = document.querySelector('#scope-pill');
const scopeCopy = document.querySelector('#scope-copy');
const floatingHome = document.querySelector('#floating-home');
const breadcrumbAnchor = document.querySelector('#breadcrumb-anchor');
const arrivalShelf = document.querySelector('#arrival-shelf');
const objectGutter = document.querySelector('#object-gutter');
const gutterButton = document.querySelector('#gutter-button');
const wrappedLabel = document.querySelector('#wrapped-label');
const homeChip = document.querySelector('#home-chip');
const x5Box = document.querySelector('#x5-box');
const x5Title = document.querySelector('#x5-title');
const x5Purpose = document.querySelector('#x5-purpose');
const x5Constraint = document.querySelector('#x5-constraint');
const x5Next = document.querySelector('#x5-next');

const storageKey = 'ads-conversation-sidebar-view';
const categories = {
  model: { kind:'MODEL WORK', rgb:'233,132,122', color:'var(--model)', glyph:'<svg viewBox="0 0 16 16"><path d="M8 3.2 12.8 8 8 12.8 3.2 8z"/></svg>' },
  investigation: { kind:'INVESTIGATION', rgb:'103,218,194', color:'var(--investigation)', glyph:'<svg viewBox="0 0 16 16"><rect x="4" y="4" width="8" height="8"/></svg>' },
  validation: { kind:'VALIDATION', rgb:'142,169,255', color:'var(--validation)', glyph:'<svg viewBox="0 0 16 16"><path d="M8 3.3 12.6 12H3.4z"/></svg>' },
  evaluation: { kind:'EVALUATION', rgb:'173,150,255', color:'var(--evaluation)', glyph:'<svg viewBox="0 0 16 16"><path d="M8 3v10M3 8h10"/></svg>' },
};

const threads = [
  { id:'project', type:'project', title:'General project discussion', meta:'6 min ago · 27 messages' },
  { id:'model', type:'work', category:'model', disposition:'CURRENT', status:'RUN', priority:true, statusRgb:'103,218,194', title:'Model selection strategy', subtitle:'Compare candidate families under one frozen validation protocol.', meta:'12 min ago · 43 messages', purpose:'Compare candidate model families under one frozen validation protocol.', constraint:'Do not let deployment selection collapse the learning-oriented comparison set.', next:'Complete comparable evaluation and record selection logic.' },
  { id:'missing', type:'work', category:'investigation', disposition:'CURRENT', status:'BLOCKED', priority:false, statusRgb:'237,112,105', title:'Production missingness', subtitle:'Blocked by unresolved upstream work.', meta:'Yesterday · 31 messages', purpose:'Determine how production missingness differs from development data.', constraint:'Upstream data contract remains unresolved.', next:'Resolve data contract, then rerun missingness profile.' },
  { id:'threshold', type:'work', category:'validation', disposition:'DEFER', status:'NONE', priority:false, statusRgb:'145,158,179', title:'Threshold policy', subtitle:'Deferred threshold decision.', meta:'Aug 25 · 18 messages', purpose:'Define an explicit operating threshold policy after model comparison.', constraint:'Model family and calibration evidence are not yet final.', next:'Reopen after calibration review.' },
];

const archived = [
  { id:'eda', type:'work', category:'investigation', disposition:'COMPLETE', status:'NONE', historical:true, title:'EDA interpretation', subtitle:'Historical work-unit state at archive time.', meta:'Aug 18' },
  { id:'baseline', type:'work', category:'evaluation', disposition:'COMPLETE', status:'NONE', historical:true, title:'Baseline review', subtitle:'Historical work-unit state at archive time.', meta:'Aug 15' },
];

let activeId = 'model';
let sidebarView = getStoredView();

render();
setup();

function setup(){
  compositionSelect.addEventListener('change', e=>setComposition(e.target.value));
  depthSelect.addEventListener('change', e=>setDepth(e.target.value));
  document.querySelectorAll('[data-composition]').forEach(btn=>btn.addEventListener('click',()=>setComposition(btn.dataset.composition)));
  document.querySelectorAll('[data-sidebar]').forEach(btn=>btn.addEventListener('click',()=>setSidebar(btn.dataset.sidebar)));
  expandHome.addEventListener('click',()=>{
    if(root.dataset.home==='project') return;
    const expanded = root.dataset.expanded!=='true';
    root.dataset.expanded=String(expanded);
    expandHome.textContent=expanded?'Collapse box':'Expand box';
  });
  closeX5.addEventListener('click',()=>{root.dataset.expanded='false';expandHome.textContent='Expand box';});
  gutterButton.addEventListener('click',()=>{
    if(root.dataset.home==='project') return;
    root.dataset.expanded='true';
    setComposition('a6');
    expandHome.textContent='Collapse box';
  });
}

function render(){
  renderThreads();
  setSidebar(sidebarView,false);
  setComposition(root.dataset.composition||'a6');
  setDepth(root.dataset.depth||'arrival');
  setActive(activeId);
}

function renderThreads(){
  threadList.innerHTML=threads.map(threadMarkup).join('');
  archiveList.innerHTML=archived.map(threadMarkup).join('');
  [...threadList.querySelectorAll('[data-thread]')].forEach(btn=>btn.addEventListener('click',()=>setActive(btn.dataset.thread)));
}

function threadMarkup(t){
  const active=t.id===activeId?' active':'';
  if(t.type==='project'){
    return `<button class="thread-item${active}" data-thread="${t.id}" style="--thread-color:var(--accent)">
      <span class="box-view project-row"><span class="project-symbol">ADS</span><span><small>PROJECT GENERAL</small><strong>${t.title}</strong></span></span>
      <span class="text-view text-thread"><i></i><span><strong>${t.title}</strong><small>${t.meta}</small></span></span>
    </button>`;
  }
  const c=categories[t.category];
  const status=t.status!=='NONE'?`<span class="status-dot ${t.status==='BLOCKED'?'blocked':''}" style="--status-rgb:${t.statusRgb}"></span>`:'';
  const bars=t.priority?'<span class="bars"><i></i><i></i><i></i></span>':'';
  return `<button class="thread-item${active}${t.historical?' historical':''}" data-thread="${t.id}" style="--thread-color:${c.color}">
    <span class="box-view rail-box" style="--rgb:${c.rgb};--status-rgb:${t.statusRgb||'145,158,179'}"><span class="top"><span class="shape">${c.glyph}</span>${c.kind} · ${t.disposition}</span>${bars}<strong>${t.title}</strong><small>${t.subtitle}</small>${status}</span>
    <span class="text-view text-thread"><i></i><span><strong>${t.title}</strong><small>${t.meta}</small></span></span>
  </button>`;
}

function setSidebar(mode,persist=true){
  sidebarView=mode==='text'?'text':'boxes';
  root.dataset.sidebarView=sidebarView;
  document.querySelectorAll('[data-sidebar]').forEach(btn=>btn.setAttribute('aria-pressed',String(btn.dataset.sidebar===sidebarView)));
  document.querySelectorAll('.box-view').forEach(el=>el.style.display=sidebarView==='boxes'?'grid':'none');
  document.querySelectorAll('.text-view').forEach(el=>el.style.display=sidebarView==='text'?'grid':'none');
  if(persist){try{localStorage.setItem(storageKey,sidebarView)}catch{}}
}

function getStoredView(){try{return localStorage.getItem(storageKey)==='text'?'text':'boxes'}catch{return 'boxes'}}

function setComposition(mode){
  root.dataset.composition=mode;
  root.dataset.expanded='false';
  expandHome.textContent='Expand box';
  compositionSelect.value=mode;
  document.querySelectorAll('[data-composition]').forEach(btn=>btn.setAttribute('aria-pressed',String(btn.dataset.composition===mode)));
}

function setDepth(depth){root.dataset.depth=depth;depthSelect.value=depth;}

function setActive(id){
  activeId=id;
  document.querySelectorAll('[data-thread]').forEach(btn=>btn.classList.toggle('active',btn.dataset.thread===id));
  const t=threads.find(x=>x.id===id) || threads[1];
  root.dataset.home=t.type==='project'?'project':'work';
  root.dataset.expanded='false';
  expandHome.textContent='Expand box';
  title.textContent=t.title;
  if(t.type==='project'){
    root.style.setProperty('--home-rgb','105,217,194');
    scopePill.textContent='PROJECT GENERAL';
    subtitle.textContent='Project-level conversation with no single work-unit home.';
    scopeCopy.innerHTML='This conversation belongs to the <strong>project as a whole</strong>. Work units can be referenced or pinned without silently becoming its home.';
    breadcrumbAnchor.innerHTML='<span>Autonomous Data Science</span> → <strong>General project discussion</strong>';
    arrivalShelf.innerHTML='<div class="project-row"><span class="project-symbol">ADS</span><span><small>PROJECT GENERAL</small><strong>Autonomous Data Science · Telco churn</strong></span></div>';
    floatingHome.innerHTML='';
    wrappedLabel.textContent='PROJECT GENERAL · AUTONOMOUS DATA SCIENCE';
    homeChip.textContent='Autonomous Data Science project';
    gutterButton.setAttribute('aria-label','Project-level conversation');
    x5Title.textContent='No work-unit home';x5Box.innerHTML='';x5Purpose.textContent='';x5Constraint.textContent='';x5Next.textContent='';
    expandHome.style.display='none';
    return;
  }
  const c=categories[t.category];
  root.style.setProperty('--home-rgb',c.rgb);
  scopePill.textContent='WORK UNIT';
  subtitle.textContent=`Conversation anchored to ${t.title}. Other project objects may be referenced without changing its home.`;
  scopeCopy.innerHTML=`This conversation is explicitly anchored to <strong>${t.title}</strong>. Its home remains stable while temporary and pinned context can include other project objects.`;
  const box=homeBox(t);
  floatingHome.innerHTML=box;
  arrivalShelf.innerHTML=`<div class="shelf-box">${box}</div>`;
  breadcrumbAnchor.innerHTML=`<span>Autonomous Data Science</span> → <span>${c.kind}</span> → <strong>${t.title}</strong>`;
  wrappedLabel.textContent=`${c.kind} · ${t.title}`;
  homeChip.textContent=`${c.kind} · ${t.title}`;
  gutterButton.style.setProperty('--home-rgb',c.rgb);
  gutterButton.setAttribute('aria-label',`Open ${t.title}`);
  x5Title.textContent=t.title;
  x5Box.innerHTML=box;
  x5Purpose.textContent=t.purpose||t.subtitle;
  x5Constraint.textContent=t.constraint||'No active constraint recorded.';
  x5Next.textContent=t.next||'Review historical work-unit state.';
  expandHome.style.display=root.dataset.composition==='a6'?'inline-block':'none';
}

function homeBox(t){
  const c=categories[t.category];
  const status=t.status!=='NONE'?`<span class="status-dot ${t.status==='BLOCKED'?'blocked':''}" style="--status-rgb:${t.statusRgb}"></span>`:'';
  const bars=t.priority?'<span class="bars"><i></i><i></i><i></i></span>':'';
  return `<div class="rail-box" style="--rgb:${c.rgb};--status-rgb:${t.statusRgb||'145,158,179'}"><span class="top"><span class="shape">${c.glyph}</span>${c.kind} · ${t.disposition}</span>${bars}<strong>${t.title}</strong><small>${t.subtitle}</small>${status}</div>`;
}
