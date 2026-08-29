/*
 * Adaptive Conversation Dock study controller.
 *
 * Opt-in route:
 *   ?conversation=adaptive-dock
 *
 * This module changes presentation and workbench ergonomics only. It does not
 * own conversation scope, thread state, Boxes/Text semantics, A6 semantics or
 * source-work restoration.
 */

const root = document.documentElement
const params = new URLSearchParams(window.location.search)
const NODE_SELECTOR = '.expansion-practical-node'
const PROJECT_RAIL_COMPACT_RESERVE = 96
const PROJECT_RAIL_EXPANDED_RESERVE = 236

if (params.get('conversation') === 'adaptive-dock') {
  root.dataset.conversationIntegration = 'adaptive-dock'
  root.dataset.conversationRailDrawer = 'closed'
  root.dataset.conversationDockResizing = 'false'
  root.dataset.practicalWorkspace = 'candidate'
  installPracticalStylesheet()
  installWhenReady()
}

function installPracticalStylesheet() {
  if (document.querySelector('link[data-practical-workspace-study]')) return
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-practical-workspace-study.css'
  link.dataset.practicalWorkspaceStudy = 'true'
  document.head.appendChild(link)
}

function installWhenReady() {
  if (installAdaptiveDock()) return
  if (!('MutationObserver' in window)) return

  const observer = new MutationObserver(() => {
    if (!installAdaptiveDock()) return
    observer.disconnect()
  })

  observer.observe(document.documentElement, { childList: true, subtree: true })
}

function installAdaptiveDock() {
  const layer = document.querySelector('#reintegration-conversation-layer')
  if (!(layer instanceof HTMLElement) || layer.dataset.adaptiveDockMounted === 'true') return layer instanceof HTMLElement

  const actions = layer.querySelector('.reintegration-conversation-actions')
  const brand = layer.querySelector('.reintegration-conversation-brand')
  const rail = layer.querySelector('.reintegration-conversation-rail')
  const threadList = layer.querySelector('#reintegration-thread-list')
  const a6Expand = layer.querySelector('#reintegration-conversation-expand-box')

  if (!(actions instanceof HTMLElement) || !(brand instanceof HTMLElement) || !(rail instanceof HTMLElement)) return false

  layer.dataset.adaptiveDockMounted = 'true'

  const threadsButton = document.createElement('button')
  threadsButton.type = 'button'
  threadsButton.id = 'adaptive-conversation-threads'
  threadsButton.className = 'adaptive-conversation-threads'
  threadsButton.textContent = 'Threads'
  threadsButton.title = 'Threads (T)'
  threadsButton.setAttribute('aria-controls', 'reintegration-thread-list')
  threadsButton.setAttribute('aria-expanded', 'false')
  threadsButton.setAttribute('aria-keyshortcuts', 'T')
  actions.insertBefore(threadsButton, actions.firstChild)

  const drawerClose = document.createElement('button')
  drawerClose.type = 'button'
  drawerClose.className = 'adaptive-conversation-drawer-close'
  drawerClose.setAttribute('aria-label', 'Close conversation threads')
  drawerClose.textContent = '×'
  brand.appendChild(drawerClose)

  const resizeHandle = document.createElement('div')
  resizeHandle.id = 'adaptive-conversation-resize-handle'
  resizeHandle.className = 'adaptive-conversation-resize-handle'
  resizeHandle.setAttribute('role', 'separator')
  resizeHandle.setAttribute('aria-label', 'Resize Conversation dock')
  resizeHandle.setAttribute('aria-orientation', 'vertical')
  resizeHandle.tabIndex = 0
  layer.appendChild(resizeHandle)

  markCompactHeaderActions(actions)
  installDirectCopresentEntry()
  installProjectRailReservation()
  installDirectDeepDiveActions()
  installShortcutBehavior()
  normalizeDeepWorkspaceChrome()

  threadsButton.addEventListener('click', () => {
    setDrawerOpen(root.dataset.conversationRailDrawer !== 'open')
  })

  drawerClose.addEventListener('click', () => {
    setDrawerOpen(false)
    threadsButton.focus({ preventScroll: true })
  })

  threadList?.addEventListener('click', (event) => {
    const target = event.target
    if (!(target instanceof Element) || !target.closest('.reintegration-thread-item')) return
    window.setTimeout(() => setDrawerOpen(false), 0)
  })

  a6Expand?.addEventListener('click', () => setDrawerOpen(false))

  installResizeBehavior(layer, resizeHandle)
  installPresentationObserver()
  syncPresentationState()

  return true
}

function markCompactHeaderActions(actions) {
  for (const button of actions.querySelectorAll(':scope > button')) {
    if (!(button instanceof HTMLButtonElement)) continue
    const label = button.textContent?.trim().toLowerCase() || ''
    if (label === 'outline' || label === '•••') button.dataset.adaptiveHideInDock = 'true'
  }

  const presentation = actions.querySelector('#reintegration-conversation-presentation-toggle')
  if (presentation instanceof HTMLButtonElement) {
    presentation.title = 'Toggle full focus / co-present (Shift+C)'
    presentation.setAttribute('aria-keyshortcuts', 'Shift+C')
  }
}

