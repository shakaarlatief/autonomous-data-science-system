/*
 * Checkpoint 251 source-faithful reintegration controller.
 *
 * WorkUnit rendering, selection and X5 contextual expansion are owned by exact
 * accepted modules loaded before this file. This module composes those sources
 * with whole-world navigation, E5 relation geometry, exact Z7 entry timing and
 * explicitly provisional shell/settings orchestration.
 */

const html = document.documentElement
const stage = document.querySelector('#reintegration-stage')
const world = document.querySelector('#reintegration-world')
const plane = document.querySelector('#reintegration-world-plane')
const relationSvg = document.querySelector('#reintegration-relations')
const jumpInput = document.querySelector('#jump-input')
const selectedLabel = document.querySelector('#selected-work-label')
const detailStateLabel = document.querySelector('#detail-state-label')
const detailToggle = document.querySelector('#toggle-detail')
const deepDiveButton = document.querySelector('#deep-dive')
const specialistLayer = document.querySelector('#reintegration-specialist-layer')
const specialistTitle = document.querySelector('#specialist-title')
const returnToProject = document.querySelector('#return-to-project')
const zoomReadout = document.querySelector('#zoom-readout')
const viewportStatus = document.querySelector('#viewport-status')
const zoomIndicator = document.querySelector('#zoom-track-indicator')
const provisionalNote = document.querySelector('.reintegration-provisional-note')
const appearanceToggle = document.querySelector('#appearance-controls-toggle')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const appearanceClose = document.querySelector('#appearance-controls-close')
const appearanceReset = document.querySelector('#appearance-reset')
const reducedMotionToggle = document.querySelector('#reduced-motion-toggle')

const NODE_SELECTOR = '.expansion-practical-node'
const WORLD_WIDTH = 1440
const WORLD_HEIGHT = 760
const MIN_ZOOM = 0.52
const MAX_ZOOM = 1.42
const DEFAULT_ZOOM = 1
const PINCH_SENSITIVITY = 0.0024
const MAX_PINCH_DELTA_PER_FRAME = 64
const X5_TRANSITION_MS = 340
const Z7_TRANSITION_MS = 780
const NAVIGATION_SETTLE_MS = 140

const relationClasses = {
  dependency: { code: 'DEP', rgb: '236, 187, 92' },
  evidence: { code: 'EVID', rgb: '103, 218, 194' },
  causal: { code: 'CAUSE', rgb: '234, 132, 122' },
  lineage: { code: 'LINE', rgb: '177, 151, 255' },
}

/*
 * Relation taxonomy remains provisional. These fixture links exercise the
 * selected E5 carrier and D1 directionality without freezing final ontology.
 */
const relations = [
  { id: 'q-i', source: 'q', target: 'i', className: 'dependency' },
  { id: 'i-v', source: 'i', target: 'v', className: 'evidence' },
  { id: 'r-m', source: 'r', target: 'm', className: 'lineage' },
  { id: 'm-v', source: 'm', target: 'v', className: 'causal' },
]

let zoom = DEFAULT_ZOOM
let panX = -WORLD_WIDTH / 2
let panY = -WORLD_HEIGHT / 2 + 8
let dragState = null
let relationFrame = 0
let relationMotionFrame = 0
let relationMotionUntil = 0
let panFrame = 0
let panDeltaX = 0
let panDeltaY = 0
let pinchFrame = 0
let pinchDelta = 0
let pinchAnchor = { x: 0, y: 0 }
let navigationSettleTimer = 0
let deepFocusTimer = 0

renderRelations()
installNavigation()
installNodeIntegration()
installShellActions()
installAppearanceControls()
installGeometryObservers()
installGlobalRecovery()
applyTransform()
syncIntegratedState()
syncAppearanceControls()
requestRelationUpdate()

