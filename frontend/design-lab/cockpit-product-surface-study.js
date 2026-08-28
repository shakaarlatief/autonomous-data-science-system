/*
 * Whole-Cockpit product-surface study A controller.
 *
 * Presentation-only exploration on top of the source-faithful reintegration.
 * Accepted semantic/interaction mechanisms remain owned by their existing
 * modules. This adapter reorganizes provisional shell controls, invokes the
 * existing Jump/search capability from a compact rail and extends the grid
 * visually across the navigable viewport while preserving the semantic plane.
 */

const root = document.documentElement
const shell = document.querySelector('#reintegration-shell')
const stage = document.querySelector('#reintegration-stage')
const hud = document.querySelector('.reintegration-hud')
const tools = document.querySelector('.reintegration-tools')
const search = document.querySelector('.reintegration-search')
const plane = document.querySelector('#reintegration-world-plane')
const world = document.querySelector('#reintegration-world')
const jumpInput = document.querySelector('#jump-input')
const jumpButton = document.querySelector('#jump-button')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const appearanceToggle = document.querySelector('#appearance-controls-toggle')

root.dataset.productSurfaceStudy = 'a'
root.dataset.productSearchOpen = 'false'
root.dataset.productChrome = 'vertical-rail-a'
root.dataset.conversationReadability = 'normal-a'

mountSpatialToolRail()
installJumpPalette()
installContinuousGridSync()
installSurfaceOwnershipSync()
installOptionalSpatialRailStudy()
installOptionalCockpitEdgeStudy()

function mountSpatialToolRail() {
  if (!stage || !tools || tools.dataset.productRailMounted === 'true') return
  tools.dataset.productRailMounted = 'true'
  tools.setAttribute('aria-label', 'Project spatial tools')

  /*
   * Search becomes an invoked spatial-navigation tool rather than a permanent
   * central bar. The existing search input and Jump action remain authoritative.
   */
  const searchToggle = document.createElement('button')
  searchToggle.type = 'button'
  searchToggle.id = 'product-jump-toggle'
  searchToggle.dataset.productGlyph = '⌕'
  searchToggle.dataset.tooltip = 'Jump / search'
  searchToggle.setAttribute('aria-label', 'Open Jump and search')
  searchToggle.setAttribute('aria-expanded', 'false')
  tools.insertBefore(searchToggle, tools.firstChild)

  const buttonPresentation = {
    'zoom-out': ['−', 'Zoom out'],
    'zoom-in': ['+', 'Zoom in'],
    'fit-world': ['⌖', 'Fit project'],
    'reset-world': ['↺', 'Reset view'],
    'toggle-detail': ['▣', 'Expand selected WorkUnit'],
    'deep-dive': ['↘', 'Deep Dive'],
    'process-focus-toggle': ['◎', 'Current process focus'],
    'global-conversations': ['◌', 'Conversations'],
    'appearance-controls-toggle': ['◐', 'Appearance'],
    'hud-hide': ['▱', 'Hide project HUD'],
    'fullscreen-world': ['⛶', 'Fullscreen'],
    'map-tools-fold': ['‹', 'Fold spatial tools'],
  }

  for (const button of tools.querySelectorAll('button')) {
    const presentation = buttonPresentation[button.id]
    if (!presentation) continue
    const [glyph, label] = presentation
    button.dataset.productGlyph = glyph
    button.dataset.tooltip = label
    button.title = label
    if (!button.getAttribute('aria-label')) button.setAttribute('aria-label', label)
  }

  /*
   * Move map controls out of the provisional horizontal HUD. Existing event
   * listeners remain attached because the actual DOM nodes are moved, not
   * recreated.
   */
  stage.appendChild(tools)
  if (search) stage.appendChild(search)

  searchToggle.addEventListener('click', () => setSearchOpen(root.dataset.productSearchOpen !== 'true'))

  /* Keep fold glyph meaningful after the existing architecture adapter toggles. */
  const fold = document.querySelector('#map-tools-fold')
  if (fold && 'MutationObserver' in window) {
    const observer = new MutationObserver(() => {
      fold.dataset.productGlyph = tools.dataset.folded === 'true' ? '›' : '‹'
      fold.dataset.tooltip = tools.dataset.folded === 'true' ? 'Restore spatial tools' : 'Fold spatial tools'
    })
    observer.observe(tools, { attributes: true, attributeFilter: ['data-folded'] })
  }
}

function installJumpPalette() {
  if (!search) return

  jumpButton?.addEventListener('click', () => window.setTimeout(() => setSearchOpen(false), 0))

  /*
   * Direct accessibility/automation input into the existing search field should
   * reveal the invoked surface rather than leave an invisible active control.
   * This also keeps the previously promoted Jump capability usable through its
   * existing DOM contract while the visible shell changes around it.
   */
  jumpInput?.addEventListener('input', () => {
    if (root.dataset.productSearchOpen !== 'true') setSearchOpen(true)
  })

  jumpInput?.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      event.preventDefault()
      setSearchOpen(false)
      return
    }
    if (event.key === 'Enter') window.setTimeout(() => setSearchOpen(false), 0)
  })

  appearanceToggle?.addEventListener('click', () => setSearchOpen(false))
  document.querySelector('#process-focus-toggle')?.addEventListener('click', () => setSearchOpen(false))

  document.addEventListener('pointerdown', (event) => {
    if (root.dataset.productSearchOpen !== 'true') return
    const target = event.target
    if (!(target instanceof Element)) return
    if (target.closest('.reintegration-search, #product-jump-toggle')) return
    setSearchOpen(false)
  })

  window.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape' || root.dataset.productSearchOpen !== 'true') return
    event.preventDefault()
    setSearchOpen(false)
  }, true)
}

