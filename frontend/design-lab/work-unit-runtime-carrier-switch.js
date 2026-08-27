const html = document.documentElement
const rowsHost = document.querySelector('#carrier-rows')
const practicalHost = document.querySelector('#carrier-practical-nodes')
const carrierSummary = document.querySelector('#carrier-summary')
const overrideSummary = document.querySelector('#override-summary')

const runtimeStates = [
  {
    id: 'none',
    code: 'NONE',
    label: 'No runtime',
    description: 'No current execution or work episode exists. Runtime instrumentation is absent rather than idle.',
    rgb: '145, 158, 179',
  },
  {
    id: 'queued',
    code: 'QUEUE',
    label: 'Queued',
    description: 'A current execution episode exists and is waiting for its turn to start.',
    rgb: '142, 169, 255',
  },
  {
    id: 'running',
    code: 'RUN',
    label: 'Running',
    description: 'The current execution episode is actively progressing now.',
    rgb: '103, 218, 194',
  },
  {
    id: 'waiting',
    code: 'WAIT',
    label: 'Waiting',
    description: 'The current execution episode is paused for an external condition or dependency.',
    rgb: '240, 178, 91',
  },
  {
    id: 'human',
    code: 'HUMAN',
    label: 'Waiting for Human',
    description: 'The current work episode requires explicit human input or approval.',
    rgb: '173, 150, 255',
  },
  {
    id: 'failed',
    code: 'FAIL',
    label: 'Failed',
    description: 'The current execution attempt ended unsuccessfully.',
    rgb: '237, 112, 105',
  },
]

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
    key: 'q',
    category: 'question',
    disposition: 'current',
    runtime: 'human',
    title: 'Approve target definition',
    subtitle: 'Current work needs an explicit human decision',
  },
  {
    key: 'i',
    category: 'investigation',
    disposition: 'current',
    runtime: 'running',
    title: 'Production missingness',
    subtitle: 'Current investigation is executing now',
  },
  {
    key: 'v',
    category: 'validation',
    disposition: 'recommended',
    runtime: 'queued',
    title: 'Chronological validation',
    subtitle: 'Recommended next check has already been queued',
  },
  {
    key: 'm',
    category: 'model',
    disposition: 'current',
    runtime: 'failed',
    title: 'Boosted candidate',
    subtitle: 'Current training attempt failed',
  },
  {
    key: 'e',
    category: 'evaluation',
    disposition: 'deferred',
    runtime: 'none',
    title: 'Calibration review',
    subtitle: 'Deferred work has no current runtime episode',
  },
  {
    key: 'f',
    category: 'investigation',
    disposition: 'future',
    runtime: 'none',
    title: 'Drift investigation',
    subtitle: 'Future work has no current runtime episode',
  },
]

const practicalEdges = [
  ['q', 'i'],
  ['i', 'v'],
  ['v', 'm'],
  ['v', 'f'],
  ['f', 'e'],
]

let globalCarrier = html.dataset.globalRuntimeCarrier === 'tag' ? 'tag' : 'dot'
let practicalMotionFrame = 0
let practicalMotionUntil = 0

renderRows()
renderPracticalScene()
applyGlobalCarrier(globalCarrier, { clearOverrides: true })
setupControls()
setupInteractions()
setupGeometry()
setupAmbientWorld()
updateControls()
requestPracticalGeometry()

function renderRows() {
  if (!rowsHost) return

  rowsHost.innerHTML = runtimeStates.map((runtime, index) => `
    <article class="carrier-row" data-runtime="${runtime.id}" style="--runtime-rgb:${runtime.rgb};">
      <div class="carrier-label">
        <span>S${index}</span>
        <strong>${runtime.label}</strong>
        <small>${runtime.description}</small>
      </div>
      ${nodeMarkup({
        category: 'investigation',
        disposition: 'current',
        runtime: runtime.id,
        title: 'Production missingness',
        subtitle: runtime.id === 'none'
          ? 'Current project work, no execution episode active'
          : 'Current project work with a live execution episode',
        extraClass: 'carrier-node',
      })}
    </article>
  `).join('')
}

function renderPracticalScene() {
  if (!practicalHost) return

  practicalHost.innerHTML = practicalFixture.map((item) => nodeMarkup({
    category: item.category,
    disposition: item.disposition,
    runtime: item.runtime,
    title: item.title,
    subtitle: item.subtitle,
    extraClass: `carrier-practical-node scene-${item.key}`,
    key: item.key,
  })).join('')
}

