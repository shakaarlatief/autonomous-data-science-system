/*
 * Spatial edge-rail interaction studies.
 *
 * This module is loaded only when the integrated Cockpit URL contains a valid
 * `rail` study parameter. It wraps and reuses the existing real tool controls;
 * no accepted command is replaced with a mock control.
 *
 * Direct manipulation is the study subject:
 *   blade  -> pull the edge blade into the Cockpit to reveal labelled controls
 *   deck   -> pull the edge spine to fan navigation/work/system control layers
 *   float  -> pull past the detachment threshold, move freely, redock at edge
 */

const root = document.documentElement
const stage = document.querySelector('#reintegration-stage')
const tools = document.querySelector('.reintegration-tools')
const search = document.querySelector('.reintegration-search')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const focusPanel = document.querySelector('#reintegration-process-focus-panel')

const VARIANTS = new Set(['blade', 'deck', 'float'])
const params = new URLSearchParams(window.location.search)
const requested = params.get('rail') || 'blade'
const variant = VARIANTS.has(requested) ? requested : 'blade'

if (stage && tools) {
  mountStudy()
}

function mountStudy() {
  root.dataset.spatialRailStudy = variant
  root.style.setProperty('--spatial-rail-pull', '0')
  root.style.setProperty('--spatial-rail-x', '0px')
  root.style.setProperty('--spatial-rail-y', '0px')

  /*
   * The prior fold button is intentionally suppressed by study CSS. Ensure an
   * old folded presentation cannot leave the real controls unavailable when
   * direct manipulation takes ownership of the edge surface.
   */
  tools.dataset.folded = 'false'

  const rig = document.createElement('aside')
  rig.className = 'spatial-rail-rig'
  rig.dataset.state = 'docked'
  rig.dataset.dragging = 'false'
  rig.dataset.open = 'false'
  rig.setAttribute('aria-label', `${variantName(variant)} spatial tool-rail study`)

  const depthTwo = document.createElement('div')
  depthTwo.className = 'spatial-rail-depth-plane'
  depthTwo.dataset.depth = '2'
  depthTwo.setAttribute('aria-hidden', 'true')

  const depthOne = document.createElement('div')
  depthOne.className = 'spatial-rail-depth-plane'
  depthOne.dataset.depth = '1'
  depthOne.setAttribute('aria-hidden', 'true')

  const tether = document.createElement('div')
  tether.className = 'spatial-rail-tether'
  tether.setAttribute('aria-hidden', 'true')

  const shell = document.createElement('div')
  shell.className = 'spatial-rail-shell'

  const grip = document.createElement('button')
  grip.type = 'button'
  grip.className = 'spatial-rail-grip'
  grip.setAttribute('aria-label', gripAriaLabel(variant))
  grip.innerHTML = `<span class="spatial-rail-grip-label">${gripHint(variant)}</span>`

  stage.insertBefore(rig, tools)
  rig.append(depthTwo, depthOne, tether, shell)
  shell.append(tools, grip)

  if (variant === 'blade' || variant === 'deck') {
    groupRealControls(tools)
  }

  const switcher = mountStudySwitcher()
  const note = mountStudyNote()

  if (variant === 'float') {
    installFloatingRailDrag(rig, grip)
  } else {
    installPullRailDrag(rig, grip)
  }

  installKeyboardManipulation(rig, grip)
  installStudyOwnershipSync(rig, switcher, note)
}

function groupRealControls(host) {
  const definitions = [
    {
      key: 'navigation',
      label: 'Navigation',
      ids: ['product-jump-toggle', 'zoom-out', 'zoom-readout', 'zoom-in', 'fit-world', 'reset-world'],
    },
    {
      key: 'work',
      label: 'Work',
      ids: ['toggle-detail', 'deep-dive', 'process-focus-toggle', 'global-conversations'],
    },
    {
      key: 'system',
      label: 'System',
      ids: ['appearance-controls-toggle', 'hud-hide', 'fullscreen-world', 'map-tools-fold'],
    },
  ]

  const claimed = new Set()
  const layers = []

  for (const definition of definitions) {
    const layer = document.createElement('div')
    layer.className = 'spatial-rail-layer'
    layer.dataset.layer = definition.key
    layer.dataset.layerLabel = definition.label

    const label = document.createElement('span')
    label.className = 'spatial-rail-layer-label'
    label.textContent = definition.label
    label.setAttribute('aria-hidden', 'true')
    layer.appendChild(label)

    for (const id of definition.ids) {
      const control = document.getElementById(id)
      if (!control || !host.contains(control)) continue
      claimed.add(control)
      layer.appendChild(control)
    }

    layers.push(layer)
  }

  /* Keep future/unknown real controls available instead of silently dropping them. */
  const systemLayer = layers[layers.length - 1]
  for (const child of [...host.children]) {
    if (layers.includes(child) || claimed.has(child)) continue
    systemLayer.appendChild(child)
  }

  host.replaceChildren(...layers)
}

