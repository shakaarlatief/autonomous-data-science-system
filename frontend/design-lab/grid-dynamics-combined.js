const html = document.documentElement
const world = document.querySelector('#combined-world')
const runtimeLayer = document.querySelector('#ambient-runtime-layer')

const GRID_STEP = 20

const intensityCopy = {
  quiet: {
    label: 'Quiet',
    description: 'Randomized currents and corner glints remain present, but with long calm gaps.',
  },
  balanced: {
    label: 'Balanced',
    description: 'Randomized currents and corner glints appear across the full grid with moderate cadence.',
  },
  lively: {
    label: 'Lively',
    description: 'Frequent randomized currents, corner glints and drifting light keep the grid visibly alive.',
  },
}

const intensityConfig = {
  quiet: {
    currentGap: [4200, 7600],
    glintGap: [2400, 4600],
    driftGap: [9000, 14000],
    currentDuration: [5200, 7600],
    glintDuration: [1300, 2000],
    driftDuration: [19000, 28000],
    currentPeak: [0.46, 0.64],
    glintPeak: [0.58, 0.78],
    driftOpacity: [0.10, 0.18],
    maxCurrents: 2,
    maxGlints: 3,
    maxDrifts: 2,
  },
  balanced: {
    currentGap: [1900, 3600],
    glintGap: [1100, 2300],
    driftGap: [6200, 9600],
    currentDuration: [4600, 6800],
    glintDuration: [1100, 1750],
    driftDuration: [17000, 25000],
    currentPeak: [0.54, 0.72],
    glintPeak: [0.66, 0.88],
    driftOpacity: [0.14, 0.24],
    maxCurrents: 3,
    maxGlints: 5,
    maxDrifts: 3,
  },
  lively: {
    currentGap: [700, 1650],
    glintGap: [450, 1100],
    driftGap: [3600, 6200],
    currentDuration: [4000, 6100],
    glintDuration: [900, 1500],
    driftDuration: [15000, 22000],
    currentPeak: [0.60, 0.80],
    glintPeak: [0.72, 0.96],
    driftOpacity: [0.18, 0.30],
    maxCurrents: 5,
    maxGlints: 8,
    maxDrifts: 4,
  },
}

const timers = {
  current: null,
  glint: null,
  drift: null,
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
    restartAmbientEngine()
  })
}

bindToggle('#ambient-toggle', 'ambient', restartAmbientEngine)
bindToggle('#semantic-toggle', 'semantic')
bindToggle('#reduced-toggle', 'reduced', restartAmbientEngine)

function bindToggle(selector, datasetKey, afterChange) {
  const input = document.querySelector(selector)
  if (!input) return

  input.addEventListener('change', () => {
    html.dataset[datasetKey] = input.checked ? 'on' : 'off'
    afterChange?.()
  })
}

function updateIntensityCopy(intensity) {
  const copy = intensityCopy[intensity] ?? intensityCopy.balanced
  const label = document.querySelector('#intensity-label')
  const description = document.querySelector('#intensity-description')

  if (label) label.textContent = copy.label
  if (description) description.textContent = copy.description
}

function currentConfig() {
  return intensityConfig[html.dataset.intensity] ?? intensityConfig.balanced
}

function ambientEnabled() {
  return html.dataset.ambient === 'on' && html.dataset.reduced !== 'on'
}

function restartAmbientEngine() {
  for (const key of Object.keys(timers)) {
    clearTimeout(timers[key])
    timers[key] = null
  }

  runtimeLayer?.replaceChildren()

  if (!ambientEnabled() || !world || !runtimeLayer) return

  scheduleCurrent(true)
  scheduleGlint(true)
  scheduleDrift(true)
}

function scheduleCurrent(immediate = false) {
  if (!ambientEnabled()) return
  const config = currentConfig()
  const delay = immediate ? randomBetween(120, 650) : randomBetween(...config.currentGap)
  timers.current = setTimeout(() => {
    if (runtimeLayer.querySelectorAll('.runtime-current').length < config.maxCurrents) {
      spawnCurrent(config)
    }
    scheduleCurrent()
  }, delay)
}

function scheduleGlint(immediate = false) {
  if (!ambientEnabled()) return
  const config = currentConfig()
  const delay = immediate ? randomBetween(250, 900) : randomBetween(...config.glintGap)
  timers.glint = setTimeout(() => {
    if (runtimeLayer.querySelectorAll('.runtime-glint').length < config.maxGlints) {
      spawnGlint(config)
    }
    scheduleGlint()
  }, delay)
}

