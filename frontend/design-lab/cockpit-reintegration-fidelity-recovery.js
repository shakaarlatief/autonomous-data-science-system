/*
 * Integrated-fidelity recovery adapter.
 *
 * This file does not define new Cockpit semantics. It restores accepted
 * mechanisms that were omitted or incompletely bound during the first
 * source-faithful reintegration pass:
 *
 * 1. shared operational-status carrier switching
 *    Sources:
 *      fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
 *      88fd3c3cfe7a1eff4664afde06341b7b654c97f4
 *
 * 2. latest human-reviewed G4 ambient scheduler
 *    Source refinement:
 *      3ec15a99b0d8103949c673eaf1dd16c3c9d00042
 *
 * 3. Chromium design-lab rerasterization adapter for geometric zoom
 *    This is integration/rendering glue, not a final renderer decision.
 */

const html = document.documentElement
const world = document.querySelector('#reintegration-world')
const plane = document.querySelector('#reintegration-world-plane')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const appearanceReset = document.querySelector('#appearance-reset')

const NODE_SELECTOR = '.expansion-practical-node'
const GRID_STEP = 20
const MAJOR_GRID_STEP = 100

const livelyAmbientConfig = {
  currentGap: [700, 1650],
  driftGap: [3600, 6200],
  currentDuration: [4000, 6100],
  driftDuration: [15000, 22000],
  currentPeak: [0.60, 0.80],
  driftOpacity: [0.18, 0.30],
  maxCurrents: 5,
  maxDrifts: 4,
}

const quietGlintConfig = {
  gap: [3200, 6200],
  duration: [1300, 2000],
  peak: [0.58, 0.78],
  maxConcurrent: 2,
}

const ambientTimers = {
  current: 0,
  glint: 0,
  drift: 0,
}

const localStatusOverrides = new Map()
let ambientRuntimeLayer = null
let rasterObserver = null
let rasterReconciliation = false

installRecoveryStylesheet()
installOperationalStatusCarriers()
installG4DynamicWorld()
installRerasterizedZoomAdapter()

function installRecoveryStylesheet() {
  if (document.querySelector('link[href="./cockpit-reintegration-fidelity-recovery.css"]')) return
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-reintegration-fidelity-recovery.css'
  document.head.appendChild(link)
}

/* -------------------------------------------------------------------------- */
/* Accepted shared operational-status carrier                                 */
/* -------------------------------------------------------------------------- */

function installOperationalStatusCarriers() {
  html.dataset.globalStatusCarrier = html.dataset.globalStatusCarrier === 'tag' ? 'tag' : 'dot'

  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    upgradeStatusCarrierMarkup(node)
  }

  mountGlobalStatusCarrierControl()
  applyGlobalStatusCarrier(html.dataset.globalStatusCarrier, { clearOverrides: true })

  appearanceReset?.addEventListener('click', () => {
    applyGlobalStatusCarrier('dot', { clearOverrides: true })
  })
}

function upgradeStatusCarrierMarkup(node) {
  const code = node.dataset.statusCode || 'NONE'
  if (code === 'NONE') return

  let dotCarrier = node.querySelector('.status-dot-carrier')
  if (dotCarrier && dotCarrier.tagName !== 'BUTTON') {
    const button = document.createElement('button')
    button.type = 'button'
    button.className = 'status-dot-carrier'
    button.innerHTML = dotCarrier.innerHTML
    dotCarrier.replaceWith(button)
    dotCarrier = button
  }

  let tagCarrier = node.querySelector('.status-tag-carrier')
  if (!tagCarrier) {
    tagCarrier = document.createElement('button')
    tagCarrier.type = 'button'
    tagCarrier.className = 'status-tag-carrier'
    tagCarrier.innerHTML = `<span class="status-tag-label">${escapeHtml(code)}</span>`
    node.querySelector('.node-surface')?.appendChild(tagCarrier)
  }

  const sourcePhrase = node.dataset.statusSource === 'constraint' ? 'progress constraint' : 'runtime state'
  if (dotCarrier) {
    dotCarrier.removeAttribute('aria-hidden')
    dotCarrier.setAttribute('aria-label', `${code} ${sourcePhrase}. Switch this work unit to explicit status tag.`)
  }
  tagCarrier.setAttribute('aria-label', `${code} ${sourcePhrase}. Switch this work unit to compact dot carrier.`)

  for (const carrier of [dotCarrier, tagCarrier]) {
    if (!carrier || carrier.dataset.integrationCarrierReady === 'true') continue
    carrier.dataset.integrationCarrierReady = 'true'
    carrier.addEventListener('click', (event) => {
      /*
       * This stopPropagation is an accepted interaction invariant. Clicking the
       * operational carrier changes presentation for this WorkUnit only and
       * must not activate the parent WorkUnit selection/expansion interaction.
       */
      event.stopPropagation()
      toggleLocalStatusCarrier(node)
    })
  }
}

