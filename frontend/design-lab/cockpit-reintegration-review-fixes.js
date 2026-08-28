/*
 * Human-review fidelity corrections for the source-faithful Cockpit reintegration.
 *
 * No new semantic or visual choice is introduced here. This adapter repairs:
 *   - the project-general rail artifact against M20 / 606e027f281b35c2dfc93d059a1681df23bc2b73
 *   - K1 Micro-dot placement against 42ec63d17095753dc4ab97628cd859473cbdf5e8
 *   - K1/K2 layer separation against 183264bdd07783eaa2354894592f2cf4a076b6ec
 *
 * Accepted connector distinction:
 *   Micro dots: above-node overlay, 2 px outward along the known endpoint side.
 *   Frame sockets: original under-node relation layer, centered on the relation
 *   anchor so the node surface visually integrates the socket into its frame.
 */

const root = document.documentElement
const world = document.querySelector('#reintegration-world')
const relationSvg = document.querySelector('#reintegration-relations')
const SVG_NS = 'http://www.w3.org/2000/svg'
const TERMINAL_OUTSET = 2
const NODE_SELECTOR = '.expansion-practical-node'

repairProjectGeneralArtifact()
restoreMicroDotPortOverlay()

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
/* Accepted K1 Micro-dot overlay                                              */
/* -------------------------------------------------------------------------- */

function restoreMicroDotPortOverlay() {
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

function copyCustomProperty(source, target, property) {
  const value = source.style.getPropertyValue(property).trim()
  if (value) target.style.setProperty(property, value)
  else target.style.removeProperty(property)
}

function syncTerminalGeometry(sourceGroup, portGroup) {
  const path = sourceGroup.querySelector('.semantic-path')
  const sourceNode = nodeByKey(sourceGroup.dataset.source)
  const targetNode = nodeByKey(sourceGroup.dataset.target)
  if (!path || !sourceNode || !targetNode) return

  let length = 0
  try {
    length = path.getTotalLength()
  } catch {
    return
  }
  if (!Number.isFinite(length) || length <= 0) return

  const start = path.getPointAtLength(0)
  const end = path.getPointAtLength(length)
  const sourceSide = chooseSourceSide(sourceNode, targetNode)
  const targetSide = oppositeSide(sourceSide)

  positionCircle(
    portGroup.querySelector('.reintegration-port-source-dot'),
    terminalAnchor(start, sourceSide),
  )
  positionCircle(
    portGroup.querySelector('.reintegration-port-target-dot'),
    terminalAnchor(end, targetSide),
  )
}

/*
 * Exact mechanism restored from 42ec63d: the dot moves outward along the
 * connector's known attachment side. A path-tangent vector is not equivalent
 * and was the reintegration regression that pushed dots back over the frame.
 */
function terminalAnchor(point, side) {
  if (side === 'left') return { x: point.x - TERMINAL_OUTSET, y: point.y }
  if (side === 'right') return { x: point.x + TERMINAL_OUTSET, y: point.y }
  if (side === 'top') return { x: point.x, y: point.y - TERMINAL_OUTSET }
  return { x: point.x, y: point.y + TERMINAL_OUTSET }
}

function chooseSourceSide(source, target) {
  const sourceRect = source.getBoundingClientRect()
  const targetRect = target.getBoundingClientRect()
  const dx = targetRect.left + targetRect.width / 2 - (sourceRect.left + sourceRect.width / 2)
  const dy = targetRect.top + targetRect.height / 2 - (sourceRect.top + sourceRect.height / 2)
  return Math.abs(dx) >= Math.abs(dy)
    ? (dx >= 0 ? 'right' : 'left')
    : (dy >= 0 ? 'bottom' : 'top')
}

function oppositeSide(side) {
  if (side === 'left') return 'right'
  if (side === 'right') return 'left'
  if (side === 'top') return 'bottom'
  return 'top'
}

function nodeByKey(key) {
  if (!key) return null
  return world?.querySelector(`${NODE_SELECTOR}[data-node-key="${CSS.escape(key)}"]`) || null
}

function positionCircle(element, point) {
  if (!element) return
  element.setAttribute('cx', format(point.x))
  element.setAttribute('cy', format(point.y))
}

function format(value) {
  return Number(value.toFixed(2)).toString()
}
