/*
 * Human-review fidelity corrections for the source-faithful Cockpit reintegration.
 *
 * No new semantic or visual choice is introduced here. This adapter repairs:
 *   - the project-general rail artifact against M20 / 606e027f281b35c2dfc93d059a1681df23bc2b73
 *   - connector endpoint layering against 183264bdd07783eaa2354894592f2cf4a076b6ec
 */

const root = document.documentElement
const world = document.querySelector('#reintegration-world')
const relationSvg = document.querySelector('#reintegration-relations')
const SVG_NS = 'http://www.w3.org/2000/svg'
const TERMINAL_OUTSET = 2

repairProjectGeneralArtifact()
restoreConnectorPortOverlay()

/* -------------------------------------------------------------------------- */
/* Project-general conversation identity                                      */
/* -------------------------------------------------------------------------- */

function repairProjectGeneralArtifact() {
  const projectThread = document.querySelector('.reintegration-thread-item[data-thread-scope="project"]')
  const artifact = projectThread?.querySelector('.reintegration-project-thread-artifact')
  if (!projectThread || !artifact) return

  projectThread.classList.add('is-project-thread')
  artifact.replaceChildren(
    projectGlyph(),
    projectCopy(),
  )
}

function projectGlyph() {
  const glyph = document.createElement('span')
  glyph.className = 'reintegration-project-thread-glyph'
  glyph.textContent = 'P'
  return glyph
}

function projectCopy() {
  const copy = document.createElement('span')
  copy.className = 'reintegration-project-thread-copy'

  const scope = document.createElement('small')
  scope.textContent = 'PROJECT'
  const title = document.createElement('strong')
  title.textContent = 'General project discussion'

  copy.append(scope, title)
  return copy
}

/* -------------------------------------------------------------------------- */
/* Accepted connector-port overlay                                            */
/* -------------------------------------------------------------------------- */

function restoreConnectorPortOverlay() {
  if (!world || !relationSvg) return

  let overlay = world.querySelector('#reintegration-port-overlay')
  if (!overlay) {
    overlay = document.createElementNS(SVG_NS, 'svg')
    overlay.id = 'reintegration-port-overlay'
    overlay.classList.add('reintegration-port-overlay')
    overlay.setAttribute('viewBox', relationSvg.getAttribute('viewBox') || '0 0 1440 760')
    overlay.setAttribute('preserveAspectRatio', relationSvg.getAttribute('preserveAspectRatio') || 'none')
    overlay.setAttribute('aria-hidden', 'true')
    world.appendChild(overlay)
  }

  root.dataset.portOverlayRecovered = 'true'
  syncOverlay(overlay)

  if (!('MutationObserver' in window)) return

  const observer = new MutationObserver((mutations) => {
    let rebuild = false
    const affectedRelations = new Set()

    for (const mutation of mutations) {
      if (mutation.type === 'childList') {
        rebuild = true
        continue
      }

      if (!(mutation.target instanceof Element)) continue
      const group = mutation.target.closest('.reintegration-relation')
      if (group) affectedRelations.add(group)
    }

    if (rebuild) {
      syncOverlay(overlay)
      return
    }

    for (const group of affectedRelations) syncOverlayRelation(group, overlay)
  })

  observer.observe(relationSvg, {
    subtree: true,
    childList: true,
    attributes: true,
    attributeFilter: ['d', 'class', 'style', 'data-source', 'data-target'],
  })
}

function syncOverlay(overlay) {
  const sourceGroups = [...relationSvg.querySelectorAll('.reintegration-relation')]
  const liveIds = new Set(sourceGroups.map((group) => group.dataset.relationId).filter(Boolean))

  for (const group of [...overlay.querySelectorAll('.reintegration-port-group')]) {
    if (!liveIds.has(group.dataset.relationId)) group.remove()
  }

  for (const sourceGroup of sourceGroups) syncOverlayRelation(sourceGroup, overlay)
}

