const html = document.documentElement
const grid = document.querySelector('#expanded-grid')

const categories = ['question', 'investigation', 'validation', 'model', 'evaluation']

const categoryMeta = {
  question: {
    glyph: 'Q',
    kind: 'Question / Blocker',
    rgb: '240, 178, 91',
    stripTitle: 'Project question',
    stripDetail: 'Unresolved definition or blocker',
    sceneTitle: 'Prediction moment',
    sceneDetail: 'Eligibility boundary unresolved',
  },
  investigation: {
    glyph: 'I',
    kind: 'Investigation',
    rgb: '103, 218, 194',
    stripTitle: 'Investigation',
    stripDetail: 'Evidence-seeking analytical work',
    sceneTitle: 'Production missingness',
    sceneDetail: 'Investigating live data behavior',
  },
  validation: {
    glyph: 'V',
    kind: 'Validation / Analysis',
    rgb: '142, 169, 255',
    stripTitle: 'Validation work',
    stripDetail: 'Designed analytical procedure',
    sceneTitle: 'Chronological validation',
    sceneDetail: 'Selected analytical work',
  },
  model: {
    glyph: 'M',
    kind: 'Model Work',
    rgb: '233, 132, 122',
    stripTitle: 'Model work',
    stripDetail: 'Baseline or alternative model',
    sceneTitle: 'Baseline logistic model',
    sceneDetail: 'Completed baseline',
  },
  evaluation: {
    glyph: 'E',
    kind: 'Evaluation',
    rgb: '173, 150, 255',
    stripTitle: 'Evaluation work',
    stripDetail: 'Comparison or decision-bearing work',
    sceneTitle: 'Evaluation',
    sceneDetail: 'Downstream comparison',
  },
}

const signatureLightAnchors = {
  w1: {
    question: { side: 'left', anchor: '50%' },
    investigation: { side: 'left', anchor: '50%' },
    validation: { side: 'left', anchor: '50%' },
    model: { side: 'left', anchor: '50%' },
    evaluation: { side: 'left', anchor: '50%' },
  },
  w3: {
    question: { side: 'left', anchor: '50%' },
    investigation: { side: 'left', anchor: '50%' },
    validation: { side: 'left', anchor: '50%' },
    model: { side: 'left', anchor: '50%' },
    evaluation: { side: 'left', anchor: '50%' },
  },
  w4: {
    question: { side: 'left', anchor: '50%' },
    investigation: { side: 'left', anchor: '50%' },
    validation: { side: 'top', anchor: 'calc(12px + 21%)' },
    model: { side: 'bottom', anchor: 'calc(12px + 23%)' },
    evaluation: { side: 'right', anchor: '50%' },
  },
}

const variants = [
  {
    id: 'g0', family: 'glyph', batch: 'Batch A', code: 'G0', baseFrame: 'w1', lightingProfile: 'w1', mark: 'letter',
    title: 'Letter Control',
    description: 'The original Q / I / V / M / E category labels on the stable W1 precision frame.',
    footer: 'Typographic category mark', verdict: 'Control',
  },
  {
    id: 'g1', family: 'glyph', batch: 'Batch A', code: 'G1', baseFrame: 'w1', lightingProfile: 'w1', mark: 'instrument',
    title: 'Instrument Glyph Family',
    description: 'Purpose-built category pictograms using one restrained technical stroke vocabulary.',
    footer: 'P&ID-inspired primitive language', verdict: 'Claude C1',
  },
  {
    id: 'g2', family: 'glyph', batch: 'Batch A', code: 'G2', baseFrame: 'w1', lightingProfile: 'w1', mark: 'rail',
    title: 'Compact Marker Rail',
    description: 'Tiny abstract instrument-code patterns replace letters without requiring illustrated icons.',
    footer: 'Abstract compact coding', verdict: 'Claude C7',
  },
  {
    id: 'g3', family: 'glyph', batch: 'Batch A', code: 'G3', baseFrame: 'w1', lightingProfile: 'w1', mark: 'scientific',
    title: 'Scientific Marker Family',
    description: 'Plot-marker geometry turns category identity into familiar circle, square, triangle, diamond and cross shapes.',
    footer: 'Data-science visual vocabulary', verdict: 'Claude C8',
  },
  {
    id: 's0', family: 'structure', batch: 'Batch B', code: 'S0', baseFrame: 'w3', lightingProfile: 'w3', mark: 'letter',
    title: 'Chamfer Control',
    description: 'The first-round W3 idea: related rounded frames differentiated mainly through corner-chamfer placement.',
    footer: 'Existing silhouette mechanism', verdict: 'W3 control',
  },
  {
    id: 's1', family: 'structure', batch: 'Batch B', code: 'S1', baseFrame: 'w1', lightingProfile: 'w1', mark: 'letter',
    title: 'Structural Topology Family',
    description: 'Different categories receive genuinely different structural motifs rather than the same chamfer move at different corners.',
    footer: 'Topology instead of parameterized chamfers', verdict: 'Claude C2',
  },
  {
    id: 's2', family: 'structure', batch: 'Batch B', code: 'S2', baseFrame: 'w1', lightingProfile: 'w1', mark: 'letter',
    title: 'Aspect & Proportion Family',
    description: 'Very small width and height deltas test whether category-specific information shape can help without breaking scan alignment.',
    footer: 'Deliberately cautious geometry delta', verdict: 'Claude C6',
  },
  {
    id: 's3', family: 'structure', batch: 'Batch B', code: 'S3', baseFrame: 'w1', lightingProfile: 'w1', mark: 'letter',
    title: 'Inner Instrument Architecture',
    description: 'Outer geometry stays stable while small internal structural line motifs carry category identity without pretending to show live data.',
    footer: 'Isolated inner-frame channel', verdict: 'ChatGPT C9',
  },
  {
    id: 'm0', family: 'surface', batch: 'Batch C', code: 'M0', baseFrame: 'w1', lightingProfile: 'w1', mark: 'letter',
    title: 'Plain Surface Control',
    description: 'The W1 material baseline: one consistent dark surface with no category-specific texture.',
    footer: 'No material differentiation', verdict: 'Control',
  },
  {
    id: 'm1', family: 'surface', batch: 'Batch C', code: 'M1', baseFrame: 'w1', lightingProfile: 'w1', mark: 'letter',
    title: 'Material Language Family',
    description: 'Extremely restrained category-specific micro-materials test whether surface language can carry recognition without becoming noise.',
    footer: 'Texture as category channel', verdict: 'Claude C3',
  },
  {
    id: 'i0', family: 'integrated', batch: 'Batch D', code: 'I0', baseFrame: 'w4', lightingProfile: 'w4', mark: 'letter',
    title: 'Current W4 Hybrid Control',
    description: 'The first-round hybrid: restrained silhouette cue, category-specific signature frame and bare-letter glyph.',
    footer: 'Existing integrated candidate', verdict: 'W4 control',
  },
  {
    id: 'i1', family: 'integrated', batch: 'Batch D', code: 'I1', baseFrame: 'w4', lightingProfile: 'w4', mark: 'instrument',
    title: 'W4 + Instrument Glyph',
    description: 'The W4 hybrid keeps its signature geometry but replaces the weak letter channel with purpose-built instrument pictograms.',
    footer: 'Hybrid + technical pictogram', verdict: 'Claude combination',
  },
  {
    id: 'i2', family: 'integrated', batch: 'Batch D', code: 'I2', baseFrame: 'w4', lightingProfile: 'w4', mark: 'scientific',
    title: 'W4 + Scientific Marker',
    description: 'The W4 hybrid keeps its signature geometry while category marks use familiar scientific plot-marker shapes.',
    footer: 'Hybrid + scientific marker', verdict: 'Claude combination',
  },
]

