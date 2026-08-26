const variants = [
  {
    code: 'D1',
    name: 'Quiet Current',
    className: 'variant-d1',
    summary: 'One or two slow neutral light traces travel along major grid lines with long quiet gaps between passes.',
    tradeoff: 'Most literal version of the requested “light moving through the grid” idea · risk: can feel event-like if too bright',
    note: 'Sparse travelling line segments',
  },
  {
    code: 'D2',
    name: 'Intersection Glints',
    className: 'variant-d2',
    summary: 'Rare grid intersections briefly brighten and fade. Adds micro-detail without persistent directional movement.',
    tradeoff: 'Lowest-motion decorative option · risk: may be too subtle to materially improve the world',
    note: 'Rare non-synchronized glints',
  },
  {
    code: 'D3',
    name: 'Ambient Drift',
    className: 'variant-d3',
    summary: 'Broad low-opacity blue-white light fields drift slowly beneath the grid, adding atmosphere rather than event-like motion.',
    tradeoff: 'Strongest depth/atmosphere treatment · risk: can become generic glow if overused',
    note: 'Slow diffuse sub-grid movement',
  },
  {
    code: 'D4',
    name: 'Restrained Hybrid',
    className: 'variant-d4',
    summary: 'Combines one sparse current, occasional glints, and very soft drift at lower individual intensities.',
    tradeoff: 'Highest visual richness while remaining intentionally restrained · risk: combined mechanisms may still exceed the motion budget',
    note: 'Trace + glint + drift, all reduced',
  },
]

const html = document.documentElement
const variantContainer = document.querySelector('#variants')
const template = document.querySelector('#variant-template')

if (!variantContainer || !template) {
  throw new Error('Grid-dynamics design lab could not find required DOM templates.')
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

const ambientToggle = document.querySelector('#ambient-toggle')
const semanticToggle = document.querySelector('#semantic-toggle')
const reducedToggle = document.querySelector('#reduced-toggle')

ambientToggle?.addEventListener('change', () => {
  html.dataset.ambient = ambientToggle.checked ? 'on' : 'off'
})

semanticToggle?.addEventListener('change', () => {
  html.dataset.semantic = semanticToggle.checked ? 'on' : 'off'
})

reducedToggle?.addEventListener('change', () => {
  html.dataset.reduced = reducedToggle.checked ? 'on' : 'off'
})

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return

  document.querySelectorAll('.variant-card.is-focused').forEach((card) => {
    card.classList.remove('is-focused')
    card.querySelector('.focus-button').textContent = 'Focus variant'
  })
})
