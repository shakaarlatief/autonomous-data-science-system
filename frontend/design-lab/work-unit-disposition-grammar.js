const html = document.documentElement
const world = document.querySelector('#disposition-world')
const rowsHost = document.querySelector('#disposition-rows')
const encodingSummary = document.querySelector('#encoding-summary')

const dispositions = [
  {
    id: 'active',
    code: 'ACTIVE',
    label: 'Active / Current',
    description: 'Work currently central to the project path.',
    rgb: '102, 181, 255',
  },
  {
    id: 'recommended',
    code: 'NEXT',
    label: 'Recommended / Next',
    description: 'A strong candidate for the next project action.',
    rgb: '177, 151, 255',
  },
  {
    id: 'deferred',
    code: 'DEFER',
    label: 'Deferred',
    description: 'Valid work intentionally postponed for now.',
    rgb: '145, 158, 179',
  },
  {
    id: 'completed',
    code: 'DONE',
    label: 'Completed',
    description: 'Work whose current project obligation is satisfied.',
    rgb: '103, 205, 151',
  },
  {
    id: 'blocked',
    code: 'BLOCKED',
    label: 'Blocked',
    description: 'Work unable to proceed until another condition is resolved.',
    rgb: '237, 112, 105',
  },
  {
    id: 'future',
    code: 'FUTURE',
    label: 'Future / Not yet active',
    description: 'Known possible work outside the current active horizon.',
    rgb: '122, 139, 163',
  },
]

const encodingLabels = {
  p0: 'Neutral control',
  p1: 'Disposition hue',
  p2: 'Explicit disposition tag',
  p3: 'Tonal hierarchy',
  p4: 'State rhythm',
  p5: 'Hue + tag',
  p6: 'Restrained hybrid',
}

renderRows()
setupControls()
setupInteractions()
setupAmbientWorld()
updateControls()

function renderRows() {
  if (!rowsHost) return
  rowsHost.innerHTML = dispositions.map((state, index) => rowMarkup(state, index)).join('')
}

function rowMarkup(state, index) {
  return `
    <article class="disposition-row" data-state="${state.id}" style="--state-rgb:${state.rgb};">
      <div class="disposition-label">
        <span>P${index}</span>
        <strong>${state.label}</strong>
        <small>${state.description}</small>
      </div>

      <div class="grammar-node custom-node category-investigation disposition-node" data-light-side="left" style="--node-rgb:103, 218, 194; --light-anchor:50%;">
        <span class="rest-spill" aria-hidden="true"></span>
        <span class="rest-light" aria-hidden="true"></span>
        <span class="hover-light" aria-hidden="true"></span>
        <span class="hover-world-light" aria-hidden="true"></span>
        <span class="disposition-state-outline" aria-hidden="true"></span>
        <div class="node-surface">
          <span class="surface-rest-light" aria-hidden="true"></span>
          <span class="custom-material-layer" aria-hidden="true"></span>
          <span class="custom-lumen-layer" aria-hidden="true"></span>
          <span class="pointer-light" aria-hidden="true"></span>
          <span class="perimeter-sweep" aria-hidden="true"></span>
          <span class="frame-signature" aria-hidden="true"></span>
          <span class="disposition-state-rhythm" aria-hidden="true"></span>
          <span class="disposition-state-badge" aria-hidden="true">${state.code}</span>
          <div class="node-heading">
            <span class="category-glyph" aria-hidden="true">
              <svg viewBox="0 0 16 16"><rect x="4" y="4" width="8" height="8" rx="0.7"/></svg>
            </span>
            <span class="unit-kind">Investigation</span>
          </div>
          <strong>Production missingness</strong>
          <small>Investigating live data behavior</small>
        </div>
      </div>
    </article>
  `
}

function setupControls() {
  for (const button of document.querySelectorAll('button[data-encoding]')) {
    button.addEventListener('click', () => {
      html.dataset.dispositionEncoding = button.dataset.encoding
      updateControls()
    })
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  reducedToggle?.addEventListener('change', () => {
    html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
  })
}

function updateControls() {
  for (const button of document.querySelectorAll('button[data-encoding]')) {
    button.setAttribute('aria-pressed', String(button.dataset.encoding === html.dataset.dispositionEncoding))
  }

  const reducedToggle = document.querySelector('#reduced-toggle')
  if (reducedToggle) reducedToggle.checked = html.dataset.reduced === 'on'

  if (encodingSummary) {
    encodingSummary.textContent = encodingLabels[html.dataset.dispositionEncoding] || encodingLabels.p0
  }
}

function setupInteractions() {
  for (const row of document.querySelectorAll('.disposition-row')) {
    const node = row.querySelector('.disposition-node')
    if (!node) continue

    node.addEventListener('pointerenter', () => {
      row.classList.add('is-hovered')
      if (html.dataset.reduced !== 'on') triggerPerimeterSweep(node)
    })

    node.addEventListener('pointermove', (event) => {
      const surface = node.querySelector('.node-surface')
      if (!surface) return

      const rect = surface.getBoundingClientRect()
      const x = ((event.clientX - rect.left) / rect.width) * 100
      const y = ((event.clientY - rect.top) / rect.height) * 100
      node.style.setProperty('--pointer-x', `${clamp(x, 0, 100)}%`)
      node.style.setProperty('--pointer-y', `${clamp(y, 0, 100)}%`)
    })

    node.addEventListener('pointerleave', () => {
      row.classList.remove('is-hovered')
    })
  }
}

function setupAmbientWorld() {
  if (!world) return

  const currents = [...world.querySelectorAll('.ambient-current')]
  const glints = [...world.querySelectorAll('.ambient-glint')]

  currents.forEach((current, index) => {
    const random = mulberry32(20260827 + index * 173)
    const horizontal = index % 2 === 0
    current.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
    current.style.setProperty('--ambient-position', `${20 * (2 + Math.floor(random() * 24))}px`)
    current.style.setProperty('--ambient-delay', `${-(2 + random() * 7).toFixed(2)}s`)
    current.style.setProperty('--ambient-duration', `${(10 + random() * 5).toFixed(2)}s`)
  })

  glints.forEach((glint, index) => {
    const random = mulberry32(20260917 + index * 251)
    glint.style.left = `${100 * (1 + Math.floor(random() * 11))}px`
    glint.style.top = `${100 * (1 + Math.floor(random() * 7))}px`
    glint.style.setProperty('--glint-delay', `${-(1 + random() * 6).toFixed(2)}s`)
  })
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

function mulberry32(seed) {
  return function random() {
    let value = (seed += 0x6d2b79f5)
    value = Math.imul(value ^ (value >>> 15), value | 1)
    value ^= value + Math.imul(value ^ (value >>> 7), value | 61)
    return ((value ^ (value >>> 14)) >>> 0) / 4294967296
  }
}
