const root = document.documentElement;

const workSelect = document.querySelector('#work-select');
const threadSelect = document.querySelector('#thread-select');
const presentationSelect = document.querySelector('#presentation-select');
const presentationButtons = [...document.querySelectorAll('[data-presentation]')];
const threadButtons = [...document.querySelectorAll('[data-thread-target]')];
const conversationPane = document.querySelector('#conversation-pane');
const chatTitle = document.querySelector('#chat-title');
const chatSubtitle = document.querySelector('#chat-subtitle');
const scopePill = document.querySelector('#scope-pill');
const homeChip = document.querySelector('#home-chip');
const userMessage = document.querySelector('#user-message');
const adsCopy = document.querySelector('#ads-copy');
const compactContextLabel = document.querySelector('#compact-context-label');
const stateWork = document.querySelector('#state-work');
const stateChat = document.querySelector('#state-chat');
const expandBoxChat = document.querySelector('#expand-box-chat');
const closeBoxPanel = document.querySelector('#close-box-panel');

const workLabels = {
  grid: 'GRID · NEUTRAL',
  selected: 'GRID · SELECTED BOX',
  x5: 'GRID · X5 EXPANDED',
  deep: 'DEEP DIVE · SPECIALIST WORKSPACE',
};

const presentationLabels = {
  work: 'WORK ONLY / COMPACT CHAT',
  full: 'FULL CHAT FOCUS',
  dock: 'RIGHT DOCK',
  split: 'BALANCED SPLIT',
  'chat-dominant': 'CHAT DOMINANT + WORK CONTEXT',
};

function setWork(value) {
  const work = ['grid', 'selected', 'x5', 'deep'].includes(value) ? value : 'grid';
  root.dataset.work = work;
  workSelect.value = work;
  compactContextLabel.textContent = work === 'grid' ? 'Project-aware' : 'Model selection strategy';
  updateStateFooter();
}

function setThread(value) {
  const thread = value === 'project' ? 'project' : 'work';
  root.dataset.thread = thread;
  threadSelect.value = thread;
  threadButtons.forEach((button) => button.classList.toggle('active', button.dataset.threadTarget === thread));

  if (thread === 'project') {
    chatTitle.textContent = 'General project discussion';
    chatSubtitle.textContent = 'Project-level conversation with no single work-unit home.';
    scopePill.textContent = 'PROJECT GENERAL';
    homeChip.textContent = 'Autonomous Data Science project';
    userMessage.textContent = 'I want to discuss the project broadly while keeping my current work surface exactly as it is.';
    adsCopy.textContent = 'Yes. A project-general conversation can be opened from any Grid or Deep Dive state without becoming owned by whichever work unit happens to be visible underneath.';
    expandBoxChat.style.display = 'none';
  } else {
    chatTitle.textContent = 'Model selection strategy';
    chatSubtitle.textContent = 'Conversation anchored to the current model-work unit.';
    scopePill.textContent = 'WORK UNIT';
    homeChip.textContent = '◇ Model selection strategy';
    userMessage.textContent = 'Can we discuss this model-selection work while I keep the current work surface open?';
    adsCopy.textContent = 'Yes. Conversation presentation is separate from the underlying work surface. The same work-unit chat can take full focus or coexist beside the Grid or Deep Dive.';
    expandBoxChat.style.display = '';
  }

  updateStateFooter();
}

function setPresentation(value) {
  const presentation = ['work', 'full', 'dock', 'split', 'chat-dominant'].includes(value) ? value : 'work';
  root.dataset.presentation = presentation;
  presentationSelect.value = presentation;
  presentationButtons.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.presentation === presentation)));
  if (presentation === 'work') conversationPane.dataset.boxOpen = 'false';
  updateStateFooter();
}

function updateStateFooter() {
  stateWork.textContent = workLabels[root.dataset.work] || workLabels.grid;
  const threadLabel = root.dataset.thread === 'project' ? 'PROJECT GENERAL' : 'WORK UNIT';
  stateChat.textContent = `${threadLabel} · ${presentationLabels[root.dataset.presentation] || presentationLabels.work}`;
}

function openGlobalConversation() {
  setPresentation('full');
}

function openWorkConversation(presentation = 'split') {
  setThread('work');
  setPresentation(presentation);
}

workSelect.addEventListener('change', (event) => setWork(event.target.value));
threadSelect.addEventListener('change', (event) => setThread(event.target.value));
presentationSelect.addEventListener('change', (event) => setPresentation(event.target.value));

presentationButtons.forEach((button) => button.addEventListener('click', () => setPresentation(button.dataset.presentation)));
threadButtons.forEach((button) => button.addEventListener('click', () => setThread(button.dataset.threadTarget)));

document.querySelector('#global-chat-grid').addEventListener('click', openGlobalConversation);
document.querySelector('#composer-expand').addEventListener('click', openGlobalConversation);
document.querySelector('#node-chat').addEventListener('click', () => openWorkConversation('split'));
document.querySelector('#x5-chat').addEventListener('click', () => openWorkConversation('split'));
document.querySelector('#deep-chat').addEventListener('click', openGlobalConversation);
document.querySelector('#deep-work-chat').addEventListener('click', () => openWorkConversation('split'));

document.querySelector('#node-expand').addEventListener('click', () => setWork('x5'));
document.querySelector('#x5-deep').addEventListener('click', () => setWork('deep'));

document.querySelector('#close-chat').addEventListener('click', () => setPresentation('work'));

expandBoxChat.addEventListener('click', () => {
  if (root.dataset.thread !== 'work') return;
  const next = conversationPane.dataset.boxOpen !== 'true';
  conversationPane.dataset.boxOpen = String(next);
});

closeBoxPanel.addEventListener('click', () => {
  conversationPane.dataset.boxOpen = 'false';
});

conversationPane.dataset.boxOpen = 'false';
setWork(root.dataset.work || 'x5');
setThread(root.dataset.thread || 'work');
setPresentation(root.dataset.presentation || 'split');
