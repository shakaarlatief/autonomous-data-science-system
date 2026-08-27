const html = document.documentElement
const rowsHost = document.querySelector('#constraint-rows')
const practicalHost = document.querySelector('#constraint-practical-nodes')
const summary = document.querySelector('#constraint-summary')

const constraintVariants = [
  {
    id: 'c0',
    code: 'C0',
    label: 'Neutral Control',
    description: 'No blocked-specific cue. Establishes how much meaning is lost if the constraint is only present in underlying state.',
  },
  {
    id: 'c1',
    code: 'C1',
    label: 'Explicit Tag',
    description: 'A compact BLOCKED tag makes the progress constraint explicit without recoloring the work-unit category perimeter.',
  },
  {
    id: 'c2',
    code: 'C2',
    label: 'Edge Clamp',
    description: 'A small red clamp grips the right edge, treating blockage as a structural inability to proceed rather than as another label.',
  },
  {
    id: 'c3',
    code: 'C3',
    label: 'Stop Rail',
    description: 'A short red stopper rail interrupts the lower frame, creating a compact learned constraint cue with no extra text.',
  },
  {
    id: 'c4',
    code: 'C4',
    label: 'Barrier Seal',
    description: 'A small edge-mounted barrier seal provides a discrete instrument-like constraint marker while leaving the main card untouched.',
  },
  {
    id: 'c5',
    code: 'C5',
    label: 'Constraint Veil',
    description: 'A subtle diagonal red veil changes the whole blocked surface. This intentionally tests whether broad tonal treatment becomes semantically confusing.',
  },
  {
    id: 'c6',
    code: 'C6',
    label: 'Tag + Clamp',
    description: 'Combines explicit BLOCKED text with the structural edge clamp to test whether critical constraints justify a restrained redundant cue.',
  },
]

