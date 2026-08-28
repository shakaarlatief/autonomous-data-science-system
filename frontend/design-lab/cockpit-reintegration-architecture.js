/*
 * M01 promoted-Cockpit architecture recovery adapter.
 *
 * Governing source:
 *   docs/specifications/008_v1_project_cockpit_interaction_architecture.md
 *   accepted integration source ed5b60bdc882bed0799ce55228ce8187f9c55aa1
 *
 * This file restores promoted interaction capabilities that were not yet
 * carried by the Phase-C design-lab reintegration: viewport-owned stage
 * orientation, fold-away chrome, fullscreen state synchronization and
 * URL-reconstructable important focus/deep-work state.
 *
 * Exact shell geometry, labels and URL parameter names remain provisional as
 * Specification 008 explicitly leaves those presentation/contracts unfrozen.
 */

const root = document.documentElement
const shell = document.querySelector('#reintegration-shell')
const stage = document.querySelector('#reintegration-stage')
const hud = document.querySelector('.reintegration-hud')
const tools = document.querySelector('.reintegration-tools')
const plane = document.querySelector('#reintegration-world-plane')
const fullscreenButton = document.querySelector('#fullscreen-world')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const appearanceToggle = document.querySelector('#appearance-controls-toggle')

const NODE_SELECTOR = '.expansion-practical-node'
const ADDRESSABLE_KEYS = new Set(['q', 'i', 'v', 'm', 'r', 'e'])
const X5_SETTLE_MS = 380

const stageDefinitions = [
  { label: 'Framing', key: 'q' },
  { label: 'Investigation', key: 'i' },
  { label: 'Validation', key: 'v' },
  { label: 'Modeling', key: 'm' },
  { label: 'Evaluation', key: 'e' },
]

let rulerFrame = 0
let urlFrame = 0
let suppressUrlWrite = false
let lastAddressableSignature = ''

installStylesheet()
mountChromeControls()
mountStageRuler()
installStageRulerSynchronization()
installFullscreenSynchronization()
installFloatingSurfaceSafety()
installAddressableState()

function installStylesheet() {
  if (document.querySelector('link[href="./cockpit-reintegration-architecture.css"]')) return
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-reintegration-architecture.css'
  document.head.appendChild(link)
}

function mountChromeControls() {
  if (!shell || !hud || !tools) return

  root.dataset.hudVisibility = 'visible'
  tools.dataset.folded = 'false'

  if (!document.querySelector('#map-tools-fold')) {
    const fold = document.createElement('button')
    fold.type = 'button'
    fold.id = 'map-tools-fold'
    fold.textContent = 'Fold'
    fold.setAttribute('aria-pressed', 'false')
    fold.setAttribute('aria-label', 'Fold map controls')
    tools.appendChild(fold)
    fold.addEventListener('click', () => setMapToolsFolded(tools.dataset.folded !== 'true'))
  }

  if (!document.querySelector('#hud-hide')) {
    const hide = document.createElement('button')
    hide.type = 'button'
    hide.id = 'hud-hide'
    hide.textContent = 'Hide HUD'
    hide.setAttribute('aria-label', 'Hide Cockpit HUD')
    const fullscreen = tools.querySelector('#fullscreen-world')
    tools.insertBefore(hide, fullscreen || document.querySelector('#map-tools-fold'))
    hide.addEventListener('click', () => setHudVisible(false))
  }

  if (!document.querySelector('#hud-restore')) {
    const restore = document.createElement('button')
    restore.type = 'button'
    restore.id = 'hud-restore'
    restore.className = 'reintegration-hud-restore'
    restore.textContent = 'Show HUD'
    restore.hidden = true
    restore.setAttribute('aria-label', 'Restore Cockpit HUD')
    shell.appendChild(restore)
    restore.addEventListener('click', () => setHudVisible(true))
  }
}

function setMapToolsFolded(folded) {
  if (!tools) return
  tools.dataset.folded = String(folded)
  const button = tools.querySelector('#map-tools-fold')
  if (button) {
    button.textContent = folded ? 'Tools' : 'Fold'
    button.setAttribute('aria-pressed', String(folded))
    button.setAttribute('aria-label', folded ? 'Restore map controls' : 'Fold map controls')
  }
  scheduleRulerSync()
}

function setHudVisible(visible) {
  if (!hud) return
  root.dataset.hudVisibility = visible ? 'visible' : 'hidden'
  hud.setAttribute('aria-hidden', String(!visible))
  const restore = document.querySelector('#hud-restore')
  if (restore) restore.hidden = visible

  if (!visible) closeFloatingPanels()
  scheduleRulerSync()
}

