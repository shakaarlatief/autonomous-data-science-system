const html = document.documentElement
const grid = document.querySelector('#focused-grid')

const categories = ['question', 'investigation', 'validation', 'model', 'evaluation']

const categoryMeta = {
  question: {
    kind: 'Question / Blocker',
    rgb: '240, 178, 91',
    stripTitle: 'Project question',
    stripDetail: 'Unresolved definition or blocker',
    sceneTitle: 'Prediction moment',
    sceneDetail: 'Eligibility boundary unresolved',
  },
  investigation: {
    kind: 'Investigation',
    rgb: '103, 218, 194',
    stripTitle: 'Investigation',
    stripDetail: 'Evidence-seeking analytical work',
    sceneTitle: 'Production missingness',
    sceneDetail: 'Investigating live data behavior',
  },
  validation: {
    kind: 'Validation / Analysis',
    rgb: '142, 169, 255',
    stripTitle: 'Validation work',
    stripDetail: 'Designed analytical procedure',
    sceneTitle: 'Chronological validation',
    sceneDetail: 'Selected analytical work',
  },
  model: {
    kind: 'Model Work',
    rgb: '233, 132, 122',
    stripTitle: 'Model work',
    stripDetail: 'Baseline or alternative model',
    sceneTitle: 'Baseline logistic model',
    sceneDetail: 'Completed baseline',
  },
  evaluation: {
    kind: 'Evaluation',
    rgb: '173, 150, 255',
    stripTitle: 'Evaluation work',
    stripDetail: 'Comparison or decision-bearing work',
    sceneTitle: 'Evaluation',
    sceneDetail: 'Downstream comparison',
  },
}

const variants = [
  {
    id: 'f0', family: 'control', batch: 'A · Marker baseline', code: 'F0', mark: 'scientific', classes: [],
    title: 'Scientific Marker Control',
    description: 'The current leading category-mark language on a clean stable W1 frame, with Reduced in-box light held as the preferred control.',
    footer: 'Circle · square · triangle · diamond · plus', verdict: 'Leading control',
  },
  {
    id: 'f1', family: 'control', batch: 'C · Shape baseline', code: 'F1', mark: 'scientific', classes: ['upper-right-control'],
    title: 'Upper-right Cut Control',
    description: 'The upper-right cut the human review explicitly liked is applied consistently to every category so its general product quality can be judged independently of category-specific shape variation.',
    footer: 'Stable left reading edge · one preferred cut', verdict: 'Human-positive probe',
  },
  {
    id: 'f2', family: 'material', batch: 'B · Material', code: 'F2', mark: 'scientific', classes: ['has-material'],
    title: 'Scientific Marker + M1 Material',
    description: 'The leading marker language is combined with the restrained M1 micro-material family that received strong positive human feedback.',
    footer: 'Texture as secondary category channel', verdict: 'Preferred mechanism combination',
  },
  {
    id: 'f3', family: 'material', batch: 'B · Micro-lumen', code: 'F3', mark: 'scientific', classes: ['has-lumen'],
    title: 'Scientific Marker + Micro-Lumen',
    description: 'Evaluation’s especially attractive internal light streak is generalized into a restrained family of category-specific micro-light events while global H4 rest light stays Reduced.',
    footer: 'Evaluation-inspired internal light language', verdict: 'New refinement',
  },
  {
    id: 'f4', family: 'shape', batch: 'C · True shapes', code: 'F4', mark: 'scientific', classes: ['true-shape-family'],
    title: 'True Shape Family',
    description: 'Each category receives a genuinely different overall silhouette rather than a repeated chamfer move. The full left edge remains stable to protect reading and scanning.',
    footer: 'Different top/right/bottom topology · left edge held', verdict: 'New shape experiment',
  },
  {
    id: 'f5', family: 'integrated', batch: 'D · Integrated', code: 'F5', mark: 'scientific', classes: ['true-shape-family', 'has-material', 'focused-integrated'],
    title: 'True Shape + M1 Material',
    description: 'The strongest existing micro-material signal is layered onto the true-shape family to test whether two category channels reinforce one another or become excessive.',
    footer: 'Shape + marker + restrained material', verdict: 'Integrated candidate',
  },
  {
    id: 'f6', family: 'integrated', batch: 'D · Integrated', code: 'F6', mark: 'scientific', classes: ['true-shape-family', 'has-lumen', 'focused-integrated'],
    title: 'True Shape + Micro-Lumen',
    description: 'Genuinely different silhouettes combine with the Evaluation-inspired internal light language while Reduced H4 remains the ambient control.',
    footer: 'Shape + marker + internal micro-light', verdict: 'Integrated candidate',
  },
  {
    id: 'f7', family: 'control', batch: 'A · Comparator', code: 'F7', mark: 'instrument', classes: [],
    title: 'Instrument Glyph Comparator',
    description: 'G1 remains alive only as a secondary comparator. It shares the same clean frame and Reduced light so the human can judge whether bespoke pictograms offer anything beyond scientific markers.',
    footer: 'Purpose-built technical pictograms', verdict: 'Secondary comparator',
  },
]