renderVariants()
setupViewControls()
setupInboxLightControls()
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
  article.className = `grammar-variant expanded-variant expanded-${variant.id} variant-${variant.baseFrame}`
  article.dataset.variant = variant.id
  article.dataset.family = variant.family
  article.dataset.lightingProfile = variant.lightingProfile

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
  node.style.setProperty('--node-rgb', meta.rgb)

  const light = signatureLightAnchors[variant.lightingProfile]?.[category] || { side: 'left', anchor: '50%' }
  node.dataset.lightSide = light.side
  node.style.setProperty('--light-anchor', light.anchor)

  node.innerHTML = `
    <span class="rest-spill" aria-hidden="true"></span>
    <span class="rest-light" aria-hidden="true"></span>
    <span class="hover-light" aria-hidden="true"></span>
    <span class="hover-world-light" aria-hidden="true"></span>
    <div class="node-surface">
      <span class="surface-rest-light" aria-hidden="true"></span>
      <span class="material-layer" aria-hidden="true"></span>
      <span class="pointer-light" aria-hidden="true"></span>
      <span class="perimeter-sweep" aria-hidden="true"></span>
      <span class="frame-signature" aria-hidden="true"></span>
      <span class="structure-motif" aria-hidden="true"></span>
      <span class="inner-architecture" aria-hidden="true"></span>
      <div class="node-heading"><span class="category-glyph" aria-hidden="true"></span><span class="unit-kind"></span></div>
      <strong></strong><small></small>
    </div>`

  const glyph = node.querySelector('.category-glyph')
  renderCategoryMark(glyph, variant.mark, category)
  node.querySelector('.unit-kind').textContent = meta.kind
  node.querySelector('strong').textContent = isScene ? meta.sceneTitle : meta.stripTitle
  node.querySelector('small').textContent = isScene ? meta.sceneDetail : meta.stripDetail

  return node
}

function renderCategoryMark(container, mark, category) {
  const meta = categoryMeta[category]
  if (mark === 'letter') {
    container.textContent = meta.glyph
    return
  }

  if (mark === 'instrument') {
    container.classList.add('instrument-glyph')
    container.innerHTML = instrumentGlyph(category)
    return
  }

  if (mark === 'scientific') {
    container.classList.add('scientific-glyph')
    container.innerHTML = scientificGlyph(category)
    return
  }

  if (mark === 'rail') {
    container.classList.add('marker-rail-glyph')
    container.innerHTML = `<span class="marker-rail pattern-${category}"><span></span></span>`
  }
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

function setupInboxLightControls() {
  const buttons = [...document.querySelectorAll('button[data-inbox-light]')]
  const initialMode = html.dataset.inboxLight || 'baseline'
  applyInboxLight(initialMode, buttons)

  for (const button of buttons) {
    button.addEventListener('click', () => applyInboxLight(button.dataset.inboxLight, buttons))
  }
}

function applyInboxLight(mode, buttons) {
  html.dataset.inboxLight = mode
  for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.inboxLight === mode))
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

  for (const variant of document.querySelectorAll('.expanded-variant')) {
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
  for (const variant of document.querySelectorAll('.expanded-variant')) {
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