function mountStudySwitcher() {
  const switcher = document.createElement('nav')
  switcher.className = 'spatial-rail-study-switcher'
  switcher.setAttribute('aria-label', 'Spatial rail design variants')

  const label = document.createElement('span')
  label.textContent = 'RAIL STUDY'
  switcher.appendChild(label)

  const choices = [
    ['blade', 'A · Blade'],
    ['deck', 'B · Layers'],
    ['float', 'C · Float'],
  ]

  for (const [key, text] of choices) {
    const button = document.createElement('button')
    button.type = 'button'
    button.textContent = text
    button.dataset.railVariant = key
    button.setAttribute('aria-pressed', String(key === variant))
    button.addEventListener('click', () => {
      if (key === variant) return
      const next = new URL(window.location.href)
      next.searchParams.set('rail', key)
      window.location.assign(next)
    })
    switcher.appendChild(button)
  }

  stage.appendChild(switcher)
  return switcher
}

function mountStudyNote() {
  const note = document.createElement('div')
  note.className = 'spatial-rail-study-note'
  note.textContent = studyInstruction(variant)
  stage.appendChild(note)
  return note
}

/* -------------------------------------------------------------------------- */
/* A/B: edge-attached direct pull                                             */
/* -------------------------------------------------------------------------- */

function installPullRailDrag(rig, grip) {
  const maxPull = variant === 'blade' ? 154 : 150
  const snaps = variant === 'blade' ? [0, 0.56, 1] : [0, 0.52, 1]
  let progress = 0
  let pointerId = null
  let startX = 0
  let startProgress = 0
  let moved = false

  const apply = (next, dragging = false) => {
    progress = clamp(next, 0, 1)
    root.style.setProperty('--spatial-rail-pull', progress.toFixed(4))
    rig.dataset.open = String(progress >= 0.36)
    rig.dataset.state = progress < 0.08 ? 'docked' : progress > 0.82 ? 'open' : 'peek'
    rig.dataset.dragging = String(dragging)
    grip.setAttribute('aria-valuenow', String(Math.round(progress * 100)))
    syncAttachedPanels(progress, maxPull)
  }

  grip.setAttribute('role', 'slider')
  grip.setAttribute('aria-valuemin', '0')
  grip.setAttribute('aria-valuemax', '100')
  grip.setAttribute('aria-valuenow', '0')
  grip.setAttribute('aria-valuetext', 'Docked')

  grip.addEventListener('pointerdown', (event) => {
    if (event.button !== 0) return
    pointerId = event.pointerId
    startX = event.clientX
    startProgress = progress
    moved = false
    grip.setPointerCapture(pointerId)
    rig.dataset.dragging = 'true'
    event.preventDefault()
  })

  grip.addEventListener('pointermove', (event) => {
    if (event.pointerId !== pointerId) return
    const delta = startX - event.clientX
    if (Math.abs(delta) > 3) moved = true
    apply(startProgress + delta / maxPull, true)
    grip.setAttribute('aria-valuetext', progressLabel(progress))
  })

  const finish = (event) => {
    if (event.pointerId !== pointerId) return
    if (grip.hasPointerCapture(pointerId)) grip.releasePointerCapture(pointerId)
    pointerId = null

    if (!moved) {
      apply(progress < 0.5 ? 1 : 0)
    } else {
      apply(nearestSnap(progress, snaps))
    }

    grip.setAttribute('aria-valuetext', progressLabel(progress))
  }

  grip.addEventListener('pointerup', finish)
  grip.addEventListener('pointercancel', finish)

  rig.__spatialRailSetProgress = (value) => apply(value)
  rig.__spatialRailGetProgress = () => progress
}

function syncAttachedPanels(progress, maxPull) {
  const additional = variant === 'deck' ? 128 * progress : maxPull * progress
  const right = 72 + additional

  for (const panel of [search, appearancePanel, focusPanel]) {
    if (!panel) continue
    panel.style.right = `${right}px`
  }
}

