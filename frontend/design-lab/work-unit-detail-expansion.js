const html = document.documentElement
const comparisonHost = document.querySelector('#expansion-grid')
const practicalHost = document.querySelector('#expansion-practical-nodes')
const inspectorDock = document.querySelector('#inspector-dock')
const summary = document.querySelector('#expansion-summary')
const nodeSummary = document.querySelector('#expansion-node-summary')
const toggleButton = document.querySelector('#toggle-expansion')
const collapseButton = document.querySelector('#collapse-expansion')

const expansionVariants = [
  { id: 'x0', code: 'X0', label: 'Compact Control', description: 'No contextual-detail layer. Establishes the selected compact node as the control and tests whether expansion is actually earning its space.' },
  { id: 'x1', code: 'X1', label: 'Vertical Drawer', description: 'The selected card keeps its width and upper anchor while growing downward into a single integrated detail object.' },
  { id: 'x2', code: 'X2', label: 'Right Sidecar', description: 'The source card remains compact while an attached right-hand detail wing preserves the original node geometry.' },
  { id: 'x3', code: 'X3', label: 'Attached Sheet', description: 'A separate detail sheet hangs directly below the compact node through a short attachment stem.' },
  { id: 'x4', code: 'X4', label: 'Wide Split Card', description: 'The selected node becomes one wider two-column object, keeping summary information on the left and contextual detail on the right.' },
  { id: 'x5', code: 'X5', label: 'Context Lens', description: 'The node grows in both axes and locally suppresses surrounding context, testing the boundary between contextual detail and deep focus.' },
  { id: 'x6', code: 'X6', label: 'Layered Reveal', description: 'The compact selected card remains visually on top while a larger offset detail layer emerges behind it.' },
  { id: 'x7', code: 'X7', label: 'Peek Rail', description: 'Only a shallow contextual rail is exposed, testing whether a minimal intermediate layer is enough before deeper work.' },
  { id: 'x8', code: 'X8', label: 'Inspector Dock', description: 'The node stays compact and a stable scene-level inspector receives the details, deliberately challenging the inline-expansion premise.' },
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
  { key: 'q', category: 'question', disposition: 'current', status: 'HUMAN', priority: 'high', title: 'Resolve target definition', subtitle: 'Waiting for a human decision', detail: detailPayload('Decision needed', 'Human response', 'Target definition evidence', 'Resolve before validation') },
  { key: 'i', category: 'investigation', disposition: 'current', status: 'BLOCKED', priority: 'high', title: 'Production missingness', subtitle: 'Blocked by unresolved upstream work', detail: detailPayload('Profile production missingness', 'Blocked by target definition', 'Schema + missingness profile', 'Resume after blocker clears') },
  { key: 'v', category: 'validation', disposition: 'recommended', status: 'NONE', priority: 'normal', title: 'Chronological validation', subtitle: 'Known next work', detail: detailPayload('Validate temporal generalization', 'No live runtime', 'Split specification', 'Queue after prerequisites') },
  { key: 'm', category: 'model', disposition: 'current', status: 'FAIL', priority: 'high', title: 'Boosted candidate', subtitle: 'Latest execution attempt failed', detail: detailPayload('Fit boosted baseline', 'Failed current attempt', 'Run diagnostics', 'Inspect failure then retry') },
  { key: 'r', category: 'investigation', disposition: 'current', status: 'RUN', priority: 'normal', title: 'Schema profiling', subtitle: 'Running normally', detail: detailPayload('Inspect schema drift', 'Running', 'Column profile', 'Review generated findings') },
  { key: 'e', category: 'evaluation', disposition: 'deferred', status: 'NONE', priority: 'normal', title: 'Calibration review', subtitle: 'Deferred context', detail: detailPayload('Assess calibration', 'Deferred', 'Evaluation plan', 'Revisit after model comparison') },
]

let selectedKey = 'i'
let expanded = false

