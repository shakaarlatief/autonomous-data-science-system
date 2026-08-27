const html = document.documentElement
const world = document.querySelector('#relation-world')
const lanesHost = document.querySelector('#relation-lanes')
const encodingSummary = document.querySelector('#encoding-summary')

const relationClasses = [
  {
    id: 'chronology',
    code: 'SEQ',
    label: 'Chronology / Sequence',
    description: 'Work B follows Work A in project order.',
    rgb: '121, 181, 255',
    dash: 'none',
  },
  {
    id: 'dependency',
    code: 'DEP',
    label: 'Dependency / Prerequisite',
    description: 'Work B depends on Work A being available or resolved.',
    rgb: '236, 187, 92',
    dash: '9 5',
  },
  {
    id: 'causal',
    code: 'CAUSE',
    label: 'Causal / Influence',
    description: 'A change in Work A can affect Work B.',
    rgb: '234, 132, 122',
    dash: '9 3 2 3',
  },
  {
    id: 'evidence',
    code: 'EVID',
    label: 'Evidence / Support',
    description: 'Work A supplies evidence used to support Work B.',
    rgb: '103, 218, 194',
    dash: '2 4',
  },
  {
    id: 'lineage',
    code: 'LINE',
    label: 'Lineage / Derivation',
    description: 'Work B is derived from an output or artifact of Work A.',
    rgb: '177, 151, 255',
    dash: '12 4 2 4',
  },
]

const encodingLabels = {
  e0: 'Neutral control',
  e1: 'Semantic hue',
  e2: 'Stroke rhythm',
  e3: 'Explicit midpoint tag',
  e4: 'Hue + stroke',
  e5: 'Hue + tag',
  e6: 'Restrained hybrid',
}

let relationFrame = 0
let relationMotionFrame = 0
let relationMotionUntil = 0

renderLanes()
setupControls()
setupInteractions()
setupGeometry()
setupAmbientWorld()
updateControls()
requestRelationUpdate()

function renderLanes() {
  if (!lanesHost) return

  lanesHost.innerHTML = relationClasses.map((relation, index) => laneMarkup(relation, index)).join('')
}

function laneMarkup(relation, index) {
  return `
    <article class="relation-lane" data-relation-class="${relation.id}" style="--class-rgb:${relation.rgb}; --class-dash:${relation.dash};">
      <div class="relation-label">
        <span>R${index}</span>
        <strong>${relation.label}</strong>
        <small>${relation.description}</small>
      </div>

      <svg class="relation-svg" viewBox="0 0 1000 140" preserveAspectRatio="none" aria-hidden="true">
        <path class="semantic-path" />
      </svg>

      <svg class="relation-overlay" viewBox="0 0 1000 140" preserveAspectRatio="none" aria-hidden="true">
        <path class="semantic-arrow" />
        <g class="semantic-tag">
          <rect class="semantic-tag-bg" width="48" height="22" rx="7" />
          <text class="semantic-tag-text">${relation.code}</text>
        </g>
      </svg>

      ${nodeMarkup('source', 'investigation', 'Investigation', 'Work A', 'Upstream work unit', '103, 218, 194')}
      ${nodeMarkup('target', 'validation', 'Validation / Analysis', 'Work B', 'Downstream work unit', '142, 169, 255')}
    </article>
  `
}

function nodeMarkup(role, category, kind, title, subtitle, rgb) {
  const glyph = category === 'investigation'
    ? '<svg viewBox="0 0 16 16"><rect x="4" y="4" width="8" height="8" rx="0.7"/></svg>'
    : '<svg viewBox="0 0 16 16"><path d="M8 3.3 12.6 12H3.4z"/></svg>'
  const side = category === 'investigation' ? 'left' : 'top'
  const anchor = category === 'investigation' ? '50%' : 'calc(12px + 21%)'

  return `
    <div class="grammar-node custom-node category-${category} relation-node ${role}-node" data-light-side="${side}" style="--node-rgb:${rgb}; --light-anchor:${anchor};">
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
        <div class="node-heading">
          <span class="category-glyph" aria-hidden="true">${glyph}</span>
          <span class="unit-kind">${kind}</span>
        </div>
        <strong>${title}</strong>
        <small>${subtitle}</small>
      </div>
    </div>
  `
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-encoding]')) {
    button.addEventListener('click', () => {
      html.dataset.relationEncoding = button.dataset.encoding
      updateControls()
    })
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  reducedToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
    requestRelationUpdate()
  })
}

function updateControls() {
  for (const button of document.querySelectorAll('button[data-encoding]')) {
    button.setAttribute('aria-pressed', String(button.dataset.encoding === html.dataset.relationEncoding))
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  if (reducedToggle) reducedToggle.checked = html.dataset.reduced === 'on'

  if (encodingSummary) {
    encodingSummary.textContent = encodingLabels[html.dataset.relationEncoding] || encodingLabels.e5
  }
}

function setupInteractions() {
  for (const lane of document.querySelectorAll('.relation-lane')) {
    for (const node of lane.querySelectorAll('.relation-node')) {
      node.addEventListener('pointerenter', () => {
        lane.classList.add('is-related')
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
        syncRelationGeometryDuringNodeMotion(380)
      })
    }
  }
}

function setupGeometry() {
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
  for (const lane of document.querySelectorAll('.relation-lane')) {
    const relationSvg = lane.querySelector('.relation-svg')
    const sourceNode = lane.querySelector('.source-node')
    const targetNode = lane.querySelector('.target-node')

    if (!relationSvg || !sourceNode || !targetNode) continue

    const laneRect = lane.getBoundingClientRect()
    const viewBox = relationSvg.viewBox.baseVal
    if (!laneRect.width || !laneRect.height || !viewBox.width || !viewBox.height) continue

    const start = relationAnchor(sourceNode, 'right', laneRect, viewBox)
    const end = relationAnchor(targetNode, 'left', laneRect, viewBox)

    lane.querySelector('.semantic-path')?.setAttribute('d', relationPath(start, end))
    positionArrow(lane.querySelector('.semantic-arrow'), end, 'left')
    positionTag(lane.querySelector('.semantic-tag'), start, end)
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
  }

  element.setAttribute('d', d)
}

function positionTag(group, start, end) {
  if (!group) return

  const x = (start.x + end.x) / 2
  const y = (start.y + end.y) / 2 - 15
  const rect = group.querySelector('rect')
  const text = group.querySelector('text')

  rect?.setAttribute('x', formatCoord(x - 24))
  rect?.setAttribute('y', formatCoord(y - 11))
  text?.setAttribute('x', formatCoord(x))
  text?.setAttribute('y', formatCoord(y + 0.5))
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
    glint.style.top = `${100 * (1 + Math.floor(random() * 6))}px`
    glint.style.setProperty('--glint-delay', `${-(1 + random() * 6).toFixed(2)}s`)
  })
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