function mountGlobalStatusCarrierControl() {
  if (!appearancePanel || appearancePanel.querySelector('[data-integration-setting="status-carrier"]')) return

  const fieldset = document.createElement('fieldset')
  fieldset.className = 'reintegration-setting'
  fieldset.dataset.integrationSetting = 'status-carrier'
  fieldset.innerHTML = `
    <legend>Operational status carrier</legend>
    <div class="reintegration-setting-options two">
      <button type="button" data-global-status-carrier="dot" aria-pressed="true">Dot + ring</button>
      <button type="button" data-global-status-carrier="tag" aria-pressed="false">Soft-shade tag</button>
    </div>
    <small class="reintegration-setting-note">Accepted global presentation switch. Clicking a carrier on one WorkUnit creates a local override without changing its operational meaning.</small>
  `

  const firstPending = appearancePanel.querySelector('.reintegration-pending-setting')
  appearancePanel.insertBefore(fieldset, firstPending || appearanceReset)

  for (const button of fieldset.querySelectorAll('[data-global-status-carrier]')) {
    button.addEventListener('click', (event) => {
      event.stopPropagation()
      applyGlobalStatusCarrier(button.dataset.globalStatusCarrier || 'dot', { clearOverrides: true })
    })
  }
}

function applyGlobalStatusCarrier(mode, { clearOverrides }) {
  const carrier = mode === 'tag' ? 'tag' : 'dot'
  html.dataset.globalStatusCarrier = carrier

  if (clearOverrides) localStatusOverrides.clear()

  for (const node of document.querySelectorAll(`${NODE_SELECTOR}:not([data-status-code="NONE"])`)) {
    const key = node.dataset.nodeKey || ''
    const local = localStatusOverrides.get(key)
    node.dataset.statusCarrier = local || carrier
    node.dataset.localOverride = local ? 'true' : 'false'
  }

  syncGlobalStatusCarrierControl()
}

function toggleLocalStatusCarrier(node) {
  if (!node || node.dataset.statusCode === 'NONE') return
  const key = node.dataset.nodeKey || ''
  if (!key) return

  const globalCarrier = html.dataset.globalStatusCarrier === 'tag' ? 'tag' : 'dot'
  const current = node.dataset.statusCarrier === 'tag' ? 'tag' : 'dot'
  const next = current === 'dot' ? 'tag' : 'dot'

  if (next === globalCarrier) localStatusOverrides.delete(key)
  else localStatusOverrides.set(key, next)

  node.dataset.statusCarrier = next
  node.dataset.localOverride = localStatusOverrides.has(key) ? 'true' : 'false'
  syncGlobalStatusCarrierControl()
}

function syncGlobalStatusCarrierControl() {
  const globalCarrier = html.dataset.globalStatusCarrier === 'tag' ? 'tag' : 'dot'
  for (const button of document.querySelectorAll('[data-global-status-carrier]')) {
    button.setAttribute('aria-pressed', String(button.dataset.globalStatusCarrier === globalCarrier))
  }
}

/* -------------------------------------------------------------------------- */
/* Latest accepted G4 dynamic scheduler                                       */
/* -------------------------------------------------------------------------- */

function installG4DynamicWorld() {
  if (!world) return

  /* Remove the older fixed-position repeating ambient fixture. */
  for (const element of world.querySelectorAll(':scope > .ambient-current, :scope > .ambient-glint, :scope > .ambient-drift')) {
    element.remove()
  }

  html.dataset.ambientCadence = 'lively'
  html.dataset.activity = 'on'
  world.classList.add('variant-g4')

  ambientRuntimeLayer = document.createElement('div')
  ambientRuntimeLayer.id = 'reintegration-ambient-runtime-layer'
  ambientRuntimeLayer.className = 'reintegration-ambient-runtime-layer'
  ambientRuntimeLayer.setAttribute('aria-hidden', 'true')

  const majorGrid = world.querySelector('.major-grid')
  majorGrid?.insertAdjacentElement('afterend', ambientRuntimeLayer)
  if (!ambientRuntimeLayer.isConnected) world.prepend(ambientRuntimeLayer)

  ensureSemanticActivityLayer()
  restartAmbientEngine()

  const reducedObserver = new MutationObserver((mutations) => {
    if (!mutations.some((mutation) => mutation.attributeName === 'data-reduced')) return
    restartAmbientEngine()
  })
  reducedObserver.observe(html, { attributes: true, attributeFilter: ['data-reduced'] })

  const motionQuery = window.matchMedia?.('(prefers-reduced-motion: reduce)')
  motionQuery?.addEventListener?.('change', restartAmbientEngine)
}

