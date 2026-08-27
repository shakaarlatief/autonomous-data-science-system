const variants = [
  { id: 'f0', code: 'F0', label: 'Hard Replace', description: 'The specialist workspace replaces the project map immediately. Control for maximum depth and minimum spatial continuity.' },
  { id: 'f1', code: 'F1', label: 'Center Stage', description: 'The map recedes softly while a centered full-resolution workspace mounts above it.' },
  { id: 'f2', code: 'F2', label: 'Anchored Morph', description: 'The specialist workspace appears to grow directly from the selected X5 work unit, preserving object continuity.' },
  { id: 'f3', code: 'F3', label: 'World Recede', description: 'The entire project world deliberately pulls backward and desaturates while the workspace becomes dominant.' },
  { id: 'f4', code: 'F4', label: 'Context Ribbon', description: 'The map gives way to the workspace but a compact project-path ribbon preserves location and return context.' },
  { id: 'f5', code: 'F5', label: 'Map Frame', description: 'A visible project-map frame remains around the specialist workspace so spatial context never disappears completely.' },
  { id: 'f6', code: 'F6', label: 'Side Context Rail', description: 'A narrow live strip of project context remains beside the specialist workspace during deep work.' },
  { id: 'f7', code: 'F7', label: 'Portal Lift', description: 'The workspace lifts out of the selected work unit as a distinct rounded layer while the world remains softly behind it.' },
  { id: 'f8', code: 'F8', label: 'Layered Stage', description: 'The workspace becomes the front layer while the map remains visibly displaced behind it as a persistent spatial stage.' },
]

const grid = document.querySelector('#focus-grid')
const controls = document.querySelector('#focus-controls')
const practical = document.querySelector('#practical-stage')
const summary = document.querySelector('#focus-summary')
let practicalFocused = false

renderGrid()
renderControls()
renderPractical('f2')

function renderGrid() {
  if (!grid) return
  grid.innerHTML = variants.map((variant) => `
    <article class="focus-tile">
      <div class="focus-copy">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${stageMarkup(variant.id, false)}
    </article>
  `).join('')

  for (const stage of grid.querySelectorAll('.focus-demo')) {
    stage.addEventListener('click', () => stage.classList.toggle('is-focused'))
  }
}

function renderControls() {
  if (!controls) return
  controls.innerHTML = variants.map((variant) => `
    <button type="button" data-focus-style="${variant.id}" aria-pressed="${variant.id === 'f2' ? 'true' : 'false'}">${variant.code}<br>${variant.label}</button>
  `).join('')

  for (const button of controls.querySelectorAll('button[data-focus-style]')) {
    button.addEventListener('click', () => {
      const next = button.dataset.focusStyle || 'f2'
      document.documentElement.dataset.focusStyle = next
      practicalFocused = false
      renderPractical(next)
      for (const candidate of controls.querySelectorAll('button[data-focus-style]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.focusStyle === next))
      }
      const variant = variants.find((item) => item.id === next) || variants[2]
      if (summary) summary.textContent = `${variant.code} · ${variant.label}`
    })
  }
}

function renderPractical(style) {
  if (!practical) return
  practical.innerHTML = stageInner(style, true)
  practical.dataset.style = style
  practical.classList.toggle('is-focused', practicalFocused)
  practical.addEventListener('click', handlePracticalClick, { once: true })
}

function handlePracticalClick(event) {
  if (event.target.closest('.workspace-bar button')) return
  practicalFocused = !practicalFocused
  practical.classList.toggle('is-focused', practicalFocused)
  practical.addEventListener('click', handlePracticalClick, { once: true })
}

function stageMarkup(style, focused) {
  return `<div class="focus-demo ${focused ? 'is-focused' : ''}" data-style="${style}">${stageInner(style, false)}</div>`
}

function stageInner(style, large) {
  return `
    <div class="map-layer">
      <div class="map-node a"><span>QUESTION</span><strong>Resolve target definition</strong></div>
      <div class="map-node b"><span>VALIDATION</span><strong>Chronological validation</strong></div>
      <div class="map-node c"><span>MODEL WORK</span><strong>Boosted candidate</strong></div>
      <div class="map-node d"><span>EVALUATION</span><strong>Calibration review</strong></div>
      <article class="x5-card">
        <span class="card-kicker">Investigation · Current · Blocked · High</span>
        <h3>Production missingness</h3>
        <span class="card-meta">SEL2 selected · X5 expanded · L0 working default</span>
        <div class="flat-fields">
          <div><span>Purpose</span><strong>Profile production missingness</strong></div>
          <div><span>Constraint</span><strong>Target definition unresolved</strong></div>
          <div><span>Evidence</span><strong>Schema + missingness profile</strong></div>
          <div><span>Next action</span><strong>Resume after blocker clears</strong></div>
        </div>
      </article>
    </div>
    <div class="workspace-layer">
      <section class="workspace-shell">
        <div class="workspace-bar">
          <div><span>Specialist workspace</span><strong>Production missingness</strong></div>
          <button type="button" tabindex="-1">Return to project</button>
        </div>
        <div class="workspace-content">
          <div class="work-main">
            <div class="work-panel"><span>Primary analytical surface</span><strong>Full-resolution investigation tools mount here</strong></div>
            <div class="work-panel"><span>Evidence / outputs</span><strong>Artifacts, plots, tables and execution results</strong></div>
          </div>
          <div class="work-side">
            <div class="work-panel"><span>Work-unit context</span><strong>Objective, constraints and current state</strong></div>
            <div class="work-panel"><span>Commands / notes</span><strong>Specialist actions without loading unrelated project work</strong></div>
          </div>
        </div>
      </section>
    </div>
    <span class="enter-chip">${large ? 'Click scene to enter / return' : 'Click to enter / return'}</span>
  `
}
