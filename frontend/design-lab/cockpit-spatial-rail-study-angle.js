/*
 * Current Project Cockpit rail controller.
 *
 * This source began as the resting-angle rail study. Later human review flattened
 * that presentation while preserving the same real controls and clarity-only
 * expansion behavior. Late presentation layers now define the current compact
 * visual treatment without changing tool ownership or semantics.
 */

const root = document.documentElement
const stage = document.querySelector('#reintegration-stage')
const tools = document.querySelector('.reintegration-tools')
const search = document.querySelector('.reintegration-search')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const focusPanel = document.querySelector('#reintegration-process-focus-panel')

installReview256Layer()
installCurrentProjectRailLayer()

if (stage && tools) mountAngledRail()

function installReview256Layer() {
  if (document.querySelector('link[data-human-review-256]')) return
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-reintegration-review-256.css'
  link.dataset.humanReview256 = 'true'
  document.head.appendChild(link)
  root.dataset.humanReview256 = 'true'
}

function installCurrentProjectRailLayer() {
  if (document.querySelector('link[data-current-project-rail]')) return
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-project-tool-rail-current.css'
  link.dataset.currentProjectRail = 'true'
  document.head.appendChild(link)
}

function mountAngledRail() {
  root.dataset.spatialRailAngle = 'angled'
  tools.dataset.folded = 'false'

  const rig = document.createElement('aside')
  rig.className = 'cockpit-angled-rail-rig'
  rig.dataset.clarity = 'compact'
  rig.setAttribute('aria-label', 'Project Cockpit tool rail')

  const back = document.createElement('div')
  back.className = 'cockpit-angled-rail-back'
  back.setAttribute('aria-hidden', 'true')

  const spine = document.createElement('div')
  spine.className = 'cockpit-angled-rail-spine'
  spine.setAttribute('aria-hidden', 'true')

  const shell = document.createElement('div')
  shell.className = 'cockpit-angled-rail-shell'

  const mark = document.createElement('div')
  mark.className = 'cockpit-angled-rail-mark'
  mark.innerHTML = '<strong>ADS</strong><span>PROJECT TOOLS</span>'

  const clarity = document.createElement('button')
  clarity.type = 'button'
  clarity.className = 'cockpit-angled-rail-clarity'
  clarity.setAttribute('aria-label', 'Show tool labels')
  clarity.setAttribute('aria-expanded', 'false')
  clarity.innerHTML = '<span class="cockpit-angled-rail-clarity-glyph" aria-hidden="true">›</span><span class="cockpit-angled-rail-clarity-label">Tool labels</span>'

  stage.insertBefore(rig, tools)
  rig.append(back, spine, shell)
  shell.append(mark, tools, clarity)

  applyCurrentRailControlSet()

  clarity.addEventListener('click', () => {
    setClarity(rig.dataset.clarity !== 'expanded')
  })

  installOwnershipSync(rig)
  syncAttachedPanels(false)

  function setClarity(expanded) {
    rig.dataset.clarity = expanded ? 'expanded' : 'compact'
    clarity.setAttribute('aria-expanded', String(expanded))
    clarity.setAttribute('aria-label', expanded ? 'Hide tool labels' : 'Show tool labels')
    syncAttachedPanels(expanded)
  }
}

function applyCurrentRailControlSet() {
  const expand = document.querySelector('#toggle-detail')
  const hideHud = document.querySelector('#hud-hide')
  const fullscreen = document.querySelector('#fullscreen-world')

  for (const control of [expand, hideHud]) {
    if (!control) continue
    control.hidden = true
    control.setAttribute('aria-hidden', 'true')
  }

  if (fullscreen) {
    fullscreen.hidden = false
    fullscreen.removeAttribute('aria-hidden')
    fullscreen.dataset.productGlyph = fullscreen.dataset.productGlyph || '⛶'
    fullscreen.dataset.tooltip = 'Fullscreen'
    fullscreen.title = 'Fullscreen'
    if (!fullscreen.getAttribute('aria-label')) fullscreen.setAttribute('aria-label', 'Fullscreen')
  }
}

function syncAttachedPanels(expanded) {
  const railWidth = expanded ? 196 : 56
  const right = railWidth + 18
  for (const panel of [search, appearancePanel, focusPanel]) {
    if (!panel) continue
    panel.style.right = `${right}px`
  }
}

function installOwnershipSync(rig) {
  const sync = () => {
    const conversationOwnsStage = root.dataset.conversationOpen === 'true'
      && root.dataset.conversationPresentation === 'full'
    const deepFocusOwnsStage = root.dataset.deepFocus !== 'false'
    rig.hidden = conversationOwnsStage || deepFocusOwnsStage
  }

  if ('MutationObserver' in window) {
    const observer = new MutationObserver(sync)
    observer.observe(root, {
      attributes: true,
      attributeFilter: ['data-conversation-open', 'data-conversation-presentation', 'data-deep-focus'],
    })
  }

  sync()
}
