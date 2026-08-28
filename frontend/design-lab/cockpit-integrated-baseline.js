const root = document.documentElement;
const cockpit = document.getElementById('cockpit');
const viewport = document.getElementById('map-viewport');
const world = document.getElementById('world');
const projectPlane = document.getElementById('project-plane');
const specialist = document.getElementById('specialist');
const conversation = document.getElementById('conversation-workspace');
const x5Panel = document.getElementById('x5-panel');
const selectionActions = document.getElementById('selection-actions');
const selectionTitle = document.getElementById('selection-title');
const surfaceCrumb = document.getElementById('surface-crumb');
const hudStatus = document.getElementById('hud-status');
const compactComposer = document.getElementById('compact-composer');
const composerContextLabel = document.getElementById('composer-context-label');
const transitionLayer = document.getElementById('transition-layer');
const conversationBoxPanel = document.getElementById('conversation-box-panel');

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const units = {
  'data-question': {
    title: 'Data quality scope',
    category: 'QUESTION / BLOCKER',
    scope: 'Framing',
    purpose: 'Define which data-quality questions require explicit project work.',
    constraint: 'Do not treat missingness as one generic preprocessing problem.',
    evidence: 'Missingness profile · schema review.',
    next: 'Resolve production-impacting gaps before deployment evaluation.'
  },
  missingness: {
    title: 'Production missingness',
    category: 'INVESTIGATION',
    scope: 'Investigation',
    purpose: 'Determine whether unresolved upstream data gaps block deployment-grade evaluation.',
    constraint: 'The cause must remain explicit rather than hidden in preprocessing.',
    evidence: 'Missingness profile · upstream contract evidence.',
    next: 'Resolve the blocker or establish an admissible handling rule.'
  },
  'model-selection': {
    title: 'Model selection strategy',
    category: 'MODEL WORK',
    scope: 'Model Work',
    purpose: 'Compare candidate model families under one frozen validation protocol.',
    constraint: 'Keep learning breadth separate from final deployment selection.',
    evidence: 'Chronological validation · linked model results.',
    next: 'Complete comparable evaluation and document selection logic.'
  },
  threshold: {
    title: 'Threshold policy',
    category: 'VALIDATION / ANALYSIS',
    scope: 'Validation',
    purpose: 'Define a decision threshold only after comparative model evidence is stable.',
    constraint: 'Do not tune policy against the final holdout.',
    evidence: 'Calibration and cost-sensitive metrics.',
    next: 'Revisit after model-family comparison is closed.'
  },
  evaluation: {
    title: 'Final evaluation',
    category: 'EVALUATION',
    scope: 'Evaluation',
    purpose: 'Evaluate the selected candidate under deployment-relevant metrics.',
    constraint: 'Use the frozen evaluation contract.',
    evidence: 'Final holdout · calibration · threshold policy.',
    next: 'Run only after model and threshold decisions are frozen.'
  },
  chronological: {
    title: 'Chronological validation',
    category: 'VALIDATION / ANALYSIS',
    scope: 'Evidence',
    purpose: 'Provide one comparable validation frame across candidate models.',
    constraint: 'Preserve chronological separation.',
    evidence: 'Frozen split specification.',
    next: 'Reuse as evidence for model selection.'
  }
};

const threadMeta = {
  general: {
    title: 'General project discussion',
    scope: 'PROJECT',
    subtitle: 'Project-level conversation with no single work-unit home.',
    home: null
  },
  'model-selection': {
    title: 'Model selection strategy',
    scope: 'WORK UNIT',
    subtitle: 'Conversation anchored to one project work unit.',
    home: 'model-selection'
  },
  missingness: {
    title: 'Production missingness',
    scope: 'WORK UNIT',
    subtitle: 'Conversation anchored to the active investigation.',
    home: 'missingness'
  },
  threshold: {
    title: 'Threshold policy',
    scope: 'WORK UNIT',
    subtitle: 'Conversation anchored to the deferred validation work unit.',
    home: 'threshold'
  }
};