/* -------------------------------------------------------------------------- */
/* C: dock, detach, float and redock                                          */
/* -------------------------------------------------------------------------- */

function installFloatingRailDrag(rig, grip) {
  const detachDistance = 112
  let state = 'docked'
  let x = 0
  let y = 0
  let pointerId = null
  let startClientX = 0
  let startClientY = 0
  let startX = 0
  let startY = 0
  let moved = false

  const apply = ({ nextX = x, nextY = y, pull = state === 'floating' ? 1 : 0, dragging = false } = {}) => {
    x = nextX
    y = nextY
    root.style.setProperty('--spatial-rail-x', `${x}px`)
    root.style.setProperty('--spatial-rail-y', `${y}px`)
    root.style.setProperty('--spatial-rail-pull', String(clamp(pull, 0, 1)))
    rig.dataset.state = state
    rig.dataset.dragging = String(dragging)
    syncFloatingPanels(rig)
  }

  const dock = () => {
    state = 'docked'
    rig.dataset.snapZone = 'false'
    x = 0
    y = 0
    apply({ nextX: 0, nextY: 0, pull: 0 })
    grip.setAttribute('aria-valuetext', 'Docked at right edge')
  }

  const detach = () => {
    state = 'floating'
    rig.dataset.state = 'floating'
    root.style.setProperty('--spatial-rail-pull', '1')
    grip.setAttribute('aria-valuetext', 'Floating over project world')
  }

  grip.setAttribute('role', 'slider')
  grip.setAttribute('aria-valuemin', '0')
  grip.setAttribute('aria-valuemax', '1')
  grip.setAttribute('aria-valuenow', '0')
  grip.setAttribute('aria-valuetext', 'Docked at right edge')

  grip.addEventListener('pointerdown', (event) => {
    if (event.button !== 0) return
    pointerId = event.pointerId
    startClientX = event.clientX
    startClientY = event.clientY
    startX = x
    startY = y
    moved = false
    grip.setPointerCapture(pointerId)
    rig.dataset.dragging = 'true'
    event.preventDefault()
  })

  grip.addEventListener('pointermove', (event) => {
    if (event.pointerId !== pointerId) return
    const dx = event.clientX - startClientX
    const dy = event.clientY - startClientY
    if (Math.hypot(dx, dy) > 3) moved = true

    const stageRect = stage.getBoundingClientRect()
    const rigRect = rig.getBoundingClientRect()

    if (state === 'docked') {
      const pullDistance = Math.max(0, -dx)
      const pull = clamp(pullDistance / detachDistance, 0, 1)
      x = -pullDistance
      y = clamp(dy * 0.18, -28, 28)
      apply({ nextX: x, nextY: y, pull, dragging: true })

      if (pullDistance >= detachDistance) {
        detach()
        startClientX = event.clientX
        startClientY = event.clientY
        startX = x
        startY = y
      }
      return
    }

    const minX = -(stageRect.width - 92)
    const maxX = 0
    const minY = -54
    const maxY = Math.max(minY, stageRect.height - rigRect.height - 74)
    x = clamp(startX + dx, minX, maxX)
    y = clamp(startY + dy, minY, maxY)

    const withinDockZone = x > -76
    rig.dataset.snapZone = String(withinDockZone)
    apply({ nextX: x, nextY: y, pull: 1, dragging: true })
  })

  const finish = (event) => {
    if (event.pointerId !== pointerId) return
    if (grip.hasPointerCapture(pointerId)) grip.releasePointerCapture(pointerId)
    pointerId = null
    rig.dataset.dragging = 'false'

    if (state === 'docked') {
      if (!moved) {
        /* A click is only a small accessibility convenience; drag is primary. */
        x = -detachDistance
        y = 0
        detach()
        apply({ nextX: x, nextY: 0, pull: 1 })
      } else {
        dock()
      }
      return
    }

    if (rig.dataset.snapZone === 'true') {
      dock()
    } else {
      rig.dataset.snapZone = 'false'
      apply({ nextX: x, nextY: y, pull: 1 })
    }
  }

  grip.addEventListener('pointerup', finish)
  grip.addEventListener('pointercancel', finish)
  grip.addEventListener('dblclick', dock)

  rig.__spatialRailDock = dock
  rig.__spatialRailFloat = () => {
    x = -detachDistance
    y = 0
    detach()
    apply({ nextX: x, nextY: y, pull: 1 })
  }
}