function ensureSemanticActivityLayer() {
  if (!world) return

  if (!world.querySelector('.activity-field-primary')) {
    const primary = document.createElement('div')
    primary.className = 'activity-field activity-field-primary'
    primary.setAttribute('aria-hidden', 'true')
    world.appendChild(primary)
  }

  if (!world.querySelector('.activity-field-secondary')) {
    const secondary = document.createElement('div')
    secondary.className = 'activity-field activity-field-secondary'
    secondary.setAttribute('aria-hidden', 'true')
    world.appendChild(secondary)
  }

  if (!world.querySelector('.packet-one')) {
    const packetOne = document.createElement('div')
    packetOne.className = 'live-packet packet-one'
    packetOne.setAttribute('aria-hidden', 'true')
    world.appendChild(packetOne)
  }

  if (!world.querySelector('.packet-two')) {
    const packetTwo = document.createElement('div')
    packetTwo.className = 'live-packet packet-two'
    packetTwo.setAttribute('aria-hidden', 'true')
    world.appendChild(packetTwo)
  }
}

function ambientEnabled() {
  const osReduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
  return html.dataset.reduced !== 'on' && !osReduced
}

function restartAmbientEngine() {
  for (const key of Object.keys(ambientTimers)) {
    window.clearTimeout(ambientTimers[key])
    ambientTimers[key] = 0
  }

  ambientRuntimeLayer?.replaceChildren()
  if (!ambientEnabled() || !world || !ambientRuntimeLayer) return

  scheduleCurrent(true)
  scheduleGlint(true)
  scheduleDrift(true)
}

function scheduleCurrent(immediate = false) {
  if (!ambientEnabled()) return
  const delay = immediate ? randomBetween(120, 650) : randomBetween(...livelyAmbientConfig.currentGap)
  ambientTimers.current = window.setTimeout(() => {
    if (ambientRuntimeLayer?.querySelectorAll('.runtime-current').length < livelyAmbientConfig.maxCurrents) {
      spawnCurrent()
    }
    scheduleCurrent()
  }, delay)
}

function scheduleGlint(immediate = false) {
  if (!ambientEnabled()) return
  const delay = immediate ? randomBetween(900, 2200) : randomBetween(...quietGlintConfig.gap)
  ambientTimers.glint = window.setTimeout(() => {
    if (ambientRuntimeLayer?.querySelectorAll('.runtime-glint').length < quietGlintConfig.maxConcurrent) {
      spawnGlint()
    }
    scheduleGlint()
  }, delay)
}

function scheduleDrift(immediate = false) {
  if (!ambientEnabled()) return
  const delay = immediate ? randomBetween(200, 1200) : randomBetween(...livelyAmbientConfig.driftGap)
  ambientTimers.drift = window.setTimeout(() => {
    if (ambientRuntimeLayer?.querySelectorAll('.runtime-drift').length < livelyAmbientConfig.maxDrifts) {
      spawnDrift()
    }
    scheduleDrift()
  }, delay)
}

function spawnCurrent() {
  if (!world) return
  const { width, height } = logicalWorldSize()
  const horizontal = Math.random() < 0.52
  const element = document.createElement('span')
  const duration = randomBetween(...livelyAmbientConfig.currentDuration)
  const peak = randomBetween(...livelyAmbientConfig.currentPeak)
  const length = horizontal ? randomBetween(150, 280) : randomBetween(130, 240)

  element.className = `reintegration-ambient-trace runtime-current ${horizontal ? 'trace-h' : 'trace-v'}`
  element.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
  element.style.setProperty('--duration', `${duration}ms`)
  element.style.setProperty('--peak', peak.toFixed(2))

  if (horizontal) {
    const y = snapToGrid(randomBetween(GRID_STEP, Math.max(GRID_STEP + 1, height - GRID_STEP)))
    const direction = Math.random() < 0.5 ? 1 : -1
    const x = direction > 0
      ? randomBetween(-length * 0.6, width * 0.72)
      : randomBetween(width * 0.28, width + length * 0.2)
    const travel = randomBetween(width * 0.32, width * 0.72) * direction

    element.dataset.gridCoordinate = String(y)
    element.style.width = `${length}px`
    element.style.left = `${x}px`
    element.style.top = `${y}px`
    element.style.setProperty('--dx', `${travel}px`)
    element.style.setProperty('--dy', '0px')
  } else {
    const x = snapToGrid(randomBetween(GRID_STEP, Math.max(GRID_STEP + 1, width - GRID_STEP)))
    const direction = Math.random() < 0.5 ? 1 : -1
    const y = direction > 0
      ? randomBetween(-length * 0.6, height * 0.72)
      : randomBetween(height * 0.28, height + length * 0.2)
    const travel = randomBetween(height * 0.34, height * 0.82) * direction

    element.dataset.gridCoordinate = String(x)
    element.style.height = `${length}px`
    element.style.left = `${x}px`
    element.style.top = `${y}px`
    element.style.setProperty('--dx', '0px')
    element.style.setProperty('--dy', `${travel}px`)
  }

  mountTransient(element)
}

