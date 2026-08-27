const variants = [
  { id: 'z0', code: 'Z0', label: 'Direct Replace Control', description: 'Baseline. Fade the project world away and reveal the fullscreen specialist workspace with no spatial metaphor.' },
  { id: 'z1', code: 'Z1', label: 'Card Zoom-In', description: 'The selected X5 work unit grows toward the viewer while the surrounding world is swallowed behind it.' },
  { id: 'z2', code: 'Z2', label: 'World Falls Away', description: 'The project world rapidly recedes into depth while the selected card pushes forward before becoming the workspace.' },
  { id: 'z3', code: 'Z3', label: 'Camera Dive', description: 'The camera appears to move directly through the selected work unit, with the project grid rushing past the viewport.' },
  { id: 'z4', code: 'Z4', label: 'Workspace Aperture', description: 'The selected card becomes a literal aperture containing the specialist workspace, then that aperture expands to fill the stage.' },
  { id: 'z5', code: 'Z5', label: 'Depth Parallax', description: 'Nearby project objects separate into depth layers and move outward while the selected object advances into the workspace.' },
  { id: 'z6', code: 'Z6', label: 'Perspective Corridor', description: 'The grid tilts into a perspective corridor and rushes beneath the camera as deep focus takes over.' },
  { id: 'z7', code: 'Z7', label: 'Pull-Back Then Dive', description: 'A brief backward camera move establishes spatial depth before accelerating forward through the selected work unit.' },
]

const grid = document.querySelector('#zoom-grid')
const controls = document.querySelector('#zoom-controls')
const practical = document.querySelector('#practical-stage')
const summary = document.querySelector('#zoom-summary')
let currentStyle = 'z3'
let practicalFocused = false

renderGrid()
renderControls()
renderPractical(currentStyle)

function renderGrid() {
  if (!grid) return
  grid.innerHTML = variants.map((variant) => `
    <article class="zoom-tile">
      <div class="zoom-copy">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${stageMarkup(variant.id, false)}
    </article>
  `).join('')

  for (const stage of grid.querySelectorAll('.zoom-demo')) bindStage(stage)
}

function renderControls() {
  if (!controls) return
  controls.innerHTML = variants.map((variant) => `
    <button type="button" data-zoom-style="${variant.id}" aria-pressed="${variant.id === currentStyle ? 'true' : 'false'}">
      ${variant.code}<br>${variant.label}
    </button>
  `).join('')

  for (const button of controls.querySelectorAll('button[data-zoom-style]')) {
    button.addEventListener('click', () => {
      currentStyle = button.dataset.zoomStyle || 'z3'
      practicalFocused = false
      renderPractical(currentStyle)
      for (const candidate of controls.querySelectorAll('button[data-zoom-style]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.zoomStyle === currentStyle))
      }
      const variant = variantById(currentStyle)
      if (summary && variant) summary.textContent = `${variant.code} · ${variant.label}`
    })
  }
}

function stageMarkup(style, large) {
  return `<div class="zoom-demo" data-style="${style}">${stageInner(large)}</div>`
}

function stageInner(large) {
  return `
    <div class="world-layer">
      <svg class="scene-links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <path class="direct" d="M17 24 C31 29 47 35 61 45" />
        <path class="direct" d="M83 26 C78 32 71 38 64 45" />
        <path d="M21 79 C36 70 49 58 61 49" />
        <path d="M82 78 C75 67 69 57 63 49" />
      </svg>
      <div class="map-node a"><span>QUESTION / BLOCKER</span><strong>Resolve target definition</strong></div>
      <div class="map-node b"><span>VALIDATION</span><strong>Chronological validation</strong></div>
      <div class="map-node c"><span>MODEL WORK</span><strong>Boosted candidate</strong></div>
      <div class="map-node d"><span>EVALUATION</span><strong>Calibration review</strong></div>
      <article class="x5-card">
        <i class="sel-corner tl"></i><i class="sel-corner tr"></i><i class="sel-corner bl"></i><i class="sel-corner br"></i>
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
          <button type="button" class="return-button" tabindex="-1">Return to project</button>
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

    <aside class="topology-compass" aria-hidden="true">
      <span>Project position</span>
      <div class="mini-map">
        <i class="mini-dot a"></i><i class="mini-dot b"></i><i class="mini-dot c"></i><i class="mini-dot d"></i><i class="mini-dot s"></i>
      </div>
    </aside>

    <span class="enter-chip">${large ? 'Click scene to enter / return' : 'Click to enter / return'}</span>
  `
}

function bindStage(stage) {
  syncOrigin(stage)
  stage.addEventListener('click', (event) => {
    if (event.target.closest('.return-button')) {
      leaveFocus(stage)
      return
    }
    stage.classList.contains('is-focused') ? leaveFocus(stage) : enterFocus(stage)
  })

  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(() => syncOrigin(stage))
    observer.observe(stage)
  }
}

function enterFocus(stage) {
  syncOrigin(stage)
  stage.classList.add('is-focused')
  if (stage === practical) practicalFocused = true
}

function leaveFocus(stage) {
  stage.classList.remove('is-focused')
  if (stage === practical) practicalFocused = false
}

function syncOrigin(stage) {
  const card = stage.querySelector('.x5-card')
  if (!card) return
  const stageRect = stage.getBoundingClientRect()
  const cardRect = card.getBoundingClientRect()
  const left = cardRect.left - stageRect.left
  const top = cardRect.top - stageRect.top
  const width = cardRect.width
  const height = cardRect.height
  const right = Math.max(0, stageRect.width - left - width)
  const bottom = Math.max(0, stageRect.height - top - height)
  const cx = left + width / 2
  const cy = top + height / 2

  stage.style.setProperty('--origin-left', `${left}px`)
  stage.style.setProperty('--origin-top', `${top}px`)
  stage.style.setProperty('--origin-width', `${width}px`)
  stage.style.setProperty('--origin-height', `${height}px`)
  stage.style.setProperty('--origin-right', `${right}px`)
  stage.style.setProperty('--origin-bottom', `${bottom}px`)
  stage.style.setProperty('--origin-cx', `${cx}px`)
  stage.style.setProperty('--origin-cy', `${cy}px`)
}

function renderPractical(style) {
  if (!practical) return
  practical.classList.remove('is-focused')
  practical.innerHTML = stageInner(true)
  practical.dataset.style = style
  practicalFocused = false
  syncOrigin(practical)

  if (practical.dataset.bound !== 'true') {
    practical.dataset.bound = 'true'
    practical.addEventListener('click', (event) => {
      if (event.target.closest('.return-button')) {
        leaveFocus(practical)
        return
      }
      practical.classList.contains('is-focused') ? leaveFocus(practical) : enterFocus(practical)
    })
    if ('ResizeObserver' in window) {
      const observer = new ResizeObserver(() => syncOrigin(practical))
      observer.observe(practical)
    }
  }
}

function variantById(id) {
  return variants.find((variant) => variant.id === id)
}
