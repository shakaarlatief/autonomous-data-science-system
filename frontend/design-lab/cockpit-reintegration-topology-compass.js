/*
 * Live topology-compass adapter for the source-faithful Cockpit.
 *
 * M17 freezes the existence of a compact topology compass, but the accepted
 * design-lab fixture used static decorative dots. In the integrated Cockpit the
 * instrument should report actual project position. This module therefore
 * derives node positions and relation links from the mounted Project Grid and
 * highlights the real current WorkUnit without taking ownership of selection.
 */

const root = document.documentElement
const compass = document.querySelector('.reintegration-topology-compass')
const miniMap = compass?.querySelector('.reintegration-mini-map')
const nodeHost = document.querySelector('#expansion-practical-nodes')
const relationSvg = document.querySelector('#reintegration-relations')
const NODE_SELECTOR = '.expansion-practical-node'
const SVG_NS = 'http://www.w3.org/2000/svg'
const CANONICAL_HALF_WIDTH = 88
const CANONICAL_HALF_HEIGHT = 46

if (compass && miniMap && nodeHost) installLiveCompass()

function installLiveCompass() {
  root.dataset.topologyCompass = 'live'
  syncCompass()

  if ('MutationObserver' in window) {
    const nodeObserver = new MutationObserver((mutations) => {
      if (!mutations.some((mutation) => mutation.type === 'childList' || mutation.type === 'attributes')) return
      scheduleSync()
    })
    nodeObserver.observe(nodeHost, {
      subtree: true,
      childList: true,
      attributes: true,
      attributeFilter: ['data-selected', 'data-expanded', 'style'],
    })

    if (relationSvg) {
      const relationObserver = new MutationObserver(scheduleSync)
      relationObserver.observe(relationSvg, {
        subtree: true,
        childList: true,
        attributes: true,
        attributeFilter: ['data-source', 'data-target'],
      })
    }
  }

  window.addEventListener('resize', scheduleSync, { passive: true })
}

let syncFrame = 0
function scheduleSync() {
  if (syncFrame) cancelAnimationFrame(syncFrame)
  syncFrame = requestAnimationFrame(() => {
    syncFrame = 0
    syncCompass()
  })
}

function syncCompass() {
  if (!miniMap || !nodeHost) return
  const nodes = [...nodeHost.querySelectorAll(NODE_SELECTOR)]
  if (!nodes.length) return

  const hostWidth = nodeHost.clientWidth || 1440
  const hostHeight = nodeHost.clientHeight || 760
  const positions = new Map()

  for (const node of nodes) {
    const key = node.dataset.nodeKey
    if (!key) continue
    positions.set(key, {
      x: clamp((node.offsetLeft + CANONICAL_HALF_WIDTH) / hostWidth, 0.04, 0.96),
      y: clamp((node.offsetTop + CANONICAL_HALF_HEIGHT) / hostHeight, 0.06, 0.94),
      title: node.querySelector('.node-surface > strong')?.textContent?.trim() || key,
      selected: node.dataset.selected === 'true',
    })
  }

  const selectedEntry = [...positions.entries()].find(([, value]) => value.selected)
  const selectedKey = selectedEntry?.[0] || ''
  const relatedKeys = relationNeighbors(selectedKey)
  const links = buildRelationLinks(positions)
  const dots = [...positions.entries()].map(([key, position]) => buildDot(key, position, relatedKeys.has(key)))

  miniMap.replaceChildren(links, ...dots)
  miniMap.setAttribute('role', 'img')
  miniMap.setAttribute('aria-label', selectedEntry
    ? `Project topology. Current position: ${selectedEntry[1].title}.`
    : 'Project topology.')

  compass.dataset.currentWork = selectedKey
  compass.setAttribute('aria-label', selectedEntry
    ? `Project position: ${selectedEntry[1].title}`
    : 'Project position')
}

function buildRelationLinks(positions) {
  const svg = document.createElementNS(SVG_NS, 'svg')
  svg.classList.add('reintegration-mini-map-links')
  svg.setAttribute('viewBox', '0 0 100 100')
  svg.setAttribute('preserveAspectRatio', 'none')
  svg.setAttribute('aria-hidden', 'true')

  for (const relation of relationGroups()) {
    const source = positions.get(relation.dataset.source || '')
    const target = positions.get(relation.dataset.target || '')
    if (!source || !target) continue
    const line = document.createElementNS(SVG_NS, 'line')
    line.setAttribute('x1', format(source.x * 100))
    line.setAttribute('y1', format(source.y * 100))
    line.setAttribute('x2', format(target.x * 100))
    line.setAttribute('y2', format(target.y * 100))
    svg.appendChild(line)
  }

  return svg
}

function buildDot(key, position, related) {
  const dot = document.createElement('i')
  dot.className = 'mini-dot'
  dot.dataset.nodeKey = key
  dot.style.left = `${format(position.x * 100)}%`
  dot.style.top = `${format(position.y * 100)}%`
  dot.title = position.title
  dot.setAttribute('aria-hidden', 'true')
  if (position.selected) dot.classList.add('is-current')
  else if (related) dot.classList.add('is-related')
  return dot
}

function relationNeighbors(selectedKey) {
  const keys = new Set()
  if (!selectedKey) return keys
  for (const relation of relationGroups()) {
    if (relation.dataset.source === selectedKey && relation.dataset.target) keys.add(relation.dataset.target)
    if (relation.dataset.target === selectedKey && relation.dataset.source) keys.add(relation.dataset.source)
  }
  return keys
}

function relationGroups() {
  return relationSvg ? [...relationSvg.querySelectorAll('.reintegration-relation')] : []
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}

function format(value) {
  return Number(value.toFixed(2)).toString()
}
