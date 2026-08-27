const variants = [
  { id: 'l0', code: 'L0', label: 'Flat Fields', description: 'Six equal fields in a neutral two-column grid. Baseline for hierarchy-free scanning.' },
  { id: 'l1', code: 'L1', label: 'Structured Grid', description: 'A compact field matrix adds subtle grouping while keeping all information equally addressable.' },
  { id: 'l2', code: 'L2', label: 'Narrative Stack', description: 'A top-to-bottom reading path pairs each label with one value, prioritizing linear comprehension over density.' },
  { id: 'l3', code: 'L3', label: 'Summary + Rail', description: 'Primary context stays left while evidence, action and activity form a narrower supporting rail.' },
  { id: 'l4', code: 'L4', label: 'Action First', description: 'Next action receives the strongest internal placement, testing whether expanded work units should be operationally oriented.' },
  { id: 'l5', code: 'L5', label: 'Dependency Path', description: 'Blocking cause, current constraint and next action form a compact process path with supporting context beneath.' },
  { id: 'l6', code: 'L6', label: 'Evidence Center', description: 'Evidence becomes the visual center while purpose, state, cause, action and activity remain peripheral.' },
  { id: 'l7', code: 'L7', label: 'Module Cards', description: 'Each field becomes a small internal module, testing strong chunking against dashboard-like visual fragmentation.' },
  { id: 'l8', code: 'L8', label: 'Balanced Instrument', description: 'Compact metadata, two structured modules and a bottom action strip create a deliberately hierarchical technical composition.' },
]

const payload = [
  ['Purpose', 'Profile production missingness'],
  ['Constraint', 'Blocked by unresolved target definition'],
  ['Evidence', 'Schema + missingness profile'],
  ['Next action', 'Resume after blocker clears'],
  ['Blocking cause', 'Resolve target definition'],
  ['Recent activity', 'Missingness profile generated'],
]

const grid = document.querySelector('#layout-grid')
const controls = document.querySelector('#layout-controls')
const practical = document.querySelector('#practical-expanded')
const summary = document.querySelector('#layout-summary')
const html = document.documentElement

renderGrid()
renderControls()
renderPractical('l0')

function renderGrid() {
  if (!grid) return
  grid.innerHTML = variants.map((variant) => `
    <article class="layout-tile">
      <div class="layout-tile-copy">
        <span>${variant.code}</span>
        <strong>${variant.label}</strong>
        <small>${variant.description}</small>
      </div>
      <div class="layout-stage">
        ${cardMarkup(variant.id)}
      </div>
    </article>
  `).join('')
}

function renderControls() {
  if (!controls) return
  controls.innerHTML = variants.map((variant, index) => `
    <button type="button" data-layout="${variant.id}" aria-pressed="${index === 0 ? 'true' : 'false'}">${variant.code} ${variant.label}</button>
  `).join('')

  for (const button of controls.querySelectorAll('button[data-layout]')) {
    button.addEventListener('click', () => {
      const next = button.dataset.layout || 'l0'
      html.dataset.layoutStyle = next
      for (const candidate of controls.querySelectorAll('button[data-layout]')) {
        candidate.setAttribute('aria-pressed', String(candidate.dataset.layout === next))
      }
      renderPractical(next)
      const variant = variants.find((item) => item.id === next) || variants[0]
      if (summary) summary.textContent = `${variant.code} · ${variant.label}`
    })
  }
}

function renderPractical(style) {
  if (!practical) return
  practical.innerHTML = cardMarkup(style)
}

function cardMarkup(style) {
  return `
    <article class="expanded-card layout-${style}">
      <span class="corner-extra" aria-hidden="true"></span>
      <div class="card-top">
        <span class="card-kind">Investigation</span>
        <span class="priority-bars" aria-hidden="true"><i></i><i></i><i></i></span>
        <span class="disposition-pill">CURRENT</span>
        <div class="card-title">Production missingness</div>
        <div class="card-subtitle">Selected contextual detail · BLOCKED · HIGH attention</div>
      </div>
      <div class="card-detail">
        ${payload.map(([label, value]) => `
          <div class="field">
            <span class="field-label">${label}</span>
            <strong class="field-value">${value}</strong>
          </div>
        `).join('')}
        <span class="blocked-carrier" aria-hidden="true"></span>
      </div>
    </article>
  `
}