function installDirectCopresentEntry() {
  const directButtons = [
    document.querySelector('#global-conversations'),
    document.querySelector('#conversation-expand'),
  ].filter((button) => button instanceof HTMLButtonElement)

  for (const button of directButtons) {
    button.title = 'Conversation (C)'
    button.setAttribute('aria-keyshortcuts', 'C')
    if (button.dataset.adaptiveDirectCopresent === 'true') continue
    button.dataset.adaptiveDirectCopresent = 'true'

    /*
     * The source-faithful controller opens the global workspace in full focus.
     * On this opt-in candidate route, convert that same opening synchronously to
     * co-present so the common action is one click instead of full -> workaround.
     */
    button.addEventListener('click', () => {
      if (root.dataset.conversationOpen !== 'true') return
      if (root.dataset.conversationPresentation !== 'full') return
      document.querySelector('#reintegration-conversation-presentation-toggle')?.click()
    })
  }
}

function installProjectRailReservation() {
  const sync = () => {
    const rig = document.querySelector('.cockpit-angled-rail-rig')
    const expanded = rig instanceof HTMLElement && rig.dataset.clarity === 'expanded'
    const reserve = expanded ? PROJECT_RAIL_EXPANDED_RESERVE : PROJECT_RAIL_COMPACT_RESERVE
    root.style.setProperty('--adaptive-project-rail-reserve', `${reserve}px`)
  }

  sync()

  if (!('MutationObserver' in window)) return
  const observer = new MutationObserver(sync)
  observer.observe(document.documentElement, {
    subtree: true,
    childList: true,
    attributes: true,
    attributeFilter: ['data-clarity'],
  })
}

function installDirectDeepDiveActions() {
  const install = () => {
    for (const node of document.querySelectorAll(NODE_SELECTOR)) {
      if (!(node instanceof HTMLElement) || node.querySelector(':scope > .adaptive-deep-dive-action')) continue

      const button = document.createElement('button')
      button.type = 'button'
      button.className = 'adaptive-deep-dive-action'
      button.textContent = 'Deep dive'
      button.title = 'Deep Dive (D)'
      button.setAttribute('aria-keyshortcuts', 'D')
      button.addEventListener('pointerdown', (event) => event.stopPropagation())
      button.addEventListener('click', (event) => {
        event.preventDefault()
        event.stopPropagation()
        document.querySelector('#deep-dive')?.click()
      })
      node.appendChild(button)
    }
  }

  install()

  const host = document.querySelector('#expansion-practical-nodes')
  if (!host || !('MutationObserver' in window)) return
  const observer = new MutationObserver(install)
  observer.observe(host, { childList: true, subtree: false })
}

function installShortcutBehavior() {
  const deepDive = document.querySelector('#deep-dive')
  const returnToProject = document.querySelector('#return-to-project')
  if (deepDive instanceof HTMLButtonElement) {
    deepDive.title = 'Deep Dive (D)'
    deepDive.setAttribute('aria-keyshortcuts', 'D')
  }

  window.addEventListener('keydown', (event) => {
    if (event.defaultPrevented || shortcutTargetIsEditable(event.target)) return
    if (event.ctrlKey || event.metaKey || event.altKey) return

    const key = event.key.toLowerCase()

    if (key === 'c' && event.shiftKey) {
      if (root.dataset.conversationOpen !== 'true') return
      event.preventDefault()
      document.querySelector('#reintegration-conversation-presentation-toggle')?.click()
      return
    }

    if (event.shiftKey) return

    if (key === 'c') {
      event.preventDefault()
      if (root.dataset.conversationOpen === 'true') {
        document.querySelector('#reintegration-conversation-close')?.click()
        return
      }

      if (root.dataset.deepFocus === 'focused') {
        document.querySelector('#deep-work-conversation')?.click()
      } else {
        document.querySelector('#global-conversations')?.click()
      }
      return
    }

    if (key === 'd') {
      if (root.dataset.conversationOpen === 'true') return
      event.preventDefault()
      if (root.dataset.deepFocus === 'focused') returnToProject?.click()
      else deepDive?.click()
      return
    }

    if (key === 't') {
      if (root.dataset.conversationOpen !== 'true' || root.dataset.conversationPresentation !== 'copresent') return
      event.preventDefault()
      document.querySelector('#adaptive-conversation-threads')?.click()
    }
  })
}

function shortcutTargetIsEditable(target) {
  if (!(target instanceof Element)) return false
  return Boolean(target.closest('input, textarea, select, [contenteditable="true"], [role="textbox"]'))
}

function normalizeDeepWorkspaceChrome() {
  const replacements = new Map([
    ['SPECIALIST WORKSPACE', 'Specialist workspace'],
    ['PRIMARY ANALYTICAL SURFACE', 'Primary analytical surface'],
    ['EVIDENCE / OUTPUTS', 'Evidence / outputs'],
    ['WORK-UNIT CONTEXT', 'Work-unit context'],
    ['COMMANDS / NOTES', 'Commands / notes'],
  ])

  for (const label of document.querySelectorAll('.reintegration-specialist-bar span, .reintegration-specialist-panel > span')) {
    const current = label.textContent?.trim() || ''
    const replacement = replacements.get(current)
    if (replacement) label.textContent = replacement
  }
}