function renderRelations() {
  if (!relationSvg) return

  relationSvg.replaceChildren(...relations.map((relation) => {
    const semantic = relationClasses[relation.className]
    const group = document.createElementNS('http://www.w3.org/2000/svg', 'g')
    group.classList.add('reintegration-relation')
    group.dataset.relationId = relation.id
    group.dataset.source = relation.source
    group.dataset.target = relation.target
    group.dataset.direction = 'forward'
    group.style.setProperty('--class-rgb', semantic.rgb)

    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path')
    path.classList.add('semantic-path')

    /* D1 target arrow remains semantic and is never toggled by appearance. */
    const arrow = document.createElementNS('http://www.w3.org/2000/svg', 'path')
    arrow.classList.add('semantic-arrow')

    const tag = document.createElementNS('http://www.w3.org/2000/svg', 'g')
    tag.classList.add('semantic-tag')

    const tagBg = document.createElementNS('http://www.w3.org/2000/svg', 'rect')
    tagBg.classList.add('semantic-tag-bg')
    tagBg.setAttribute('width', '48')
    tagBg.setAttribute('height', '22')
    tagBg.setAttribute('rx', '7')

    const tagText = document.createElementNS('http://www.w3.org/2000/svg', 'text')
    tagText.classList.add('semantic-tag-text')
    tagText.textContent = semantic.code

    tag.append(tagBg, tagText)
    group.append(path, arrow, tag)
    return group
  }))
}

function installNavigation() {
  document.querySelector('#zoom-in')?.addEventListener('click', () => {
    markNavigating()
    zoomAtStageCenter(zoom * 1.12)
  })
  document.querySelector('#zoom-out')?.addEventListener('click', () => {
    markNavigating()
    zoomAtStageCenter(zoom / 1.12)
  })
  document.querySelector('#fit-world')?.addEventListener('click', () => {
    markNavigating()
    fitWorld()
  })
  document.querySelector('#reset-world')?.addEventListener('click', () => {
    markNavigating()
    resetWorld()
  })

  stage?.addEventListener('wheel', (event) => {
    if (html.dataset.deepFocus !== 'false') return
    if (event.target.closest('.reintegration-appearance-panel')) return
    if (!stage) return

    const deltaModeScale = wheelDeltaModeScale(event)

    /*
     * Chromium exposes native trackpad pinch as ctrl+wheel. This mirrors the
     * already promoted V1 pinch architecture: frame-coalesced deltas, bounded
     * per-frame travel and pointer-anchor preservation.
     */
    if (event.ctrlKey) {
      event.preventDefault()
      const rect = stage.getBoundingClientRect()
      pinchDelta += event.deltaY * deltaModeScale
      pinchAnchor = {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top,
      }
      markNavigating()

      if (pinchFrame) return
      pinchFrame = requestAnimationFrame(() => {
        pinchFrame = 0
        const delta = clamp(pinchDelta, -MAX_PINCH_DELTA_PER_FRAME, MAX_PINCH_DELTA_PER_FRAME)
        pinchDelta = 0
        if (Math.abs(delta) < 0.01) return
        const factor = Math.exp(-delta * PINCH_SENSITIVITY)
        zoomAround(pinchAnchor.x, pinchAnchor.y, zoom * factor)
      })
      return
    }

    /*
     * Ordinary two-finger scrolling is spatial movement, not zoom. This is the
     * promoted Project Cockpit navigation contract and matches native scroll
     * direction: positive wheel delta moves the world up/left in the viewport.
     */
    event.preventDefault()
    let deltaX = event.deltaX * deltaModeScale
    let deltaY = event.deltaY * deltaModeScale
    if (event.shiftKey && Math.abs(deltaX) < Math.abs(deltaY)) {
      deltaX = deltaY
      deltaY = 0
    }

    panDeltaX += deltaX
    panDeltaY += deltaY
    markNavigating()
    if (panFrame) return

    panFrame = requestAnimationFrame(() => {
      panFrame = 0
      panX -= panDeltaX
      panY -= panDeltaY
      panDeltaX = 0
      panDeltaY = 0
      applyTransform()
    })
  }, { passive: false })

  stage?.addEventListener('pointerdown', (event) => {
    if (html.dataset.deepFocus !== 'false') return
    if (event.button !== 0) return
    if (event.target.closest(`${NODE_SELECTOR}, button, input, textarea, select, .reintegration-appearance-panel`)) return

    dragState = {
      pointerId: event.pointerId,
      startX: event.clientX,
      startY: event.clientY,
      startPanX: panX,
      startPanY: panY,
    }
    stage.setPointerCapture(event.pointerId)
    stage.classList.add('is-dragging')
    markNavigating()
  })

  stage?.addEventListener('pointermove', (event) => {
    if (!dragState || event.pointerId !== dragState.pointerId) return
    panX = dragState.startPanX + event.clientX - dragState.startX
    panY = dragState.startPanY + event.clientY - dragState.startY
    markNavigating()
    applyTransform()
  })

  const endDrag = (event) => {
    if (!dragState || event.pointerId !== dragState.pointerId) return
    if (stage?.hasPointerCapture(event.pointerId)) stage.releasePointerCapture(event.pointerId)
    dragState = null
    stage?.classList.remove('is-dragging')
    scheduleNavigationSettle()
  }

  stage?.addEventListener('pointerup', endDrag)
  stage?.addEventListener('pointercancel', endDrag)

  stage?.addEventListener('keydown', (event) => {
    if (html.dataset.deepFocus !== 'false' || event.target !== stage) return
    const step = event.shiftKey ? 320 : 150
    const movement = {
      ArrowLeft: [step, 0],
      ArrowRight: [-step, 0],
      ArrowUp: [0, step],
      ArrowDown: [0, -step],
    }[event.key]

    if (movement) {
      event.preventDefault()
      panX += movement[0]
      panY += movement[1]
      markNavigating()
      applyTransform()
      return
    }

    if (event.key === '+' || event.key === '=') {
      event.preventDefault()
      markNavigating()
      zoomAtStageCenter(zoom * 1.12)
    } else if (event.key === '-') {
      event.preventDefault()
      markNavigating()
      zoomAtStageCenter(zoom / 1.12)
    } else if (event.key === '0') {
      event.preventDefault()
      markNavigating()
      resetWorld()
    }
  })

  document.querySelector('#jump-button')?.addEventListener('click', jumpToSearch)
  jumpInput?.addEventListener('keydown', (event) => {
    if (event.key !== 'Enter') return
    event.preventDefault()
    jumpToSearch()
  })
}

