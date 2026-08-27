const batches = {
  a: [
    { id: 'a0', code: 'A0', label: 'F2 Anchored Morph Control', description: 'Current object-continuity control. The workspace grows from the selected card into a near-full workspace while the world softly recedes.' },
    { id: 'a1', code: 'A1', label: 'Anchored Center Stage', description: 'T1 applied to F1. Keep Center Stage retention, but derive workspace entry from the selected card\'s actual rendered position.' },
    { id: 'a2', code: 'A2', label: 'Anchored Context Rail', description: 'T1 applied to F6. Keep the original fixed side rail, but make the workspace itself originate from the selected card.' },
    { id: 'a3', code: 'A3', label: 'Camera Push-Through', description: 'T5. Move the world forward through the selected card with a simulated depth push rather than a 2D card-to-workspace morph.' },
  ],
  b: [
    { id: 'b0', code: 'B0', label: 'F6 Fixed Rail Control', description: 'Intentionally preserves F6\'s known flaw: the same left 22% of the map remains visible regardless of which work unit was selected.' },
    { id: 'b1', code: 'B1', label: 'Neighbor-Aware Context', description: 'T2. Replace arbitrary geometric retention with compact representations of work directly connected to the selected node.' },
    { id: 'b2', code: 'B2', label: 'Neighbor-Aware + Anchor', description: 'T2 + T1. Retain only relevant connected work while also growing the workspace from the selected card\'s actual rendered position.' },
  ],
  c: [
    { id: 'c0', code: 'C0', label: 'Hard Replace Control', description: 'F0 floor. The workspace replaces the map with no retained map or orientation aid.' },
    { id: 'c1', code: 'C1', label: 'Staged Two-Step Entry', description: 'T3. One click passes through a brief lift-and-preview stage before continuing automatically into full deep focus.' },
    { id: 'c2', code: 'C2', label: 'Compass + Soft World', description: 'T7 with a lightly retained world. A compact topology compass marks the selected node\'s position while the map becomes strongly secondary.' },
    { id: 'c3', code: 'C3', label: 'Hard Replace + Compass', description: 'F0 + T7. Remove the map completely but preserve a minimal topology anchor for return orientation.' },
  ],
}

const variants = [...batches.a, ...batches.b, ...batches.c]
const controls = document.querySelector('#focus-controls')
const practical = document.querySelector('#practical-stage')
const summary = document.querySelector('#focus-summary')
const stagedTimers = new WeakMap()
let currentStyle = 'a0'
let practicalFocused = false
let returnMode = 'symmetric'

renderBatch('batch-a', batches.a)
renderBatch('batch-b', batches.b)
renderBatch('batch-c', batches.c)
renderControls()
setupReturnControls()
renderPractical(currentStyle)

function renderBatch(id, batch) {
  const root = document.querySelector(`#${id}`)
  if (!root) return
  root.innerHTML = batch.map((variant) => `
    <article class="focus-tile">
      <div class="focus-copy">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${stageMarkup(variant.id, false)}
    </article>
  `).join('')

  for (const stage of root.querySelectorAll('.focus-demo')) bindStage(stage)
}

