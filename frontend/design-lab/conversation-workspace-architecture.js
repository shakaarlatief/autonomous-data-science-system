const variants = [
  { id: 'cv0', code: 'CV0', label: 'Focus Workspace', description: 'The full Conversation Workspace replaces the project map and becomes a first-class focused surface.' },
  { id: 'cv1', code: 'CV1', label: 'Right Dock', description: 'A resizable-style right region opens while the project map contracts into the remaining safe area.' },
  { id: 'cv2', code: 'CV2', label: 'Split Workbench', description: 'Project context and conversation share the stage equally for sustained discussion about visible work.' },
  { id: 'cv3', code: 'CV3', label: 'Canvas Lens', description: 'A large floating transcript remains visually anchored inside the spatial Cockpit while the map recedes behind it.' },
  { id: 'cv4', code: 'CV4', label: 'Bottom Workbench', description: 'Conversation rises from the native composer into a bottom workbench while the project remains visible above.' },
  { id: 'cv5', code: 'CV5', label: 'Focus + Context Rail', description: 'Conversation owns most of the stage while a narrow project-context rail preserves orientation and selected-work identity.' },
  { id: 'cv6', code: 'CV6', label: 'Conversation + Inspector', description: 'Long-form conversation is paired with a persistent contextual inspector for the selected work unit and project references.' },
  { id: 'cv7', code: 'CV7', label: 'Progressive Recent-to-Full', description: 'The compact composer first reveals recent turns; a second activation promotes that same conversation into the full workspace.' },
  { id: 'cv8', code: 'CV8', label: 'Tabbed Stage', description: 'Conversation becomes a route-like stage peer to the project map, with clear Project / Conversation navigation at the top.' },
]

const grid = document.querySelector('#conversation-grid')
const controls = document.querySelector('#conversation-controls')
const practical = document.querySelector('#practical-stage')
const summary = document.querySelector('#conversation-summary')
let currentStyle = 'cv0'

renderGrid()
renderControls()
renderPractical(currentStyle)

function renderGrid() {
  if (!grid) return
  grid.innerHTML = variants.map((variant) => `
    <article class="conversation-tile">
      <div class="conversation-copy">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${stageMarkup(variant.id, false)}
    </article>
  `).join('')

  for (const stage of grid.querySelectorAll('.conversation-demo')) bindStage(stage)
}

