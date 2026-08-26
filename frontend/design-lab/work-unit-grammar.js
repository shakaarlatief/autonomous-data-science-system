const html = document.documentElement
const template = document.querySelector('#node-template')

const categoryMeta = {
  question: {
    glyph: 'Q',
    kind: 'Question / Blocker',
    stripTitle: 'Project question',
    stripDetail: 'Unresolved definition or blocker',
    sceneTitle: 'Prediction moment',
    sceneDetail: 'Eligibility boundary unresolved',
  },
  investigation: {
    glyph: 'I',
    kind: 'Investigation',
    stripTitle: 'Investigation',
    stripDetail: 'Evidence-seeking analytical work',
    sceneTitle: 'Production missingness',
    sceneDetail: 'Investigating live data behavior',
  },
  validation: {
    glyph: 'V',
    kind: 'Validation / Analysis',
    stripTitle: 'Validation work',
    stripDetail: 'Designed analytical procedure',
    sceneTitle: 'Chronological validation',
    sceneDetail: 'Selected analytical work',
  },
  model: {
    glyph: 'M',
    kind: 'Model Work',
    stripTitle: 'Model work',
    stripDetail: 'Baseline or alternative model',
    sceneTitle: 'Baseline logistic model',
    sceneDetail: 'Completed baseline',
  },
  evaluation: {
    glyph: 'E',
    kind: 'Evaluation',
    stripTitle: 'Evaluation work',
    stripDetail: 'Comparison or decision-bearing work',
    sceneTitle: 'Evaluation',
    sceneDetail: 'Downstream comparison',
  },
}

/*
 * Resting light follows both the signature edge and the signature's position
 * along that edge. Expressions mirror the frame-signature geometry in CSS so
 * the light remains attached when the same grammar is rendered at different
 * node widths.
 */
const signatureLightAnchors = {
  w1: {
    question: { side: 'left', anchor: '50%' },
    investigation: { side: 'left', anchor: '50%' },
    validation: { side: 'left', anchor: '50%' },
    model: { side: 'left', anchor: '50%' },
    evaluation: { side: 'left', anchor: '50%' },
  },
  w2: {
    question: { side: 'left', anchor: '50%' },
    investigation: { side: 'left', anchor: '50%' },
    validation: { side: 'top', anchor: 'calc(14px + 23%)' },
    model: { side: 'bottom', anchor: 'calc(14px + 25%)' },
    evaluation: { side: 'right', anchor: '50%' },
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

renderNodes()
setupViewControls()
setupInboxLightControls()
setupReducedMotion()
setupInteractions()
setupAmbientWorlds()

function renderNodes() {
  if (!template) return

  for (const node of document.querySelectorAll('.grammar-node')) {
    const category = Object.keys(categoryMeta).find((name) => node.classList.contains(`category-${name}`))
    if (!category) continue

    const meta = categoryMeta[category]
    const variant = node.closest('.grammar-variant')?.dataset.variant || 'w1'
    const lightAnchor = signatureLightAnchors[variant]?.[category] || { side: 'left', anchor: '50%' }
    const isScene = Boolean(node.closest('.project-scene'))
    const content = template.content.cloneNode(true)

    content.querySelector('.category-glyph').textContent = meta.glyph
    content.querySelector('.unit-kind').textContent = meta.kind
    content.querySelector('strong').textContent = isScene ? meta.sceneTitle : meta.stripTitle
    content.querySelector('small').textContent = isScene ? meta.sceneDetail : meta.stripDetail

    node.dataset.lightSide = lightAnchor.side
    node.style.setProperty('--light-anchor', lightAnchor.anchor)
    node.replaceChildren(content)
  }
}

function setupViewControls() {
  const buttons = [...document.querySelectorAll('[data-view]')]
  const initialView = html.dataset.grammarView || 'strip'

  applyView(initialView, buttons)

  for (const button of buttons) {
    button.addEventListener('click', () => {
      applyView(button.dataset.view, buttons)
    })
  }
}

function applyView(view, buttons) {
  html.dataset.grammarView = view

  for (const candidate of buttons) {
    candidate.setAttribute('aria-pressed', String(candidate.dataset.view === view))
  }

  for (const panel of document.querySelectorAll('[data-panel]')) {
    const isVisible = panel.dataset.panel === view
    panel.hidden = !isVisible
    panel.style.display = isVisible ? '' : 'none'
  }
}

function setupInboxLightControls() {
  const buttons = [...document.querySelectorAll('button[data-inbox-light]')]
  const initialMode = html.dataset.inboxLight || 'baseline'

  applyInboxLight(initialMode, buttons)

  for (const button of buttons) {
    button.addEventListener('click', () => {
      applyInboxLight(button.dataset.inboxLight, buttons)
    })
  }
}

function applyInboxLight(mode, buttons) {
  html.dataset.inboxLight = mode

  for (const candidate of buttons) {
    candidate.setAttribute('aria-pressed', String(candidate.dataset.inboxLight === mode))
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
  for (const variant of document.querySelectorAll('.grammar-variant')) {
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

  worlds.forEach((world) => {
    const currents = [...world.querySelectorAll('.ambient-current')]
    const glints = [...world.querySelectorAll('.ambient-glint')]

    currents.forEach((current, index) => {
      const random = mulberry32(20260826 + index * 117)
      const horizontal = index % 2 === 0
      current.dataset.orientation = horizontal ? 'horizontal' : 'vertical'
      current.style.setProperty('--ambient-position', `${20 * (2 + Math.floor(random() * 12))}px`)
      current.style.setProperty('--ambient-delay', `${-(2 + random() * 7).toFixed(2)}s`)
      current.style.setProperty('--ambient-duration', `${(10 + random() * 5).toFixed(2)}s`)
    })

    glints.forEach((glint, index) => {
      const random = mulberry32(20260910 + index * 223)
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