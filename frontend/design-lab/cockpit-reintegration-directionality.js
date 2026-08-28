/*
 * Source-faithful M06 directionality adapter.
 *
 * Accepted source:
 *   07d573b6569b9f09a3b7e00936f3eadecee721b3
 *
 * The existing integrated E5 fixture currently uses forward relations. This
 * adapter completes the underlying D0-D3 rendering capability without changing
 * that fixture: undirected, forward, reverse and bidirectional states are all
 * represented by the same restrained edge-docked arrow treatment.
 *
 * Relation meaning remains independent from directionality. The adapter reads
 * only each relation group's data-direction attribute and never infers or
 * changes semantic direction from appearance settings.
 */

const relationSvg = document.querySelector('#reintegration-relations')

installStylesheet()
upgradeDirectionality()

function installStylesheet() {
  if (document.querySelector('link[href="./cockpit-reintegration-directionality.css"]')) return
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-reintegration-directionality.css'
  document.head.appendChild(link)
}

function upgradeDirectionality() {
  if (!relationSvg) return

  for (const group of relationSvg.querySelectorAll('.reintegration-relation')) {
    const endArrow = group.querySelector('.semantic-arrow')
    if (endArrow) endArrow.classList.add('semantic-arrow-end')

    if (!group.querySelector('.semantic-arrow-start')) {
      const startArrow = document.createElementNS('http://www.w3.org/2000/svg', 'path')
      startArrow.classList.add('semantic-arrow', 'semantic-arrow-start')
      const tag = group.querySelector('.semantic-tag')
      group.insertBefore(startArrow, tag || null)
    }

    if (!['none', 'forward', 'reverse', 'both'].includes(group.dataset.direction || '')) {
      group.dataset.direction = 'forward'
    }

    syncStartArrow(group)
  }

  if ('MutationObserver' in window) {
    const observer = new MutationObserver((mutations) => {
      const groups = new Set()
      for (const mutation of mutations) {
        const group = mutation.target.closest?.('.reintegration-relation')
          || mutation.target.parentElement?.closest?.('.reintegration-relation')
        if (group) groups.add(group)
      }
      for (const group of groups) syncStartArrow(group)
    })

    observer.observe(relationSvg, {
      subtree: true,
      attributes: true,
      attributeFilter: ['d', 'data-direction'],
    })
  }
}

function syncStartArrow(group) {
  const path = group.querySelector('.semantic-path')
  const arrow = group.querySelector('.semantic-arrow-start')
  if (!path || !arrow) return

  let totalLength = 0
  try {
    totalLength = path.getTotalLength()
  } catch {
    return
  }
  if (!Number.isFinite(totalLength) || totalLength <= 0) return

  const tip = path.getPointAtLength(0)
  const tangentPoint = path.getPointAtLength(Math.min(8, totalLength))
  const dx = tangentPoint.x - tip.x
  const dy = tangentPoint.y - tip.y
  const magnitude = Math.hypot(dx, dy) || 1
  const ux = dx / magnitude
  const uy = dy / magnitude
  const nx = -uy
  const ny = ux
  const armLength = 5
  const halfWidth = 3.5
  const baseX = tip.x + ux * armLength
  const baseY = tip.y + uy * armLength
  const aX = baseX + nx * halfWidth
  const aY = baseY + ny * halfWidth
  const bX = baseX - nx * halfWidth
  const bY = baseY - ny * halfWidth

  arrow.setAttribute(
    'd',
    `M${format(aX)} ${format(aY)} L${format(tip.x)} ${format(tip.y)} L${format(bX)} ${format(bY)}`,
  )
  arrow.dataset.tipX = format(tip.x)
  arrow.dataset.tipY = format(tip.y)
}

function format(value) {
  return Number(value.toFixed(2)).toString()
}