function renderControls() {
  if (!controls) return
  controls.innerHTML = variants.map((variant) => `
    <button type="button" data-focus-style="${variant.id}" aria-pressed="${variant.id === currentStyle ? 'true' : 'false'}">
      ${variant.code}<br>${variant.label.replace(' Control', '')}
    </button>
  `).join('')

  for (const button of controls.querySelectorAll('button[data-focus-style]')) {
    button.addEventListener('click', () => {
      currentStyle = button.dataset.focusStyle || 'a0'
      practicalFocused = false
      renderPractical(currentStyle)
      for (const candidate of controls.querySelectorAll('button[data-focus-style]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.focusStyle === currentStyle))
      }
      const variant = variantById(currentStyle)
      if (summary && variant) summary.textContent = `${variant.code} · ${variant.label}`
    })
  }
}

function setupReturnControls() {
  for (const button of document.querySelectorAll('button[data-return-mode]')) {
    button.addEventListener('click', () => {
      returnMode = button.dataset.returnMode || 'symmetric'
      for (const candidate of document.querySelectorAll('button[data-return-mode]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.returnMode === returnMode))
      }
      if (practical) practical.dataset.returnMode = returnMode
    })
  }
}

function stageMarkup(style, large) {
  return `<div class="focus-demo" data-style="${style}" data-return-mode="symmetric">${stageInner(style, large)}</div>`
}

function stageInner(style, large) {
  const variant = variantById(style)
  const staged = style === 'c1'
  const chip = staged
    ? 'Click: preview → deep focus → return'
    : (large ? 'Click scene to enter / return' : 'Click to enter / return')

  return `
    <div class="map-layer">
      <svg class="scene-links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <path class="direct" d="M18 26 C34 29 46 38 61 47" />
        <path class="direct" d="M82 25 C76 31 70 39 63 46" />
        <path d="M20 79 C35 72 48 60 61 50" />
        <path d="M82 78 C76 68 70 59 63 50" />
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

    <aside class="neighbor-tray" aria-hidden="true">
      <div class="neighbor-card"><span>Direct neighbor</span><strong>Resolve target definition</strong><em>BLOCKS selected work</em></div>
      <div class="neighbor-card"><span>Direct neighbor</span><strong>Chronological validation</strong><em>Connected downstream context</em></div>
    </aside>

    <aside class="topology-compass" aria-hidden="true">
      <span>Project position</span>
      <div class="mini-map">
        <i class="mini-dot a"></i><i class="mini-dot b"></i><i class="mini-dot c"></i><i class="mini-dot d"></i><i class="mini-dot s"></i>
      </div>
    </aside>

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
    <span class="enter-chip">${chip}</span>
  `
}

function bindStage(stage) {
  syncOrigin(stage)
  stage.addEventListener('click', (event) => {
    if (event.target.closest('.return-button')) {
      returnFromFocus(stage)
      return
    }
    toggleStage(stage)
  })

  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(() => syncOrigin(stage))
    observer.observe(stage)
  }
}

function toggleStage(stage) {
  if (stage.classList.contains('is-focused')) {
    returnFromFocus(stage)
    return
  }

  if (stage.classList.contains('is-preview')) {
    clearStagedTimer(stage)
    finishStagedEntry(stage)
    return
  }

  if (stage.dataset.style === 'c1') {
    beginStagedEntry(stage)
    return
  }

  enterFocus(stage)
}

function enterFocus(stage) {
  syncOrigin(stage)
  stage.classList.remove('is-returning', 'is-preview')
  stage.classList.add('is-focused')
  if (stage === practical) practicalFocused = true
}

function beginStagedEntry(stage) {
  syncOrigin(stage)
  stage.classList.remove('is-returning', 'is-focused')
  stage.classList.add('is-preview')
  const timer = window.setTimeout(() => finishStagedEntry(stage), 620)
  stagedTimers.set(stage, timer)
}

function finishStagedEntry(stage) {
  clearStagedTimer(stage)
  stage.classList.remove('is-preview')
  stage.classList.add('is-focused')
  if (stage === practical) practicalFocused = true
}

function returnFromFocus(stage) {
  clearStagedTimer(stage)
  const fast = stage.dataset.returnMode === 'fast'
  stage.classList.toggle('is-returning', fast)
  stage.classList.remove('is-preview', 'is-focused')
  if (stage === practical) practicalFocused = false
  if (fast) window.setTimeout(() => stage.classList.remove('is-returning'), 210)
}

function clearStagedTimer(stage) {
  const timer = stagedTimers.get(stage)
  if (timer) window.clearTimeout(timer)
  stagedTimers.delete(stage)
}

function syncOrigin(stage) {
  const card = stage.querySelector('.x5-card')
  if (!card) return
  const stageRect = stage.getBoundingClientRect()
  const cardRect = card.getBoundingClientRect()
  const left = cardRect.left - stageRect.left
  const top = cardRect.top - stageRect.top
  const cx = left + cardRect.width / 2
  const cy = top + cardRect.height / 2
  stage.style.setProperty('--origin-left', `${left}px`)
  stage.style.setProperty('--origin-top', `${top}px`)
  stage.style.setProperty('--origin-width', `${cardRect.width}px`)
  stage.style.setProperty('--origin-height', `${cardRect.height}px`)
  stage.style.setProperty('--origin-cx', `${cx}px`)
  stage.style.setProperty('--origin-cy', `${cy}px`)
}

function renderPractical(style) {
  if (!practical) return
  clearStagedTimer(practical)
  practical.classList.remove('is-focused', 'is-preview', 'is-returning')
  practical.innerHTML = stageInner(style, true)
  practical.dataset.style = style
  practical.dataset.returnMode = returnMode
  syncOrigin(practical)

  if (practical.dataset.bound !== 'true') {
    practical.dataset.bound = 'true'
    practical.addEventListener('click', (event) => {
      if (event.target.closest('.return-button')) {
        returnFromFocus(practical)
        return
      }
      toggleStage(practical)
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
