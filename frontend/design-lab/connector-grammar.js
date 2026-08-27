const html = document.documentElement
const scene = document.querySelector('#connector-scene')
const summary = document.querySelector('#connector-summary')

const categories = ['question', 'investigation', 'validation', 'model', 'evaluation']

const categoryMeta = {
  question: {
    kind: 'Question / Blocker',
    rgb: '240, 178, 91',
    title: 'Prediction moment',
    detail: 'Eligibility boundary unresolved',
  },
  investigation: {
    kind: 'Investigation',
    rgb: '103, 218, 194',
    title: 'Production missingness',
    detail: 'Investigating live data behavior',
  },
  validation: {
    kind: 'Validation / Analysis',
    rgb: '142, 169, 255',
    title: 'Chronological validation',
    detail: 'Selected analytical work',
  },
  model: {
    kind: 'Model Work',
    rgb: '233, 132, 122',
    title: 'Baseline logistic model',
    detail: 'Completed baseline',
  },
  evaluation: {
    kind: 'Evaluation',
    rgb: '173, 150, 255',
    title: 'Evaluation',
    detail: 'Downstream comparison',
  },
}

const connectorMeta = {
  k0: 'K0 · Clean curve',
  k1: 'K1 · Micro dots',
  k2: 'K2 · Frame sockets',
  k3: 'K3 · Target cue',
  k4: 'K4 · Hover ports',
}

const relationGeometry = {
  'q-i': { source: 'q', target: 'i', sourceSide: 'right', targetSide: 'left' },
  'i-v': { source: 'i', target: 'v', sourceSide: 'right', targetSide: 'left' },
  'v-m': { source: 'v', target: 'm', sourceSide: 'right', targetSide: 'left' },
  'm-e': { source: 'm', target: 'e', sourceSide: 'bottom', targetSide: 'top' },
}

const svgNamespace = 'http://www.w3.org/2000/svg'
let relationFrame = 0
let relationMotionFrame = 0
let relationMotionUntil = 0

renderNodes()
prepareConnectorTerminals()
setupConnectorControls()
setupReducedMotion()
setupInteractions()
setupAmbientWorld()
setupRelationGeometry()
updateConnectorControls()
updateConnectorSummary()
requestRelationUpdate()

function renderNodes() {
  if (!scene) return

  for (const category of categories) {
    scene.appendChild(buildNode(category))
  }
}

function buildNode(category) {
  const meta = categoryMeta[category]
  const node = document.createElement('div')
  node.className = `grammar-node custom-node category-${category} scene-${category[0]}`
  node.dataset.node = category[0]
  node.dataset.lightSide = 'left'
  node.style.setProperty('--light-anchor', '50%')
  node.style.setProperty('--node-rgb', meta.rgb)

  node.innerHTML = `
    <span class="rest-spill" aria-hidden="true"></span>
    <span class="rest-light" aria-hidden="true"></span>
    <span class="hover-light" aria-hidden="true"></span>
    <span class="hover-world-light" aria-hidden="true"></span>
    <div class="node-surface">
      <span class="surface-rest-light" aria-hidden="true"></span>
      <span class="custom-material-layer" aria-hidden="true"></span>
      <span class="custom-lumen-layer" aria-hidden="true"></span>
      <span class="pointer-light" aria-hidden="true"></span>
      <span class="perimeter-sweep" aria-hidden="true"></span>
      <span class="frame-signature" aria-hidden="true"></span>
      <div class="node-heading"><span class="category-glyph" aria-hidden="true"></span><span class="unit-kind"></span></div>
      <strong></strong><small></small>
    </div>`

  node.querySelector('.category-glyph').innerHTML = scientificGlyph(category)
  node.querySelector('.unit-kind').textContent = meta.kind
  node.querySelector('strong').textContent = meta.title
  node.querySelector('small').textContent = meta.detail

  return node
}

function scientificGlyph(category) {
  const glyphs = {
    question: `<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="4.1"/></svg>`,
    investigation: `<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="4" y="4" width="8" height="8" rx="0.7"/></svg>`,
    validation: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3.3 12.6 12H3.4z"/></svg>`,
    model: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="m8 2.9 5.1 5.1L8 13.1 2.9 8z"/></svg>`,
    evaluation: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2.6v10.8M2.6 8h10.8"/></svg>`,
  }
  return glyphs[category]
}