renderVariants()
setupViewControls()
setupFamilyControls()
setupReducedMotion()
setupInteractions()
setupAmbientWorlds()

function renderVariants() {
  if (!grid) return

  const fragment = document.createDocumentFragment()
  for (const variant of variants) fragment.appendChild(buildVariant(variant))
  grid.replaceChildren(fragment)
}

function buildVariant(variant) {
  const article = document.createElement('article')
  article.className = ['grammar-variant', 'focused-variant', `focused-${variant.id}`, 'variant-w1', ...variant.classes].join(' ')
  article.dataset.variant = variant.id
  article.dataset.family = variant.family

  const header = document.createElement('header')
  header.className = 'variant-header'
  header.dataset.batchLabel = variant.batch
  header.innerHTML = `<div><span class="variant-code">${variant.code}</span><h2>${variant.title}</h2></div><p>${variant.description}</p>`

  const world = document.createElement('div')
  world.className = 'grammar-world'
  world.innerHTML = worldBackgroundMarkup()

  const strip = document.createElement('div')
  strip.className = 'category-strip'
  strip.dataset.panel = 'strip'
  for (const category of categories) strip.appendChild(buildNode(variant, category, false))

  const scene = document.createElement('div')
  scene.className = 'project-scene'
  scene.dataset.panel = 'scene'
  scene.hidden = true
  scene.innerHTML = relationMarkup()
  for (const category of categories) scene.appendChild(buildNode(variant, category, true))

  world.append(strip, scene)

  const footer = document.createElement('footer')
  footer.className = 'variant-footer'
  footer.innerHTML = `<span>${variant.footer}</span><strong>${variant.verdict}</strong>`

  article.append(header, world, footer)
  return article
}

function buildNode(variant, category, isScene) {
  const meta = categoryMeta[category]
  const node = document.createElement('div')
  node.className = `grammar-node category-${category}${isScene ? ` scene-${category[0]}` : ''}`
  node.dataset.node = category[0]
  node.dataset.lightSide = 'left'
  node.style.setProperty('--light-anchor', '50%')
  node.style.setProperty('--node-rgb', meta.rgb)

  node.innerHTML = `
    <span class="rest-spill" aria-hidden="true"></span>
    <span class="rest-light" aria-hidden="true"></span>
    <span class="hover-light" aria-hidden="true"></span>
    <span class="hover-world-light" aria-hidden="true"></span>
    <div class="node-surface">
      <span class="surface-rest-light" aria-hidden="true"></span>
      <span class="focused-material-layer" aria-hidden="true"></span>
      <span class="focused-lumen-layer" aria-hidden="true"></span>
      <span class="pointer-light" aria-hidden="true"></span>
      <span class="perimeter-sweep" aria-hidden="true"></span>
      <span class="frame-signature" aria-hidden="true"></span>
      <div class="node-heading"><span class="category-glyph" aria-hidden="true"></span><span class="unit-kind"></span></div>
      <strong></strong><small></small>
    </div>`

  renderCategoryMark(node.querySelector('.category-glyph'), variant.mark, category)
  node.querySelector('.unit-kind').textContent = meta.kind
  node.querySelector('strong').textContent = isScene ? meta.sceneTitle : meta.stripTitle
  node.querySelector('small').textContent = isScene ? meta.sceneDetail : meta.stripDetail

  return node
}

function renderCategoryMark(container, mark, category) {
  if (mark === 'instrument') {
    container.classList.add('focused-instrument')
    container.innerHTML = instrumentGlyph(category)
    return
  }

  container.classList.add('focused-scientific')
  container.innerHTML = scientificGlyph(category)
}

function scientificGlyph(category) {
  const glyphs = {
    question: `<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="4.1"/></svg>`,
    investigation: `<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="4" y="4" width="8" height="8" rx="0.7"/></svg>`,
    validation: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3.3 12.6 12H3.4z"/></svg>`,
    model: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="m8 2.9 5.1 5.1L8 13.1 2.9 8z"/></svg>`,
    evaluation: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2.6v10.8M2.6 8h10.8"/></svg>`,
  }
  return glyphs[category]
}

function instrumentGlyph(category) {
  const glyphs = {
    question: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 4.5h6.5l2.5 2.5v4.5H6l-3-3z"/><path d="M9.5 4.5v2.7h2.5"/></svg>`,
    investigation: `<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.7" cy="6.7" r="3.7"/><path d="m9.5 9.5 3.2 3.2"/><path d="M5.2 6.7h3"/></svg>`,
    validation: `<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="2.6" y="2.6" width="10.8" height="10.8" rx="1.5"/><path d="m5 8 2 2 4-4"/></svg>`,
    model: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 5.2 8 2.8l5 2.4-5 2.4z"/><path d="m3 8.1 5 2.4 5-2.4"/><path d="m3 10.8 5 2.4 5-2.4"/></svg>`,
    evaluation: `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.8 4.3h10.4M2.8 11.7h10.4"/><circle cx="6" cy="4.3" r="1.6"/><circle cx="10" cy="11.7" r="1.6"/></svg>`,
  }
  return glyphs[category]
}

