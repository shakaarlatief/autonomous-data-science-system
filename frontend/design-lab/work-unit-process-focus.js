const html = document.documentElement
const nodesHost = document.querySelector('#focus-nodes')
const focusSummary = document.querySelector('#focus-summary')
const membershipSummary = document.querySelector('#focus-membership-summary')
const focusEditToggle = document.querySelector('#focus-edit-toggle')
const focusReset = document.querySelector('#focus-reset')

const STORAGE_KEY = 'ads-design-lab-current-process-focus-v1'
const defaultFocusKeys = new Set(['q', 'i', 'v'])

const dispositions = {
  active: { code: 'ACTIVE', rgb: '102, 181, 255' },
  recommended: { code: 'NEXT', rgb: '177, 151, 255' },
  deferred: { code: 'DEFER', rgb: '145, 158, 179' },
  completed: { code: 'DONE', rgb: '103, 205, 151' },
  blocked: { code: 'BLOCKED', rgb: '237, 112, 105' },
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

const fixture = [
  {
    key: 'q',
    category: 'question',
    state: 'blocked',
    scope: 'current',
    title: 'Define target leakage',
    subtitle: 'Blocking data-contract decision',
  },
  {
    key: 'i',
    category: 'investigation',
    state: 'active',
    scope: 'current',
    title: 'Production missingness',
    subtitle: 'Investigating live data behavior',
  },
  {
    key: 'v',
    category: 'validation',
    state: 'recommended',
    scope: 'current',
    title: 'Chronological validation',
    subtitle: 'Recommended next analytical check',
  },
  {
    key: 'm',
    category: 'model',
    state: 'completed',
    scope: 'context',
    title: 'Logistic baseline',
    subtitle: 'Completed context retained for reference',
  },
  {
    key: 'e',
    category: 'evaluation',
    state: 'deferred',
    scope: 'context',
    title: 'Calibration review',
    subtitle: 'Valid comparison postponed for now',
  },
  {
    key: 'f',
    category: 'investigation',
    state: 'future',
    scope: 'context',
    title: 'Drift investigation',
    subtitle: 'Known later-horizon investigation',
  },
]

const edges = [
  ['q', 'i'],
  ['i', 'v'],
  ['v', 'm'],
  ['v', 'f'],
  ['f', 'e'],
]

let motionFrame = 0
let motionUntil = 0

restoreFocusMembership()
renderScene()
setupControls()
setupInteractions()
setupGeometry()
setupAmbientWorld()
updateControls()
requestGeometry()

function renderScene() {
  if (!nodesHost) return
  nodesHost.innerHTML = fixture.map(nodeMarkup).join('')
  classifyEdges()
}

function nodeMarkup(item) {
  const meta = categoryMeta[item.category]
  const state = dispositions[item.state]
  const inFocus = item.scope === 'current'

  return `
    <div class="grammar-node custom-node category-${item.category} focus-node scene-${item.key}"
      data-state="${item.state}"
      data-process-scope="${item.scope}"
      data-node-key="${item.key}"
      data-light-side="left"
      style="--node-rgb:${meta.rgb}; --state-rgb:${state.rgb}; --light-anchor:50%;">
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
        <span class="disposition-state-badge" aria-hidden="true">${state.code}</span>
        <button
          class="focus-membership-toggle"
          type="button"
          data-membership-toggle="${item.key}"
          aria-label="${inFocus ? 'Remove' : 'Add'} ${item.title} ${inFocus ? 'from' : 'to'} current focus"
          title="${inFocus ? 'Remove from current focus' : 'Add to current focus'}">
          ${inFocus ? '− FOCUS' : '+ FOCUS'}
        </button>
        <div class="node-heading">
          <span class="category-glyph" aria-hidden="true">${meta.glyph}</span>
          <span class="unit-kind">${meta.kind}</span>
        </div>
        <strong>${item.title}</strong>
        <small>${item.subtitle}</small>
      </div>
    </div>
  `
}

function fixtureByKey(key) {
  return fixture.find((item) => item.key === key)
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-focus-mode]')) {
    button.addEventListener('click', () => {
      html.dataset.processFocus = button.dataset.focusMode
      updateControls()
    })
  }

  focusEditToggle?.addEventListener('click', () => {
    html.dataset.focusEdit = html.dataset.focusEdit === 'on' ? 'off' : 'on'
    updateControls()
  })

  focusReset?.addEventListener('click', () => {
    resetFocusMembership()
  })

  const reducedToggle = document.querySelector('#reduced-toggle')
  reducedToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
  })
}

