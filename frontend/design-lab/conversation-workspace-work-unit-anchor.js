const root = document.documentElement;

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

function cloneWorkUnitArtifact(target) {
  target.replaceChildren(template.content.cloneNode(true));
}

function cloneProjectArtifact(target) {
  target.replaceChildren(projectTemplate.content.cloneNode(true));
}

anchorTargets.forEach(cloneWorkUnitArtifact);

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

function setThreadIdentity(mode) {
  root.dataset.threadIdentity = mode;
  threadIdentitySelect.value = mode;
}

function setActiveThread(scope) {
  scopeThreads.forEach((thread) => {
    const shouldActivate = thread.dataset.threadScope === scope;
    thread.classList.toggle('is-active', shouldActivate);
  });
}

function setScope(scope) {
  root.dataset.scope = scope;
  scopeSelect.value = scope;
  root.dataset.anchorExpanded = 'false';
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
threadIdentitySelect.addEventListener('change', (event) => setThreadIdentity(event.target.value));
anchorModeSelect.addEventListener('change', (event) => setAnchorMode(event.target.value));

studyChips.forEach((chip) => {
  chip.addEventListener('click', () => {
    if (root.dataset.scope === 'project') return;
    setAnchorMode(chip.dataset.anchor);
  });
});

scopeThreads.forEach((thread) => {
  thread.addEventListener('click', () => {
    const scope = thread.dataset.threadScope;
    if (scope === 'project') {
      setScope('project');
      return;
    }

    setScope('work-unit');
  });
});

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

setThreadIdentity('artifact');
setAnchorMode('adaptive');
setScope('work-unit');
