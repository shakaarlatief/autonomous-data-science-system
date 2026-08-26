const html = document.documentElement
const strip = document.querySelector('.customization-strip')
const scene = document.querySelector('.customization-scene')
const summary = document.querySelector('#appearance-summary')
const storageKey = 'ads-design-lab-cockpit-appearance-v1'

const categories = ['question', 'investigation', 'validation', 'model', 'evaluation']

const categoryMeta = {
  question: {
    kind: 'Question / Blocker',
    rgb: '240, 178, 91',
    stripTitle: 'Project question',
    stripDetail: 'Unresolved definition or blocker',
    sceneTitle: 'Prediction moment',
    sceneDetail: 'Eligibility boundary unresolved',
  },
  investigation: {
    kind: 'Investigation',
    rgb: '103, 218, 194',
    stripTitle: 'Investigation',
    stripDetail: 'Evidence-seeking analytical work',
    sceneTitle: 'Production missingness',
    sceneDetail: 'Investigating live data behavior',
  },
  validation: {
    kind: 'Validation / Analysis',
    rgb: '142, 169, 255',
    stripTitle: 'Validation work',
    stripDetail: 'Designed analytical procedure',
    sceneTitle: 'Chronological validation',
    sceneDetail: 'Selected analytical work',
  },
  model: {
    kind: 'Model Work',
    rgb: '233, 132, 122',
    stripTitle: 'Model work',
    stripDetail: 'Baseline or alternative model',
    sceneTitle: 'Baseline logistic model',
    sceneDetail: 'Completed baseline',
  },
  evaluation: {
    kind: 'Evaluation',
    rgb: '173, 150, 255',
    stripTitle: 'Evaluation work',
    stripDetail: 'Comparison or decision-bearing work',
    sceneTitle: 'Evaluation',
    sceneDetail: 'Downstream comparison',
  },
}

const defaults = {
  shape: 'true',
  surface: 'material',
}

const relationGeometry = {
  'q-i': { source: 'q', target: 'i', sourceSide: 'right', targetSide: 'left' },
  'i-v': { source: 'i', target: 'v', sourceSide: 'right', targetSide: 'left' },
  'v-m': { source: 'v', target: 'm', sourceSide: 'right', targetSide: 'left' },
  'm-e': { source: 'm', target: 'e', sourceSide: 'bottom', targetSide: 'top' },
}

let relationFrame = 0

renderNodes()
restoreAppearance()
setupViewControls()
setupShapeControls()
setupSurfaceControls()
setupPresetControls()
setupReset()
setupReducedMotion()
setupInteractions()
setupAmbientWorld()
setupRelationGeometry()
updateControlState()
updateSummary()
requestRelationUpdate()

function renderNodes() {
  if (!strip || !scene) return

  for (const category of categories) {
    strip.appendChild(buildNode(category, false))
    scene.appendChild(buildNode(category, true))
  }
}

function buildNode(category, isScene) {
  const meta = categoryMeta[category]
  const node = document.createElement('div')
  node.className = `grammar-node custom-node category-${category}${isScene ? ` scene-${category[0]}` : ''}`
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
  node.querySelector('strong').textContent = isScene ? meta.sceneTitle : meta.stripTitle
  node.querySelector('small').textContent = isScene ? meta.sceneDetail : meta.stripDetail

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

function restoreAppearance() {
  let stored = null
  try {
    stored = JSON.parse(localStorage.getItem(storageKey) || 'null')
  } catch {
    stored = null
  }

  const shape = stored?.shape === 'normal' || stored?.shape === 'true' ? stored.shape : defaults.shape
  const surface = ['none', 'material', 'lumen'].includes(stored?.surface) ? stored.surface : defaults.surface
  applyAppearance({ shape, surface }, false)
}

function setupViewControls() {
  const buttons = [...document.querySelectorAll('button[data-view]')]
  const initialView = html.dataset.grammarView || 'scene'
  applyView(initialView, buttons)

  for (const button of buttons) {
    button.addEventListener('click', () => applyView(button.dataset.view, buttons))
  }
}

function applyView(view, buttons) {
  html.dataset.grammarView = view
  for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.view === view))

  for (const panel of document.querySelectorAll('[data-panel]')) {
    const visible = panel.dataset.panel === view
    panel.hidden = !visible
    panel.style.display = visible ? '' : 'none'
  }

  requestRelationUpdate()
}

function setupShapeControls() {
  for (const button of document.querySelectorAll('button[data-shape-option]')) {
    button.addEventListener('click', () => {
      applyAppearance({ shape: button.dataset.shapeOption, surface: html.dataset.surfaceStyle })
    })
  }
}

