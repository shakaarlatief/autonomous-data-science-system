const root = document.documentElement;

root.dataset.reduced = root.dataset.reduced || 'off';
root.dataset.inboxLight = root.dataset.inboxLight || 'reduced';
root.dataset.shapeStyle = root.dataset.shapeStyle || 'true';
root.dataset.surfaceStyle = root.dataset.surfaceStyle || 'material';

ensureCanonicalSidebarStyles();

const scopeSelect = document.querySelector('#scope-select');
const threadIdentitySelect = document.querySelector('#thread-identity-select');
const anchorModeSelect = document.querySelector('#anchor-mode-select');
const studyChips = [...document.querySelectorAll('.study-chip')];
const scopeThreads = [...document.querySelectorAll('.scope-thread[data-thread-scope]')];
const conversationTitle = document.querySelector('#conversation-title');
const conversationSubtitle = document.querySelector('#conversation-subtitle');
const scopePill = document.querySelector('#scope-pill');
const scopeExplanation = document.querySelector('#scope-explanation');
const firstUserMessage = document.querySelector('#first-user-message');
const homeContextChip = document.querySelector('#home-context-chip');
const anchorExpandButton = document.querySelector('#anchor-expand-button');
const inspectorClose = document.querySelector('#inspector-close');

const template = document.querySelector('#work-unit-template');
const projectTemplate = document.querySelector('#project-template');
const anchorTargets = [
  document.querySelector('#header-anchor-slot'),
  document.querySelector('#anchor-shelf'),
  document.querySelector('#inner-anchor-sidecar'),
  document.querySelector('#floating-anchor'),
  document.querySelector('#inspector-artifact'),
];

const sidebarViewStorageKey = 'ads-conversation-sidebar-view';

const categoryMeta = {
  question: {
    kind: 'Question / Blocker',
    rgb: '240, 178, 91',
    glyph: '<svg viewBox="0 0 16 16"><circle cx="8" cy="8" r="4.4"/></svg>',
  },
  investigation: {
    kind: 'Investigation',
    rgb: '103, 218, 194',
    glyph: '<svg viewBox="0 0 16 16"><rect x="4" y="4" width="8" height="8" rx="0.7"/></svg>',
  },
  validation: {
    kind: 'Validation / Analysis',
    rgb: '142, 169, 255',
    glyph: '<svg viewBox="0 0 16 16"><path d="M8 3.3 12.6 12H3.4z"/></svg>',
  },
  model: {
    kind: 'Model Work',
    rgb: '233, 132, 122',
    glyph: '<svg viewBox="0 0 16 16"><path d="M8 3.2 12.8 8 8 12.8 3.2 8z"/></svg>',
  },
  evaluation: {
    kind: 'Evaluation',
    rgb: '173, 150, 255',
    glyph: '<svg viewBox="0 0 16 16"><path d="M8 3v10M3 8h10"/></svg>',
  },
};

const dispositions = {
  current: { code: 'CURRENT', rgb: '102, 181, 255' },
  recommended: { code: 'NEXT', rgb: '177, 151, 255' },
  deferred: { code: 'DEFER', rgb: '145, 158, 179' },
  future: { code: 'FUTURE', rgb: '122, 139, 163' },
};

const statusMeta = {
  NONE: { code: 'NONE', rgb: '145, 158, 179', source: 'none' },
  BLOCKED: { code: 'BLOCKED', rgb: '237, 112, 105', source: 'constraint' },
  FAIL: { code: 'FAIL', rgb: '237, 112, 105', source: 'runtime' },
  RUN: { code: 'RUN', rgb: '103, 218, 194', source: 'runtime' },
  HUMAN: { code: 'HUMAN', rgb: '173, 150, 255', source: 'runtime' },
};

const sidebarWorkUnits = [
  {
    host: '.model-artifact',
    category: 'model',
    disposition: 'current',
    status: 'RUN',
    priority: 'high',
    title: 'Model selection strategy',
    subtitle: 'Compare candidate families under one frozen validation protocol.',
  },
  {
    host: '.investigation-artifact',
    category: 'investigation',
    disposition: 'current',
    status: 'BLOCKED',
    priority: 'normal',
    title: 'Production missingness',
    subtitle: 'Blocked by unresolved upstream work.',
  },
  {
    host: '.validation-artifact',
    category: 'validation',
    disposition: 'deferred',
    status: 'NONE',
    priority: 'normal',
    title: 'Threshold policy',
    subtitle: 'Deferred threshold decision.',
  },
];