function installNodeIntegration() {
  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    const key = node.dataset.nodeKey
    if (!key) continue

    node.addEventListener('click', () => {
      syncIntegratedState()
      syncRelationGeometryDuringNodeMotion(430)
    })

    node.addEventListener('keydown', (event) => {
      if (event.key !== 'Enter' && event.key !== ' ') return
      window.setTimeout(() => {
        syncIntegratedState()
        syncRelationGeometryDuringNodeMotion(430)
      }, 0)
    })

    node.addEventListener('pointerenter', () => {
      setRelatedState(key, true)
      syncRelationGeometryDuringNodeMotion(250)
    })

    node.addEventListener('pointerleave', () => {
      setRelatedState(key, false)
      syncRelationGeometryDuringNodeMotion(390)
    })
  }
}

function installShellActions() {
  detailToggle?.addEventListener('click', () => {
    if (html.dataset.deepFocus !== 'false') return
    const selected = currentSelectedNode()
    if (!selected) return
    selected.click()
    syncIntegratedState()
    syncRelationGeometryDuringNodeMotion(430)
  })

  deepDiveButton?.addEventListener('click', () => enterDeepFocus())
  returnToProject?.addEventListener('click', () => leaveDeepFocus())

  document.querySelector('#fullscreen-world')?.addEventListener('click', async () => {
    try {
      if (!document.fullscreenElement) {
        await document.documentElement.requestFullscreen?.()
      } else {
        await document.exitFullscreen?.()
      }
    } catch {
      showProvisionalMessage('Browser fullscreen was unavailable; the Cockpit remains usable in the current window.')
    }
  })

  document.querySelector('#conversation-expand')?.addEventListener('click', () => {
    showProvisionalMessage('Conversation Workspace is the next exact-source reintegration layer. This button deliberately does not open an approximate substitute.')
  })

  document.querySelector('#composer-send')?.addEventListener('click', () => {
    showProvisionalMessage('Live conversation execution is outside this design-lab reintegration slice. The compact composer is preserved as an interaction affordance only.')
  })
}

