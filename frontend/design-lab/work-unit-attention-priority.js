const html = document.documentElement
const rowsHost = document.querySelector('#priority-rows')
const practicalHost = document.querySelector('#priority-practical-nodes')
const summary = document.querySelector('#priority-summary')

const priorityVariants = [
  { id: 'a0', code: 'A0', label: 'Neutral Control', description: 'No priority-specific cue. Establishes the baseline and whether priority can be inferred at all without a dedicated carrier.' },
  { id: 'a1', code: 'A1', label: 'Twin Tick', description: 'Two tiny neutral attention ticks rise from the upper frame, adding a compact learned signal without another label.' },
  { id: 'a2', code: 'A2', label: 'Top Rail', description: 'A short champagne rail sits on the upper frame. It is structural, restrained and spatially separated from disposition and status.' },
  { id: 'a3', code: 'A3', label: 'Signal Bars', description: 'Three ascending micro-bars test an instrument-like attention signal with future ordinal potential but no scale is frozen here.' },
  { id: 'a4', code: 'A4', label: 'Side Bracket', description: 'A slim bracket grips the right-middle edge, testing whether importance can read as emphasis without text or broad recoloring.' },
  { id: 'a5', code: 'A5', label: 'HIGH Tag', description: 'An explicit HIGH tag maximizes clarity but deliberately tests whether another textual badge creates excessive label density.' },
  { id: 'a6', code: 'A6', label: 'Beacon', description: 'A small hollow diamond sits just above the frame. This tests a compact beacon while risking confusion with connector ports.' },
  { id: 'a7', code: 'A7', label: 'Luminance Lift', description: 'No new symbol. The whole surface becomes slightly brighter, intentionally testing whether priority collapses into focus/hover language.' },
  { id: 'a8', code: 'A8', label: 'Rail + Tag', description: 'Combines the structural top rail with explicit HIGH text to test whether restrained redundant signaling is worth the extra density.' },
]

const statusMeta = {
  NONE: { code: 'NONE', rgb: '145, 158, 179', source: 'none' },
  BLOCKED: { code: 'BLOCKED', rgb: '237, 112, 105', source: 'constraint' },
  FAIL: { code: 'FAIL', rgb: '237, 112, 105', source: 'runtime' },
  RUN: { code: 'RUN', rgb: '103, 218, 194', source: 'runtime' },
  HUMAN: { code: 'HUMAN', rgb: '173, 150, 255', source: 'runtime' },
}

const dispositions = {
  current: { code: 'CURRENT', rgb: '102, 181, 255' },
  recommended: { code: 'NEXT', rgb: '177, 151, 255' },
  deferred: { code: 'DEFER', rgb: '145, 158, 179' },
  future: { code: 'FUTURE', rgb: '122, 139, 163' },
}

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
}

const practicalFixture = [
  { key: 'q', category: 'question', disposition: 'current', status: 'HUMAN', priority: 'high', title: 'Resolve target definition', subtitle: 'High attention while waiting for a human decision' },
  { key: 'i', category: 'investigation', disposition: 'current', status: 'BLOCKED', priority: 'high', title: 'Production missingness', subtitle: 'High attention even though progress is currently blocked' },
  { key: 'v', category: 'validation', disposition: 'recommended', status: 'NONE', priority: 'normal', title: 'Chronological validation', subtitle: 'Known next work without elevated attention' },
  { key: 'm', category: 'model', disposition: 'current', status: 'FAIL', priority: 'high', title: 'Boosted candidate', subtitle: 'Failed attempt that still deserves immediate attention' },
  { key: 'r', category: 'investigation', disposition: 'current', status: 'RUN', priority: 'normal', title: 'Schema profiling', subtitle: 'Running normally, but not currently elevated in attention' },
  { key: 'e', category: 'evaluation', disposition: 'deferred', status: 'NONE', priority: 'normal', title: 'Calibration review', subtitle: 'Deferred and not currently high attention' },
]

renderRows()
renderPractical()
setupControls()
setupInteractions()
updateControls()

function renderRows() {
  if (!rowsHost) return
  rowsHost.innerHTML = priorityVariants.map((variant) => `
    <article class="priority-row">
      <div class="priority-label">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${nodeMarkup({
        category: 'investigation',
        disposition: 'current',
        status: 'RUN',
        priority: 'high',
        priorityStyle: variant.id,
        title: 'Production missingness',
        subtitle: 'Current + RUN + HIGH attention',
        extraClass: 'priority-node',
      })}
    </article>
  `).join('')
}

function renderPractical() {
  if (!practicalHost) return
  const style = html.dataset.practicalPriority || 'a2'
  practicalHost.innerHTML = practicalFixture.map((item) => nodeMarkup({
    ...item,
    priorityStyle: style,
    extraClass: `priority-practical-node scene-${item.key}`,
  })).join('')
  setupInteractions()
}