function worldBackgroundMarkup() {
  return `
    <div class="major-grid" aria-hidden="true"></div>
    <div class="ambient-drift" aria-hidden="true"></div>
    <span class="ambient-current current-a" aria-hidden="true"></span>
    <span class="ambient-current current-b" aria-hidden="true"></span>
    <span class="ambient-glint glint-a" aria-hidden="true"></span>
    <span class="ambient-glint glint-b" aria-hidden="true"></span>`
}

function relationMarkup() {
  return `
    <svg class="grammar-relations" viewBox="0 0 1000 390" preserveAspectRatio="none" aria-hidden="true">
      <path data-link="q-i" d="M214 220 C310 220, 300 120, 392 120" />
      <path data-link="i-v" d="M545 120 C625 120, 610 224, 700 224" />
      <path data-link="v-m" d="M845 224 C900 224, 875 115, 940 115" />
      <path data-link="m-e" d="M940 160 C930 270, 835 300, 775 318" />
    </svg>`
}

function setupViewControls() {
  const buttons = [...document.querySelectorAll('button[data-view]')]
  const initialView = html.dataset.grammarView || 'strip'
  applyView(initialView, buttons)

  for (const button of buttons) {
    button.addEventListener('click', () => applyView(button.dataset.view, buttons))
  }
}

function applyView(view, buttons) {
  html.dataset.grammarView = view
  for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.view === view))

  for (const panel of document.querySelectorAll('[data-panel]')) {
    const visible = panel.dataset.panel === view
    panel.hidden = !visible
    panel.style.display = visible ? '' : 'none'
  }
}

function setupFamilyControls() {
  const buttons = [...document.querySelectorAll('button[data-family-filter]')]
  const initialFamily = html.dataset.family || 'all'
  applyFamily(initialFamily, buttons)

  for (const button of buttons) {
    button.addEventListener('click', () => applyFamily(button.dataset.familyFilter, buttons))
  }
}

function applyFamily(family, buttons) {
  html.dataset.family = family
  for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.familyFilter === family))

  for (const variant of document.querySelectorAll('.focused-variant')) {
    variant.dataset.filtered = String(family !== 'all' && variant.dataset.family !== family)
  }
}

function setupReducedMotion() {
  const toggle = document.querySelector('#reduced-toggle')
  if (!toggle) return
  toggle.addEventListener('change', () => {
    html.dataset.reduced = toggle.checked ? 'on' : 'off'
  })
}

function setupInteractions() {
  for (const variant of document.querySelectorAll('.focused-variant')) {
    const relationPaths = [...variant.querySelectorAll('.grammar-relations path')]

    for (const node of variant.querySelectorAll('.grammar-node')) {
      node.addEventListener('pointerenter', () => {
        const nodeId = node.dataset.node
        const rgb = readNodeRgb(node)

        for (const path of relationPaths) {
          const linkedNodes = path.dataset.link?.split('-') ?? []
          const isRelated = linkedNodes.includes(nodeId) && !path.closest('[hidden]')
          path.classList.toggle('is-related', isRelated)
          if (isRelated) path.style.setProperty('--related-rgb', rgb)
        }

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
        for (const path of relationPaths) {
          path.classList.remove('is-related')
          path.style.removeProperty('--related-rgb')
        }
      })
    }
  }
}

function setupAmbientWorlds() {
  const worlds = [...document.querySelectorAll('.grammar-world')]
  worlds.forEach((world, worldIndex) => {
    const currents = [...world.querySelectorAll('.ambient-current')]
    const glints = [...world.querySelectorAll('.ambient-glint')]

    currents.forEach((current, index) => {
      const random = mulberry32(20260826 + worldIndex * 311 + index * 117)
      const horizontal = index % 2 === 0
      current.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
      current.style.setProperty('--ambient-position', `${20 * (2 + Math.floor(random() * 12))}px`)
      current.style.setProperty('--ambient-delay', `${-(2 + random() * 7).toFixed(2)}s`)
      current.style.setProperty('--ambient-duration', `${(10 + random() * 5).toFixed(2)}s`)
    })

    glints.forEach((glint, index) => {
      const random = mulberry32(20260910 + worldIndex * 401 + index * 223)
      glint.style.left = `${100 * (1 + Math.floor(random() * 5))}px`
      glint.style.top = `${100 * (1 + Math.floor(random() * 2))}px`
      glint.style.setProperty('--glint-delay', `${-(1 + random() * 6).toFixed(2)}s`)
    })
  })
}

function readNodeRgb(node) {
  return node.style.getPropertyValue('--node-rgb').trim() || '142, 169, 255'
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