function installAppearanceControls() {
  appearanceToggle?.addEventListener('click', () => setAppearancePanelOpen(Boolean(appearancePanel?.hidden)))
  appearanceClose?.addEventListener('click', () => setAppearancePanelOpen(false))

  for (const button of document.querySelectorAll('[data-shape-option]')) {
    button.addEventListener('click', () => {
      html.dataset.shapeStyle = button.dataset.shapeOption || 'true'
      syncAppearanceControls()
      syncRelationGeometryDuringNodeMotion(120)
    })
  }

  for (const button of document.querySelectorAll('[data-surface-option]')) {
    button.addEventListener('click', () => {
      html.dataset.surfaceStyle = button.dataset.surfaceOption || 'material'
      syncAppearanceControls()
    })
  }

  reducedMotionToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedMotionToggle.checked ? 'on' : 'off'
    syncAppearanceControls()
    requestRelationUpdate()
  })

  appearanceReset?.addEventListener('click', () => {
    html.dataset.shapeStyle = 'true'
    html.dataset.surfaceStyle = 'material'
    html.dataset.reduced = 'off'
    syncAppearanceControls()
    syncRelationGeometryDuringNodeMotion(120)
  })
}

function installGeometryObservers() {
  window.addEventListener('resize', () => {
    requestRelationUpdate()
    updateViewportStatus()
  }, { passive: true })

  if ('ResizeObserver' in window && world) {
    const observer = new ResizeObserver(requestRelationUpdate)
    observer.observe(world)
  }

  const host = document.querySelector('#expansion-practical-nodes')
  if ('MutationObserver' in window && host) {
    const observer = new MutationObserver((mutations) => {
      if (!mutations.some((mutation) => mutation.type === 'attributes')) return
      syncIntegratedState()
      syncRelationGeometryDuringNodeMotion(430)
    })
    observer.observe(host, {
      subtree: true,
      attributes: true,
      attributeFilter: ['data-selected', 'data-expanded', 'data-expansion-style'],
    })
  }
}

function installGlobalRecovery() {
  window.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return
    if (html.dataset.deepFocus !== 'false') {
      event.preventDefault()
      leaveDeepFocus()
      return
    }
    if (appearancePanel && !appearancePanel.hidden) {
      event.preventDefault()
      setAppearancePanelOpen(false)
      appearanceToggle?.focus({ preventScroll: true })
    }
  })
}

function jumpToSearch() {
  if (html.dataset.deepFocus !== 'false') return
  const query = jumpInput?.value.trim().toLowerCase()
  if (!query) return

  const nodes = [...document.querySelectorAll(NODE_SELECTOR)]
  const node = nodes.find((candidate) => {
    const title = candidate.querySelector('.node-surface strong')?.textContent?.trim().toLowerCase() || ''
    const kind = candidate.querySelector('.unit-kind')?.textContent?.trim().toLowerCase() || ''
    return title.includes(query) || kind.includes(query) || candidate.dataset.nodeKey === query
  })

  if (!node) {
    showProvisionalMessage(`No work unit matched “${jumpInput.value.trim()}”.`)
    return
  }

  /*
   * Exact X5 behavior toggles expansion when an already-selected node is
   * clicked. Jump/search selects without accidentally changing depth.
   */
  if (node.dataset.selected !== 'true') node.click()
  syncIntegratedState()
  centerNode(node)
  node.focus({ preventScroll: true })
}

function centerNode(node) {
  const worldRect = world?.getBoundingClientRect()
  const nodeRect = node.getBoundingClientRect()
  if (!worldRect || !nodeRect || !stage) return

  const worldX = (nodeRect.left + nodeRect.width / 2 - worldRect.left) / zoom
  const worldY = (nodeRect.top + nodeRect.height / 2 - worldRect.top) / zoom

  panX = -worldX * zoom
  panY = -worldY * zoom
  markNavigating()
  applyTransform()
}

function zoomAtStageCenter(nextZoom) {
  if (!stage) return
  const rect = stage.getBoundingClientRect()
  zoomAround(rect.width / 2, rect.height / 2, nextZoom)
}

