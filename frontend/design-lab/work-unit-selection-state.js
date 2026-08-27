const html = document.documentElement
const rowsHost = document.querySelector('#selection-rows')
const practicalHost = document.querySelector('#selection-practical-nodes')
const summary = document.querySelector('#selection-summary')
const nodeSummary = document.querySelector('#selection-node-summary')
const clearButton = document.querySelector('#clear-selection')

const selectionVariants = [
  { id: 'sel0', code: 'SEL0', label: 'Neutral Control', description: 'No selected-specific cue. Establishes whether selection can remain understandable without a persistent visual carrier.' },
  { id: 'sel1', code: 'SEL1', label: 'Outer Keyline', description: 'A thin neutral-cool outline sits just outside the work-unit frame and remains after pointer exit.' },
  { id: 'sel2', code: 'SEL2', label: 'Corner Brackets', description: 'Four compact persistent brackets mark the selected work unit without recoloring its category perimeter.' },
  { id: 'sel3', code: 'SEL3', label: 'Inner Frame', description: 'A restrained inset frame marks selection inside the card while leaving outer hover/world effects untouched.' },
  { id: 'sel4', code: 'SEL4', label: 'Edge Ticks', description: 'Four small mid-edge ticks provide an instrument-like selected-object cue while intentionally testing port/priority confusion.' },
  { id: 'sel5', code: 'SEL5', label: 'Selection Plate', description: 'Persistent subtle elevation and shadow test whether selected state can be expressed spatially without collapsing into H4 hover lift.' },
  { id: 'sel6', code: 'SEL6', label: 'Soft Contour', description: 'A low-salience cool contour/glow tests a gentle persistent treatment while risking confusion with H4 world illumination.' },
  { id: 'sel7', code: 'SEL7', label: 'Double Corner', description: 'Only upper-left and lower-right receive selection brackets, testing an asymmetric minimal signal.' },
  { id: 'sel8', code: 'SEL8', label: 'Keyline + Corners', description: 'Combines the outer keyline and corner brackets to test whether restrained redundancy improves persistence recognition.' },
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
  { key: 'q', category: 'question', disposition: 'current', status: 'HUMAN', priority: 'high', title: 'Resolve target definition', subtitle: 'High attention and waiting for a human decision' },
  { key: 'i', category: 'investigation', disposition: 'current', status: 'BLOCKED', priority: 'high', title: 'Production missingness', subtitle: 'Selected initially; blocked by unresolved upstream work' },
  { key: 'v', category: 'validation', disposition: 'recommended', status: 'NONE', priority: 'normal', title: 'Chronological validation', subtitle: 'Known next work without elevated attention' },
  { key: 'm', category: 'model', disposition: 'current', status: 'FAIL', priority: 'high', title: 'Boosted candidate', subtitle: 'Failed attempt that still deserves elevated attention' },
  { key: 'r', category: 'investigation', disposition: 'current', status: 'RUN', priority: 'normal', title: 'Schema profiling', subtitle: 'Running normally with ordinary attention' },
  { key: 'e', category: 'evaluation', disposition: 'deferred', status: 'NONE', priority: 'normal', title: 'Calibration review', subtitle: 'Deferred and currently unselected' },
]

let selectedKey = 'i'

renderRows()
renderPractical()
setupControls()
setupPracticalInteractions()
updateControls()
updateSelectionSummary()

function renderRows() {
  if (!rowsHost) return
  rowsHost.innerHTML = selectionVariants.map((variant) => `
    <article class="selection-row">
      <div class="selection-label">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${nodeMarkup({
        key: `controlled-${variant.id}`,
        category: 'investigation',
        disposition: 'current',
        status: 'RUN',
        priority: 'high',
        selected: true,
        selectionStyle: variant.id,
        title: 'Production missingness',
        subtitle: 'Current + RUN + HIGH attention + SELECTED',
        extraClass: 'selection-node',
        interactive: false,
      })}
    </article>
  `).join('')

  setupHoverInteractions('.selection-node')
}

function renderPractical() {
  if (!practicalHost) return
  const style = html.dataset.practicalSelection || 'sel2'
  practicalHost.innerHTML = practicalFixture.map((item) => nodeMarkup({
    ...item,
    selected: item.key === selectedKey,
    selectionStyle: style,
    extraClass: `selection-practical-node scene-${item.key}`,
    interactive: true,
  })).join('')
}