function mountStageRuler() {
  if (!stage || document.querySelector('#reintegration-stage-ruler')) return

  const ruler = document.createElement('aside')
  ruler.id = 'reintegration-stage-ruler'
  ruler.className = 'reintegration-stage-ruler'
  ruler.setAttribute('aria-label', 'Project stage orientation')
  ruler.innerHTML = `
    <span class="reintegration-stage-ruler-title">PROJECT ORIENTATION</span>
    <div class="reintegration-stage-ruler-track" id="reintegration-stage-ruler-track">
      ${stageDefinitions.map((item) => `<span class="reintegration-stage-marker" data-stage-key="${item.key}">${item.label}</span>`).join('')}
    </div>
  `
  stage.appendChild(ruler)
  scheduleRulerSync()
}

function installStageRulerSynchronization() {
  if (!stage) return

  const schedule = () => scheduleRulerSync()
  stage.addEventListener('wheel', schedule, { passive: true })
  stage.addEventListener('pointermove', schedule, { passive: true })
  stage.addEventListener('keydown', schedule)
  stage.addEventListener('click', schedule)
  window.addEventListener('resize', schedule, { passive: true })

  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(schedule)
    observer.observe(stage)
    const world = document.querySelector('#reintegration-world')
    if (world) observer.observe(world)
  }

  if ('MutationObserver' in window) {
    const observer = new MutationObserver(schedule)
    if (plane) observer.observe(plane, { attributes: true, attributeFilter: ['style'] })
    const host = document.querySelector('#expansion-practical-nodes')
    if (host) observer.observe(host, {
      subtree: true,
      attributes: true,
      attributeFilter: ['data-expanded', 'data-selected', 'style'],
    })
  }
}

function scheduleRulerSync() {
  if (rulerFrame) cancelAnimationFrame(rulerFrame)
  rulerFrame = requestAnimationFrame(() => {
    rulerFrame = requestAnimationFrame(() => {
      rulerFrame = 0
      syncStageRuler()
    })
  })
}

function syncStageRuler() {
  const track = document.querySelector('#reintegration-stage-ruler-track')
  if (!stage || !track) return

  const stageRect = stage.getBoundingClientRect()
  const first = document.querySelector(`${NODE_SELECTOR}[data-node-key="q"] .node-surface`)
  const last = document.querySelector(`${NODE_SELECTOR}[data-node-key="e"] .node-surface`)
  if (!first || !last) return

  const firstRect = first.getBoundingClientRect()
  const lastRect = last.getBoundingClientRect()
  const semanticLeft = firstRect.left - stageRect.left
  const semanticRight = lastRect.right - stageRect.left
  const semanticWidth = Math.max(1, semanticRight - semanticLeft)

  track.style.left = `${semanticLeft}px`
  track.style.width = `${semanticWidth}px`

  for (const item of stageDefinitions) {
    const node = document.querySelector(`${NODE_SELECTOR}[data-node-key="${item.key}"] .node-surface`)
    const marker = track.querySelector(`[data-stage-key="${item.key}"]`)
    if (!node || !marker) continue
    const rect = node.getBoundingClientRect()
    const center = rect.left - stageRect.left + rect.width / 2
    marker.style.left = `${center - semanticLeft}px`
  }
}

function installFullscreenSynchronization() {
  const sync = () => {
    const active = Boolean(document.fullscreenElement)
    root.dataset.fullscreen = String(active)
    if (fullscreenButton) {
      fullscreenButton.textContent = active ? 'Exit fullscreen' : 'Fullscreen'
      fullscreenButton.setAttribute('aria-pressed', String(active))
    }
    scheduleRulerSync()
  }

  document.addEventListener('fullscreenchange', sync)
  sync()
}

function installFloatingSurfaceSafety() {
  appearanceToggle?.addEventListener('click', () => {
    const focusPanel = document.querySelector('#reintegration-process-focus-panel')
    const focusToggle = document.querySelector('#process-focus-toggle')
    if (focusPanel && !focusPanel.hidden) {
      focusPanel.hidden = true
      focusToggle?.setAttribute('aria-expanded', 'false')
    }
  })

  if ('MutationObserver' in window) {
    const observer = new MutationObserver(() => {
      if (root.dataset.deepFocus !== 'false' || root.dataset.conversationOpen === 'true') {
        closeFloatingPanels()
      }
      scheduleRulerSync()
    })
    observer.observe(root, {
      attributes: true,
      attributeFilter: ['data-deep-focus', 'data-conversation-open', 'data-hud-visibility'],
    })
  }
}