function prepareConnectorTerminals() {
  if (!scene) return

  for (const group of scene.querySelectorAll('.connector-link')) {
    const sourceDot = document.createElementNS(svgNamespace, 'circle')
    sourceDot.classList.add('connector-terminal', 'connector-source-terminal')
    sourceDot.setAttribute('r', '2.6')

    const targetDot = document.createElementNS(svgNamespace, 'circle')
    targetDot.classList.add('connector-terminal', 'connector-target-terminal')
    targetDot.setAttribute('r', '2.6')

    const sourceSocket = document.createElementNS(svgNamespace, 'rect')
    sourceSocket.classList.add('connector-socket', 'connector-source-socket')
    sourceSocket.setAttribute('width', '5.2')
    sourceSocket.setAttribute('height', '5.2')
    sourceSocket.setAttribute('rx', '1.1')

    const targetSocket = document.createElementNS(svgNamespace, 'rect')
    targetSocket.classList.add('connector-socket', 'connector-target-socket')
    targetSocket.setAttribute('width', '5.2')
    targetSocket.setAttribute('height', '5.2')
    targetSocket.setAttribute('rx', '1.1')

    const targetChevron = document.createElementNS(svgNamespace, 'path')
    targetChevron.classList.add('connector-chevron')

    group.append(sourceDot, targetDot, sourceSocket, targetSocket, targetChevron)
  }
}

function setupConnectorControls() {
  for (const button of document.querySelectorAll('button[data-connector-option]')) {
    button.addEventListener('click', () => {
      html.dataset.connectorStyle = button.dataset.connectorOption
      updateConnectorControls()
      updateConnectorSummary()
    })
  }
}

function updateConnectorControls() {
  for (const button of document.querySelectorAll('button[data-connector-option]')) {
    button.setAttribute('aria-pressed', String(button.dataset.connectorOption === html.dataset.connectorStyle))
  }

  for (const note of document.querySelectorAll('[data-candidate-note]')) {
    note.classList.toggle('is-active', note.dataset.candidateNote === html.dataset.connectorStyle)
  }
}

function updateConnectorSummary() {
  if (!summary) return
  summary.textContent = connectorMeta[html.dataset.connectorStyle] || connectorMeta.k0
}

function setupReducedMotion() {
  const toggle = document.querySelector('#reduced-toggle')
  if (!toggle) return

  toggle.addEventListener('change', () => {
    html.dataset.reduced = toggle.checked ? 'on' : 'off'
  })
}

function setupInteractions() {
  if (!scene) return
  const relationGroups = [...scene.querySelectorAll('.connector-link')]

  for (const node of scene.querySelectorAll('.custom-node')) {
    node.addEventListener('pointerenter', () => {
      const nodeId = node.dataset.node
      const rgb = readNodeRgb(node)

      for (const group of relationGroups) {
        const linkedNodes = group.dataset.link?.split('-') ?? []
        const related = linkedNodes.includes(nodeId)
        group.classList.toggle('is-related', related)
        if (related) group.style.setProperty('--related-rgb', rgb)
      }

      syncRelationGeometryDuringNodeMotion(230)
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
      for (const group of relationGroups) {
        group.classList.remove('is-related')
        group.style.removeProperty('--related-rgb')
      }

      syncRelationGeometryDuringNodeMotion(380)
    })
  }
}

function setupRelationGeometry() {
  window.addEventListener('resize', requestRelationUpdate, { passive: true })

  if ('ResizeObserver' in window && scene) {
    const observer = new ResizeObserver(requestRelationUpdate)
    observer.observe(scene)
  }
}

function requestRelationUpdate() {
  if (relationFrame) cancelAnimationFrame(relationFrame)
  relationFrame = requestAnimationFrame(() => {
    relationFrame = 0
    updateRelationGeometry()
  })
}

function syncRelationGeometryDuringNodeMotion(durationMs) {
  if (html.dataset.reduced === 'on') {
    requestRelationUpdate()
    return
  }

  relationMotionUntil = Math.max(relationMotionUntil, performance.now() + durationMs)
  if (relationMotionFrame) return

  const syncFrame = () => {
    updateRelationGeometry()

    if (performance.now() < relationMotionUntil) {
      relationMotionFrame = requestAnimationFrame(syncFrame)
      return
    }

    relationMotionFrame = 0
    updateRelationGeometry()
  }

  relationMotionFrame = requestAnimationFrame(syncFrame)
}

function updateRelationGeometry() {
  if (!scene) return

  const svg = scene.querySelector('.connector-relations')
  if (!svg) return

  const sceneRect = scene.getBoundingClientRect()
  const viewBox = svg.viewBox.baseVal
  if (!sceneRect.width || !sceneRect.height || !viewBox.width || !viewBox.height) return

  for (const group of svg.querySelectorAll('.connector-link')) {
    const key = group.dataset.link
    const geometry = relationGeometry[key]
    if (!geometry) continue

    const sourceNode = scene.querySelector(`.custom-node[data-node="${geometry.source}"]`)
    const targetNode = scene.querySelector(`.custom-node[data-node="${geometry.target}"]`)
    if (!sourceNode || !targetNode) continue

    const start = relationAnchor(sourceNode, geometry.sourceSide, sceneRect, viewBox)
    const end = relationAnchor(targetNode, geometry.targetSide, sceneRect, viewBox)

    const path = group.querySelector('.connector-path')
    path?.setAttribute('d', relationPath(start, end, geometry.sourceSide, geometry.targetSide))

    positionCircle(group.querySelector('.connector-source-terminal'), start)
    positionCircle(group.querySelector('.connector-target-terminal'), end)
    positionSocket(group.querySelector('.connector-source-socket'), start)
    positionSocket(group.querySelector('.connector-target-socket'), end)
    positionChevron(group.querySelector('.connector-chevron'), end, geometry.targetSide)
  }
}

