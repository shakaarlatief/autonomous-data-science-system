const html = document.documentElement
const world = document.querySelector('#directionality-world')
const lanesRoot = document.querySelector('#direction-lanes')

const directionStates = [
  { id: 'none', code: 'D0', label: 'Undirected', notation: 'A — B' },
  { id: 'forward', code: 'D1', label: 'Forward', notation: 'A → B' },
  { id: 'reverse', code: 'D2', label: 'Reverse', notation: 'A ← B' },
  { id: 'both', code: 'D3', label: 'Bidirectional', notation: 'A ↔ B' },
]

let relationFrame = 0
let relationMotionFrame = 0
let relationMotionUntil = 0

renderDirectionLanes()
setupReducedMotion()
setupInteractions()
setupRelationGeometry()
setupAmbientWorld()
requestRelationUpdate()

function renderDirectionLanes() {
  if (!lanesRoot) return

  for (const state of directionStates) {
    const lane = document.createElement('article')
    lane.className = 'direction-lane'
    lane.dataset.direction = state.id
    lane.innerHTML = `
      <div class="direction-label">
        <span>${state.code}</span>
        <strong>${state.label}</strong>
        <small>${state.notation}</small>
      </div>
      <svg class="direction-relations" viewBox="0 0 1000 150" preserveAspectRatio="none" aria-hidden="true">
        <path class="direction-path"></path>
      </svg>
      <svg class="direction-overlay" viewBox="0 0 1000 150" preserveAspectRatio="none" aria-hidden="true">
        <path class="direction-arrow source-arrow"></path>
        <path class="direction-arrow target-arrow"></path>
      </svg>
      ${nodeMarkup('source')}
      ${nodeMarkup('target')}
    `
    lanesRoot.appendChild(lane)
  }
}

function nodeMarkup(role) {
  const source = role === 'source'
  const category = source ? 'investigation' : 'validation'
  const rgb = source ? '103, 218, 194' : '142, 169, 255'
  const kind = source ? 'Investigation' : 'Validation / Analysis'
  const title = source ? 'Work A' : 'Work B'
  const detail = source ? 'First work unit' : 'Second work unit'
  const glyph = source
    ? '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="4" y="4" width="8" height="8" rx="0.7"/></svg>'
    : '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3.3 12.6 12H3.4z"/></svg>'
  const lightSide = source ? 'left' : 'top'
  const lightAnchor = source ? '50%' : 'calc(12px + 21%)'

  return `
    <div class="grammar-node custom-node category-${category} direction-node ${role}-node" data-node="${source ? 'a' : 'b'}" data-light-side="${lightSide}" style="--node-rgb: ${rgb}; --light-anchor: ${lightAnchor};">
      <span class="rest-spill" aria-hidden="true"></span>
      <span class="rest-light" aria-hidden="true"></span>
      <span class="hover-light" aria-hidden="true"></span>
      <span class="hover-world-light" aria-hidden="true"></span>
      <div class="node-surface">
        <span class="surface-rest-light" aria-hidden="true"></span>
        <span class="custom-material-layer" aria-hidden="true"></span>
        <span class="pointer-light" aria-hidden="true"></span>
        <span class="perimeter-sweep" aria-hidden="true"></span>
        <span class="frame-signature" aria-hidden="true"></span>
        <div class="node-heading"><span class="category-glyph" aria-hidden="true">${glyph}</span><span class="unit-kind">${kind}</span></div>
        <strong>${title}</strong><small>${detail}</small>
      </div>
    </div>
  `
}

function setupReducedMotion() {
  const toggle = document.querySelector('#reduced-toggle')
  toggle?.addEventListener('change', () => {
    html.dataset.reduced = toggle.checked ? 'on' : 'off'
    requestRelationUpdate()
  })
}