function updateControls() {
  for (const button of document.querySelectorAll('button[data-focus-mode]')) {
    button.setAttribute('aria-pressed', String(button.dataset.focusMode === html.dataset.processFocus))
  }

  if (focusSummary) {
    focusSummary.textContent = html.dataset.processFocus === 'focused'
      ? 'Focus current process'
      : 'Context visible'
  }

  if (focusEditToggle) {
    const editing = html.dataset.focusEdit === 'on'
    focusEditToggle.setAttribute('aria-pressed', String(editing))
    focusEditToggle.textContent = editing ? 'Done editing' : 'Edit focus set'
  }

  updateMembershipSummary()

  const reducedToggle = document.querySelector('#reduced-toggle')
  if (reducedToggle) reducedToggle.checked = html.dataset.reduced === 'on'
}

function setupInteractions() {
  for (const node of document.querySelectorAll('.focus-node')) {
    node.addEventListener('pointerenter', () => {
      node.classList.add('is-hovered')
      syncGeometryDuringNodeMotion(240)
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
      node.classList.remove('is-hovered')
      syncGeometryDuringNodeMotion(390)
    })
  }

  for (const button of document.querySelectorAll('[data-membership-toggle]')) {
    button.addEventListener('pointerdown', (event) => event.stopPropagation())
    button.addEventListener('click', (event) => {
      event.stopPropagation()
      toggleFocusMembership(button.dataset.membershipToggle)
    })
  }
}

function toggleFocusMembership(key) {
  const item = fixtureByKey(key)
  if (!item) return

  item.scope = item.scope === 'current' ? 'context' : 'current'
  applyMembershipToNode(key)
  classifyEdges()
  persistFocusMembership()
  updateMembershipSummary()
  requestGeometry()
}

function applyMembershipToNode(key) {
  const item = fixtureByKey(key)
  const node = document.querySelector(`[data-node-key="${key}"]`)
  if (!item || !node) return

  node.dataset.processScope = item.scope

  const button = node.querySelector('[data-membership-toggle]')
  if (!button) return

  const inFocus = item.scope === 'current'
  button.textContent = inFocus ? '− FOCUS' : '+ FOCUS'
  button.setAttribute('aria-label', `${inFocus ? 'Remove' : 'Add'} ${item.title} ${inFocus ? 'from' : 'to'} current focus`)
  button.title = inFocus ? 'Remove from current focus' : 'Add to current focus'
}

function classifyEdges() {
  const paths = [...document.querySelectorAll('.focus-relations path')]

  edges.forEach(([fromKey, toKey], index) => {
    const path = paths[index]
    if (!path) return

    const from = fixtureByKey(fromKey)
    const to = fixtureByKey(toKey)
    const contextEdge = from?.scope === 'context' || to?.scope === 'context'

    path.classList.toggle('is-context-edge', contextEdge)
    path.classList.toggle('is-current-edge', !contextEdge)
    path.dataset.from = fromKey
    path.dataset.to = toKey
  })
}

function updateMembershipSummary() {
  if (!membershipSummary) return
  const currentCount = fixture.filter((item) => item.scope === 'current').length
  const contextCount = fixture.length - currentCount
  membershipSummary.textContent = `${currentCount} in focus · ${contextCount} context`
}

function restoreFocusMembership() {
  const storedKeys = readStoredFocusKeys()
  const focusKeys = storedKeys ?? defaultFocusKeys

  fixture.forEach((item) => {
    item.scope = focusKeys.has(item.key) ? 'current' : 'context'
  })
}

function readStoredFocusKeys() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY)
    if (!raw) return null

    const parsed = JSON.parse(raw)
    if (!Array.isArray(parsed)) return null

    const validKeys = new Set(fixture.map((item) => item.key))
    return new Set(parsed.filter((key) => validKeys.has(key)))
  } catch {
    return null
  }
}