let selectedUnit = null;
let expandedUnit = null;
let zoom = 1;
let preChatMode = 'map';
let activeThread = 'model-selection';
let specialistUnit = 'model-selection';
let chatSplit = false;

function setHudSurface(label, title, status) {
  surfaceCrumb.querySelector('span').textContent = label;
  surfaceCrumb.querySelector('strong').textContent = title;
  hudStatus.textContent = status;
}

function updateWorldTransform() {
  world.style.transform = `scale(${zoom})`;
  document.getElementById('zoom-label').textContent = `${Math.round(zoom * 100)}%`;
}

function clampZoom(next) {
  return Math.min(1.35, Math.max(.55, next));
}

function setZoom(next) {
  zoom = clampZoom(next);
  updateWorldTransform();
}

function getNode(unitId) {
  return document.querySelector(`.work-unit[data-unit="${unitId}"]`);
}

function clearSelection() {
  document.querySelectorAll('.work-unit.selected').forEach(node => node.classList.remove('selected'));
  selectedUnit = null;
  expandedUnit = null;
  selectionActions.hidden = true;
  x5Panel.hidden = true;
  composerContextLabel.textContent = 'Project-aware';
}

function selectUnit(unitId, { scroll = false } = {}) {
  const node = getNode(unitId);
  if (!node) return;
  document.querySelectorAll('.work-unit.selected').forEach(item => item.classList.remove('selected'));
  node.classList.add('selected');
  selectedUnit = unitId;
  const meta = units[unitId];
  selectionTitle.textContent = meta.title;
  composerContextLabel.textContent = `Context · ${meta.title}`;
  positionSelectionActions(node);
  selectionActions.hidden = false;
  if (scroll) centerNode(node);
}

function positionSelectionActions(node) {
  const left = parseFloat(node.style.left || '0');
  const top = parseFloat(node.style.top || '0');
  selectionActions.style.left = `${left}px`;
  selectionActions.style.top = `${top + node.offsetHeight + 13}px`;
}

function centerNode(node) {
  const left = parseFloat(node.style.left || '0') + 100;
  const top = parseFloat(node.style.top || '0') + 80;
  const centerX = (left + node.offsetWidth / 2) * zoom;
  const centerY = (top + node.offsetHeight / 2) * zoom;
  viewport.scrollTo({
    left: Math.max(0, centerX - viewport.clientWidth / 2),
    top: Math.max(0, centerY - viewport.clientHeight / 2),
    behavior: prefersReducedMotion ? 'auto' : 'smooth'
  });
}

function populateX5(unitId) {
  const meta = units[unitId];
  if (!meta) return;
  x5Panel.querySelector('.x5-heading small').textContent = `${meta.category} · CURRENT`;
  x5Panel.querySelector('h2').textContent = meta.title;
  const values = [meta.purpose, meta.constraint, meta.evidence, meta.next];
  x5Panel.querySelectorAll('.x5-fields p').forEach((p, index) => { p.textContent = values[index]; });
}

function expandSelected() {
  if (!selectedUnit) return;
  const node = getNode(selectedUnit);
  const left = parseFloat(node.style.left || '0');
  const top = parseFloat(node.style.top || '0');
  populateX5(selectedUnit);
  x5Panel.style.left = `${Math.min(left, 1740)}px`;
  x5Panel.style.top = `${top}px`;
  x5Panel.hidden = false;
  selectionActions.hidden = true;
  node.style.opacity = '.12';
  node.style.pointerEvents = 'none';
  expandedUnit = selectedUnit;
  composerContextLabel.textContent = `Expanded · ${units[selectedUnit].title}`;
}

function collapseX5() {
  if (!expandedUnit) return;
  const node = getNode(expandedUnit);
  if (node) {
    node.style.opacity = '';
    node.style.pointerEvents = '';
  }
  x5Panel.hidden = true;
  expandedUnit = null;
  if (selectedUnit) {
    positionSelectionActions(getNode(selectedUnit));
    selectionActions.hidden = false;
    composerContextLabel.textContent = `Context · ${units[selectedUnit].title}`;
  }
}

