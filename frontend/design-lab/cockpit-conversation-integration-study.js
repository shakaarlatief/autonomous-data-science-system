/*
 * Adaptive Conversation Dock study controller.
 *
 * Opt-in route:
 *   ?conversation=adaptive-dock
 *
 * This module changes presentation only. It does not own conversation scope,
 * thread state, Boxes/Text semantics, A6 semantics or source-work restoration.
 */

const root = document.documentElement
const params = new URLSearchParams(window.location.search)

if (params.get('conversation') === 'adaptive-dock') {
  root.dataset.conversationIntegration = 'adaptive-dock'
  root.dataset.conversationRailDrawer = 'closed'
  root.dataset.conversationDockResizing = 'false'
  installWhenReady()
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
  threadsButton.setAttribute('aria-controls', 'reintegration-thread-list')
  threadsButton.setAttribute('aria-expanded', 'false')
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
    ],
  })
}

function syncPresentationState() {
  if (root.dataset.conversationPresentation !== 'copresent' || root.dataset.conversationOpen !== 'true') {
    setDrawerOpen(false)
  }

  if (root.dataset.conversationA6Expanded === 'true') setDrawerOpen(false)
}

function installResizeBehavior(layer, handle) {
  const resetWidth = () => layer.style.removeProperty('--adaptive-conversation-dock-width')

  const applyWidth = (requestedWidth) => {
    const viewportWidth = window.innerWidth
    const maximum = Math.max(360, Math.min(760, viewportWidth - 560))
    const minimum = Math.min(480, maximum)
    const next = Math.max(minimum, Math.min(maximum, requestedWidth))
    layer.style.setProperty('--adaptive-conversation-dock-width', `${Math.round(next)}px`)
    handle.setAttribute('aria-valuenow', String(Math.round(next)))
    return next
  }

  const currentWidth = () => layer.getBoundingClientRect().width

  handle.addEventListener('pointerdown', (event) => {
    if (root.dataset.conversationPresentation !== 'copresent') return
    event.preventDefault()
    handle.setPointerCapture(event.pointerId)
    root.dataset.conversationDockResizing = 'true'
  })

  handle.addEventListener('pointermove', (event) => {
    if (root.dataset.conversationDockResizing !== 'true' || !handle.hasPointerCapture(event.pointerId)) return
    applyWidth(window.innerWidth - event.clientX)
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

    const delta = event.key === 'ArrowLeft' ? 32 : -32
    applyWidth(currentWidth() + delta)
  })

  window.addEventListener('resize', () => {
    const authored = layer.style.getPropertyValue('--adaptive-conversation-dock-width')
    if (!authored) return
    applyWidth(currentWidth())
  }, { passive: true })
}
