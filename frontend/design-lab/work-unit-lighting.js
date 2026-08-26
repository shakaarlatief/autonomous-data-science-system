const html = document.documentElement

const reducedToggle = document.querySelector('#reduced-toggle')
if (reducedToggle) {
  reducedToggle.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
  })
}

for (const variant of document.querySelectorAll('.lighting-variant')) {
  const world = variant.querySelector('.lighting-world')
  const spill = variant.querySelector('.world-spill')
  const relationPaths = [...variant.querySelectorAll('.lighting-relations path')]

  for (const node of variant.querySelectorAll('.lighting-node')) {
    node.addEventListener('pointerenter', () => {
      const nodeId = node.dataset.node
      const rgb = readNodeRgb(node)

      if (spill && world) {
        positionWorldSpill(world, node, spill, rgb)
        world.classList.add('has-hover')
      }

      for (const path of relationPaths) {
        const linkedNodes = path.dataset.link?.split('-') ?? []
        const isRelated = linkedNodes.includes(nodeId)
        path.classList.toggle('is-related', isRelated)
        if (isRelated) path.style.setProperty('--related-rgb', rgb)
      }

      if (variant.dataset.variant === 'h4' && html.dataset.reduced !== 'on') {
        triggerPerimeterSweep(node)
      }
    })

    node.addEventListener('pointermove', (event) => {
      const rect = node.getBoundingClientRect()
      const x = ((event.clientX - rect.left) / rect.width) * 100
      const y = ((event.clientY - rect.top) / rect.height) * 100
      node.style.setProperty('--pointer-x', `${clamp(x, 0, 100)}%`)
      node.style.setProperty('--pointer-y', `${clamp(y, 0, 100)}%`)

      if (spill && world) {
        const rgb = readNodeRgb(node)
        positionWorldSpill(world, node, spill, rgb)
      }
    })

    node.addEventListener('pointerleave', () => {
      if (world) world.classList.remove('has-hover')
      for (const path of relationPaths) {
        path.classList.remove('is-related')
        path.style.removeProperty('--related-rgb')
      }
    })
  }
}

function readNodeRgb(node) {
  return node.style.getPropertyValue('--node-rgb').trim() || '142, 169, 255'
}

function positionWorldSpill(world, node, spill, rgb) {
  const worldRect = world.getBoundingClientRect()
  const nodeRect = node.getBoundingClientRect()
  const x = nodeRect.left - worldRect.left + nodeRect.width / 2
  const y = nodeRect.top - worldRect.top + nodeRect.height / 2

  spill.style.setProperty('--spill-x', `${x}px`)
  spill.style.setProperty('--spill-y', `${y}px`)
  spill.style.setProperty('--spill-rgb', rgb)
}

function triggerPerimeterSweep(node) {
  const sweep = node.querySelector('.perimeter-sweep')
  if (!sweep) return

  sweep.classList.remove('sweep-active')
  void sweep.offsetWidth
  sweep.classList.add('sweep-active')
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}
