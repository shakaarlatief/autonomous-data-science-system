const html = document.documentElement
const contrastHost = document.querySelector('#blocked-contrast-grid')
const practicalHost = document.querySelector('#blocked-practical-nodes')
const edgeTagsHost = document.querySelector('#blocked-edge-tags')
const summary = document.querySelector('#status-summary')
const overrideSummary = document.querySelector('#status-override-summary')

const statusMeta = {
  NONE: { code: 'NONE', rgb: '145, 158, 179', source: 'none', label: 'No operational status' },
  BLOCKED: { code: 'BLOCKED', rgb: '237, 112, 105', source: 'constraint', label: 'Blocked progress constraint' },
  FAIL: { code: 'FAIL', rgb: '237, 112, 105', source: 'runtime', label: 'Failed current execution attempt' },
  RUN: { code: 'RUN', rgb: '103, 218, 194', source: 'runtime', label: 'Running execution episode' },
  WAIT: { code: 'WAIT', rgb: '240, 178, 91', source: 'runtime', label: 'Waiting execution episode' },
  HUMAN: { code: 'HUMAN', rgb: '173, 150, 255', source: 'runtime', label: 'Waiting for human' },
}

const dispositions = {
  current: { code: 'CURRENT', rgb: '102, 181, 255' },
  recommended: { code: 'NEXT', rgb: '177, 151, 255' },
  deferred: { code: 'DEFER', rgb: '145, 158, 179' },
  completed: { code: 'DONE', rgb: '103, 205, 151' },
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

const contrastFixture = [
  {
    key: 'blocked-dot', status: 'BLOCKED', carrier: 'dot', category: 'investigation', disposition: 'current',
    title: 'Production missingness', subtitle: 'Cannot proceed; no live execution episode',
    label: 'BLOCKED · DOT', note: 'Constraint carrier · circular red ring',
  },
  {
    key: 'blocked-tag', status: 'BLOCKED', carrier: 'tag', category: 'investigation', disposition: 'current',
    title: 'Production missingness', subtitle: 'Cannot proceed; no live execution episode',
    label: 'BLOCKED · TAG', note: 'Same constraint · explicit BLOCKED text',
  },
  {
    key: 'fail-dot', status: 'FAIL', carrier: 'dot', category: 'model', disposition: 'current',
    title: 'Boosted candidate', subtitle: 'Current execution attempt failed; work remains retryable',
    label: 'FAIL · DOT', note: 'Runtime failure · sharper red ring',
  },
  {
    key: 'fail-tag', status: 'FAIL', carrier: 'tag', category: 'model', disposition: 'current',
    title: 'Boosted candidate', subtitle: 'Current execution attempt failed; work remains retryable',
    label: 'FAIL · TAG', note: 'Same runtime failure · explicit FAIL text',
  },
]

const practicalFixture = [
  {
    key: 'q', category: 'question', disposition: 'current', status: 'HUMAN',
    title: 'Resolve data contract', subtitle: 'Cause-resolution work; currently waiting for human input',
  },
  {
    key: 'i', category: 'investigation', disposition: 'current', status: 'BLOCKED',
    title: 'Production missingness', subtitle: 'Blocked by the unresolved data contract',
  },
  {
    key: 'v', category: 'validation', disposition: 'recommended', status: 'BLOCKED',
    title: 'Chronological validation', subtitle: 'Known next work, but cannot begin yet',
  },
  {
    key: 'm', category: 'model', disposition: 'current', status: 'FAIL',
    title: 'Boosted candidate', subtitle: 'Attempt failed, but no blocker currently prevents retry',
  },
  {
    key: 'r', category: 'investigation', disposition: 'current', status: 'RUN',
    title: 'Schema profiling', subtitle: 'Current live runtime episode is executing normally',
  },
  {
    key: 'e', category: 'evaluation', disposition: 'deferred', status: 'NONE',
    title: 'Calibration review', subtitle: 'Deferred by project disposition; neither blocked nor running',
  },
]

const practicalEdges = [
  { key: 'q-i', from: 'q', to: 'i', type: 'blocks', label: 'BLOCKS' },
  { key: 'q-v', from: 'q', to: 'v', type: 'blocks', label: 'BLOCKS' },
  { key: 'i-r', from: 'i', to: 'r', type: 'neutral', label: '' },
  { key: 'r-e', from: 'r', to: 'e', type: 'neutral', label: '' },
]

const localCarrierOverrides = new Map()
let geometryFrame = 0
let motionUntil = 0

renderContrast()
renderPractical()
setupControls()
setupNodeInteractions()
setupGeometry()
updateCarrierPresentation()
requestGeometry()

function renderContrast() {
  if (!contrastHost) return

  contrastHost.innerHTML = contrastFixture.map((item) => {
    const status = statusMeta[item.status]
    return `
      <article class="blocked-contrast-cell" style="--status-rgb:${status.rgb};">
        <div class="blocked-contrast-label">
          <span>${item.label}</span>
          <strong>${status.label}</strong>
          <small>${item.note}</small>
        </div>
        ${nodeMarkup({ ...item, extraClass: 'blocked-contrast-node', fixedCarrier: item.carrier })}
      </article>
    `
  }).join('')
}

function renderPractical() {
  if (!practicalHost) return

  practicalHost.innerHTML = practicalFixture.map((item) => nodeMarkup({
    ...item,
    extraClass: `blocked-practical-node scene-${item.key}`,
  })).join('')

  if (edgeTagsHost) {
    edgeTagsHost.innerHTML = practicalEdges
      .filter((edge) => edge.label)
      .map((edge) => `<span class="blocked-edge-tag" data-edge-tag="${edge.key}">${edge.label}</span>`)
      .join('')
  }
}

function nodeMarkup({ key = '', category, disposition, status, title, subtitle, extraClass, fixedCarrier = '' }) {
  const meta = categoryMeta[category]
  const projectState = dispositions[disposition]
  const statusState = statusMeta[status] || statusMeta.NONE
  const fixedAttribute = fixedCarrier ? `data-fixed-status-carrier="${fixedCarrier}"` : ''
  const statusCarrier = fixedCarrier || currentCarrierFor(key)
  const localOverride = key && localCarrierOverrides.has(key)

  return `
    <div class="grammar-node custom-node category-${category} ${extraClass}"
      data-node-key="${key}"
      data-state="${disposition}"
      data-status-source="${statusState.source}"
      data-status-code="${statusState.code}"
      data-status-carrier="${statusCarrier}"
      data-local-override="${localOverride ? 'true' : 'false'}"
      ${fixedAttribute}
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
        ${statusMarkup(statusState, Boolean(fixedCarrier))}
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

function statusMarkup(statusState, fixed) {
  if (statusState.code === 'NONE') return ''
  const disabled = fixed ? 'tabindex="-1" aria-hidden="true"' : ''
  const sourcePhrase = statusState.source === 'constraint' ? 'progress constraint' : 'runtime state'
  return `
    <button type="button" class="status-dot-carrier" ${disabled}
      aria-label="${statusState.code} ${sourcePhrase}. Switch this work unit to explicit status tag.">
      <span class="status-dot-core" aria-hidden="true"></span>
      <span class="status-dot-ring" aria-hidden="true"></span>
    </button>
    <button type="button" class="status-tag-carrier" ${disabled}
      aria-label="${statusState.code} ${sourcePhrase}. Switch this work unit to compact dot carrier.">
      <span class="status-tag-label">${statusState.code}</span>
    </button>
  `
}

function currentCarrierFor(key) {
  if (key && localCarrierOverrides.has(key)) return localCarrierOverrides.get(key)
  return html.dataset.globalStatusCarrier || 'dot'
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-global-status-carrier]')) {
    button.addEventListener('click', () => {
      html.dataset.globalStatusCarrier = button.dataset.globalStatusCarrier
      localCarrierOverrides.clear()
      updateCarrierPresentation()
    })
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  reducedToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
  })
}

function setupNodeInteractions() {
  for (const node of document.querySelectorAll('.blocked-practical-node, .blocked-contrast-node')) {
    const fixed = node.hasAttribute('data-fixed-status-carrier')
    const key = node.dataset.nodeKey || ''

    if (!fixed && key && node.dataset.statusCode !== 'NONE') {
      for (const carrier of node.querySelectorAll('.status-dot-carrier, .status-tag-carrier')) {
        carrier.addEventListener('click', (event) => {
          event.stopPropagation()
          toggleLocalCarrier(key)
        })
      }
    }

    node.addEventListener('pointerenter', () => {
      node.classList.add('is-hovered')
      triggerSweep(node)
      if (node.classList.contains('blocked-practical-node')) syncGeometryDuringMotion(240)
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
      if (node.classList.contains('blocked-practical-node')) syncGeometryDuringMotion(390)
    })
  }
}

function toggleLocalCarrier(key) {
  const globalCarrier = html.dataset.globalStatusCarrier || 'dot'
  const current = localCarrierOverrides.get(key) || globalCarrier
  const next = current === 'dot' ? 'tag' : 'dot'

  if (next === globalCarrier) localCarrierOverrides.delete(key)
  else localCarrierOverrides.set(key, next)

  updateCarrierPresentation()
}

function updateCarrierPresentation() {
  const globalCarrier = html.dataset.globalStatusCarrier || 'dot'

  for (const button of document.querySelectorAll('button[data-global-status-carrier]')) {
    button.setAttribute('aria-pressed', String(button.dataset.globalStatusCarrier === globalCarrier))
  }

  for (const node of document.querySelectorAll('.blocked-practical-node')) {
    const key = node.dataset.nodeKey
    const carrier = currentCarrierFor(key)
    node.dataset.statusCarrier = carrier
    node.dataset.localOverride = localCarrierOverrides.has(key) ? 'true' : 'false'
  }

  if (summary) {
    summary.textContent = globalCarrier === 'dot'
      ? 'Dot + dynamic ring · global'
      : 'Soft-shade status tag · global'
  }

  if (overrideSummary) {
    const count = localCarrierOverrides.size
    overrideSummary.textContent = `${count} local override${count === 1 ? '' : 's'}`
  }
}

function setupGeometry() {
  window.addEventListener('resize', requestGeometry, { passive: true })
  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(requestGeometry)
    const world = document.querySelector('#blocked-practical-world')
    if (world) observer.observe(world)
  }
}

function requestGeometry() {
  requestAnimationFrame(updateGeometry)
}

function syncGeometryDuringMotion(durationMs) {
  motionUntil = Math.max(motionUntil, performance.now() + durationMs)
  if (geometryFrame) return

  const syncFrame = () => {
    updateGeometry()
    if (performance.now() < motionUntil) {
      geometryFrame = requestAnimationFrame(syncFrame)
      return
    }
    geometryFrame = 0
    updateGeometry()
  }

  geometryFrame = requestAnimationFrame(syncFrame)
}

function updateGeometry() {
  const world = document.querySelector('#blocked-practical-world')
  const svg = document.querySelector('.blocked-relations')
  if (!world || !svg) return

  const worldRect = world.getBoundingClientRect()
  const viewBox = svg.viewBox.baseVal
  if (!worldRect.width || !worldRect.height || !viewBox.width || !viewBox.height) return

  for (const edge of practicalEdges) {
    const source = document.querySelector(`.blocked-practical-node[data-node-key="${edge.from}"]`)
    const target = document.querySelector(`.blocked-practical-node[data-node-key="${edge.to}"]`)
    const path = svg.querySelector(`path[data-edge="${edge.key}"]`)
    if (!source || !target || !path) continue

    const anchors = edgeAnchors(source, target, worldRect, viewBox)
    path.setAttribute('d', edgePath(anchors.start, anchors.end, anchors.orientation))

    const tag = document.querySelector(`[data-edge-tag="${edge.key}"]`)
    if (tag) positionEdgeTag(tag, anchors, worldRect, viewBox)
  }
}

function edgeAnchors(source, target, worldRect, viewBox) {
  const sourceRect = (source.querySelector('.node-surface') || source).getBoundingClientRect()
  const targetRect = (target.querySelector('.node-surface') || target).getBoundingClientRect()

  if (targetRect.left > sourceRect.right + 4) {
    return {
      start: anchor(source, 'right', worldRect, viewBox),
      end: anchor(target, 'left', worldRect, viewBox),
      orientation: 'horizontal',
    }
  }

  if (sourceRect.left > targetRect.right + 4) {
    return {
      start: anchor(source, 'left', worldRect, viewBox),
      end: anchor(target, 'right', worldRect, viewBox),
      orientation: 'horizontal',
    }
  }

  const downward = targetRect.top + targetRect.height / 2 >= sourceRect.top + sourceRect.height / 2
  return {
    start: anchor(source, downward ? 'bottom' : 'top', worldRect, viewBox),
    end: anchor(target, downward ? 'top' : 'bottom', worldRect, viewBox),
    orientation: 'vertical',
  }
}

function anchor(node, side, worldRect, viewBox) {
  const surface = node.querySelector('.node-surface') || node
  const rect = surface.getBoundingClientRect()
  let x = rect.left + rect.width / 2
  let y = rect.top + rect.height / 2

  if (side === 'left') x = rect.left
  if (side === 'right') x = rect.right
  if (side === 'top') y = rect.top
  if (side === 'bottom') y = rect.bottom

  if (side === 'right' && node.classList.contains('category-investigation')) {
    x = rect.right - rect.width * 0.07
  }

  return {
    x: ((x - worldRect.left) / worldRect.width) * viewBox.width,
    y: ((y - worldRect.top) / worldRect.height) * viewBox.height,
  }
}

function edgePath(start, end, orientation) {
  if (orientation === 'horizontal') {
    const dx = Math.max(55, Math.abs(end.x - start.x) * 0.44)
    const direction = end.x >= start.x ? 1 : -1
    return `M ${start.x.toFixed(2)} ${start.y.toFixed(2)} C ${(start.x + dx * direction).toFixed(2)} ${start.y.toFixed(2)}, ${(end.x - dx * direction).toFixed(2)} ${end.y.toFixed(2)}, ${end.x.toFixed(2)} ${end.y.toFixed(2)}`
  }

  const dy = Math.max(48, Math.abs(end.y - start.y) * 0.44)
  const direction = end.y >= start.y ? 1 : -1
  return `M ${start.x.toFixed(2)} ${start.y.toFixed(2)} C ${start.x.toFixed(2)} ${(start.y + dy * direction).toFixed(2)}, ${end.x.toFixed(2)} ${(end.y - dy * direction).toFixed(2)}, ${end.x.toFixed(2)} ${end.y.toFixed(2)}`
}

function positionEdgeTag(tag, anchors, worldRect, viewBox) {
  const midX = (anchors.start.x + anchors.end.x) / 2
  const midY = (anchors.start.y + anchors.end.y) / 2
  tag.style.left = `${(midX / viewBox.width) * worldRect.width}px`
  tag.style.top = `${(midY / viewBox.height) * worldRect.height}px`
}

function triggerSweep(node) {
  const sweep = node.querySelector('.perimeter-sweep')
  if (!sweep) return
  sweep.classList.remove('is-running')
  void sweep.offsetWidth
  sweep.classList.add('is-running')
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}
