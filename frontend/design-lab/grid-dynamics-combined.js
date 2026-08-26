const html = document.documentElement

const intensityCopy = {
  quiet: {
    label: 'Quiet',
    description: 'All ambient mechanisms remain, but with longer gaps and softer presence.',
  },
  balanced: {
    label: 'Balanced',
    description: 'More frequent than the first dynamics round while keeping quiet gaps.',
  },
  lively: {
    label: 'Lively',
    description: 'Noticeably more continuous ambient life without turning the grid into constant motion.',
  },
}

for (const control of document.querySelectorAll('[data-control="intensity"]')) {
  control.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-value]')
    if (!button) return

    for (const candidate of control.querySelectorAll('button[data-value]')) {
      candidate.setAttribute('aria-pressed', String(candidate === button))
    }

    const intensity = button.dataset.value
    html.dataset.intensity = intensity
    updateIntensityCopy(intensity)
  })
}

bindToggle('#ambient-toggle', 'ambient')
bindToggle('#semantic-toggle', 'semantic')
bindToggle('#reduced-toggle', 'reduced')

function bindToggle(selector, datasetKey) {
  const input = document.querySelector(selector)
  if (!input) return

  input.addEventListener('change', () => {
    html.dataset[datasetKey] = input.checked ? 'on' : 'off'
  })
}

function updateIntensityCopy(intensity) {
  const copy = intensityCopy[intensity] ?? intensityCopy.balanced
  const label = document.querySelector('#intensity-label')
  const description = document.querySelector('#intensity-description')

  if (label) label.textContent = copy.label
  if (description) description.textContent = copy.description
}

updateIntensityCopy(html.dataset.intensity)
