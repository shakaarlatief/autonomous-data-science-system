const html = document.documentElement
const rowsHost = document.querySelector('#disposition-rows')
const encodingSummary = document.querySelector('#encoding-summary')

const dispositions = [
  {
    id: 'active',
    code: 'ACTIVE',
    label: 'Active / Current',
    description: 'Work currently central to the project path.',
    rgb: '102, 181, 255',
  },
  {
    id: 'recommended',
    code: 'NEXT',
    label: 'Recommended / Next',
    description: 'A strong candidate for the next project action.',
    rgb: '177, 151, 255',
  },
  {
    id: 'deferred',
    code: 'DEFER',
    label: 'Deferred',
    description: 'Valid work intentionally postponed for now.',
    rgb: '145, 158, 179',
  },
  {
    id: 'completed',
    code: 'DONE',
    label: 'Completed',
    description: 'Work whose current project obligation is satisfied.',
    rgb: '103, 205, 151',
  },
  {
    id: 'blocked',
    code: 'BLOCKED',
    label: 'Blocked',
    description: 'Work unable to proceed until another condition is resolved.',
    rgb: '237, 112, 105',
  },
  {
    id: 'future',
    code: 'FUTURE',
    label: 'Future / Not yet active',
    description: 'Known possible work outside the current active horizon.',
    rgb: '122, 139, 163',
  },
]

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
  { key: 'q', category: 'question', state: 'blocked', title: 'Define target leakage', subtitle: 'Blocking data-contract decision' },
  { key: 'i', category: 'investigation', state: 'active', title: 'Production missingness', subtitle: 'Investigating live data behavior' },
  { key: 'v', category: 'validation', state: 'recommended', title: 'Chronological validation', subtitle: 'Recommended next analytical check' },
  { key: 'm', category: 'model', state: 'completed', title: 'Logistic baseline', subtitle: 'Baseline model obligation satisfied' },
  { key: 'e', category: 'evaluation', state: 'deferred', title: 'Calibration review', subtitle: 'Valid comparison postponed for now' },
  { key: 'f', category: 'investigation', state: 'future', title: 'Drift investigation', subtitle: 'Known later-horizon investigation' },
]

const practicalEdges = [
  ['q', 'i'],
  ['i', 'v'],
  ['v', 'm'],
  ['v', 'f'],
  ['f', 'e'],
]

const encodingLabels = {
  p0: 'Neutral control',
  p1: 'Disposition hue',
  p2: 'Explicit disposition tag',
  p3: 'Tonal hierarchy',
  p4: 'State rhythm',
  p5: 'Hue + tag',
  p6: 'Hue + colored tag + tone',
  p7: 'Neutral tag + tone',
}

let practicalMotionFrame = 0
let practicalMotionUntil = 0

renderRows()
renderPracticalScenes()
setupControls()
setupInteractions()
setupGeometry()
setupAmbientWorld()
updateControls()
requestPracticalGeometry()

function renderRows() {
  if (!rowsHost) return
  rowsHost.innerHTML = dispositions.map((state, index) => rowMarkup(state, index)).join('')
}

function rowMarkup(state, index) {
  return `
    <article class="disposition-row" data-state="${state.id}" style="--state-rgb:${state.rgb};">
      <div class="disposition-label">
        <span>S${index}</span>
        <strong>${state.label}</strong>
        <small>${state.description}</small>
      </div>

      ${nodeMarkup({
        category: 'investigation',
        state: state.id,
        stateCode: state.code,
        stateRgb: state.rgb,
        title: 'Production missingness',
        subtitle: 'Investigating live data behavior',
        extraClass: 'disposition-node',
      })}
    </article>
  `
}

function renderPracticalScenes() {
  for (const host of document.querySelectorAll('.practical-nodes')) {
    host.innerHTML = practicalFixture.map((item) => {
      const state = dispositionById(item.state)
      return nodeMarkup({
        category: item.category,
        state: item.state,
        stateCode: state.code,
        stateRgb: state.rgb,
        title: item.title,
        subtitle: item.subtitle,
        extraClass: `practical-node scene-${item.key}`,
        key: item.key,
      })
    }).join('')
  }
}