function syncFloatingPanels(rig) {
  if (variant !== 'float') return

  if (rig.dataset.state !== 'floating') {
    for (const panel of [search, appearancePanel, focusPanel]) {
      if (!panel) continue
      panel.style.removeProperty('left')
      panel.style.removeProperty('right')
      panel.style.removeProperty('top')
    }
    return
  }

  const stageRect = stage.getBoundingClientRect()
  const rigRect = rig.getBoundingClientRect()
  const panelWidth = 380
  const gap = 14
  const preferredLeft = rigRect.left - stageRect.left - panelWidth - gap
  const alternateLeft = rigRect.right - stageRect.left + gap
  const left = preferredLeft >= 12
    ? preferredLeft
    : Math.min(stageRect.width - panelWidth - 12, alternateLeft)
  const top = clamp(rigRect.top - stageRect.top, 12, Math.max(12, stageRect.height - 420))

  for (const panel of [search, appearancePanel, focusPanel]) {
    if (!panel) continue
    panel.style.right = 'auto'
    panel.style.left = `${left}px`
    panel.style.top = `${top}px`
  }
}

/* -------------------------------------------------------------------------- */
/* Keyboard and lifecycle                                                     */
/* -------------------------------------------------------------------------- */

function installKeyboardManipulation(rig, grip) {
  grip.addEventListener('keydown', (event) => {
    if (variant === 'float') {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault()
        if (rig.dataset.state === 'floating') rig.__spatialRailDock?.()
        else rig.__spatialRailFloat?.()
      } else if (event.key === 'Escape' && rig.dataset.state === 'floating') {
        event.preventDefault()
        rig.__spatialRailDock?.()
      }
      return
    }

    const current = rig.__spatialRailGetProgress?.() || 0
    if (event.key === 'ArrowLeft') {
      event.preventDefault()
      rig.__spatialRailSetProgress?.(clamp(current + 0.25, 0, 1))
    } else if (event.key === 'ArrowRight') {
      event.preventDefault()
      rig.__spatialRailSetProgress?.(clamp(current - 0.25, 0, 1))
    } else if (event.key === 'Home') {
      event.preventDefault()
      rig.__spatialRailSetProgress?.(0)
    } else if (event.key === 'End') {
      event.preventDefault()
      rig.__spatialRailSetProgress?.(1)
    } else if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault()
      rig.__spatialRailSetProgress?.(current < 0.5 ? 1 : 0)
    }
  })
}

function installStudyOwnershipSync(rig, switcher, note) {
  if (!('MutationObserver' in window)) return

  const observer = new MutationObserver(() => {
    const unavailable = root.dataset.deepFocus !== 'false'
      || (root.dataset.conversationOpen === 'true' && root.dataset.conversationPresentation === 'full')

    rig.setAttribute('aria-hidden', String(unavailable))
    switcher.setAttribute('aria-hidden', String(unavailable))
    note.setAttribute('aria-hidden', String(unavailable))
  })

  observer.observe(root, {
    attributes: true,
    attributeFilter: ['data-deep-focus', 'data-conversation-open', 'data-conversation-presentation'],
  })
}

function nearestSnap(value, snaps) {
  return snaps.reduce((best, candidate) => (
    Math.abs(candidate - value) < Math.abs(best - value) ? candidate : best
  ), snaps[0])
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}

function progressLabel(progress) {
  if (progress < 0.12) return 'Docked'
  if (progress < 0.8) return 'Partially pulled into Cockpit'
  return 'Fully open in Cockpit'
}

function variantName(key) {
  if (key === 'deck') return 'Layered Deck'
  if (key === 'float') return 'Dock and Float'
  return 'Extruded Blade'
}

function gripAriaLabel(key) {
  if (key === 'deck') return 'Drag left to fan Cockpit tool layers; drag right to stack them back at the edge'
  if (key === 'float') return 'Drag left to detach the Cockpit tool rail; drag it to the right edge to redock'
  return 'Drag left to pull the Cockpit tool blade open; drag right to stow it'
}

function gripHint(key) {
  if (key === 'deck') return 'Drag to fan layers'
  if (key === 'float') return 'Pull to detach'
  return 'Drag to pull open'
}

function studyInstruction(key) {
  if (key === 'deck') return 'Pull the grip left: NAVIGATION · WORK · SYSTEM fan into separate depth layers'
  if (key === 'float') return 'Pull past the threshold to detach · move freely · return to the right edge to redock'
  return 'Pull the grip left: compact edge blade becomes a labelled spatial tool surface'
}