prepareSidebarViewControls();
renderCanonicalThreadBoxes();
anchorTargets.forEach(cloneWorkUnitArtifact);

function ensureCanonicalSidebarStyles() {
  if (document.querySelector('link[data-canonical-sidebar-styles]')) return;
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = './conversation-workspace-work-unit-anchor-canonical-boxes.css';
  link.dataset.canonicalSidebarStyles = 'true';
  document.head.appendChild(link);
}

function prepareSidebarViewControls() {
  const markerOption = threadIdentitySelect?.querySelector('option[value="marker"]');
  markerOption?.remove();

  const artifactOption = threadIdentitySelect?.querySelector('option[value="artifact"]');
  if (artifactOption) artifactOption.textContent = 'Canonical boxes';

  const textOption = threadIdentitySelect?.querySelector('option[value="text"]');
  if (textOption) textOption.textContent = 'Text';

  const label = threadIdentitySelect?.closest('label')?.querySelector('span');
  if (label) label.textContent = 'Sidebar view';

  const searchBox = document.querySelector('.search-box');
  if (searchBox && !document.querySelector('.sidebar-view-switch')) {
    const switcher = document.createElement('div');
    switcher.className = 'sidebar-view-switch';
    switcher.setAttribute('role', 'group');
    switcher.setAttribute('aria-label', 'Conversation sidebar view');
    switcher.innerHTML = `
      <button type="button" data-sidebar-view="artifact" aria-pressed="true">Boxes</button>
      <button type="button" data-sidebar-view="text" aria-pressed="false">Text</button>
    `;
    searchBox.insertAdjacentElement('afterend', switcher);
  }

  for (const button of document.querySelectorAll('[data-sidebar-view]')) {
    button.addEventListener('click', () => setThreadIdentity(button.dataset.sidebarView, true));
  }
}

function renderCanonicalThreadBoxes() {
  for (const fixture of sidebarWorkUnits) {
    const host = document.querySelector(fixture.host);
    if (!host) continue;
    host.replaceChildren();
    host.insertAdjacentHTML('afterbegin', `<span class="rail-node-scale">${canonicalNodeMarkup(fixture)}</span>`);
  }
}

function canonicalNodeMarkup({ category, disposition, status, priority, title, subtitle }) {
  const meta = categoryMeta[category];
  const projectState = dispositions[disposition];
  const statusState = statusMeta[status] || statusMeta.NONE;

  return `
    <span class="grammar-node custom-node rail-canonical-node category-${category}"
      data-state="${disposition}"
      data-status-source="${statusState.source}"
      data-status-code="${statusState.code}"
      data-status-carrier="dot"
      data-priority="${priority}"
      data-priority-style="a3"
      data-selected="false"
      data-light-side="left"
      style="--node-rgb:${meta.rgb}; --state-rgb:${projectState.rgb}; --status-rgb:${statusState.rgb}; --light-anchor:50%;">
      <span class="rest-spill" aria-hidden="true"></span>
      <span class="rest-light" aria-hidden="true"></span>
      <span class="hover-light" aria-hidden="true"></span>
      <span class="hover-world-light" aria-hidden="true"></span>
      <span class="disposition-state-outline" aria-hidden="true"></span>
      <span class="node-surface">
        <span class="surface-rest-light" aria-hidden="true"></span>
        <span class="custom-material-layer" aria-hidden="true"></span>
        <span class="custom-lumen-layer" aria-hidden="true"></span>
        <span class="pointer-light" aria-hidden="true"></span>
        <span class="perimeter-sweep" aria-hidden="true"></span>
        <span class="frame-signature" aria-hidden="true"></span>
        <span class="disposition-state-rhythm" aria-hidden="true"></span>
        <span class="disposition-state-badge" aria-hidden="true">${projectState.code}</span>
        ${statusMarkup(statusState)}
        ${priorityMarkup(priority)}
        <span class="node-heading">
          <span class="category-glyph" aria-hidden="true">${meta.glyph}</span>
          <span class="unit-kind">${meta.kind}</span>
        </span>
        <strong>${title}</strong>
        <small>${subtitle}</small>
      </span>
    </span>
  `;
}

function statusMarkup(statusState) {
  if (statusState.code === 'NONE') return '';
  return `
    <span class="status-dot-carrier" aria-hidden="true">
      <span class="status-dot-core"></span>
      <span class="status-dot-ring"></span>
    </span>
  `;
}

function priorityMarkup(priority) {
  if (priority !== 'high') return '';
  return '<span class="priority-signal-bars" aria-hidden="true"><i></i><i></i><i></i></span>';
}