function originForTransition(unitId) {
  let rect;
  if (expandedUnit === unitId && !x5Panel.hidden) rect = x5Panel.getBoundingClientRect();
  else rect = getNode(unitId)?.getBoundingClientRect();
  if (!rect) return { x: window.innerWidth / 2, y: window.innerHeight / 2 };
  return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
}

function pulseTransition(origin, duration = 300) {
  if (prefersReducedMotion) return Promise.resolve();
  transitionLayer.style.setProperty('--tx', `${origin.x}px`);
  transitionLayer.style.setProperty('--ty', `${origin.y}px`);
  transitionLayer.classList.add('active');
  return new Promise(resolve => {
    window.setTimeout(() => {
      transitionLayer.classList.remove('active');
      window.setTimeout(resolve, 100);
    }, duration);
  });
}

async function enterDeepDive(unitId = selectedUnit || 'model-selection') {
  if (!unitId) return;
  specialistUnit = unitId;
  const meta = units[unitId] || units['model-selection'];
  const origin = originForTransition(unitId);
  document.querySelector('.specialist-header h1').textContent = meta.title;
  document.querySelector('.specialist-header small').textContent = `${meta.category} · DEEP DIVE`;
  const compass = specialist.querySelector('.topology-compass');
  compass.querySelector('.c3').classList.add('active');

  if (!prefersReducedMotion) {
    projectPlane.style.transition = 'transform 360ms cubic-bezier(.18,.78,.2,1), opacity 240ms ease, filter 280ms ease';
    projectPlane.style.transformOrigin = `${origin.x}px ${origin.y}px`;
    projectPlane.style.transform = 'scale(.94)';
    await new Promise(resolve => setTimeout(resolve, 120));
    projectPlane.style.transform = 'scale(1.22)';
    projectPlane.style.opacity = '0';
    projectPlane.style.filter = 'blur(2px)';
  }
  await pulseTransition(origin, 190);
  cockpit.classList.remove('mode-chat', 'chat-split', 'source-map', 'source-specialist');
  cockpit.classList.add('mode-specialist');
  specialist.hidden = false;
  requestAnimationFrame(() => specialist.classList.add('visible'));
  setHudSurface('SPECIALIST WORKSPACE', meta.title, 'Deep work · project context preserved');
  window.setTimeout(() => {
    projectPlane.style.transition = '';
    projectPlane.style.transform = '';
    projectPlane.style.opacity = '';
    projectPlane.style.filter = '';
  }, 420);
}

async function returnToProject() {
  const origin = { x: window.innerWidth * .72, y: window.innerHeight * .58 };
  specialist.classList.remove('visible');
  await pulseTransition(origin, 120);
  cockpit.classList.remove('mode-specialist', 'mode-chat', 'chat-split', 'source-map', 'source-specialist');
  specialist.hidden = true;
  conversation.hidden = true;
  setHudSurface('PROJECT COCKPIT', 'Project map', 'Project state synchronized');
  if (selectedUnit) composerContextLabel.textContent = expandedUnit ? `Expanded · ${units[selectedUnit].title}` : `Context · ${units[selectedUnit].title}`;
}

function setRailMode(mode) {
  root.dataset.railMode = mode;
  localStorage.setItem('ads-cockpit-rail-mode', mode);
  document.getElementById('rail-boxes').classList.toggle('active', mode === 'boxes');
  document.getElementById('rail-text').classList.toggle('active', mode === 'text');
}