function closeFloatingPanels() {
  if (appearancePanel && !appearancePanel.hidden) {
    appearancePanel.hidden = true
    appearanceToggle?.setAttribute('aria-expanded', 'false')
  }

  const focusPanel = document.querySelector('#reintegration-process-focus-panel')
  const focusToggle = document.querySelector('#process-focus-toggle')
  if (focusPanel && !focusPanel.hidden) {
    focusPanel.hidden = true
    focusToggle?.setAttribute('aria-expanded', 'false')
  }
}

function installAddressableState() {
  const params = new URLSearchParams(window.location.search)
  const hasAddressableState = ['focus', 'work', 'depth'].some((key) => params.has(key))

  window.addEventListener('popstate', () => restoreAddressableState())

  if ('MutationObserver' in window) {
    const rootObserver = new MutationObserver(() => scheduleAddressableWrite())
    rootObserver.observe(root, { attributes: true, attributeFilter: ['data-deep-focus'] })

    const host = document.querySelector('#expansion-practical-nodes')
    if (host) {
      const nodeObserver = new MutationObserver(() => {
        scheduleAddressableWrite()
        scheduleRulerSync()
      })
      nodeObserver.observe(host, {
        subtree: true,
        attributes: true,
        attributeFilter: ['data-selected', 'data-expanded'],
      })
    }
  }

  window.setTimeout(async () => {
    if (hasAddressableState) {
      await restoreAddressableState()
    }
    lastAddressableSignature = addressableState().signature
  }, 0)
}

function scheduleAddressableWrite() {
  if (suppressUrlWrite) return
  if (urlFrame) cancelAnimationFrame(urlFrame)
  urlFrame = requestAnimationFrame(() => {
    urlFrame = 0
    const state = addressableState()
    if (state.signature === lastAddressableSignature) return
    lastAddressableSignature = state.signature
    writeAddressableUrl(state, 'push')
  })
}

function addressableState() {
  const selected = document.querySelector(`${NODE_SELECTOR}[data-selected="true"]`)
  const work = selected?.dataset.nodeKey || 'i'
  const expanded = selected?.dataset.expanded === 'true'
  const deep = root.dataset.deepFocus !== 'false'
  const focus = deep || expanded ? 'work' : 'map'
  const depth = deep ? 'deep' : expanded ? 'x5' : ''
  return {
    focus,
    work,
    depth,
    signature: `${focus}:${work}:${depth || 'compact'}`,
  }
}

function writeAddressableUrl(state, mode) {
  const url = new URL(window.location.href)
  url.searchParams.set('focus', state.focus)
  url.searchParams.set('work', state.work)
  if (state.depth) url.searchParams.set('depth', state.depth)
  else url.searchParams.delete('depth')

  const payload = { adsCockpit: true, focus: state.focus, work: state.work, depth: state.depth }
  if (mode === 'replace') window.history.replaceState(payload, '', url)
  else window.history.pushState(payload, '', url)
}

async function restoreAddressableState() {
  suppressUrlWrite = true
  try {
    const params = new URLSearchParams(window.location.search)
    const desiredWork = ADDRESSABLE_KEYS.has(params.get('work') || '') ? params.get('work') : 'i'
    const desiredDepth = params.get('depth') === 'deep'
      ? 'deep'
      : params.get('depth') === 'x5'
        ? 'x5'
        : ''

    if (root.dataset.deepFocus !== 'false') {
      document.querySelector('#return-to-project')?.click()
      await wait(40)
    }

    let selected = document.querySelector(`${NODE_SELECTOR}[data-selected="true"]`)
    if (selected?.dataset.nodeKey !== desiredWork) {
      document.querySelector(`${NODE_SELECTOR}[data-node-key="${desiredWork}"]`)?.click()
      await wait(30)
      selected = document.querySelector(`${NODE_SELECTOR}[data-selected="true"]`)
    }

    if (!selected) return

    const expanded = selected.dataset.expanded === 'true'
    if ((desiredDepth === 'x5' || desiredDepth === 'deep') && !expanded) {
      selected.click()
      await wait(X5_SETTLE_MS)
    } else if (!desiredDepth && expanded) {
      selected.click()
      await wait(30)
    }

    if (desiredDepth === 'deep') {
      document.querySelector('#deep-dive')?.click()
      await wait(840)
    }

    lastAddressableSignature = addressableState().signature
    scheduleRulerSync()
  } finally {
    suppressUrlWrite = false
  }
}

function wait(milliseconds) {
  return new Promise((resolve) => window.setTimeout(resolve, milliseconds))
}
