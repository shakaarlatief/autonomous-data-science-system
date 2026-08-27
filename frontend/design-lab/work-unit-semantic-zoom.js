const variants = [
  { id: 's0', code: 'S0', label: 'Geometric Control', description: 'Control. Keep essentially the same information at every scale and only make the objects physically smaller.' },
  { id: 's1', code: 'S1', label: 'Progressive Detail', description: 'Reveal information in tiers: identity at overview, operational metadata at work scale, richer rationale at inspection.' },
  { id: 's2', code: 'S2', label: 'Stage Clusters', description: 'At distance, replace individual work units with stage-level aggregate objects; progressively resolve into real units as scale increases.' },
  { id: 's3', code: 'S3', label: 'Topology First', description: 'At overview scale, privilege relation structure and category markers over labels and metadata.' },
  { id: 's4', code: 'S4', label: 'Focus Preserving', description: 'Current and selected work retain more information while surrounding context simplifies much earlier.' },
  { id: 's5', code: 'S5', label: 'Status First', description: 'Overview scale preserves operational/project-state signals before descriptive identity and detail.' },
  { id: 's6', code: 'S6', label: 'Glyph Field', description: 'Collapse distant work units almost entirely into scientific/category glyphs and topology, then resolve them on approach.' },
  { id: 's7', code: 'S7', label: 'Hybrid Contextual', description: 'Keep current/selected work richer, compress background work, and preserve enough labels plus topology to keep the world readable.' },
  { id: 's8', code: 'S8', label: 'Local Detail Lens', description: 'Keep the global map highly compressed at overview scale but allow the selected object to remain locally rich like a semantic lens.' },
]

const scales = ['overview', 'work', 'inspection']
const grid = document.querySelector('#semantic-grid')
const controls = document.querySelector('#semantic-controls')
const practical = document.querySelector('#practical-stage')
const summary = document.querySelector('#semantic-summary')
let currentStyle = 's7'
let currentScale = 'work'

renderGrid()
renderControls()
setupScaleControls()
renderPractical()

function renderGrid() {
  if (!grid) return
  grid.innerHTML = variants.map((variant) => `
    <article class="semantic-row">
      <div class="semantic-copy">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${scales.map((scale) => `
        <div class="scale-cell">
          <span class="scale-label">${scale}</span>
          <div class="semantic-stage" data-style="${variant.id}" data-scale="${scale}">${stageInner(false)}</div>
        </div>
      `).join('')}
    </article>
  `).join('')
}

function renderControls() {
  if (!controls) return
  controls.innerHTML = variants.map((variant) => `
    <button type="button" data-semantic-style="${variant.id}" aria-pressed="${variant.id === currentStyle}">
      ${variant.code}<br>${variant.label}
    </button>
  `).join('')

  for (const button of controls.querySelectorAll('button[data-semantic-style]')) {
    button.addEventListener('click', () => {
      currentStyle = button.dataset.semanticStyle || 's7'
      document.documentElement.dataset.semanticStyle = currentStyle
      for (const candidate of controls.querySelectorAll('button[data-semantic-style]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.semanticStyle === currentStyle))
      }
      const variant = variantById(currentStyle)
      if (summary && variant) summary.textContent = `${variant.code} · ${variant.label}`
      renderPractical()
    })
  }
}

function setupScaleControls() {
  for (const button of document.querySelectorAll('button[data-scale-mode]')) {
    button.addEventListener('click', () => {
      currentScale = button.dataset.scaleMode || 'work'
      document.documentElement.dataset.scale = currentScale
      for (const candidate of document.querySelectorAll('button[data-scale-mode]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.scaleMode === currentScale))
      }
      renderPractical()
    })
  }
}

function renderPractical() {
  if (!practical) return
  practical.dataset.style = currentStyle
  practical.dataset.scale = currentScale
  practical.innerHTML = stageInner(true)
}

function stageInner(large) {
  const scaleFactor = large ? 1.8 : 1
  return `
    <div class="stage-band one"></div><div class="stage-band two"></div><div class="stage-band three"></div>
    <span class="stage-name one">Define</span><span class="stage-name two">Investigate</span><span class="stage-name three">Evaluate</span>
    <svg class="links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
      <path class="active" d="M18 34 C29 38 39 42 47 33" />
      <path class="active" d="M49 36 C56 41 64 39 75 38" />
      <path d="M48 37 C50 49 48 60 47 68" />
      <path d="M51 68 C61 66 68 68 76 73" />
    </svg>
    <div class="cluster one"><span>Stage</span><strong>Definition · 1 open blocker</strong></div>
    <div class="cluster two"><span>Stage</span><strong>Investigation · 2 current units</strong></div>
    <div class="cluster three"><span>Stage</span><strong>Evaluation · 2 downstream units</strong></div>

    <article class="unit question a" style="--fixture-scale:${scaleFactor}">
      <div class="kind"><span class="marker"></span><span>Question / Blocker</span></div>
      <h3>Resolve target definition</h3>
      <div class="meta"><span class="tag">CURRENT</span><span class="tag status">HUMAN</span></div>
      <p class="detail">Resolve business target semantics before validation can proceed.</p>
    </article>

    <article class="unit investigation c current selected" style="--fixture-scale:${scaleFactor}">
      <span class="signal"><i></i><i></i><i></i></span>
      <div class="kind"><span class="marker"></span><span>Investigation</span></div>
      <h3>Production missingness</h3>
      <div class="meta"><span class="tag">CURRENT</span><span class="tag status">BLOCKED</span></div>
      <p class="detail">Profile schema drift and production missingness before resuming model validation.</p>
    </article>

    <article class="unit validation b current" style="--fixture-scale:${scaleFactor}">
      <div class="kind"><span class="marker"></span><span>Validation</span></div>
      <h3>Chronological validation</h3>
      <div class="meta"><span class="tag">NEXT</span><span class="tag status">QUEUE</span></div>
      <p class="detail">Run leakage-safe chronological validation after the blocker clears.</p>
    </article>

    <article class="unit model d" style="--fixture-scale:${scaleFactor}">
      <div class="kind"><span class="marker"></span><span>Model Work</span></div>
      <h3>Boosted candidate</h3>
      <div class="meta"><span class="tag">DEFER</span></div>
      <p class="detail">Candidate remains downstream context and is not part of the current process focus.</p>
    </article>

    <article class="unit evaluation e" style="--fixture-scale:${scaleFactor}">
      <div class="kind"><span class="marker"></span><span>Evaluation</span></div>
      <h3>Calibration review</h3>
      <div class="meta"><span class="tag">FUTURE</span></div>
      <p class="detail">Review calibration and threshold behavior after final validation evidence exists.</p>
    </article>
  `
}

function variantById(id) {
  return variants.find((variant) => variant.id === id)
}