function zoomAround(pointerX, pointerY, requestedZoom) {
  if (!stage) return
  const nextZoom = clamp(requestedZoom, MIN_ZOOM, MAX_ZOOM)
  if (Math.abs(nextZoom - zoom) < 0.0001) return

  const rect = stage.getBoundingClientRect()
  const centerX = rect.width / 2
  const centerY = rect.height / 2
  const worldX = (pointerX - centerX - panX) / zoom
  const worldY = (pointerY - centerY - panY) / zoom

  panX = pointerX - centerX - worldX * nextZoom
  panY = pointerY - centerY - worldY * nextZoom
  zoom = nextZoom
  markNavigating()
  applyTransform()
}

function fitWorld() {
  if (!stage) return
  const rect = stage.getBoundingClientRect()
  const availableWidth = Math.max(400, rect.width - 120)
  const availableHeight = Math.max(320, rect.height - 150)
  zoom = clamp(Math.min(availableWidth / WORLD_WIDTH, availableHeight / WORLD_HEIGHT), MIN_ZOOM, 1.08)
  panX = -(WORLD_WIDTH * zoom) / 2
  panY = -(WORLD_HEIGHT * zoom) / 2 + 10
  applyTransform()
}

function resetWorld() {
  zoom = DEFAULT_ZOOM
  panX = -WORLD_WIDTH / 2
  panY = -WORLD_HEIGHT / 2 + 8
  applyTransform()
}

function applyTransform() {
  if (!plane) return
  const renderPanX = snapToDevicePixel(panX)
  const renderPanY = snapToDevicePixel(panY)
  plane.style.transform = `translate3d(${renderPanX}px, ${renderPanY}px, 0) scale(${zoom})`
  updateViewportStatus()
}

function markNavigating() {
  stage?.classList.add('is-navigating')
  scheduleNavigationSettle()
}

function scheduleNavigationSettle() {
  if (navigationSettleTimer) window.clearTimeout(navigationSettleTimer)
  navigationSettleTimer = window.setTimeout(() => {
    navigationSettleTimer = 0
    stage?.classList.remove('is-navigating')
    /* Reapply a device-pixel-aligned transform after compositing is released. */
    applyTransform()
  }, NAVIGATION_SETTLE_MS)
}

function wheelDeltaModeScale(event) {
  if (event.deltaMode === 1) return 16
  if (event.deltaMode === 2) return stage?.clientHeight || window.innerHeight
  return 1
}

function snapToDevicePixel(value) {
  const ratio = window.devicePixelRatio || 1
  return Math.round(value * ratio) / ratio
}

async function enterDeepFocus() {
  if (html.dataset.deepFocus !== 'false') return
  setAppearancePanelOpen(false)

  let selected = currentSelectedNode()
  if (!selected) return

  /* Z7 begins from the actual selected X5 object, not a recreated source card. */
  if (selected.dataset.expanded !== 'true') {
    selected.click()
    syncIntegratedState()
    syncRelationGeometryDuringNodeMotion(430)
    await wait(html.dataset.reduced === 'on' ? 0 : X5_TRANSITION_MS)
    selected = currentSelectedNode()
  }

  if (!selected || selected.dataset.expanded !== 'true') {
    showProvisionalMessage('Deep focus requires the selected work unit to reach the accepted X5 expanded state first.')
    return
  }

  syncDeepFocusOrigin(selected)
  const title = selected.querySelector('.node-surface strong')?.textContent?.trim() || selected.dataset.nodeKey || 'Selected work unit'
  if (specialistTitle) specialistTitle.textContent = title

  specialistLayer?.setAttribute('aria-hidden', 'false')
  html.dataset.deepFocus = 'entering'

  if (deepFocusTimer) window.clearTimeout(deepFocusTimer)
  deepFocusTimer = window.setTimeout(() => {
    deepFocusTimer = 0
    html.dataset.deepFocus = 'focused'
    stage?.setAttribute('aria-hidden', 'true')
    returnToProject?.focus({ preventScroll: true })
  }, html.dataset.reduced === 'on' ? 20 : Z7_TRANSITION_MS + 20)
}