function relationAnchor(node, side, sceneRect, viewBox) {
  const surface = node.querySelector('.node-surface') || node
  const rect = surface.getBoundingClientRect()

  let x = rect.left + rect.width / 2
  let y = rect.top + rect.height / 2

  if (side === 'left') x = rect.left
  if (side === 'right') x = rect.right
  if (side === 'top') y = rect.top
  if (side === 'bottom') y = rect.bottom

  if (side === 'right' && node.dataset.node === 'i') {
    x = rect.right - rect.width * 0.07
  }

  return {
    x: ((x - sceneRect.left) / sceneRect.width) * viewBox.width + viewBox.x,
    y: ((y - sceneRect.top) / sceneRect.height) * viewBox.height + viewBox.y,
  }
}

function relationPath(start, end, sourceSide, targetSide) {
  const horizontal = (sourceSide === 'left' || sourceSide === 'right') && (targetSide === 'left' || targetSide === 'right')

  if (horizontal) {
    const direction = Math.sign(end.x - start.x) || 1
    const bend = Math.max(36, Math.abs(end.x - start.x) * 0.42)
    const c1x = start.x + direction * bend
    const c2x = end.x - direction * bend
    return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(c1x)} ${formatCoord(start.y)}, ${formatCoord(c2x)} ${formatCoord(end.y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
  }

  const direction = Math.sign(end.y - start.y) || 1
  const bend = Math.max(30, Math.abs(end.y - start.y) * 0.44)
  const c1y = start.y + direction * bend
  const c2y = end.y - direction * bend
  return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(start.x)} ${formatCoord(c1y)}, ${formatCoord(end.x)} ${formatCoord(c2y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
}

function positionCircle(element, point) {
  if (!element) return
  element.setAttribute('cx', formatCoord(point.x))
  element.setAttribute('cy', formatCoord(point.y))
}

function positionSocket(element, point) {
  if (!element) return
  element.setAttribute('x', formatCoord(point.x - 2.6))
  element.setAttribute('y', formatCoord(point.y - 2.6))
}

function positionChevron(element, point, targetSide) {
  if (!element) return

  const x = point.x
  const y = point.y
  let d = ''

  if (targetSide === 'left') {
    d = `M${formatCoord(x - 5)} ${formatCoord(y - 3.5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x - 5)} ${formatCoord(y + 3.5)}`
  } else if (targetSide === 'right') {
    d = `M${formatCoord(x + 5)} ${formatCoord(y - 3.5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x + 5)} ${formatCoord(y + 3.5)}`
  } else if (targetSide === 'top') {
    d = `M${formatCoord(x - 3.5)} ${formatCoord(y - 5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x + 3.5)} ${formatCoord(y - 5)}`
  } else {
    d = `M${formatCoord(x - 3.5)} ${formatCoord(y + 5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x + 3.5)} ${formatCoord(y + 5)}`
  }

  element.setAttribute('d', d)
}

function setupAmbientWorld() {
  const world = document.querySelector('#connector-world')
  if (!world) return

  const currents = [...world.querySelectorAll('.ambient-current')]
  const glints = [...world.querySelectorAll('.ambient-glint')]

  currents.forEach((current, index) => {
    const random = mulberry32(20260826 + index * 117)
    const horizontal = index % 2 === 0
    current.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
    current.style.setProperty('--ambient-position', `${20 * (2 + Math.floor(random() * 12))}px`)
    current.style.setProperty('--ambient-delay', `${-(2 + random() * 7).toFixed(2)}s`)
    current.style.setProperty('--ambient-duration', `${(10 + random() * 5).toFixed(2)}s`)
  })

  glints.forEach((glint, index) => {
    const random = mulberry32(20260910 + index * 223)
    glint.style.left = `${100 * (1 + Math.floor(random() * 8))}px`
    glint.style.top = `${100 * (1 + Math.floor(random() * 3))}px`
    glint.style.setProperty('--glint-delay', `${-(1 + random() * 6).toFixed(2)}s`)
  })
}

function readNodeRgb(node) {
  return node.style.getPropertyValue('--node-rgb').trim() || '142, 169, 255'
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