function setSearchOpen(open) {
  if (!search) return
  const next = Boolean(open)
  root.dataset.productSearchOpen = String(next)
  document.querySelector('#product-jump-toggle')?.setAttribute('aria-expanded', String(next))

  if (next) {
    /* Floating product surfaces are mutually exclusive. */
    if (appearancePanel && !appearancePanel.hidden) {
      appearancePanel.hidden = true
      appearanceToggle?.setAttribute('aria-expanded', 'false')
    }
    const focusPanel = document.querySelector('#reintegration-process-focus-panel')
    const focusToggle = document.querySelector('#process-focus-toggle')
    if (focusPanel && !focusPanel.hidden) {
      focusPanel.hidden = true
      focusToggle?.setAttribute('aria-expanded', 'false')
    }
    requestAnimationFrame(() => jumpInput?.focus({ preventScroll: true }))
  } else if (document.activeElement && search.contains(document.activeElement)) {
    document.querySelector('#product-jump-toggle')?.focus({ preventScroll: true })
  }
}

/* -------------------------------------------------------------------------- */
/* Continuous grid-world synchronization                                      */
/* -------------------------------------------------------------------------- */

function installContinuousGridSync() {
  if (!stage || !plane || !world) return

  const sync = () => {
    const transform = plane.style.transform || getComputedStyle(plane).transform
    const camera = readCameraTransform(transform)
    if (!camera) return

    /*
     * The sharpness adapter transfers geometric scale from the plane transform
     * into CSS `zoom` on the world so Chromium can rerasterize text and 1px
     * lines. Translation therefore comes from the camera transform, while the
     * authoritative settled scale comes from the world layout zoom whenever it
     * is present. This keeps the viewport-owned grid spatially aligned with the
     * accepted sharpness strategy instead of creating a second zoom model.
     */
    const layoutScale = Number.parseFloat(world.style.zoom || '')
    const scale = Number.isFinite(layoutScale) && layoutScale > 0 ? layoutScale : camera.scale

    const rect = stage.getBoundingClientRect()
    const originX = rect.width / 2 + camera.x
    const originY = rect.height / 2 + camera.y
    const minor = Math.max(4, 20 * scale)
    const major = Math.max(20, 100 * scale)

    stage.style.setProperty('--product-grid-minor', `${minor}px`)
    stage.style.setProperty('--product-grid-major', `${major}px`)
    stage.style.setProperty('--product-grid-x', `${originX}px`)
    stage.style.setProperty('--product-grid-y', `${originY}px`)
  }

  sync()
  window.addEventListener('resize', sync, { passive: true })

  if ('MutationObserver' in window) {
    const planeObserver = new MutationObserver(sync)
    planeObserver.observe(plane, { attributes: true, attributeFilter: ['style'] })

    const worldObserver = new MutationObserver(sync)
    worldObserver.observe(world, { attributes: true, attributeFilter: ['style'] })
  }
}

function readCameraTransform(transform) {
  if (!transform || transform === 'none') return null

  const authored = transform.match(/translate3d\(([-\d.]+)px,\s*([-\d.]+)px,\s*0(?:px)?\)(?:\s*scale\(([-\d.]+)\))?/)
  if (authored) {
    return {
      x: Number(authored[1]),
      y: Number(authored[2]),
      scale: authored[3] ? Number(authored[3]) : 1,
    }
  }

  const matrix = transform.match(/^matrix\(([-\d.e]+),\s*[-\d.e]+,\s*[-\d.e]+,\s*([-\d.e]+),\s*([-\d.e]+),\s*([-\d.e]+)\)$/)
  if (matrix) {
    return { x: Number(matrix[3]), y: Number(matrix[4]), scale: Number(matrix[1]) }
  }

  return null
}

function installSurfaceOwnershipSync() {
  if (!('MutationObserver' in window)) return

  const observer = new MutationObserver(() => {
    if (root.dataset.deepFocus !== 'false' || (root.dataset.conversationOpen === 'true' && root.dataset.conversationPresentation === 'full')) {
      setSearchOpen(false)
    }
  })

  observer.observe(root, {
    attributes: true,
    attributeFilter: ['data-deep-focus', 'data-conversation-open', 'data-conversation-presentation'],
  })
}

/* -------------------------------------------------------------------------- */
/* Optional advanced edge-rail studies                                        */
/* -------------------------------------------------------------------------- */

function installOptionalSpatialRailStudy() {
  const rail = new URLSearchParams(window.location.search).get('rail')
  if (!['blade', 'deck', 'float'].includes(rail || '')) return

  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-spatial-rail-study.css'
  link.dataset.spatialRailStudyAsset = 'true'
  document.head.appendChild(link)

  import('./cockpit-spatial-rail-study.js').catch((error) => {
    console.error('Spatial rail study failed to load', error)
  })
}

function installOptionalCockpitEdgeStudy() {
  const edge = new URLSearchParams(window.location.search).get('edge')
  if (!['hinge', 'stack', 'console'].includes(edge || '')) return

  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-spatial-rail-study-gen2.css'
  link.dataset.spatialRailGen2Asset = 'true'
  document.head.appendChild(link)

  import('./cockpit-spatial-rail-study-gen2.js').catch((error) => {
    console.error('Second-generation Cockpit edge study failed to load', error)
  })
}
