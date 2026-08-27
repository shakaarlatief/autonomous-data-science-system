const scene = document.querySelector('#connector-scene')
const relationLayer = scene?.querySelector('.connector-relations')
const portLayer = scene?.querySelector('.connector-port-overlay')

/*
 * Only markers that should visually sit above the work-unit perimeter are
 * mirrored into the overlay. K2 frame sockets intentionally remain in the
 * original under-node relation layer because human review preferred that
 * structural, frame-integrated treatment.
 */
const markerSelectors = [
  '.connector-source-terminal',
  '.connector-target-terminal',
  '.connector-chevron',
]

let initialized = false
let initializationAttempts = 0

scheduleInitialization()

function scheduleInitialization() {
  requestAnimationFrame(() => {
    requestAnimationFrame(initializePortLayer)
  })
}

function initializePortLayer() {
  if (initialized || !scene || !relationLayer || !portLayer) return

  const relationGroups = [...relationLayer.querySelectorAll('.connector-link')]
  const markersReady = relationGroups.every((group) => markerSelectors.some((selector) => group.querySelector(selector)))

  if (!markersReady && initializationAttempts < 8) {
    initializationAttempts += 1
    scheduleInitialization()
    return
  }

  for (const relationGroup of relationGroups) {
    const overlayGroup = overlayGroupFor(relationGroup.dataset.link)
    if (!overlayGroup) continue

    overlayGroup.replaceChildren()

    for (const selector of markerSelectors) {
      const sourceMarker = relationGroup.querySelector(selector)
      if (sourceMarker) overlayGroup.appendChild(sourceMarker.cloneNode(true))
    }

    syncOverlayGroup(relationGroup)
  }

  const observer = new MutationObserver((mutations) => {
    const changedGroups = new Set()

    for (const mutation of mutations) {
      const group = mutation.target.closest?.('.connector-link')
      if (group) changedGroups.add(group)
    }

    for (const group of changedGroups) syncOverlayGroup(group)
  })

  observer.observe(relationLayer, {
    subtree: true,
    attributes: true,
    attributeFilter: ['cx', 'cy', 'x', 'y', 'd', 'class', 'style'],
  })

  initialized = true
}

function overlayGroupFor(link) {
  if (!link || !portLayer) return null
  return portLayer.querySelector(`.connector-port-link[data-link="${link}"]`)
}

function syncOverlayGroup(relationGroup) {
  const overlayGroup = overlayGroupFor(relationGroup.dataset.link)
  if (!overlayGroup) return

  overlayGroup.classList.toggle('is-related', relationGroup.classList.contains('is-related'))

  const relatedRgb = relationGroup.style.getPropertyValue('--related-rgb')
  if (relatedRgb) overlayGroup.style.setProperty('--related-rgb', relatedRgb)
  else overlayGroup.style.removeProperty('--related-rgb')

  for (const selector of markerSelectors) {
    const sourceMarker = relationGroup.querySelector(selector)
    const overlayMarker = overlayGroup.querySelector(selector)
    if (!sourceMarker || !overlayMarker) continue

    copyAttribute(sourceMarker, overlayMarker, 'cx')
    copyAttribute(sourceMarker, overlayMarker, 'cy')
    copyAttribute(sourceMarker, overlayMarker, 'd')
  }
}

function copyAttribute(source, target, name) {
  if (!source.hasAttribute(name)) return
  target.setAttribute(name, source.getAttribute(name))
}