function updateConversationThread(threadId) {
  const meta = threadMeta[threadId] || threadMeta.general;
  activeThread = threadId;
  document.getElementById('conversation-title').textContent = meta.title;
  document.getElementById('conversation-scope').textContent = meta.scope;
  document.getElementById('conversation-subtitle').textContent = meta.subtitle;
  document.querySelectorAll('.conversation-thread').forEach(button => button.classList.toggle('active', button.dataset.thread === threadId));

  const expandButton = document.getElementById('conversation-expand-box');
  const fullContext = document.getElementById('full-context');
  if (meta.home) {
    expandButton.hidden = false;
    fullContext.hidden = false;
    fullContext.querySelector('button').textContent = `◆ ${units[meta.home]?.title || meta.title}`;
    updateConversationBoxPanel(meta.home);
  } else {
    expandButton.hidden = true;
    fullContext.hidden = true;
    conversation.classList.remove('box-open');
    conversationBoxPanel.hidden = true;
  }
}

function updateConversationBoxPanel(unitId) {
  const meta = units[unitId];
  if (!meta) return;
  conversationBoxPanel.querySelector('.box-panel-head strong').textContent = meta.title;
  conversationBoxPanel.querySelector('.expanded-home-box h2').textContent = meta.title;
  conversationBoxPanel.querySelector('.expanded-home-box small').textContent = `${meta.category} · CURRENT`;
  const values = [meta.purpose, meta.constraint, meta.evidence, meta.next];
  conversationBoxPanel.querySelectorAll('dd').forEach((dd, index) => { dd.textContent = values[index]; });
}

function currentSurfaceMode() {
  if (cockpit.classList.contains('mode-specialist')) return 'specialist';
  if (cockpit.classList.contains('mode-chat')) return preChatMode;
  return 'map';
}

async function openConversation(threadId = 'general', { split = false } = {}) {
  preChatMode = currentSurfaceMode();
  updateConversationThread(threadId);
  conversation.hidden = false;
  conversation.classList.remove('box-open');
  conversationBoxPanel.hidden = true;
  chatSplit = split;
  cockpit.classList.add('mode-chat');
  cockpit.classList.toggle('chat-split', split);
  cockpit.classList.toggle('source-map', preChatMode === 'map');
  cockpit.classList.toggle('source-specialist', preChatMode === 'specialist');
  requestAnimationFrame(() => conversation.classList.add('visible'));
  const meta = threadMeta[threadId] || threadMeta.general;
  setHudSurface('CONVERSATION WORKSPACE', meta.title, split ? 'Conversation + work co-present' : 'Full conversation focus · source state preserved');
}

async function closeConversation() {
  conversation.classList.remove('visible');
  conversation.classList.remove('box-open');
  conversationBoxPanel.hidden = true;
  await new Promise(resolve => setTimeout(resolve, prefersReducedMotion ? 0 : 100));
  cockpit.classList.remove('mode-chat', 'chat-split', 'source-map', 'source-specialist');
  conversation.hidden = true;
  chatSplit = false;
  if (preChatMode === 'specialist') {
    cockpit.classList.add('mode-specialist');
    specialist.hidden = false;
    specialist.classList.add('visible');
    setHudSurface('SPECIALIST WORKSPACE', units[specialistUnit]?.title || 'Specialist workspace', 'Deep work · project context preserved');
  } else {
    setHudSurface('PROJECT COCKPIT', 'Project map', 'Project state synchronized');
  }
}

function toggleCoPresent() {
  chatSplit = !chatSplit;
  cockpit.classList.toggle('chat-split', chatSplit);
  document.getElementById('conversation-split').textContent = chatSplit ? 'Full focus' : 'Co-present';
  hudStatus.textContent = chatSplit ? 'Conversation + work co-present' : 'Full conversation focus · source state preserved';
}

function openConversationBox() {
  const home = threadMeta[activeThread]?.home;
  if (!home || cockpit.classList.contains('chat-split')) return;
  updateConversationBoxPanel(home);
  conversationBoxPanel.hidden = false;
  conversation.classList.add('box-open');
}

function closeConversationBox() {
  conversation.classList.remove('box-open');
  conversationBoxPanel.hidden = true;
}