function setupSurfaceControls() {
  for (const button of document.querySelectorAll('button[data-surface-option]')) {
    button.addEventListener('click', () => {
      applyAppearance({ shape: html.dataset.shapeStyle, surface: button.dataset.surfaceOption })
    })
  }
}

function setupPresetControls() {
  const presets = {
    clean: { shape: 'normal', surface: 'none' },
    structured: { shape: 'true', surface: 'none' },
    rich: { shape: 'true', surface: 'material' },
  }

  for (const button of document.querySelectorAll('button[data-preset]')) {
    button.addEventListener('click', () => {
      const preset = presets[button.dataset.preset]
      if (preset) applyAppearance(preset)
    })
  }
}

function setupReset() {
  const button = document.querySelector('#appearance-reset')
  if (!button) return

  button.addEventListener('click', () => {
    localStorage.removeItem(storageKey)
    applyAppearance(defaults, false)
  })
}

function applyAppearance({ shape, surface }, persist = true) {
  html.dataset.shapeStyle = shape
  html.dataset.surfaceStyle = surface

  if (persist) {
    try {
      localStorage.setItem(storageKey, JSON.stringify({ shape, surface }))
    } catch {
      // Local persistence is convenience-only in this design-lab prototype.
    }
  }

  updateControlState()
  updateSummary()
  requestRelationUpdate()
}

function updateControlState() {
  for (const button of document.querySelectorAll('button[data-shape-option]')) {
    button.setAttribute('aria-pressed', String(button.dataset.shapeOption === html.dataset.shapeStyle))
  }

  for (const button of document.querySelectorAll('button[data-surface-option]')) {
    button.setAttribute('aria-pressed', String(button.dataset.surfaceOption === html.dataset.surfaceStyle))
  }
}

function updateSummary() {
  if (!summary) return

  const shapeLabel = html.dataset.shapeStyle === 'true' ? 'Subtle shapes' : 'Normal boxes'
  const surfaceLabels = {
    none: 'No micro design',
    material: 'Micro material',
    lumen: 'Micro light',
  }
  summary.textContent = `${shapeLabel} · ${surfaceLabels[html.dataset.surfaceStyle] || 'No micro design'}`
}

function setupReducedMotion() {
  const toggle = document.querySelector('#reduced-toggle')
  if (!toggle) return

  toggle.addEventListener('change', () => {
    html.dataset.reduced = toggle.checked ? 'on' : 'off'
  })
}

function setupInteractions() {
  const relationPaths = [...document.querySelectorAll('.grammar-relations path')]

  for (const node of document.querySelectorAll('.custom-node')) {
    node.addEventListener('pointerenter', () => {
      const nodeId = node.dataset.node
      const rgb = readNodeRgb(node)

      for (const path of relationPaths) {
        const linkedNodes = path.dataset.link?.split('-') ?? []
        const isRelated = linkedNodes.includes(nodeId) && !path.closest('[hidden]')
        path.classList.toggle('is-related', isRelated)
        if (isRelated) path.style.setProperty('--related-rgb', rgb)
      }

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
      for (const path of relationPaths) {
        path.classList.remove('is-related')
        path.style.removeProperty('--related-rgb')
      }
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
    updateRelationPaths()
  })
}

function updateRelationPaths() {
  if (!scene || html.dataset.grammarView !== 'scene' || scene.hidden) return

  const svg = scene.querySelector('.grammar-relations')
  if (!svg) return

  const sceneRect = scene.getBoundingClientRect()
  const viewBox = svg.viewBox.baseVal
  if (!sceneRect.width || !sceneRect.height || !viewBox.width || !viewBox.height) return

  for (const path of svg.querySelectorAll('path[data-link]')) {
    const key = path.dataset.link
    const geometry = relationGeometry[key]
    if (!geometry) continue

    const sourceNode = scene.querySelector(`.custom-node[data-node="${geometry.source}"]`)
    const targetNode = scene.querySelector(`.custom-node[data-node="${geometry.target}"]`)
    if (!sourceNode || !targetNode) continue

    const start = relationAnchor(sourceNode, geometry.sourceSide, sceneRect, viewBox)
    const end = relationAnchor(targetNode, geometry.targetSide, sceneRect, viewBox)
    path.setAttribute('d', relationPath(start, end, geometry.sourceSide, geometry.targetSide))
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

  // The subtle Investigation silhouette has a centered right-edge notch.
  // Connect to the visible notch edge rather than to the rectangular wrapper.
  if (side === 'right' && node.dataset.node === 'i' && html.dataset.shapeStyle === 'true') {
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

function formatCoord(value) {
  return Number(value.toFixed(1))
}

function setupAmbientWorld() {
  const world = document.querySelector('#customization-world')
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