function scheduleDrift(immediate = false) {
  if (!ambientEnabled()) return
  const config = currentConfig()
  const delay = immediate ? randomBetween(200, 1200) : randomBetween(...config.driftGap)
  timers.drift = setTimeout(() => {
    if (runtimeLayer.querySelectorAll('.runtime-drift').length < config.maxDrifts) {
      spawnDrift(config)
    }
    scheduleDrift()
  }, delay)
}

function spawnCurrent(config) {
  const rect = world.getBoundingClientRect()
  const horizontal = Math.random() < 0.52
  const element = document.createElement('span')
  const duration = randomBetween(...config.currentDuration)
  const peak = randomBetween(...config.currentPeak)
  const length = horizontal ? randomBetween(150, 280) : randomBetween(130, 240)

  element.className = `ambient-trace runtime-current ${horizontal ? 'trace-h' : 'trace-v'}`
  element.style.setProperty('--duration', `${duration}ms`)
  element.style.setProperty('--peak', peak.toFixed(2))

  if (horizontal) {
    const y = snapToGrid(randomBetween(GRID_STEP, rect.height - GRID_STEP))
    const direction = Math.random() < 0.5 ? 1 : -1
    const x = direction > 0
      ? randomBetween(-length * 0.6, rect.width * 0.72)
      : randomBetween(rect.width * 0.28, rect.width + length * 0.2)
    const travel = randomBetween(rect.width * 0.32, rect.width * 0.72) * direction

    element.style.width = `${length}px`
    element.style.left = `${x}px`
    element.style.top = `${y}px`
    element.style.setProperty('--dx', `${travel}px`)
    element.style.setProperty('--dy', '0px')
  } else {
    const x = snapToGrid(randomBetween(GRID_STEP, rect.width - GRID_STEP))
    const direction = Math.random() < 0.5 ? 1 : -1
    const y = direction > 0
      ? randomBetween(-length * 0.6, rect.height * 0.72)
      : randomBetween(rect.height * 0.28, rect.height + length * 0.2)
    const travel = randomBetween(rect.height * 0.34, rect.height * 0.82) * direction

    element.style.height = `${length}px`
    element.style.left = `${x}px`
    element.style.top = `${y}px`
    element.style.setProperty('--dx', '0px')
    element.style.setProperty('--dy', `${travel}px`)
  }

  mountTransient(element)
}

function spawnGlint(config) {
  const rect = world.getBoundingClientRect()
  const element = document.createElement('span')
  const duration = randomBetween(...config.glintDuration)
  const peak = randomBetween(...config.glintPeak)

  const x = snapToGrid(randomBetween(GRID_STEP, rect.width - GRID_STEP))
  const y = snapToGrid(randomBetween(GRID_STEP, rect.height - GRID_STEP))

  element.className = 'ambient-glint runtime-glint'
  element.style.left = `${x}px`
  element.style.top = `${y}px`
  element.style.setProperty('--duration', `${duration}ms`)
  element.style.setProperty('--peak', peak.toFixed(2))

  mountTransient(element)
}

function spawnDrift(config) {
  const rect = world.getBoundingClientRect()
  const element = document.createElement('span')
  const duration = randomBetween(...config.driftDuration)
  const size = randomBetween(260, 460)
  const startX = randomBetween(-size * 0.35, rect.width - size * 0.65)
  const startY = randomBetween(-size * 0.35, rect.height - size * 0.65)
  const dx = randomBetween(-rect.width * 0.28, rect.width * 0.28)
  const dy = randomBetween(-rect.height * 0.24, rect.height * 0.24)
  const opacity = randomBetween(...config.driftOpacity)

  element.className = 'ambient-drift runtime-drift'
  element.style.width = `${size}px`
  element.style.height = `${size}px`
  element.style.left = `${startX}px`
  element.style.top = `${startY}px`
  element.style.setProperty('--duration', `${duration}ms`)
  element.style.setProperty('--dx', `${dx}px`)
  element.style.setProperty('--dy', `${dy}px`)
  element.style.setProperty('--peak', opacity.toFixed(2))

  mountTransient(element)
}

function mountTransient(element) {
  runtimeLayer.appendChild(element)
  element.addEventListener('animationend', () => element.remove(), { once: true })
}

function snapToGrid(value) {
  return Math.round(value / GRID_STEP) * GRID_STEP
}

function randomBetween(min, max) {
  return min + Math.random() * (max - min)
}

updateIntensityCopy(html.dataset.intensity)
restartAmbientEngine()