renderComparison()
renderPractical()
setupControls()
setupPracticalInteractions()
updateUi()

function detailPayload(purpose, state, evidence, next) {
  return { purpose, state, evidence, next }
}

function renderComparison() {
  if (!comparisonHost) return
  const fixture = practicalFixture[1]
  comparisonHost.innerHTML = expansionVariants.map((variant) => `
    <article class="expansion-tile" data-variant="${variant.id}">
      <div class="expansion-tile-copy">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      <div class="expansion-demo">
        ${nodeMarkup({
          ...fixture,
          selected: true,
          expanded: variant.id !== 'x0',
          expansionStyle: variant.id,
          extraClass: 'expansion-demo-node',
          interactive: false,
        })}
        ${variant.id === 'x8' ? `<div class="demo-dock">${detailBody(fixture)}</div>` : ''}
      </div>
    </article>
  `).join('')

  setupHoverInteractions('.expansion-demo-node')
}

function renderPractical() {
  if (!practicalHost) return
  const style = html.dataset.expansionStyle || 'x1'
  practicalHost.innerHTML = practicalFixture.map((item) => nodeMarkup({
    ...item,
    selected: item.key === selectedKey,
    expanded: item.key === selectedKey && expanded && style !== 'x0' && style !== 'x8',
    expansionStyle: style,
    extraClass: `expansion-practical-node scene-${item.key}`,
    interactive: true,
  })).join('')
  setupPracticalInteractions()
  updateInspector()
}

