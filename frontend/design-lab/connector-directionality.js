const html = document.documentElement
const world = document.querySelector('#directionality-world')
const lanes = [...document.querySelectorAll('.direction-lane')]
const presentationSummary = document.querySelector('#presentation-summary')

let relationFrame = 0
let relationMotionFrame = 0
let relationMotionUntil = 0

setupPresentationControls()
setupInteractions()
setupRelationGeometry()
setupAmbientWorld()
updatePresentationControls()
requestRelationUpdate()

function setupPresentationControls() {
  for (const button of document.querySelectorAll('button[data-attachment-option]')) {
    button.addEventListener('click', () => {
      html.dataset.attachmentStyle = button.dataset.attachmentOption
      updatePresentationControls()
    })
  }

  const hoverToggle = document.querySelector('#hover-port-toggle')
  hoverToggle?.addEventListener('change', () => {
    html.dataset.hoverPorts = hoverToggle.checked ? 'on' : 'off'
    updatePresentationControls()
  })

  const reducedToggle = document.querySelector('#reduced-toggle')
  reducedToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
    requestRelationUpdate()
  })
}

function updatePresentationControls() {
  for (const button of document.querySelectorAll('button[data-attachment-option]')) {
    button.setAttribute('aria-pressed', String(button.dataset.attachmentOption === html.dataset.attachmentStyle))
  }

  const hoverToggle = document.querySelector('#hover-port-toggle')
  if (hoverToggle) hoverToggle.checked = html.dataset.hoverPorts === 'on'

  if (!presentationSummary) return

  const attachmentLabels = {
    none: 'Clean',
    dots: 'Micro dots',
    sockets: 'Frame sockets',
  }

  const attachment = attachmentLabels[html.dataset.attachmentStyle] || attachmentLabels.none
  const hover = html.dataset.hoverPorts === 'on' ? 'Hover emphasis on' : 'Hover emphasis off'
  presentationSummary.textContent = `${attachment} · ${hover}`
}

function setupInteractions() {
  for (const lane of lanes) {
    const nodes = [...lane.querySelectorAll('.direction-node')]

    for (const node of nodes) {
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
  for (const lane of lanes) {
    const relationSvg = lane.querySelector('.direction-relations')
    const overlaySvg = lane.querySelector('.direction-overlay')
    const sourceNode = lane.querySelector('.source-node')
    const targetNode = lane.querySelector('.target-node')

    if (!relationSvg || !overlaySvg || !sourceNode || !targetNode) continue

    const laneRect = lane.getBoundingClientRect()
    const viewBox = relationSvg.viewBox.baseVal
    if (!laneRect.width || !laneRect.height || !viewBox.width || !viewBox.height) continue

    const start = relationAnchor(sourceNode, 'right', laneRect, viewBox)
    const end = relationAnchor(targetNode, 'left', laneRect, viewBox)

    lane.querySelector('.direction-path')?.setAttribute('d', relationPath(start, end))

    positionSocket(lane.querySelector('.source-socket'), start)
    positionSocket(lane.querySelector('.target-socket'), end)

    positionCircle(lane.querySelector('.source-port'), offsetPoint(start, 'right', 2))
    positionCircle(lane.querySelector('.target-port'), offsetPoint(end, 'left', 2))

    positionCue(lane.querySelector('.source-cue'), start, 'right')
    positionCue(lane.querySelector('.target-cue'), end, 'left')
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

function offsetPoint(point, side, distance) {
  const offset = { x: point.x, y: point.y }

  if (side === 'left') offset.x -= distance
  if (side === 'right') offset.x += distance
  if (side === 'top') offset.y -= distance
  if (side === 'bottom') offset.y += distance

  return offset
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

function positionCue(element, edgePoint, side) {
  if (!element) return

  const tip = offsetPoint(edgePoint, side, 8)
  const armCenter = offsetPoint(edgePoint, side, 13)
  let d = ''

  if (side === 'left' || side === 'right') {
    d = `M${formatCoord(armCenter.x)} ${formatCoord(tip.y - 3.7)} L${formatCoord(tip.x)} ${formatCoord(tip.y)} L${formatCoord(armCenter.x)} ${formatCoord(tip.y + 3.7)}`
  } else {
    d = `M${formatCoord(tip.x - 3.7)} ${formatCoord(armCenter.y)} L${formatCoord(tip.x)} ${formatCoord(tip.y)} L${formatCoord(tip.x + 3.7)} ${formatCoord(armCenter.y)}`
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