function leaveDeepFocus() {
  if (html.dataset.deepFocus === 'false') return
  if (deepFocusTimer) {
    window.clearTimeout(deepFocusTimer)
    deepFocusTimer = 0
  }

  /* Return choreography is intentionally direct because no reverse motion was frozen. */
  html.dataset.deepFocus = 'false'
  stage?.setAttribute('aria-hidden', 'false')
  specialistLayer?.setAttribute('aria-hidden', 'true')
  requestAnimationFrame(() => {
    const selected = currentSelectedNode()
    selected?.focus({ preventScroll: true })
    syncIntegratedState()
    requestRelationUpdate()
  })
}

function syncDeepFocusOrigin(node) {
  if (!stage) return
  const stageRect = stage.getBoundingClientRect()
  const nodeRect = node.getBoundingClientRect()
  const x = nodeRect.left - stageRect.left + nodeRect.width / 2
  const y = nodeRect.top - stageRect.top + nodeRect.height / 2
  html.style.setProperty('--deep-origin-x', `${snapToDevicePixel(x)}px`)
  html.style.setProperty('--deep-origin-y', `${snapToDevicePixel(y)}px`)
}

function setAppearancePanelOpen(open) {
  if (!appearancePanel || !appearanceToggle) return
  appearancePanel.hidden = !open
  appearanceToggle.setAttribute('aria-expanded', String(open))
}

function syncAppearanceControls() {
  const shape = html.dataset.shapeStyle || 'true'
  const surface = html.dataset.surfaceStyle || 'material'

  for (const button of document.querySelectorAll('[data-shape-option]')) {
    button.setAttribute('aria-pressed', String(button.dataset.shapeOption === shape))
  }
  for (const button of document.querySelectorAll('[data-surface-option]')) {
    button.setAttribute('aria-pressed', String(button.dataset.surfaceOption === surface))
  }
  if (reducedMotionToggle) reducedMotionToggle.checked = html.dataset.reduced === 'on'
}

function updateViewportStatus() {
  const percentage = Math.round(zoom * 100)
  if (zoomReadout) zoomReadout.textContent = `${percentage}%`
  if (viewportStatus) viewportStatus.textContent = `x ${Math.round(panX)} · y ${Math.round(panY)} · ${percentage}%`
  if (zoomIndicator) {
    const normalized = (zoom - MIN_ZOOM) / (MAX_ZOOM - MIN_ZOOM)
    zoomIndicator.style.left = `${clamp(normalized * 100, 0, 100)}%`
  }
}

function currentSelectedNode() {
  return document.querySelector(`${NODE_SELECTOR}[data-selected="true"]`)
}

function syncIntegratedState() {
  const selected = currentSelectedNode()
  if (!selected) return

  const title = selected.querySelector('.node-surface strong')?.textContent?.trim() || selected.dataset.nodeKey || 'unknown'
  const expanded = selected.dataset.expanded === 'true'

  if (selectedLabel) selectedLabel.textContent = `Selected: ${title}`
  if (detailStateLabel) detailStateLabel.textContent = `SEL2 selected · X5 ${expanded ? 'expanded' : 'compact'} · E5 relations`
  if (detailToggle) detailToggle.textContent = expanded ? 'Collapse' : 'Expand'
  if (specialistTitle) specialistTitle.textContent = title

  const composerContext = document.querySelector('#composer-context')
  if (composerContext) composerContext.textContent = title
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

  const frame = () => {
    updateRelationGeometry()
    if (performance.now() < relationMotionUntil) {
      relationMotionFrame = requestAnimationFrame(frame)
      return
    }
    relationMotionFrame = 0
    updateRelationGeometry()
  }

  relationMotionFrame = requestAnimationFrame(frame)
}

