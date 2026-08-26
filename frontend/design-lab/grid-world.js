const variants = [
  {
    code: 'G1',
    name: 'Precision Lines',
    className: 'variant-g1',
    summary: 'Fine technical minor lines with stronger major divisions. Calm, explicit orientation with no decorative activity treatment.',
    tradeoff: 'Best orientation candidate · risk: conventional / slightly busier at close scale',
    note: 'Major/minor Cartesian hierarchy',
  },
  {
    code: 'G2',
    name: 'Dot Matrix',
    className: 'variant-g2',
    summary: 'Low-noise dot field with sparse stronger anchors. Prioritizes content legibility while retaining a clear spatial coordinate substrate.',
    tradeoff: 'Lowest continuous-line noise · risk: weaker directional structure',
    note: 'Fine dots + sparse anchor dots',
  },
  {
    code: 'G3',
    name: 'Cross Lattice',
    className: 'variant-g3',
    summary: 'Sparse intersection marks create a more distinctive technical world without filling the canvas with continuous lines.',
    tradeoff: 'Distinctive spatial identity · risk: stylization may exceed utility',
    note: 'Sparse cross/intersection rhythm',
  },
  {
    code: 'G4',
    name: 'Adaptive Hybrid',
    className: 'variant-g4',
    summary: 'Scale-aware major/minor hierarchy plus localized activity response around genuinely active work. Quiet when project state is settled.',
    tradeoff: 'Most ADS-specific behavior · risk: activity field may feel ornamental',
    note: 'Scale-aware lines + bounded local activity',
  },
]

const scaleLabels = {
  project: 'Project scale · 60%',
  work: 'Work scale · 85%',
  inspection: 'Inspection scale · 100%',
}

const html = document.documentElement
const variantContainer = document.querySelector('#variants')
const template = document.querySelector('#variant-template')

if (!variantContainer || !template) {
  throw new Error('Grid-world design lab could not find required DOM templates.')
}

for (const variant of variants) {
  const fragment = template.content.cloneNode(true)
  const card = fragment.querySelector('.variant-card')
  const code = fragment.querySelector('.variant-code')
  const name = fragment.querySelector('.variant-name')
  const summary = fragment.querySelector('.variant-summary')
  const note = fragment.querySelector('.world-note')
  const tradeoff = fragment.querySelector('.tradeoff')
  const focusButton = fragment.querySelector('.focus-button')

  card.classList.add(variant.className)
  card.dataset.variant = variant.code
  code.textContent = variant.code
  name.textContent = variant.name
  summary.textContent = variant.summary
  note.textContent = variant.note
  tradeoff.textContent = variant.tradeoff

  focusButton.addEventListener('click', () => {
    const shouldFocus = !card.classList.contains('is-focused')
    document.querySelectorAll('.variant-card.is-focused').forEach((item) => {
      item.classList.remove('is-focused')
      item.querySelector('.focus-button').textContent = 'Focus variant'
    })

    if (shouldFocus) {
      card.classList.add('is-focused')
      focusButton.textContent = 'Exit focus'
    }
  })

  variantContainer.appendChild(fragment)
}

for (const control of document.querySelectorAll('[data-control]')) {
  const controlName = control.dataset.control

  control.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-value]')
    if (!button) return

    for (const candidate of control.querySelectorAll('button[data-value]')) {
      candidate.setAttribute('aria-pressed', String(candidate === button))
    }

    html.dataset[controlName] = button.dataset.value

    if (controlName === 'scale') {
      updateScaleLabels(button.dataset.value)
    }
  })
}

const contentToggle = document.querySelector('#content-toggle')
const activityToggle = document.querySelector('#activity-toggle')

contentToggle?.addEventListener('change', () => {
  html.dataset.content = contentToggle.checked ? 'on' : 'off'
})

activityToggle?.addEventListener('change', () => {
  html.dataset.activity = activityToggle.checked ? 'on' : 'off'
})

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return

  document.querySelectorAll('.variant-card.is-focused').forEach((card) => {
    card.classList.remove('is-focused')
    card.querySelector('.focus-button').textContent = 'Focus variant'
  })
})

function updateScaleLabels(scale) {
  const label = scaleLabels[scale] ?? scaleLabels.work
  document.querySelectorAll('.scale-readout').forEach((element) => {
    element.textContent = label
  })
}

updateScaleLabels(html.dataset.scale)