function cloneWorkUnitArtifact(target) {
  target.replaceChildren(template.content.cloneNode(true));
}

function cloneProjectArtifact(target) {
  target.replaceChildren(projectTemplate.content.cloneNode(true));
}

function setAnchorMode(mode) {
  root.dataset.anchorMode = mode;
  anchorModeSelect.value = mode;

  if (mode !== 'adaptive') {
    root.dataset.anchorExpanded = 'false';
  }

  studyChips.forEach((chip) => {
    chip.setAttribute('aria-pressed', String(chip.dataset.anchor === mode));
  });
}

function setThreadIdentity(mode, persist = false) {
  const resolvedMode = mode === 'text' ? 'text' : 'artifact';
  root.dataset.threadIdentity = resolvedMode;
  threadIdentitySelect.value = resolvedMode;

  for (const button of document.querySelectorAll('[data-sidebar-view]')) {
    button.setAttribute('aria-pressed', String(button.dataset.sidebarView === resolvedMode));
  }

  if (persist) {
    try {
      window.localStorage.setItem(sidebarViewStorageKey, resolvedMode);
    } catch {
      // The preference remains session-local if storage is unavailable.
    }
  }
}

function getInitialSidebarView() {
  try {
    const stored = window.localStorage.getItem(sidebarViewStorageKey);
    return stored === 'text' ? 'text' : 'artifact';
  } catch {
    return 'artifact';
  }
}

function setActiveThread(scope) {
  scopeThreads.forEach((thread) => thread.classList.remove('is-active'));

  const selector = scope === 'project' ? '.thread-project' : '.thread-model';
  document.querySelector(selector)?.classList.add('is-active');
}

function setScope(scope) {
  root.dataset.scope = scope;
  scopeSelect.value = scope;
  root.dataset.anchorExpanded = 'false';
  anchorExpandButton.textContent = 'Expand box';
  setActiveThread(scope);

  if (scope === 'project') {
    conversationTitle.textContent = 'General project discussion';
    conversationSubtitle.textContent = 'Project-level conversation. It can reference any work unit without being owned by one.';
    scopePill.textContent = 'PROJECT GENERAL';
    firstUserMessage.textContent = 'I want to discuss the project broadly without attaching this conversation to one specific work unit.';
    scopeExplanation.innerHTML = 'This conversation has <strong>no work-unit home</strong>. It can still reference, inspect, or temporarily bring project objects into context without silently becoming attached to one of them.';
    homeContextChip.hidden = true;
    anchorTargets.forEach(cloneProjectArtifact);
  } else {
    conversationTitle.textContent = 'Model selection strategy';
    conversationSubtitle.textContent = 'Conversation anchored to one project work unit. Other objects can still be referenced without changing its home.';
    scopePill.textContent = 'WORK UNIT';
    firstUserMessage.textContent = 'I want the model comparison to stay broad, but I also want the final selection logic to be disciplined and easy to recover later.';
    scopeExplanation.innerHTML = 'Because this conversation has a work-unit home, the transcript can stay explicitly connected to <strong>Model selection strategy</strong> while still bringing in evidence from other parts of the project.';
    homeContextChip.hidden = false;
    anchorTargets.forEach(cloneWorkUnitArtifact);
  }
}

scopeSelect.addEventListener('change', (event) => setScope(event.target.value));
threadIdentitySelect.addEventListener('change', (event) => setThreadIdentity(event.target.value, true));
anchorModeSelect.addEventListener('change', (event) => setAnchorMode(event.target.value));

studyChips.forEach((chip) => {
  chip.addEventListener('click', () => {
    if (root.dataset.scope === 'project') return;
    setAnchorMode(chip.dataset.anchor);
  });
});

document.querySelector('.thread-project')?.addEventListener('click', () => setScope('project'));
document.querySelector('.thread-model')?.addEventListener('click', () => setScope('work-unit'));

anchorExpandButton.addEventListener('click', () => {
  if (root.dataset.anchorMode !== 'adaptive' || root.dataset.scope !== 'work-unit') return;
  const next = root.dataset.anchorExpanded !== 'true';
  root.dataset.anchorExpanded = String(next);
  anchorExpandButton.textContent = next ? 'Collapse box' : 'Expand box';
});

inspectorClose.addEventListener('click', () => {
  if (root.dataset.anchorMode === 'adaptive') {
    root.dataset.anchorExpanded = 'false';
    anchorExpandButton.textContent = 'Expand box';
    return;
  }
  setAnchorMode('none');
});

setThreadIdentity(getInitialSidebarView());
setAnchorMode('adaptive');
setScope('work-unit');