function renderControls() {
  if (!controls) return
  controls.innerHTML = variants.map((variant) => `
    <button type="button" data-conversation-style="${variant.id}" aria-pressed="${variant.id === currentStyle ? 'true' : 'false'}">
      ${variant.code}<br>${variant.label}
    </button>
  `).join('')

  for (const button of controls.querySelectorAll('button[data-conversation-style]')) {
    button.addEventListener('click', () => {
      currentStyle = button.dataset.conversationStyle || 'cv0'
      renderPractical(currentStyle)
      for (const candidate of controls.querySelectorAll('button[data-conversation-style]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.conversationStyle === currentStyle))
      }
      const variant = variantById(currentStyle)
      if (summary && variant) summary.textContent = `${variant.code} · ${variant.label}`
    })
  }
}

function stageMarkup(style, large) {
  return `<div class="conversation-demo" data-style="${style}">${stageInner(style, large)}</div>`
}

function stageInner(style, large) {
  const progressive = style === 'cv7'
  const chip = progressive
    ? 'Click composer / scene: recent → full → project'
    : (large ? 'Click composer or scene to open / close' : 'Click to open / close')

  return `
    <div class="project-layer">
      <svg class="scene-links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <path class="direct" d="M18 25 C34 30 45 39 56 47" />
        <path class="direct" d="M82 25 C75 31 67 39 59 46" />
        <path d="M20 79 C34 70 46 58 56 51" />
        <path d="M82 78 C75 67 67 58 59 50" />
      </svg>
      <div class="map-node a"><span>QUESTION / BLOCKER</span><strong>Resolve target definition</strong></div>
      <div class="map-node b"><span>VALIDATION</span><strong>Chronological validation</strong></div>
      <div class="map-node c"><span>MODEL WORK</span><strong>Boosted candidate</strong></div>
      <div class="map-node d"><span>EVALUATION</span><strong>Calibration review</strong></div>
      <article class="selected-unit">
        <i class="sel-corner tl"></i><i class="sel-corner tr"></i><i class="sel-corner bl"></i><i class="sel-corner br"></i>
        <span>Investigation · Current · Blocked · High</span>
        <h3>Production missingness</h3>
        <p>Selected work unit. Conversation can reference and discuss this structured project object.</p>
      </article>
      <div class="compact-composer">
        <span>Ask ADS</span>
        <strong>Continue the project conversation…</strong>
        <button type="button" class="open-conversation">Open conversation</button>
      </div>
    </div>

    <div class="recent-layer" aria-hidden="true">
      <span>Recent conversation</span>
      <p><strong>You:</strong> Why is Production missingness blocked?</p>
      <p><strong>ADS:</strong> The current blocker is the unresolved target definition. Open the full conversation for history and linked project context.</p>
    </div>

    <aside class="context-rail" aria-hidden="true">
      <span>Project context</span>
      <strong>Current process</strong>
      <div class="context-card">
        <span>Selected work</span>
        <strong>Production missingness</strong>
        <em>Current · Blocked · High</em>
      </div>
      <div class="context-card">
        <span>Blocking cause</span>
        <strong>Resolve target definition</strong>
        <em>Question / Blocker</em>
      </div>
    </aside>

    <div class="conversation-layer">
      <section class="conversation-shell">
        <div class="conversation-bar">
          <div><span>Conversation Workspace</span><strong>Project dialogue · Main thread</strong></div>
          <button type="button" class="close-conversation">Return to project</button>
        </div>
        <div class="transcript">
          <div class="message user"><span>You</span><p>Before we continue modelling, explain why Production missingness is blocked and what decision actually unlocks it.</p><div class="project-ref">↗ Production missingness</div></div>
          <div class="message"><span>ADS</span><p>The work unit is blocked because the target definition is unresolved. The blocker is a separate Question / Blocker work unit. Resolving it removes the blocking relation; it does not change the Investigation category.</p><div class="project-ref">↗ Resolve target definition · BLOCKS · Production missingness</div></div>
          <div class="message user"><span>You</span><p>Keep that distinction in the project state. I also want to know what evidence we already have about missingness.</p></div>
          <div class="message"><span>ADS</span><p>The structured work unit already references the schema and missingness profile as evidence. The conversation can explain and navigate those artifacts, but the transcript is not the canonical home of the project decision.</p><div class="project-ref">↗ Evidence: schema + missingness profile</div></div>
          <div class="message"><span>System-visible project change</span><p>Decision recorded: do not begin the dependent validation until the target definition is resolved.</p><div class="project-ref">↗ Structured project state updated</div></div>
        </div>
        <div class="conversation-input"><span>Continue the same persistent project conversation…</span><button type="button">Send</button></div>
      </section>
    </div>

    <span class="enter-chip">${chip}</span>
  `
}

function bindStage(stage) {
  stage.addEventListener('click', (event) => {
    if (event.target.closest('.close-conversation')) {
      closeConversation(stage)
      event.stopPropagation()
      return
    }
    if (event.target.closest('.conversation-layer')) return
    advanceStage(stage)
  })
}

function advanceStage(stage) {
  if (stage.dataset.style === 'cv7') {
    if (!stage.classList.contains('is-recent-open') && !stage.classList.contains('is-conversation-open')) {
      stage.classList.add('is-recent-open')
      return
    }
    if (stage.classList.contains('is-recent-open') && !stage.classList.contains('is-conversation-open')) {
      stage.classList.remove('is-recent-open')
      stage.classList.add('is-conversation-open')
      return
    }
  }

  stage.classList.contains('is-conversation-open') ? closeConversation(stage) : openConversation(stage)
}

function openConversation(stage) {
  stage.classList.remove('is-recent-open')
  stage.classList.add('is-conversation-open')
}

function closeConversation(stage) {
  stage.classList.remove('is-conversation-open', 'is-recent-open')
}

function renderPractical(style) {
  if (!practical) return
  practical.classList.remove('is-conversation-open', 'is-recent-open')
  practical.innerHTML = stageInner(style, true)
  practical.dataset.style = style

  if (practical.dataset.bound !== 'true') {
    practical.dataset.bound = 'true'
    bindStage(practical)
  }
}

function variantById(id) {
  return variants.find((variant) => variant.id === id)
}