const runtimeStates = {
  none: { code: 'NONE', rgb: '145, 158, 179' },
  running: { code: 'RUN', rgb: '103, 218, 194' },
  waiting: { code: 'WAIT', rgb: '240, 178, 91' },
  human: { code: 'HUMAN', rgb: '173, 150, 255' },
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

const practicalFixture = [
  {
    key: 'q', category: 'question', disposition: 'current', runtime: 'human', blocked: false,
    title: 'Approve data contract', subtitle: 'A Question / Blocker work unit can resolve a constraint without itself being blocked',
  },
  {
    key: 'i', category: 'investigation', disposition: 'current', runtime: 'none', blocked: true,
    title: 'Production missingness', subtitle: 'Current work cannot proceed until the data contract is resolved',
  },
  {
    key: 'v', category: 'validation', disposition: 'recommended', runtime: 'none', blocked: true,
    title: 'Chronological validation', subtitle: 'Next work is known but cannot begin yet',
  },
  {
    key: 'm', category: 'model', disposition: 'current', runtime: 'running', blocked: false,
    title: 'Boosted candidate', subtitle: 'Current and executing now; not blocked',
  },
  {
    key: 'w', category: 'investigation', disposition: 'current', runtime: 'waiting', blocked: false,
    title: 'External feature pull', subtitle: 'A live episode is waiting, but the work is not semantically blocked',
  },
  {
    key: 'e', category: 'evaluation', disposition: 'deferred', runtime: 'none', blocked: false,
    title: 'Calibration review', subtitle: 'Deferred work is inactive by disposition, not because it is blocked',
  },
  {
    key: 'f', category: 'investigation', disposition: 'future', runtime: 'none', blocked: false,
    title: 'Drift investigation', subtitle: 'Future work is not yet active and needs no blocked cue',
  },
]

const practicalEdges = [
  ['q', 'i'],
  ['i', 'v'],
  ['v', 'm'],
  ['i', 'w'],
  ['w', 'e'],
  ['e', 'f'],
]

let practicalMotionFrame = 0
let practicalMotionUntil = 0

renderRows()
renderPracticalScene()
setupControls()
setupInteractions()
setupGeometry()
setupAmbientWorld()
updateControls()
requestPracticalGeometry()

function renderRows() {
  if (!rowsHost) return

  rowsHost.innerHTML = constraintVariants.map((variant) => `
    <article class="constraint-row">
      <div class="constraint-label">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      ${nodeMarkup({
        category: 'investigation',
        disposition: 'current',
        runtime: 'none',
        blocked: true,
        constraintStyle: variant.id,
        title: 'Production missingness',
        subtitle: 'Current work cannot proceed; no live runtime episode exists',
        extraClass: 'constraint-node',
      })}
    </article>
  `).join('')
}

function renderPracticalScene() {
  if (!practicalHost) return

  const constraintStyle = html.dataset.practicalConstraint || 'c6'
  practicalHost.innerHTML = practicalFixture.map((item) => nodeMarkup({
    category: item.category,
    disposition: item.disposition,
    runtime: item.runtime,
    blocked: item.blocked,
    constraintStyle,
    title: item.title,
    subtitle: item.subtitle,
    extraClass: `constraint-practical-node scene-${item.key}`,
    key: item.key,
  })).join('')
}

function nodeMarkup({ category, disposition, runtime, blocked, constraintStyle, title, subtitle, extraClass, key = '' }) {
  const meta = categoryMeta[category]
  const projectState = dispositions[disposition]
  const runtimeState = runtimeStates[runtime] || runtimeStates.none
  const runtimeTag = runtime === 'none' ? '' : `<span class="constraint-runtime-tag" aria-hidden="true">${runtimeState.code}</span>`

  return `
    <div class="grammar-node custom-node category-${category} ${extraClass}"
      data-state="${disposition}"
      data-runtime="${runtime}"
      data-blocked="${blocked ? 'true' : 'false'}"
      data-constraint-style="${constraintStyle}"
      data-node-key="${key}"
      data-light-side="left"
      style="--node-rgb:${meta.rgb}; --state-rgb:${projectState.rgb}; --runtime-rgb:${runtimeState.rgb}; --light-anchor:50%;">
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
        ${runtimeTag}
        <span class="constraint-tag" aria-hidden="true">BLOCKED</span>
        <span class="constraint-clamp" aria-hidden="true"></span>
        <span class="constraint-stop-rail" aria-hidden="true"></span>
        <span class="constraint-seal" aria-hidden="true"></span>
        <span class="constraint-veil" aria-hidden="true"></span>
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

function setupControls() {
  for (const button of document.querySelectorAll('button[data-constraint-style]')) {
    button.addEventListener('click', () => {
      html.dataset.practicalConstraint = button.dataset.constraintStyle
      for (const node of document.querySelectorAll('.constraint-practical-node')) {
        node.dataset.constraintStyle = button.dataset.constraintStyle
      }
      updateControls()
    })
  }
}

function updateControls() {
  const active = html.dataset.practicalConstraint || 'c6'
  for (const button of document.querySelectorAll('button[data-constraint-style]')) {
    button.setAttribute('aria-pressed', String(button.dataset.constraintStyle === active))
  }

  const variant = constraintVariants.find((item) => item.id === active) || constraintVariants[6]
  if (summary) summary.textContent = `${variant.code} · ${variant.label}`
}

function setupInteractions() {
  for (const node of document.querySelectorAll('.constraint-node, .constraint-practical-node')) {
    const practical = node.classList.contains('constraint-practical-node')

    node.addEventListener('pointerenter', () => {
      node.classList.add('is-hovered')
      if (practical) syncPracticalGeometryDuringNodeMotion(240)
      triggerPerimeterSweep(node)
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
      if (practical) syncPracticalGeometryDuringNodeMotion(390)
    })
  }
}

function setupGeometry() {
  window.addEventListener('resize', requestPracticalGeometry, { passive: true })
  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(requestPracticalGeometry)
    const world = document.querySelector('#constraint-practical-world')
    if (world) observer.observe(world)
  }
}

function requestPracticalGeometry() {
  requestAnimationFrame(updatePracticalGeometry)
}

function syncPracticalGeometryDuringNodeMotion(durationMs) {
  practicalMotionUntil = Math.max(practicalMotionUntil, performance.now() + durationMs)
  if (practicalMotionFrame) return

  const syncFrame = () => {
    updatePracticalGeometry()
    if (performance.now() < practicalMotionUntil) {
      practicalMotionFrame = requestAnimationFrame(syncFrame)
      return
    }
    practicalMotionFrame = 0
    updatePracticalGeometry()
  }

  practicalMotionFrame = requestAnimationFrame(syncFrame)
}

function updatePracticalGeometry() {
  const world = document.querySelector('#constraint-practical-world')
  const svg = document.querySelector('.constraint-relations')
  if (!world || !svg) return

  const worldRect = world.getBoundingClientRect()
  const viewBox = svg.viewBox.baseVal
  if (!worldRect.width || !worldRect.height || !viewBox.width || !viewBox.height) return

  const paths = [...svg.querySelectorAll('path')]
  practicalEdges.forEach(([fromKey, toKey], index) => {
    const source = document.querySelector(`[data-node-key="${fromKey}"]`)
    const target = document.querySelector(`[data-node-key="${toKey}"]`)
    const path = paths[index]
    if (!source || !target || !path) return

    const edge = practicalEdgeAnchors(source, target, worldRect, viewBox)
    path.setAttribute('d', practicalPath(edge.start, edge.end, edge.orientation))
  })
}

function practicalEdgeAnchors(source, target, worldRect, viewBox) {
  const sourceSurface = source.querySelector('.node-surface') || source
  const targetSurface = target.querySelector('.node-surface') || target
  const sourceRect = sourceSurface.getBoundingClientRect()
  const targetRect = targetSurface.getBoundingClientRect()

  if (targetRect.left > sourceRect.right + 4) {
    return {
      start: practicalAnchor(source, 'right', worldRect, viewBox),
      end: practicalAnchor(target, 'left', worldRect, viewBox),
      orientation: 'horizontal',
    }
  }

  if (sourceRect.left > targetRect.right + 4) {
    return {
      start: practicalAnchor(source, 'left', worldRect, viewBox),
      end: practicalAnchor(target, 'right', worldRect, viewBox),
      orientation: 'horizontal',
    }
  }

  const downward = targetRect.top + targetRect.height / 2 >= sourceRect.top + sourceRect.height / 2
  return {
    start: practicalAnchor(source, downward ? 'bottom' : 'top', worldRect, viewBox),
    end: practicalAnchor(target, downward ? 'top' : 'bottom', worldRect, viewBox),
    orientation: 'vertical',
  }
}

function practicalAnchor(node, side, worldRect, viewBox) {
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
    x: ((x - worldRect.left) / worldRect.width) * viewBox.width + viewBox.x,
    y: ((y - worldRect.top) / worldRect.height) * viewBox.height + viewBox.y,
  }
}

function practicalPath(start, end, orientation) {
  if (orientation === 'vertical') {
    const direction = Math.sign(end.y - start.y) || 1
    const bend = Math.max(34, Math.abs(end.y - start.y) * 0.42)
    const c1y = start.y + direction * bend
    const c2y = end.y - direction * bend
    return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(start.x)} ${formatCoord(c1y)}, ${formatCoord(end.x)} ${formatCoord(c2y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
  }

  const direction = Math.sign(end.x - start.x) || 1
  const bend = Math.max(38, Math.abs(end.x - start.x) * 0.36)
  const c1x = start.x + direction * bend
  const c2x = end.x - direction * bend
  return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(c1x)} ${formatCoord(start.y)}, ${formatCoord(c2x)} ${formatCoord(end.y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
}

function setupAmbientWorld() {
  for (const [worldIndex, world] of [...document.querySelectorAll('.grammar-world')].entries()) {
    const currents = [...world.querySelectorAll('.ambient-current')]
    const glints = [...world.querySelectorAll('.ambient-glint')]

    currents.forEach((current, index) => {
      const random = mulberry32(20260827 + worldIndex * 997 + index * 173)
      const horizontal = index % 2 === 0
      current.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
      current.style.setProperty('--ambient-position', `${20 * (2 + Math.floor(random() * 24))}px`)
      current.style.setProperty('--ambient-delay', `${-(2 + random() * 7).toFixed(2)}s`)
      current.style.setProperty('--ambient-duration', `${(10 + random() * 5).toFixed(2)}s`)
    })

    glints.forEach((glint, index) => {
      const random = mulberry32(20260917 + worldIndex * 1231 + index * 251)
      glint.style.left = `${100 * (1 + Math.floor(random() * 11))}px`
      glint.style.top = `${100 * (1 + Math.floor(random() * 7))}px`
      glint.style.setProperty('--glint-delay', `${-(1 + random() * 6).toFixed(2)}s`)
    })
  }
}

function triggerPerimeterSweep(node) {
  const sweep = node.querySelector('.perimeter-sweep')
  if (!sweep) return
  sweep.classList.remove('sweep-active')
  void sweep.offsetWidth
  sweep.classList.add('sweep-active')
}

function formatCoord(value) {
  return Number(value.toFixed(1))
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}

function mulberry32(seed) {
  return function random() {
    let value = (seed += 0x6d2b79f5)
    value = Math.imul(value ^ (value >>> 15), value | 1)
    value ^= value + Math.imul(value ^ (value >>> 7), value | 61)
    return ((value ^ (value >>> 14)) >>> 0) / 4294967296
  }
}