function nodeMarkup({ category, disposition, status, priority, priorityStyle, title, subtitle, extraClass }) {
  const meta = categoryMeta[category]
  const projectState = dispositions[disposition]
  const statusState = statusMeta[status] || statusMeta.NONE

  return `
    <div class="grammar-node custom-node category-${category} ${extraClass}"
      data-state="${disposition}"
      data-status-source="${statusState.source}"
      data-status-code="${statusState.code}"
      data-status-carrier="dot"
      data-priority="${priority}"
      data-priority-style="${priorityStyle}"
      data-light-side="left"
      style="--node-rgb:${meta.rgb}; --state-rgb:${projectState.rgb}; --status-rgb:${statusState.rgb}; --light-anchor:50%;">
      <span class="rest-spill" aria-hidden="true"></span>
      <span class="rest-light" aria-hidden="true"></span>
      <span class="hover-light" aria-hidden="true"></span>
      <span class="hover-world-light" aria-hidden="true"></span>
      <span class="disposition-state-outline" aria-hidden="true"></span>
      <div class="node-surface">
        <span class="surface-rest-light" aria-hidden="true"></span>
        <span class="custom-material-layer" aria-hidden="true"></span>
        <span class="custom-lumen-layer" aria-hidden="true"></span>
        <span class="pointer-light" aria-hidden="true"></span>
        <span class="perimeter-sweep" aria-hidden="true"></span>
        <span class="frame-signature" aria-hidden="true"></span>
        <span class="disposition-state-rhythm" aria-hidden="true"></span>
        <span class="disposition-state-badge" aria-hidden="true">${projectState.code}</span>
        ${statusMarkup(statusState)}
        ${priorityMarkup()}
        <div class="node-heading">
          <span class="category-glyph" aria-hidden="true">${meta.glyph}</span>
          <span class="unit-kind">${meta.kind}</span>
        </div>
        <strong>${title}</strong>
        <small>${subtitle}</small>
      </div>
    </div>
  `
}

function statusMarkup(statusState) {
  if (statusState.code === 'NONE') return ''
  return `
    <span class="status-dot-carrier" aria-hidden="true">
      <span class="status-dot-core"></span>
      <span class="status-dot-ring"></span>
    </span>
  `
}

function priorityMarkup() {
  return `
    <span class="priority-twin-tick" aria-hidden="true"></span>
    <span class="priority-top-rail" aria-hidden="true"></span>
    <span class="priority-signal-bars" aria-hidden="true"><i></i><i></i><i></i></span>
    <span class="priority-side-bracket" aria-hidden="true"></span>
    <span class="priority-tag" aria-hidden="true">HIGH</span>
    <span class="priority-beacon" aria-hidden="true"></span>
  `
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-priority-style]')) {
    button.addEventListener('click', () => {
      html.dataset.practicalPriority = button.dataset.priorityStyle
      for (const node of document.querySelectorAll('.priority-practical-node')) {
        node.dataset.priorityStyle = button.dataset.priorityStyle
      }
      updateControls()
    })
  }
}

function updateControls() {
  const active = html.dataset.practicalPriority || 'a2'
  for (const button of document.querySelectorAll('button[data-priority-style]')) {
    button.setAttribute('aria-pressed', String(button.dataset.priorityStyle === active))
  }
  const variant = priorityVariants.find((item) => item.id === active) || priorityVariants[2]
  if (summary) summary.textContent = `${variant.code} · ${variant.label}`
}

function setupInteractions() {
  for (const node of document.querySelectorAll('.priority-node, .priority-practical-node')) {
    if (node.dataset.priorityInteractionReady === 'true') continue
    node.dataset.priorityInteractionReady = 'true'

    node.addEventListener('pointerenter', () => {
      node.classList.add('is-hovered')
      triggerSweep(node)
    })

    node.addEventListener('pointermove', (event) => {
      const surface = node.querySelector('.node-surface')
      if (!surface) return
      const rect = surface.getBoundingClientRect()
      const x = ((event.clientX - rect.left) / rect.width) * 100
      const y = ((event.clientY - rect.top) / rect.height) * 100
      node.style.setProperty('--pointer-x', `${clamp(x, 0, 100)}%`)
      node.style.setProperty('--pointer-y', `${clamp(y, 0, 100)}%`)
    })

    node.addEventListener('pointerleave', () => {
      node.classList.remove('is-hovered')
    })
  }
}

function triggerSweep(node) {
  node.classList.remove('sweep-active')
  void node.offsetWidth
  node.classList.add('sweep-active')
  window.setTimeout(() => node.classList.remove('sweep-active'), 820)
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}