function syncOverlayRelation(sourceGroup, overlay) {
  const relationId = sourceGroup.dataset.relationId
  if (!relationId) return

  let portGroup = [...overlay.querySelectorAll('.reintegration-port-group')]
    .find((group) => group.dataset.relationId === relationId)

  if (!portGroup) {
    portGroup = document.createElementNS(SVG_NS, 'g')
    portGroup.classList.add('reintegration-port-group')
    portGroup.dataset.relationId = relationId
    portGroup.append(
      makeCircle('reintegration-port-dot reintegration-port-source-dot', 2.6),
      makeCircle('reintegration-port-dot reintegration-port-target-dot', 2.6),
      makeSocket('reintegration-port-socket reintegration-port-source-socket'),
      makeSocket('reintegration-port-socket reintegration-port-target-socket'),
    )
    overlay.appendChild(portGroup)
  }

  portGroup.dataset.source = sourceGroup.dataset.source || ''
  portGroup.dataset.target = sourceGroup.dataset.target || ''
  portGroup.classList.toggle('is-related', sourceGroup.classList.contains('is-related'))
  copyCustomProperty(sourceGroup, portGroup, '--class-rgb')
  copyCustomProperty(sourceGroup, portGroup, '--hover-rgb')
  syncTerminalGeometry(sourceGroup, portGroup)
}

function makeCircle(classNames, radius) {
  const circle = document.createElementNS(SVG_NS, 'circle')
  circle.setAttribute('class', `reintegration-port-terminal ${classNames}`)
  circle.setAttribute('r', String(radius))
  return circle
}

function makeSocket(classNames) {
  const socket = document.createElementNS(SVG_NS, 'rect')
  socket.setAttribute('class', `reintegration-port-terminal ${classNames}`)
  socket.setAttribute('width', '5.2')
  socket.setAttribute('height', '5.2')
  socket.setAttribute('rx', '1.1')
  return socket
}

function copyCustomProperty(source, target, property) {
  const value = source.style.getPropertyValue(property).trim()
  if (value) target.style.setProperty(property, value)
  else target.style.removeProperty(property)
}

function syncTerminalGeometry(sourceGroup, portGroup) {
  const path = sourceGroup.querySelector('.semantic-path')
  if (!path) return

  let length = 0
  try {
    length = path.getTotalLength()
  } catch {
    return
  }
  if (!Number.isFinite(length) || length <= 0) return

  const start = path.getPointAtLength(0)
  const startTangent = path.getPointAtLength(Math.min(8, length))
  const end = path.getPointAtLength(length)
  const endTangent = path.getPointAtLength(Math.max(0, length - Math.min(8, length)))

  const sourceVector = normalize(start.x - startTangent.x, start.y - startTangent.y)
  const targetVector = normalize(end.x - endTangent.x, end.y - endTangent.y)

  const sourceDot = {
    x: start.x + sourceVector.x * TERMINAL_OUTSET,
    y: start.y + sourceVector.y * TERMINAL_OUTSET,
  }
  const targetDot = {
    x: end.x + targetVector.x * TERMINAL_OUTSET,
    y: end.y + targetVector.y * TERMINAL_OUTSET,
  }

  positionCircle(portGroup.querySelector('.reintegration-port-source-dot'), sourceDot)
  positionCircle(portGroup.querySelector('.reintegration-port-target-dot'), targetDot)
  positionSocket(portGroup.querySelector('.reintegration-port-source-socket'), start)
  positionSocket(portGroup.querySelector('.reintegration-port-target-socket'), end)
}

function positionCircle(element, point) {
  if (!element) return
  element.setAttribute('cx', format(point.x))
  element.setAttribute('cy', format(point.y))
}

function positionSocket(element, point) {
  if (!element) return
  element.setAttribute('x', format(point.x - 2.6))
  element.setAttribute('y', format(point.y - 2.6))
}

function normalize(x, y) {
  const magnitude = Math.hypot(x, y) || 1
  return { x: x / magnitude, y: y / magnitude }
}

function format(value) {
  return Number(value.toFixed(2)).toString()
}
