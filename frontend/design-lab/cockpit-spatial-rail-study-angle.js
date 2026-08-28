/*
 * Resting-angle Cockpit rail study.
 *
 * The rail's spatial identity is permanent: angle, perspective, thickness and
 * edge attachment are present in the normal compact state. The only expansion
 * in this study is a readability aid that exposes labels. Expansion does not
 * create or intensify the 3D treatment.
 */

const root = document.documentElement
const stage = document.querySelector('#reintegration-stage')
const tools = document.querySelector('.reintegration-tools')
const search = document.querySelector('.reintegration-search')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const focusPanel = document.querySelector('#reintegration-process-focus-panel')

if (stage && tools) mountAngledRail()

function mountAngledRail() {
  root.dataset.spatialRailAngle = 'angled'
  tools.dataset.folded = 'false'

  const rig = document.createElement('aside')
  rig.className = 'cockpit-angled-rail-rig'
  rig.dataset.clarity = 'compact'
  rig.setAttribute('aria-label', 'Angled Project Cockpit tool rail study')

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

function syncAttachedPanels(expanded) {
  const right = expanded ? 246 : 94
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