function nodeMarkup({ key, category, disposition, status, priority, selected, selectionStyle, title, subtitle, extraClass, interactive }) {
  const meta = categoryMeta[category]
  const projectState = dispositions[disposition]
  const statusState = statusMeta[status] || statusMeta.NONE
  const tab = interactive ? 'tabindex="0" role="button"' : ''
  const aria = interactive ? `aria-label="Select ${title}"` : ''

  return `
    <div class="grammar-node custom-node category-${category} ${extraClass}"
      data-node-key="${key}"
      data-state="${disposition}"
      data-status-source="${statusState.source}"
      data-status-code="${statusState.code}"
      data-status-carrier="dot"
      data-priority="${priority}"
      data-priority-style="a3"
      data-selected="${selected ? 'true' : 'false'}"
      data-selection-style="${selectionStyle}"
      data-light-side="left"
      ${tab}
      ${aria}
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
        ${priorityMarkup(priority)}
        ${selectionMarkup()}
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

function priorityMarkup(priority) {
  if (priority !== 'high') return ''
  return '<span class="priority-signal-bars" aria-hidden="true"><i></i><i></i><i></i></span>'
}

function selectionMarkup() {
  return `
    <span class="selection-keyline" aria-hidden="true"></span>
    <span class="selection-corners" aria-hidden="true">
      <i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i>
    </span>
    <span class="selection-inner-frame" aria-hidden="true"></span>
    <span class="selection-edge-ticks" aria-hidden="true">
      <i class="top"></i><i class="right"></i><i class="bottom"></i><i class="left"></i>
    </span>
    <span class="selection-soft-contour" aria-hidden="true"></span>
    <span class="selection-double-corner" aria-hidden="true"><i class="tl"></i><i class="br"></i></span>
  `
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-selection-style]')) {
    button.addEventListener('click', () => {
      html.dataset.practicalSelection = button.dataset.selectionStyle
      for (const node of document.querySelectorAll('.selection-practical-node')) {
        node.dataset.selectionStyle = button.dataset.selectionStyle
      }
      updateControls()
    })
  }

  clearButton?.addEventListener('click', () => {
    selectedKey = ''
    for (const node of document.querySelectorAll('.selection-practical-node')) {
      node.dataset.selected = 'false'
    }
    updateSelectionSummary()
  })
}

function setupPracticalInteractions() {
  setupHoverInteractions('.selection-practical-node')

  for (const node of document.querySelectorAll('.selection-practical-node')) {
    if (node.dataset.selectionReady === 'true') continue
    node.dataset.selectionReady = 'true'

    node.addEventListener('click', () => selectNode(node.dataset.nodeKey || ''))
    node.addEventListener('keydown', (event) => {
      if (event.key !== 'Enter' && event.key !== ' ') return
      event.preventDefault()
      selectNode(node.dataset.nodeKey || '')
    })
  }
}

function selectNode(key) {
  if (!key) return
  selectedKey = key
  for (const node of document.querySelectorAll('.selection-practical-node')) {
    node.dataset.selected = String(node.dataset.nodeKey === selectedKey)
  }
  updateSelectionSummary()
}

function updateControls() {
  const active = html.dataset.practicalSelection || 'sel2'
  for (const button of document.querySelectorAll('button[data-selection-style]')) {
    button.setAttribute('aria-pressed', String(button.dataset.selectionStyle === active))
  }
  const variant = selectionVariants.find((item) => item.id === active) || selectionVariants[2]
  if (summary) summary.textContent = `${variant.code} · ${variant.label}`
}

function updateSelectionSummary() {
  if (!nodeSummary) return
  if (!selectedKey) {
    nodeSummary.textContent = 'Selected: none'
    return
  }
  const item = practicalFixture.find((candidate) => candidate.key === selectedKey)
  nodeSummary.textContent = item ? `Selected: ${item.title}` : `Selected: ${selectedKey}`
}

function setupHoverInteractions(selector) {
  for (const node of document.querySelectorAll(selector)) {
    if (node.dataset.selectionHoverReady === 'true') continue
    node.dataset.selectionHoverReady = 'true'

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