function restoreAppearanceSettings() {
  const settings = {
    boxShape: localStorage.getItem('ads-cockpit-box-shape') || 'subtle',
    microDesign: localStorage.getItem('ads-cockpit-micro-design') || 'light',
    connectorTerminal: localStorage.getItem('ads-cockpit-connector-terminal') || 'arrows',
    runtimeCarrier: localStorage.getItem('ads-cockpit-runtime-carrier') || 'ring'
  };
  root.dataset.boxShape = settings.boxShape;
  root.dataset.microDesign = settings.microDesign;
  root.dataset.connectorTerminal = settings.connectorTerminal;
  root.dataset.runtimeCarrier = settings.runtimeCarrier;
  document.getElementById('box-shape-select').value = settings.boxShape;
  document.getElementById('micro-design-select').value = settings.microDesign;
  document.getElementById('connector-terminal-select').value = settings.connectorTerminal;
  document.getElementById('runtime-select').value = settings.runtimeCarrier;
  setRailMode(localStorage.getItem('ads-cockpit-rail-mode') || 'boxes');
}

function bindAppearanceSelect(id, dataKey, storageKey) {
  document.getElementById(id).addEventListener('change', event => {
    root.dataset[dataKey] = event.target.value;
    localStorage.setItem(storageKey, event.target.value);
  });
}

function bindNodeInteractions() {
  document.querySelectorAll('.work-unit').forEach(node => {
    node.addEventListener('mousemove', event => {
      const rect = node.getBoundingClientRect();
      node.style.setProperty('--mx', `${event.clientX - rect.left}px`);
      node.style.setProperty('--my', `${event.clientY - rect.top}px`);
    });
    node.addEventListener('click', event => {
      event.stopPropagation();
      if (expandedUnit) collapseX5();
      selectUnit(node.dataset.unit);
    });
    node.addEventListener('dblclick', event => {
      event.preventDefault();
      event.stopPropagation();
      selectUnit(node.dataset.unit);
      expandSelected();
    });
  });
}

bindNodeInteractions();
restoreAppearanceSettings();
updateWorldTransform();

projectPlane.addEventListener('click', event => {
  if (event.target === projectPlane || event.target.closest('.connectors')) clearSelection();
});

document.getElementById('selection-expand').addEventListener('click', expandSelected);
document.getElementById('selection-chat').addEventListener('click', () => openConversation(selectedUnit || 'general'));
document.getElementById('selection-deep').addEventListener('click', () => enterDeepDive(selectedUnit));
document.getElementById('x5-collapse').addEventListener('click', collapseX5);
document.getElementById('x5-chat').addEventListener('click', () => openConversation(expandedUnit || selectedUnit || 'general'));
document.getElementById('x5-deep').addEventListener('click', () => enterDeepDive(expandedUnit || selectedUnit));
document.getElementById('specialist-back').addEventListener('click', returnToProject);
document.getElementById('specialist-conversations').addEventListener('click', () => openConversation('general'));
document.getElementById('specialist-work-chat').addEventListener('click', () => openConversation(specialistUnit));
document.getElementById('global-conversations').addEventListener('click', () => openConversation('general'));
document.getElementById('composer-open-chat').addEventListener('click', () => openConversation('general'));
document.getElementById('conversation-close').addEventListener('click', closeConversation);
document.getElementById('conversation-split').addEventListener('click', toggleCoPresent);
document.getElementById('conversation-expand-box').addEventListener('click', openConversationBox);
document.getElementById('conversation-box-close').addEventListener('click', closeConversationBox);

document.querySelectorAll('.conversation-thread').forEach(button => button.addEventListener('click', () => updateConversationThread(button.dataset.thread)));
document.getElementById('rail-boxes').addEventListener('click', () => setRailMode('boxes'));
document.getElementById('rail-text').addEventListener('click', () => setRailMode('text'));