function nodeMarkup({ category, disposition, runtime, title, subtitle, extraClass, key = '' }) {
  const meta = categoryMeta[category]
  const projectState = dispositions[disposition]
  const runtimeState = runtimeById(runtime)
  const runtimeControls = runtime === 'none' ? '' : `
    <button class="runtime-dot-carrier" type="button" aria-label="Switch this work unit to animated runtime tag" title="Switch this work unit to animated runtime tag">
      <span class="runtime-dot-ring" aria-hidden="true"></span>
      <span class="runtime-dot-core" aria-hidden="true"></span>
    </button>
    <button class="runtime-tag-carrier" type="button" aria-label="Switch this work unit to dot and dynamic ring" title="Switch this work unit to dot and dynamic ring">
      ${runtimeState.code}
    </button>
  `

  return `
    <div class="grammar-node custom-node category-${category} ${extraClass}"
      data-state="${disposition}"
      data-runtime="${runtime}"
      data-runtime-carrier="${globalCarrier}"
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
        ${runtimeControls}
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

function runtimeById(id) {
  return runtimeStates.find((state) => state.id === id) || runtimeStates[0]
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-global-carrier]')) {
    button.addEventListener('click', () => {
      applyGlobalCarrier(button.dataset.globalCarrier, { clearOverrides: true })
      updateControls()
    })
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  reducedToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
  })
}

function applyGlobalCarrier(mode, { clearOverrides }) {
  globalCarrier = mode === 'tag' ? 'tag' : 'dot'
  html.dataset.globalRuntimeCarrier = globalCarrier

  for (const node of liveRuntimeNodes()) {
    node.dataset.runtimeCarrier = globalCarrier
    if (clearOverrides) delete node.dataset.localOverride
  }
}

function toggleNodeCarrier(node) {
  if (!node || node.dataset.runtime === 'none') return

  const current = node.dataset.runtimeCarrier === 'tag' ? 'tag' : 'dot'
  node.dataset.runtimeCarrier = current === 'dot' ? 'tag' : 'dot'

  if (node.dataset.runtimeCarrier === globalCarrier) {
    delete node.dataset.localOverride
  } else {
    node.dataset.localOverride = 'true'
  }

  updateControls()
}

function updateControls() {
  for (const button of document.querySelectorAll('button[data-global-carrier]')) {
    button.setAttribute('aria-pressed', String(button.dataset.globalCarrier === globalCarrier))
  }

  const overrides = [...liveRuntimeNodes()].filter((node) => node.dataset.localOverride === 'true').length

  if (carrierSummary) {
    carrierSummary.textContent = globalCarrier === 'dot'
      ? 'Dot + dynamic ring · global'
      : 'Animated runtime tag · global'
  }

  if (overrideSummary) {
    overrideSummary.textContent = `${overrides} local override${overrides === 1 ? '' : 's'}`
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  if (reducedToggle) reducedToggle.checked = html.dataset.reduced === 'on'
}

function liveRuntimeNodes() {
  return document.querySelectorAll('.carrier-node:not([data-runtime="none"]), .carrier-practical-node:not([data-runtime="none"])')
}

function setupInteractions() {
  for (const node of document.querySelectorAll('.carrier-node, .carrier-practical-node')) {
    const practical = node.classList.contains('carrier-practical-node')

    node.addEventListener('pointerenter', () => {
      node.classList.add('is-hovered')
      if (practical) syncPracticalGeometryDuringNodeMotion(240)
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
      if (practical) syncPracticalGeometryDuringNodeMotion(390)
    })

    node.querySelector('.runtime-dot-carrier')?.addEventListener('click', (event) => {
      event.stopPropagation()
      toggleNodeCarrier(node)
    })

    node.querySelector('.runtime-tag-carrier')?.addEventListener('click', (event) => {
      event.stopPropagation()
      toggleNodeCarrier(node)
    })
  }
}

function setupGeometry() {
  window.addEventListener('resize', requestPracticalGeometry, { passive: true })

  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(requestPracticalGeometry)
    const world = document.querySelector('#carrier-practical-world')
    if (world) observer.observe(world)
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
  const world = document.querySelector('#carrier-practical-world')
  const svg = document.querySelector('.carrier-relations')
  if (!world || !svg) return

  const worldRect = world.getBoundingClientRect()
  const viewBox = svg.viewBox.baseVal
  if (!worldRect.width || !worldRect.height || !viewBox.width || !viewBox.height) return

  const paths = [...svg.querySelectorAll('path')]
  practicalEdges.forEach(([fromKey, toKey], index) => {
    const source = document.querySelector(`.carrier-practical-node[data-node-key="${fromKey}"]`)
    const target = document.querySelector(`.carrier-practical-node[data-node-key="${toKey}"]`)
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
