/*
 * Second-generation spatial Cockpit edge studies.
 *
 * Human reference direction:
 *   architectural instrument surfaces around a central world, with real depth,
 *   perspective, frame thickness and progressive reveal rather than a toolbar
 *   that merely acquires a shadow.
 *
 * These candidates remain presentation-only. The real existing Cockpit controls
 * are moved into the study surface, so their behavior and semantic ownership do
 * not change.
 *
 * edge=hinge   -> a cockpit instrument wing that pivots and translates inward
 * edge=stack   -> three functional instrument planes that telescope into depth
 * edge=console -> a deeper command console with live selected-work context
 */

const root = document.documentElement
const stage = document.querySelector('#reintegration-stage')
const tools = document.querySelector('.reintegration-tools')
const search = document.querySelector('.reintegration-search')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const focusPanel = document.querySelector('#reintegration-process-focus-panel')

const VARIANTS = new Set(['hinge', 'stack', 'console'])
const params = new URLSearchParams(window.location.search)
const requested = params.get('edge') || ''
const variant = VARIANTS.has(requested) ? requested : null

if (variant && stage && tools) mountStudy()

function mountStudy() {
  root.dataset.spatialRailGen2 = variant
  root.style.setProperty('--edge-pull', '0')
  tools.dataset.folded = 'false'

  const rig = document.createElement('aside')
  rig.className = 'cockpit-edge-rig'
  rig.dataset.variant = variant
  rig.dataset.state = 'docked'
  rig.dataset.dragging = 'false'
  rig.setAttribute('aria-label', `${variantName(variant)} Cockpit edge study`)

  const rearFrame = document.createElement('div')
  rearFrame.className = 'cockpit-edge-rear-frame'
  rearFrame.setAttribute('aria-hidden', 'true')

  const midFrame = document.createElement('div')
  midFrame.className = 'cockpit-edge-mid-frame'
  midFrame.setAttribute('aria-hidden', 'true')

  const shell = document.createElement('div')
  shell.className = 'cockpit-edge-shell'

  const header = document.createElement('div')
  header.className = 'cockpit-edge-header'
  header.innerHTML = `
    <span>ADS · INSTRUMENT SURFACE</span>
    <strong id="cockpit-edge-context-title">Project controls</strong>
    <small>${variantSubtitle(variant)}</small>
  `

  const grip = document.createElement('button')
  grip.type = 'button'
  grip.className = 'cockpit-edge-grip'
  grip.setAttribute('aria-label', `Pull ${variantName(variant)} into the Cockpit`)
  grip.innerHTML = '<i></i><i></i><i></i><span>pull</span>'

  stage.insertBefore(rig, tools)
  rig.append(rearFrame, midFrame, shell)
  shell.append(header, tools, grip)

  groupRealControls(tools)
  mountVariantSwitcher()
  mountStudyNote()
  syncContextTitle()
  installSelectionContextSync()
  installDirectPull(rig, grip)
  installOwnershipSync(rig)
}

function groupRealControls(host) {
  const definitions = [
    {
      key: 'navigation',
      label: 'Navigation',
      ids: ['product-jump-toggle', 'zoom-out', 'zoom-readout', 'zoom-in', 'fit-world', 'reset-world'],
    },
    {
      key: 'work',
      label: 'Work',
      ids: ['toggle-detail', 'deep-dive', 'process-focus-toggle', 'global-conversations'],
    },
    {
      key: 'system',
      label: 'System',
      ids: ['appearance-controls-toggle', 'hud-hide', 'fullscreen-world', 'map-tools-fold'],
    },
  ]

  const claimed = new Set()
  const banks = []

  for (const definition of definitions) {
    const bank = document.createElement('section')
    bank.className = 'cockpit-edge-bank'
    bank.dataset.bank = definition.key

    const label = document.createElement('span')
    label.className = 'cockpit-edge-bank-label'
    label.textContent = definition.label

    const controls = document.createElement('div')
    controls.className = 'cockpit-edge-bank-controls'

    for (const id of definition.ids) {
      const control = document.getElementById(id)
      if (!control || !host.contains(control)) continue
      claimed.add(control)
      controls.appendChild(control)
    }

    bank.append(label, controls)
    banks.push(bank)
  }

  const systemControls = banks.at(-1)?.querySelector('.cockpit-edge-bank-controls')
  if (systemControls) {
    for (const child of [...host.children]) {
      if (claimed.has(child)) continue
      systemControls.appendChild(child)
    }
  }

  host.replaceChildren(...banks)
}

function mountVariantSwitcher() {
  const switcher = document.createElement('nav')
  switcher.className = 'cockpit-edge-switcher'
  switcher.setAttribute('aria-label', 'Cockpit architectural edge variants')
  switcher.innerHTML = '<span>COCKPIT EDGE · GEN 2</span>'

  const choices = [
    ['hinge', 'A · Hinge'],
    ['stack', 'B · Stack'],
    ['console', 'C · Console'],
  ]

  for (const [key, label] of choices) {
    const button = document.createElement('button')
    button.type = 'button'
    button.textContent = label
    button.dataset.edgeVariant = key
    button.setAttribute('aria-pressed', String(key === variant))
    button.addEventListener('click', () => {
      if (key === variant) return
      const next = new URL(window.location.href)
      next.searchParams.delete('rail')
      next.searchParams.set('edge', key)
      window.location.assign(next)
    })
    switcher.appendChild(button)
  }

  stage.appendChild(switcher)
}

function mountStudyNote() {
  const note = document.createElement('div')
  note.className = 'cockpit-edge-study-note'
  note.textContent = instruction(variant)
  stage.appendChild(note)
}