function nodeMarkup({ category, state, stateCode, stateRgb, title, subtitle, extraClass, key = '' }) {
  const meta = categoryMeta[category]
  return `
    <div class="grammar-node custom-node category-${category} ${extraClass}" data-state="${state}" data-node-key="${key}" data-light-side="left" style="--node-rgb:${meta.rgb}; --state-rgb:${stateRgb}; --light-anchor:50%;">
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
        <span class="disposition-state-badge" aria-hidden="true">${stateCode}</span>
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

function dispositionById(id) {
  return dispositions.find((state) => state.id === id) || dispositions[0]
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-encoding]')) {
    button.addEventListener('click', () => {
      html.dataset.dispositionEncoding = button.dataset.encoding
      updateControls()
    })
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  reducedToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
  })
}

function updateControls() {
  for (const button of document.querySelectorAll('button[data-encoding]')) {
    button.setAttribute('aria-pressed', String(button.dataset.encoding === html.dataset.dispositionEncoding))
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  if (reducedToggle) reducedToggle.checked = html.dataset.reduced === 'on'

  if (encodingSummary) {
    encodingSummary.textContent = encodingLabels[html.dataset.dispositionEncoding] || encodingLabels.p0
  }
}

function setupInteractions() {
  for (const row of document.querySelectorAll('.disposition-row')) {
    const node = row.querySelector('.disposition-node')
    if (!node) continue
    bindNodeInteraction(node, row)
  }

  for (const node of document.querySelectorAll('.practical-node')) {
    bindNodeInteraction(node, node, true)
  }
}

function bindNodeInteraction(node, stateHost, practical = false) {
  node.addEventListener('pointerenter', () => {
    stateHost.classList.add('is-hovered')
    if (practical) syncPracticalGeometryDuringNodeMotion(230)
    if (html.dataset.reduced !== 'on') triggerPerimeterSweep(node)
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
    stateHost.classList.remove('is-hovered')
    if (practical) syncPracticalGeometryDuringNodeMotion(380)
  })
}

function setupGeometry() {
  window.addEventListener('resize', requestPracticalGeometry, { passive: true })

  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(requestPracticalGeometry)
    for (const world of document.querySelectorAll('.practical-world')) observer.observe(world)
  }
}

function requestPracticalGeometry() {
  requestAnimationFrame(updatePracticalGeometry)
}

function syncPracticalGeometryDuringNodeMotion(durationMs) {
  if (html.dataset.reduced === 'on') {
    requestPracticalGeometry()
    return
  }

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
  for (const card of document.querySelectorAll('.practical-card')) {
    const world = card.querySelector('.practical-world')
    const svg = card.querySelector('.practical-relations')
    if (!world || !svg) continue

    const worldRect = world.getBoundingClientRect()
    const viewBox = svg.viewBox.baseVal
    if (!worldRect.width || !worldRect.height || !viewBox.width || !viewBox.height) continue

    const paths = [...svg.querySelectorAll('path')]
    practicalEdges.forEach(([fromKey, toKey], index) => {
      const source = card.querySelector(`[data-node-key="${fromKey}"]`)
      const target = card.querySelector(`[data-node-key="${toKey}"]`)
      const path = paths[index]
      if (!source || !target || !path) return

      const edge = practicalEdgeAnchors(source, target, worldRect, viewBox)
      path.setAttribute('d', practicalPath(edge.start, edge.end, edge.orientation))
    })
  }
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

  const sourceCenterY = sourceRect.top + sourceRect.height / 2
  const targetCenterY = targetRect.top + targetRect.height / 2
  const downward = targetCenterY >= sourceCenterY

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
    const bend = Math.max(30, Math.abs(end.y - start.y) * 0.42)
    const c1y = start.y + direction * bend
    const c2y = end.y - direction * bend
    return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(start.x)} ${formatCoord(c1y)}, ${formatCoord(end.x)} ${formatCoord(c2y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
  }

  const direction = Math.sign(end.x - start.x) || 1
  const bend = Math.max(34, Math.abs(end.x - start.x) * 0.36)
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
