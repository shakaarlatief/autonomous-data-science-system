const visualSystems = [
  {
    id: 'quiet-graphite',
    name: 'Quiet Graphite',
    note: 'Neutral graphite + restrained mint signal',
    thesis: 'Document-like ADS responses, compact user prompts, semantic color reserved for project meaning.'
  },
  {
    id: 'deep-navy',
    name: 'Deep Navy',
    note: 'Cool analytical navy + cyan depth',
    thesis: 'More technical spatial depth without neon spectacle; references and focus use cool cyan.'
  },
  {
    id: 'warm-slate',
    name: 'Warm Slate',
    note: 'Dark research desk + warm amber',
    thesis: 'A calmer research-reading atmosphere with warmer surfaces and less software-blue visual pressure.'
  },
  {
    id: 'monochrome-signal',
    name: 'Monochrome Signal',
    note: 'Near-monochrome + one semantic signal',
    thesis: 'Maximum restraint. Most decoration disappears so the transcript and structured project references dominate.'
  },
  {
    id: 'violet-ink',
    name: 'Violet Ink',
    note: 'Dark ink + muted violet intelligence layer',
    thesis: 'A more distinctive ADS identity while keeping project-category colors semantically independent.'
  },
  {
    id: 'editorial-dark',
    name: 'Editorial Dark',
    note: 'Harder editorial geometry + minimal cards',
    thesis: 'Treat the conversation as a professional technical document rather than a chat app; bubbles largely disappear.'
  }
]

const html = document.documentElement
const systemStrip = document.querySelector('#system-strip')
const visualSelect = document.querySelector('#visual-select')
const densitySelect = document.querySelector('#density-select')
const contextToggle = document.querySelector('#context-toggle')
const contextClose = document.querySelector('#context-close')
const stage = document.querySelector('.conversation-stage')
const transcript = document.querySelector('#transcript-scroll')

let currentVisual = 'quiet-graphite'

renderVisualControls()
bindControls()
restoreScroll()

function renderVisualControls() {
  if (visualSelect) {
    visualSelect.innerHTML = visualSystems.map((system) => `<option value="${system.id}">${system.name}</option>`).join('')
    visualSelect.value = currentVisual
  }

  if (systemStrip) {
    systemStrip.innerHTML = visualSystems.map((system) => `
      <button class="system-chip" type="button" data-visual-system="${system.id}" aria-pressed="${system.id === currentVisual}">
        <strong>${system.name}</strong>
        <small>${system.note}</small>
      </button>
    `).join('')
  }
}

function bindControls() {
  visualSelect?.addEventListener('change', () => setVisual(visualSelect.value))
  densitySelect?.addEventListener('change', () => {
    html.dataset.density = densitySelect.value
  })

  systemStrip?.addEventListener('click', (event) => {
    const button = event.target.closest('[data-visual-system]')
    if (!button) return
    setVisual(button.dataset.visualSystem)
  })

  contextToggle?.addEventListener('click', () => {
    stage?.classList.toggle('context-hidden')
  })

  contextClose?.addEventListener('click', () => {
    stage?.classList.add('context-hidden')
  })

  transcript?.addEventListener('scroll', () => {
    sessionStorage.setItem('ads-conversation-study-scroll', String(transcript.scrollTop))
  })

  document.addEventListener('keydown', (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault()
      document.querySelector('.search-box')?.focus()
    }

    if (event.key === 'Escape' && stage?.classList.contains('context-hidden') === false) {
      stage.classList.add('context-hidden')
    }
  })
}

function setVisual(id) {
  if (!visualSystems.some((system) => system.id === id)) return
  currentVisual = id
  html.dataset.visual = id
  if (visualSelect) visualSelect.value = id

  for (const button of document.querySelectorAll('[data-visual-system]')) {
    button.setAttribute('aria-pressed', String(button.dataset.visualSystem === id))
  }
}

function restoreScroll() {
  if (!transcript) return
  const saved = Number(sessionStorage.getItem('ads-conversation-study-scroll'))
  if (Number.isFinite(saved) && saved > 0) transcript.scrollTop = saved
}