function spawnGlint() {
  const { width, height } = logicalWorldSize()
  const element = document.createElement('span')
  const duration = randomBetween(...quietGlintConfig.duration)
  const peak = randomBetween(...quietGlintConfig.peak)
  const x = randomMajorGridCoordinate(width)
  const y = randomMajorGridCoordinate(height)

  element.className = 'reintegration-ambient-glint runtime-glint'
  element.dataset.majorX = String(x)
  element.dataset.majorY = String(y)
  element.style.left = `${x}px`
  element.style.top = `${y}px`
  element.style.setProperty('--duration', `${duration}ms`)
  element.style.setProperty('--peak', peak.toFixed(2))

  mountTransient(element)
}

function spawnDrift() {
  const { width, height } = logicalWorldSize()
  const element = document.createElement('span')
  const duration = randomBetween(...livelyAmbientConfig.driftDuration)
  const size = randomBetween(260, 460)
  const startX = randomBetween(-size * 0.35, width - size * 0.65)
  const startY = randomBetween(-size * 0.35, height - size * 0.65)
  const dx = randomBetween(-width * 0.28, width * 0.28)
  const dy = randomBetween(-height * 0.24, height * 0.24)
  const opacity = randomBetween(...livelyAmbientConfig.driftOpacity)

  element.className = 'reintegration-ambient-drift runtime-drift'
  element.style.width = `${size}px`
  element.style.height = `${size}px`
  element.style.left = `${startX}px`
  element.style.top = `${startY}px`
  element.style.setProperty('--duration', `${duration}ms`)
  element.style.setProperty('--dx', `${dx}px`)
  element.style.setProperty('--dy', `${dy}px`)
  element.style.setProperty('--peak', opacity.toFixed(2))

  mountTransient(element)
}

function mountTransient(element) {
  if (!ambientRuntimeLayer) return
  ambientRuntimeLayer.appendChild(element)
  element.addEventListener('animationend', () => element.remove(), { once: true })
}

function logicalWorldSize() {
  if (!world) return { width: 1440, height: 760 }
  const style = getComputedStyle(world)
  return {
    width: Number.parseFloat(style.width) || 1440,
    height: Number.parseFloat(style.height) || 760,
  }
}

function snapToGrid(value) {
  return Math.round(value / GRID_STEP) * GRID_STEP
}

function randomMajorGridCoordinate(size) {
  const maximumIndex = Math.max(1, Math.floor((size - 1) / MAJOR_GRID_STEP))
  const index = Math.floor(randomBetween(1, maximumIndex + 1))
  return index * MAJOR_GRID_STEP
}

function randomBetween(min, max) {
  return min + Math.random() * (max - min)
}

/* -------------------------------------------------------------------------- */
/* Design-lab geometric-zoom rerasterization                                  */
/* -------------------------------------------------------------------------- */

function installRerasterizedZoomAdapter() {
  if (!world || !plane) return

  const supportsLayoutZoom = Boolean(window.CSS?.supports?.('zoom', '1'))
  if (!supportsLayoutZoom) {
    plane.dataset.rasterMode = 'transform-fallback'
    return
  }

  plane.dataset.rasterMode = 'layout-zoom'

  const reconcile = () => {
    if (rasterReconciliation) return
    const projection = parseScaledTransform(plane.style.transform)
    if (!projection) return

    rasterReconciliation = true
    const { x, y, scale } = projection
    world.style.setProperty('zoom', String(scale))
    world.style.setProperty('--reintegration-grid-hairline', `${1 / scale}px`)
    plane.style.transform = `translate3d(${x}px, ${y}px, 0)`
    rasterReconciliation = false
  }

  rasterObserver = new MutationObserver((mutations) => {
    if (!mutations.some((mutation) => mutation.attributeName === 'style')) return
    reconcile()
  })
  rasterObserver.observe(plane, { attributes: true, attributeFilter: ['style'] })

  reconcile()
  requestAnimationFrame(reconcile)
}

function parseScaledTransform(value) {
  if (!value || !value.includes('scale(')) return null
  const match = value.match(/translate3d\(([-\d.]+)px,\s*([-\d.]+)px,\s*0(?:px)?\)\s*scale\(([-\d.]+)\)/)
  if (!match) return null
  const x = Number(match[1])
  const y = Number(match[2])
  const scale = Number(match[3])
  if (![x, y, scale].every(Number.isFinite) || scale <= 0) return null
  return { x, y, scale }
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;')
}