function updateRelationGeometry() {
  if (!world || !relationSvg) return
  const worldRect = world.getBoundingClientRect()
  const viewBox = relationSvg.viewBox.baseVal
  if (!worldRect.width || !worldRect.height || !viewBox.width || !viewBox.height) return

  for (const relation of relations) {
    const group = relationSvg.querySelector(`[data-relation-id="${relation.id}"]`)
    const source = world.querySelector(`${NODE_SELECTOR}[data-node-key="${relation.source}"]`)
    const target = world.querySelector(`${NODE_SELECTOR}[data-node-key="${relation.target}"]`)
    if (!group || !source || !target) continue

    const start = relationAnchor(source, chooseSourceSide(source, target), worldRect, viewBox)
    const end = relationAnchor(target, chooseTargetSide(source, target), worldRect, viewBox)

    group.querySelector('.semantic-path')?.setAttribute('d', relationPath(start, end))
    positionArrow(group.querySelector('.semantic-arrow'), end, end.side)
    positionTag(group.querySelector('.semantic-tag'), start, end)
  }
}

function relationAnchor(node, side, worldRect, viewBox) {
  const surface = node.querySelector('.node-surface') || node
  const rect = surface.getBoundingClientRect()

  let x = rect.left + rect.width / 2
  let y = rect.top + rect.height / 2

  if (side === 'left') x = rect.left
  if (side === 'right') x = rect.right
  if (side === 'top') y = rect.top
  if (side === 'bottom') y = rect.bottom

  if (side === 'right' && node.classList.contains('category-investigation') && html.dataset.shapeStyle === 'true') {
    x = rect.right - rect.width * 0.07
  }

  return {
    x: ((x - worldRect.left) / worldRect.width) * viewBox.width + viewBox.x,
    y: ((y - worldRect.top) / worldRect.height) * viewBox.height + viewBox.y,
    side,
  }
}

function chooseSourceSide(source, target) {
  const sourceRect = source.getBoundingClientRect()
  const targetRect = target.getBoundingClientRect()
  const dx = targetRect.left + targetRect.width / 2 - (sourceRect.left + sourceRect.width / 2)
  const dy = targetRect.top + targetRect.height / 2 - (sourceRect.top + sourceRect.height / 2)
  return Math.abs(dx) >= Math.abs(dy) ? (dx >= 0 ? 'right' : 'left') : (dy >= 0 ? 'bottom' : 'top')
}

function chooseTargetSide(source, target) {
  const sourceSide = chooseSourceSide(source, target)
  if (sourceSide === 'right') return 'left'
  if (sourceSide === 'left') return 'right'
  if (sourceSide === 'bottom') return 'top'
  return 'bottom'
}

function relationPath(start, end) {
  const horizontal = (start.side === 'left' || start.side === 'right') && (end.side === 'left' || end.side === 'right')

  if (horizontal) {
    const direction = Math.sign(end.x - start.x) || 1
    const bend = Math.max(42, Math.abs(end.x - start.x) * 0.38)
    const c1x = start.x + direction * bend
    const c2x = end.x - direction * bend
    return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(c1x)} ${formatCoord(start.y)}, ${formatCoord(c2x)} ${formatCoord(end.y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
  }

  const direction = Math.sign(end.y - start.y) || 1
  const bend = Math.max(38, Math.abs(end.y - start.y) * 0.40)
  const c1y = start.y + direction * bend
  const c2y = end.y - direction * bend
  return `M${formatCoord(start.x)} ${formatCoord(start.y)} C${formatCoord(start.x)} ${formatCoord(c1y)}, ${formatCoord(end.x)} ${formatCoord(c2y)}, ${formatCoord(end.x)} ${formatCoord(end.y)}`
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

function setRelatedState(nodeKey, active) {
  if (!relationSvg) return
  for (const group of relationSvg.querySelectorAll('.reintegration-relation')) {
    if (group.dataset.source === nodeKey || group.dataset.target === nodeKey) {
      group.classList.toggle('is-related', active)
    }
  }
}

function showProvisionalMessage(message) {
  if (!provisionalNote) return
  const strong = provisionalNote.querySelector('strong')
  const small = provisionalNote.querySelector('small')
  if (strong) strong.textContent = 'Integration boundary'
  if (small) small.textContent = message
}

function wait(milliseconds) {
  return new Promise((resolve) => window.setTimeout(resolve, milliseconds))
}

function formatCoord(value) {
  return Number(value.toFixed(1))
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}