function setupInteractions() {
  for (const lane of document.querySelectorAll('.direction-lane')) {
    for (const node of lane.querySelectorAll('.direction-node')) {
      node.addEventListener('pointerenter', () => {
        lane.classList.add('is-related')
        lane.style.setProperty('--related-rgb', readNodeRgb(node))
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
        lane.classList.remove('is-related')
        lane.style.removeProperty('--related-rgb')
        syncRelationGeometryDuringNodeMotion(380)
      })
    }
  }
}

function setupRelationGeometry() {
  window.addEventListener('resize', requestRelationUpdate, { passive: true })

  if ('ResizeObserver' in window && world) {
    const observer = new ResizeObserver(requestRelationUpdate)
    observer.observe(world)
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
  for (const lane of document.querySelectorAll('.direction-lane')) {
    const relationSvg = lane.querySelector('.direction-relations')
    const sourceNode = lane.querySelector('.source-node')
    const targetNode = lane.querySelector('.target-node')

    if (!relationSvg || !sourceNode || !targetNode) continue

    const laneRect = lane.getBoundingClientRect()
    const viewBox = relationSvg.viewBox.baseVal
    if (!laneRect.width || !laneRect.height || !viewBox.width || !viewBox.height) continue

    const start = relationAnchor(sourceNode, 'right', laneRect, viewBox)
    const end = relationAnchor(targetNode, 'left', laneRect, viewBox)

    lane.querySelector('.direction-path')?.setAttribute('d', relationPath(start, end))

    positionArrow(lane.querySelector('.source-arrow'), start, 'right')
    positionArrow(lane.querySelector('.target-arrow'), end, 'left')
  }
}

function relationAnchor(node, side, laneRect, viewBox) {
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
    x: ((x - laneRect.left) / laneRect.width) * viewBox.width + viewBox.x,
    y: ((y - laneRect.top) / laneRect.height) * viewBox.height + viewBox.y,
  }
}

function relationPath(start, end) {
  const direction = Math.sign(end.x - start.x) || 1
  const bend = Math.max(42, Math.abs(end.x - start.x) * 0.38)
  const c1x = start.x + direction * bend
  const c2x = end.x - direction * bend

  return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(c1x)} ${formatCoord(start.y)}, ${formatCoord(c2x)} ${formatCoord(end.y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
}

function positionArrow(element, point, side) {
  if (!element) return

  const x = point.x
  const y = point.y
  let d = ''

  if (side === 'left') {
    d = `M${formatCoord(x - 5)} ${formatCoord(y - 3.5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x - 5)} ${formatCoord(y + 3.5)}`
  } else if (side === 'right') {
    d = `M${formatCoord(x + 5)} ${formatCoord(y - 3.5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x + 5)} ${formatCoord(y + 3.5)}`
  } else if (side === 'top') {
    d = `M${formatCoord(x - 3.5)} ${formatCoord(y - 5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x + 3.5)} ${formatCoord(y - 5)}`
  } else {
    d = `M${formatCoord(x - 3.5)} ${formatCoord(y + 5)} L${formatCoord(x)} ${formatCoord(y)} L${formatCoord(x + 3.5)} ${formatCoord(y + 5)}`
  }

  element.setAttribute('d', d)
}

function setupAmbientWorld() {
  if (!world) return

  const currents = [...world.querySelectorAll('.ambient-current')]
  const glints = [...world.querySelectorAll('.ambient-glint')]

  currents.forEach((current, index) => {
    const random = mulberry32(20260827 + index * 131)
    const horizontal = index % 2 === 0
    current.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
    current.style.setProperty('--ambient-position', `${20 * (2 + Math.floor(random() * 20))}px`)
    current.style.setProperty('--ambient-delay', `${-(2 + random() * 7).toFixed(2)}s`)
    current.style.setProperty('--ambient-duration', `${(10 + random() * 5).toFixed(2)}s`)
  })

  glints.forEach((glint, index) => {
    const random = mulberry32(20260911 + index * 241)
    glint.style.left = `${100 * (1 + Math.floor(random() * 11))}px`
    glint.style.top = `${100 * (1 + Math.floor(random() * 5))}px`
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