function persistFocusMembership() {
  try {
    const currentKeys = fixture
      .filter((item) => item.scope === 'current')
      .map((item) => item.key)
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(currentKeys))
  } catch {
    // Local persistence is a prototype convenience only. The interaction remains functional without it.
  }
}

function resetFocusMembership() {
  fixture.forEach((item) => {
    item.scope = defaultFocusKeys.has(item.key) ? 'current' : 'context'
    applyMembershipToNode(item.key)
  })

  try {
    window.localStorage.removeItem(STORAGE_KEY)
  } catch {
    // Reset still applies to the live browser state if storage is unavailable.
  }

  classifyEdges()
  updateMembershipSummary()
  requestGeometry()
}

function setupGeometry() {
  window.addEventListener('resize', requestGeometry, { passive: true })

  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(requestGeometry)
    const world = document.querySelector('#focus-world')
    if (world) observer.observe(world)
  }
}

function requestGeometry() {
  requestAnimationFrame(updateGeometry)
}

function syncGeometryDuringNodeMotion(durationMs) {
  if (html.dataset.reduced === 'on') {
    requestGeometry()
    return
  }

  motionUntil = Math.max(motionUntil, performance.now() + durationMs)
  if (motionFrame) return

  const syncFrame = () => {
    updateGeometry()

    if (performance.now() < motionUntil) {
      motionFrame = requestAnimationFrame(syncFrame)
      return
    }

    motionFrame = 0
    updateGeometry()
  }

  motionFrame = requestAnimationFrame(syncFrame)
}

function updateGeometry() {
  const world = document.querySelector('#focus-world')
  const svg = document.querySelector('.focus-relations')
  if (!world || !svg) return

  const worldRect = world.getBoundingClientRect()
  const viewBox = svg.viewBox.baseVal
  if (!worldRect.width || !worldRect.height || !viewBox.width || !viewBox.height) return

  const paths = [...svg.querySelectorAll('path')]
  edges.forEach(([fromKey, toKey], index) => {
    const source = document.querySelector(`[data-node-key="${fromKey}"]`)
    const target = document.querySelector(`[data-node-key="${toKey}"]`)
    const path = paths[index]
    if (!source || !target || !path) return

    const edge = edgeAnchors(source, target, worldRect, viewBox)
    path.setAttribute('d', connectionPath(edge.start, edge.end, edge.orientation))
  })
}

function edgeAnchors(source, target, worldRect, viewBox) {
  const sourceSurface = source.querySelector('.node-surface') || source
  const targetSurface = target.querySelector('.node-surface') || target
  const sourceRect = sourceSurface.getBoundingClientRect()
  const targetRect = targetSurface.getBoundingClientRect()

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

  const sourceCenterY = sourceRect.top + sourceRect.height / 2
  const targetCenterY = targetRect.top + targetRect.height / 2
  const downward = targetCenterY >= sourceCenterY

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
    x: ((x - worldRect.left) / worldRect.width) * viewBox.width + viewBox.x,
    y: ((y - worldRect.top) / worldRect.height) * viewBox.height + viewBox.y,
  }
}

function connectionPath(start, end, orientation) {
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
  const world = document.querySelector('#focus-world')
  if (!world) return

  const currents = [...world.querySelectorAll('.ambient-current')]
  const glints = [...world.querySelectorAll('.ambient-glint')]

  currents.forEach((current, index) => {
    const random = mulberry32(20260827 + index * 173)
    const horizontal = index % 2 === 0
    current.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
    current.style.setProperty('--ambient-position', `${20 * (2 + Math.floor(random() * 24))}px`)
    current.style.setProperty('--ambient-delay', `${-(2 + random() * 7).toFixed(2)}s`)
    current.style.setProperty('--ambient-duration', `${(10 + random() * 5).toFixed(2)}s`)
  })

  glints.forEach((glint, index) => {
    const random = mulberry32(20260917 + index * 251)
    glint.style.left = `${100 * (1 + Math.floor(random() * 11))}px`
    glint.style.top = `${100 * (1 + Math.floor(random() * 5))}px`
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