function installDirectPull(rig, grip) {
  const maxPull = variant === 'hinge' ? 210 : variant === 'stack' ? 245 : 286
  const snaps = variant === 'stack' ? [0, 0.42, 1] : [0, 0.5, 1]
  let progress = 0
  let pointerId = null
  let startX = 0
  let startProgress = 0
  let moved = false

  const apply = (next, dragging = false) => {
    progress = clamp(next, 0, 1)
    root.style.setProperty('--edge-pull', progress.toFixed(4))
    rig.dataset.state = progress < 0.08 ? 'docked' : progress > 0.82 ? 'open' : 'peek'
    rig.dataset.dragging = String(dragging)
    grip.setAttribute('aria-valuenow', String(Math.round(progress * 100)))
    grip.setAttribute('aria-valuetext', progressLabel(progress))
    syncAttachedPanels(progress, maxPull)
  }

  const onMove = (event) => {
    if (event.pointerId !== pointerId) return
    const delta = startX - event.clientX
    if (Math.abs(delta) > 3) moved = true
    apply(startProgress + delta / maxPull, true)
    event.preventDefault()
  }

  const finish = (event) => {
    if (event.pointerId !== pointerId) return
    pointerId = null
    window.removeEventListener('pointermove', onMove, true)
    window.removeEventListener('pointerup', finish, true)
    window.removeEventListener('pointercancel', finish, true)

    if (!moved) apply(progress < 0.5 ? 1 : 0)
    else apply(nearestSnap(progress, snaps))
  }

  grip.setAttribute('role', 'slider')
  grip.setAttribute('aria-valuemin', '0')
  grip.setAttribute('aria-valuemax', '100')
  grip.setAttribute('aria-valuenow', '0')
  grip.setAttribute('aria-valuetext', 'Docked')

  grip.addEventListener('pointerdown', (event) => {
    if (event.button !== 0) return
    pointerId = event.pointerId
    startX = event.clientX
    startProgress = progress
    moved = false
    rig.dataset.dragging = 'true'
    window.addEventListener('pointermove', onMove, true)
    window.addEventListener('pointerup', finish, true)
    window.addEventListener('pointercancel', finish, true)
    event.preventDefault()
  })

  grip.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') {
      event.preventDefault()
      apply(progress + 0.12)
    } else if (event.key === 'ArrowRight') {
      event.preventDefault()
      apply(progress - 0.12)
    } else if (event.key === 'Home' || event.key === 'Escape') {
      event.preventDefault()
      apply(0)
    } else if (event.key === 'End' || event.key === 'Enter' || event.key === ' ') {
      event.preventDefault()
      apply(progress < 0.5 ? 1 : 0)
    }
  })

  rig.__cockpitEdgeSetProgress = (value) => apply(value)
  rig.__cockpitEdgeGetProgress = () => progress
}

function syncAttachedPanels(progress, maxPull) {
  const right = 82 + maxPull * progress
  for (const panel of [search, appearancePanel, focusPanel]) {
    if (!panel) continue
    panel.style.right = `${right}px`
  }
}

function syncContextTitle() {
  const title = document.querySelector('.expansion-practical-node[data-selected="true"] .node-surface > strong')?.textContent?.trim()
    || document.querySelector('#composer-context')?.textContent?.trim()
    || 'Project controls'
  const target = document.querySelector('#cockpit-edge-context-title')
  if (target) target.textContent = title
}

function installSelectionContextSync() {
  if (!('MutationObserver' in window)) return
  const host = document.querySelector('#expansion-practical-nodes')
  if (!host) return

  const observer = new MutationObserver(syncContextTitle)
  observer.observe(host, {
    subtree: true,
    attributes: true,
    attributeFilter: ['data-selected'],
  })
}

function installOwnershipSync(rig) {
  if (!('MutationObserver' in window)) return

  const sync = () => {
    const conversationOwnsStage = root.dataset.conversationOpen === 'true'
      && root.dataset.conversationPresentation === 'full'
    const deepFocusOwnsStage = root.dataset.deepFocus !== 'false'
    const hidden = conversationOwnsStage || deepFocusOwnsStage
    rig.hidden = hidden
    const switcher = document.querySelector('.cockpit-edge-switcher')
    const note = document.querySelector('.cockpit-edge-study-note')
    if (switcher) switcher.hidden = hidden
    if (note) note.hidden = hidden
  }

  const observer = new MutationObserver(sync)
  observer.observe(root, {
    attributes: true,
    attributeFilter: ['data-conversation-open', 'data-conversation-presentation', 'data-deep-focus'],
  })
  sync()
}

function variantName(value) {
  return value === 'hinge'
    ? 'Hinged Instrument Panel'
    : value === 'stack'
      ? 'Telescoping Layer Stack'
      : 'Spatial Command Console'
}

function variantSubtitle(value) {
  return value === 'hinge'
    ? 'Pivoting edge-mounted instrument wing'
    : value === 'stack'
      ? 'Functional planes telescope into the project world'
      : 'Deep command surface surrounding the active project plane'
}

function instruction(value) {
  return value === 'hinge'
    ? 'Drag the inner grip left. The Cockpit wing pivots toward you instead of opening like a flat drawer.'
    : value === 'stack'
      ? 'Drag left. Navigation, Work and System become separate instrument planes with increasing depth.'
      : 'Drag left. The edge grows into a deeper command console while retaining the live selected-work context.'
}

function progressLabel(progress) {
  if (progress < 0.08) return 'Docked'
  if (progress > 0.82) return 'Fully deployed'
  return 'Partially deployed'
}

function nearestSnap(value, snaps) {
  return snaps.reduce((best, snap) => Math.abs(snap - value) < Math.abs(best - value) ? snap : best, snaps[0])
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value))
}