function setDrawerOpen(open) {
  const copresent = root.dataset.conversationPresentation === 'copresent'
  const conversationOpen = root.dataset.conversationOpen === 'true'
  const next = Boolean(open && copresent && conversationOpen)
  root.dataset.conversationRailDrawer = next ? 'open' : 'closed'
  document.querySelector('#adaptive-conversation-threads')?.setAttribute('aria-expanded', String(next))
}

function installPresentationObserver() {
  if (!('MutationObserver' in window)) return

  const observer = new MutationObserver(syncPresentationState)
  observer.observe(root, {
    attributes: true,
    attributeFilter: [
      'data-conversation-open',
      'data-conversation-presentation',
      'data-conversation-a6-expanded',
      'data-deep-focus',
    ],
  })
}

function syncPresentationState() {
  if (root.dataset.conversationPresentation !== 'copresent' || root.dataset.conversationOpen !== 'true') {
    setDrawerOpen(false)
  }

  if (root.dataset.conversationA6Expanded === 'true') setDrawerOpen(false)
  clampAuthoredDockWidth()
}

function installResizeBehavior(layer, handle) {
  const resetWidth = () => {
    root.style.removeProperty('--adaptive-conversation-dock-width')
    handle.removeAttribute('aria-valuenow')
    handle.setAttribute('aria-valuemin', String(minimumDockWidth()))
    handle.setAttribute('aria-valuemax', String(maximumDockWidth()))
  }

  const applyWidth = (requestedWidth) => {
    const minimum = minimumDockWidth()
    const maximum = maximumDockWidth()
    const next = Math.max(minimum, Math.min(maximum, requestedWidth))
    root.style.setProperty('--adaptive-conversation-dock-width', `${Math.round(next)}px`)
    handle.setAttribute('aria-valuemin', String(Math.round(minimum)))
    handle.setAttribute('aria-valuemax', String(Math.round(maximum)))
    handle.setAttribute('aria-valuenow', String(Math.round(next)))
    return next
  }

  const currentRequestedWidth = () => {
    const authored = Number.parseFloat(root.style.getPropertyValue('--adaptive-conversation-dock-width'))
    return Number.isFinite(authored) ? authored : layer.getBoundingClientRect().width
  }

  handle.setAttribute('aria-valuemin', String(minimumDockWidth()))
  handle.setAttribute('aria-valuemax', String(maximumDockWidth()))

  handle.addEventListener('pointerdown', (event) => {
    if (root.dataset.conversationPresentation !== 'copresent') return
    event.preventDefault()
    handle.setPointerCapture(event.pointerId)
    root.dataset.conversationDockResizing = 'true'
  })

  handle.addEventListener('pointermove', (event) => {
    if (root.dataset.conversationDockResizing !== 'true' || !handle.hasPointerCapture(event.pointerId)) return
    const rightReserve = root.dataset.deepFocus === 'focused' ? 0 : projectRailReserve()
    applyWidth(window.innerWidth - rightReserve - event.clientX)
  })

  const endResize = (event) => {
    if (handle.hasPointerCapture(event.pointerId)) handle.releasePointerCapture(event.pointerId)
    root.dataset.conversationDockResizing = 'false'
  }

  handle.addEventListener('pointerup', endResize)
  handle.addEventListener('pointercancel', endResize)
  handle.addEventListener('dblclick', resetWidth)

  handle.addEventListener('keydown', (event) => {
    if (root.dataset.conversationPresentation !== 'copresent') return
    if (!['ArrowLeft', 'ArrowRight', 'Home'].includes(event.key)) return
    event.preventDefault()

    if (event.key === 'Home') {
      resetWidth()
      return
    }

    const delta = event.key === 'ArrowLeft' ? 40 : -40
    applyWidth(currentRequestedWidth() + delta)
  })

  window.addEventListener('resize', clampAuthoredDockWidth, { passive: true })
}

function minimumDockWidth() {
  return Math.min(360, maximumDockWidth())
}

function maximumDockWidth() {
  const reserve = root.dataset.deepFocus === 'focused' ? 0 : projectRailReserve()
  return Math.max(320, Math.min(900, window.innerWidth - reserve - 520))
}

function projectRailReserve() {
  const value = Number.parseFloat(getComputedStyle(root).getPropertyValue('--adaptive-project-rail-reserve'))
  return Number.isFinite(value) ? value : PROJECT_RAIL_COMPACT_RESERVE
}

function clampAuthoredDockWidth() {
  const authored = root.style.getPropertyValue('--adaptive-conversation-dock-width')
  if (!authored) return
  const requested = Number.parseFloat(authored)
  if (!Number.isFinite(requested)) return
  const minimum = minimumDockWidth()
  const maximum = maximumDockWidth()
  root.style.setProperty('--adaptive-conversation-dock-width', `${Math.round(Math.max(minimum, Math.min(maximum, requested)))}px`)
}