function nodeMarkup({ key, category, disposition, status, priority, selected, expanded, expansionStyle, title, subtitle, detail, extraClass, interactive }) {
  const meta = categoryMeta[category]
  const projectState = dispositions[disposition]
  const statusState = statusMeta[status] || statusMeta.NONE
  const tab = interactive ? 'tabindex="0" role="button"' : ''
  const aria = interactive ? `aria-label="Select or expand ${title}"` : ''
  const payload = detail || detailPayload('Inspect this work unit', 'Current', 'Preserved evidence', 'Continue current process')

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
      data-selection-style="sel2"
      data-expanded="${expanded ? 'true' : 'false'}"
      data-expansion-style="${expansionStyle}"
      data-light-side="left"
      ${tab}
      ${aria}
      style="--node-rgb:${meta.rgb}; --state-rgb:${projectState.rgb}; --status-rgb:${statusState.rgb}; --light-anchor:50%;">
      <span class="rest-spill" aria-hidden="true"></span>
      <span class="rest-light" aria-hidden="true"></span>
      <span class="hover-light" aria-hidden="true"></span>
      <span class="hover-world-light" aria-hidden="true"></span>
      <span class="disposition-state-outline" aria-hidden="true"></span>
      ${selectionMarkup()}
      <div class="detail-layer">${detailBody({ title, detail: payload })}</div>
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
        <div class="node-heading">
          <span class="category-glyph" aria-hidden="true">${meta.glyph}</span>
          <span class="unit-kind">${meta.kind}</span>
        </div>
        <strong>${title}</strong>
        <small>${subtitle}</small>
        <div class="detail-inline">${detailBody({ title, detail: payload }, false)}</div>
        <div class="detail-rail">
          <div><span>Constraint / state</span><strong>${payload.state}</strong></div>
          <div><span>Next</span><strong>${payload.next}</strong></div>
        </div>
      </div>
      <div class="detail-panel">${detailBody({ title, detail: payload })}</div>
      <div class="detail-sheet">${detailBody({ title, detail: payload })}</div>
    </div>
  `
}

function detailBody(item, includeTitle = true) {
  const payload = item.detail || detailPayload('Inspect this work unit', 'Current', 'Preserved evidence', 'Continue current process')
  return `
    ${includeTitle ? `<span class="detail-kicker">Contextual detail</span><div class="detail-title">${item.title}</div>` : ''}
    <div class="detail-grid">
      <div class="detail-cell"><span>Purpose</span><strong>${payload.purpose}</strong></div>
      <div class="detail-cell"><span>Constraint / state</span><strong>${payload.state}</strong></div>
      <div class="detail-cell"><span>Evidence</span><strong>${payload.evidence}</strong></div>
      <div class="detail-cell"><span>Next action</span><strong>${payload.next}</strong></div>
    </div>
  `
}

function selectionMarkup() {
  return `
    <span class="selection-corners" aria-hidden="true">
      <i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i>
    </span>
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

function setupControls() {
  for (const button of document.querySelectorAll('button[data-expansion-style]')) {
    button.addEventListener('click', () => {
      const next = button.dataset.expansionStyle || 'x1'
      html.dataset.expansionStyle = next
      if (next === 'x0') expanded = false
      renderPractical()
      updateUi()
    })
  }

  toggleButton?.addEventListener('click', () => toggleExpanded())
  collapseButton?.addEventListener('click', () => {
    expanded = false
    syncPracticalState()
    updateUi()
  })
}

function setupPracticalInteractions() {
  setupHoverInteractions('.expansion-practical-node')

  for (const node of document.querySelectorAll('.expansion-practical-node')) {
    if (node.dataset.expansionReady === 'true') continue
    node.dataset.expansionReady = 'true'

    node.addEventListener('click', () => activateNode(node.dataset.nodeKey || ''))
    node.addEventListener('keydown', (event) => {
      if (event.key !== 'Enter' && event.key !== ' ') return
      event.preventDefault()
      activateNode(node.dataset.nodeKey || '')
    })
  }
}

function activateNode(key) {
  if (!key) return
  if (key !== selectedKey) {
    selectedKey = key
    expanded = false
    syncPracticalState()
    updateUi()
    return
  }
  toggleExpanded()
}

function toggleExpanded() {
  const style = html.dataset.expansionStyle || 'x1'
  if (style === 'x0') {
    expanded = false
  } else {
    expanded = !expanded
  }
  syncPracticalState()
  updateUi()
}

function syncPracticalState() {
  const style = html.dataset.expansionStyle || 'x1'
  for (const node of document.querySelectorAll('.expansion-practical-node')) {
    const isSelected = node.dataset.nodeKey === selectedKey
    node.dataset.selected = String(isSelected)
    node.dataset.expansionStyle = style
    node.dataset.expanded = String(isSelected && expanded && style !== 'x0' && style !== 'x8')
  }
  updateInspector()
}

function updateInspector() {
  const style = html.dataset.expansionStyle || 'x1'
  html.dataset.sceneExpanded = String(expanded)
  if (!inspectorDock) return
  const item = practicalFixture.find((candidate) => candidate.key === selectedKey)
  if (style === 'x8' && expanded && item) {
    inspectorDock.innerHTML = detailBody(item)
  } else {
    inspectorDock.innerHTML = ''
  }
}

function updateUi() {
  const style = html.dataset.expansionStyle || 'x1'
  const variant = expansionVariants.find((item) => item.id === style) || expansionVariants[1]
  const selected = practicalFixture.find((item) => item.key === selectedKey)

  for (const button of document.querySelectorAll('button[data-expansion-style]')) {
    button.setAttribute('aria-pressed', String(button.dataset.expansionStyle === style))
  }

  if (summary) summary.textContent = `${variant.code} · ${variant.label}`
  if (nodeSummary) nodeSummary.textContent = selected
    ? `Selected: ${selected.title} · ${expanded ? 'expanded' : 'compact'}`
    : 'Selected: none'
  if (toggleButton) toggleButton.textContent = expanded ? 'Collapse selected' : 'Expand selected'

  updateInspector()
}

function setupHoverInteractions(selector) {
  for (const node of document.querySelectorAll(selector)) {
    if (node.dataset.expansionHoverReady === 'true') continue
    node.dataset.expansionHoverReady = 'true'

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