document.getElementById('zoom-in').addEventListener('click', () => setZoom(zoom + .1));
document.getElementById('zoom-out').addEventListener('click', () => setZoom(zoom - .1));
document.getElementById('zoom-label').addEventListener('click', () => setZoom(1));
document.getElementById('reset-view').addEventListener('click', () => {
  setZoom(1);
  viewport.scrollTo({ left: 390, top: 180, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
});
document.getElementById('fit-project').addEventListener('click', () => {
  const fit = Math.min(.88, (viewport.clientWidth - 80) / 2200, (viewport.clientHeight - 80) / 1100);
  setZoom(Math.max(.55, fit));
  viewport.scrollTo({ left: 45, top: 35, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
});

viewport.addEventListener('wheel', event => {
  if (!event.ctrlKey) return;
  event.preventDefault();
  setZoom(zoom * Math.exp(-event.deltaY * .002));
}, { passive: false });

document.getElementById('focus-current').addEventListener('click', event => {
  const next = root.dataset.focusCurrent !== 'true';
  root.dataset.focusCurrent = String(next);
  event.currentTarget.textContent = next ? 'Context visible' : 'Focus current';
});

const settingsPopover = document.getElementById('settings-popover');
document.getElementById('settings-button').addEventListener('click', () => { settingsPopover.hidden = !settingsPopover.hidden; document.getElementById('jump-popover').hidden = true; });
document.getElementById('settings-close').addEventListener('click', () => { settingsPopover.hidden = true; });
bindAppearanceSelect('box-shape-select', 'boxShape', 'ads-cockpit-box-shape');
bindAppearanceSelect('micro-design-select', 'microDesign', 'ads-cockpit-micro-design');
bindAppearanceSelect('connector-terminal-select', 'connectorTerminal', 'ads-cockpit-connector-terminal');
bindAppearanceSelect('runtime-select', 'runtimeCarrier', 'ads-cockpit-runtime-carrier');

const jumpPopover = document.getElementById('jump-popover');
document.getElementById('jump-button').addEventListener('click', () => { jumpPopover.hidden = !jumpPopover.hidden; settingsPopover.hidden = true; if (!jumpPopover.hidden) document.getElementById('jump-search').focus(); });
document.getElementById('jump-close').addEventListener('click', () => { jumpPopover.hidden = true; });
jumpPopover.querySelectorAll('[data-jump]').forEach(button => button.addEventListener('click', () => {
  jumpPopover.hidden = true;
  selectUnit(button.dataset.jump, { scroll: true });
}));
document.getElementById('jump-search').addEventListener('input', event => {
  const query = event.target.value.toLowerCase();
  jumpPopover.querySelectorAll('[data-jump]').forEach(button => { button.hidden = !button.textContent.toLowerCase().includes(query); });
});

document.getElementById('fullscreen-button').addEventListener('click', async () => {
  try {
    if (!document.fullscreenElement) await cockpit.requestFullscreen();
    else await document.exitFullscreen();
  } catch {
    hudStatus.textContent = 'Fullscreen unavailable · immersive Cockpit remains active';
  }
});

document.addEventListener('fullscreenchange', () => {
  document.getElementById('fullscreen-button').textContent = document.fullscreenElement ? '×' : '⛶';
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    settingsPopover.hidden = true;
    jumpPopover.hidden = true;
    if (conversation.classList.contains('box-open')) closeConversationBox();
    else if (cockpit.classList.contains('mode-chat')) closeConversation();
    else if (cockpit.classList.contains('mode-specialist')) returnToProject();
    else if (expandedUnit) collapseX5();
  }
  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
    event.preventDefault();
    jumpPopover.hidden = false;
    settingsPopover.hidden = true;
    document.getElementById('jump-search').focus();
  }
  if ((event.metaKey || event.ctrlKey) && event.key === '+') { event.preventDefault(); setZoom(zoom + .1); }
  if ((event.metaKey || event.ctrlKey) && event.key === '-') { event.preventDefault(); setZoom(zoom - .1); }
  if ((event.metaKey || event.ctrlKey) && event.key === '0') { event.preventDefault(); setZoom(1); }
});

window.addEventListener('load', () => {
  viewport.scrollTo({ left: 390, top: 175 });
  setHudSurface('PROJECT COCKPIT', 'Project map', 'Project state synchronized');
});
