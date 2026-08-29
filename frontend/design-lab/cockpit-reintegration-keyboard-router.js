/*
 * Cockpit top-layer keyboard router.
 *
 * The Adaptive Conversation Dock gives Escape one application meaning: Back.
 * Browser fullscreen is entered and exited explicitly with F. While adaptive
 * fullscreen is active, browser-reserved Escape handling is captured with the
 * Fullscreen/Keyboard Lock APIs so a normal Escape press stays available to
 * the Cockpit instead of silently becoming a second fullscreen toggle.
 *
 * Outside the opt-in Adaptive Dock route, the existing source controllers keep
 * their historical keyboard behavior unchanged.
 */

const root = document.documentElement
const params = new URLSearchParams(window.location.search)
const adaptiveDock = params.get('conversation') === 'adaptive-dock'
const fullscreenButton = document.querySelector('#fullscreen-world')

if (adaptiveDock && fullscreenButton instanceof HTMLButtonElement) {
  syncFullscreenShortcutHint()
  fullscreenButton.addEventListener('click', toggleAdaptiveFullscreen, true)
  document.addEventListener('fullscreenchange', syncFullscreenEscapeOwnership)
  window.addEventListener('load', syncFullscreenShortcutHint, { once: true })
  window.setTimeout(syncFullscreenShortcutHint, 120)
}

window.addEventListener('keydown', (event) => {
  if (!adaptiveDock) return
  if (shortcutTargetIsEditable(event.target)) return
  if (event.ctrlKey || event.metaKey || event.altKey || event.shiftKey) return

  if (event.key.toLowerCase() === 'f') {
    event.preventDefault()
    event.stopImmediatePropagation()
    fullscreenButton?.click()
    return
  }

  if (event.key !== 'Escape') return

  /*
   * A normal Escape press must never be interpreted as fullscreen exit on the
   * Adaptive Dock route. Keyboard Lock makes the browser deliver Escape while
   * fullscreen is active; preventDefault keeps the browser fullscreen layer in
   * place while the Cockpit performs its own Back action, if one exists.
   */
  if (document.fullscreenElement) event.preventDefault()

  if (root.dataset.conversationOpen !== 'true') return

  /*
   * Escape exits Conversation in one step, regardless of whether its Threads
   * drawer or A6 inspector is open and regardless of full-focus/co-present
   * presentation. Fullscreen remains unchanged and is owned exclusively by F.
   */
  event.preventDefault()
  event.stopImmediatePropagation()
  document.querySelector('#reintegration-conversation-close')?.click()
}, true)

async function toggleAdaptiveFullscreen(event) {
  event.preventDefault()
  event.stopImmediatePropagation()

  try {
    if (document.fullscreenElement) {
      releaseFullscreenEscapeLock()
      await document.exitFullscreen?.()
      return
    }

    const requestFullscreen = document.documentElement.requestFullscreen
    if (typeof requestFullscreen !== 'function') return

    try {
      await requestFullscreen.call(document.documentElement, {
        keyboardLock: 'browser',
        navigationUI: 'hide',
      })
    } catch (error) {
      const errorName = error && typeof error === 'object' && 'name' in error ? error.name : ''
      if (errorName !== 'NotSupportedError' && errorName !== 'TypeError') throw error
      await requestFullscreen.call(document.documentElement)
    }

    await captureFullscreenEscape()
  } catch {
    root.dataset.fullscreenEscapeLock = 'unavailable'
  }
}

function syncFullscreenEscapeOwnership() {
  if (document.fullscreenElement) {
    void captureFullscreenEscape()
    return
  }
  releaseFullscreenEscapeLock()
}

async function captureFullscreenEscape() {
  if (!adaptiveDock || !document.fullscreenElement) return

  const keyboard = navigator.keyboard
  if (!keyboard || typeof keyboard.lock !== 'function') {
    root.dataset.fullscreenEscapeLock = 'unsupported'
    return
  }

  try {
    await keyboard.lock(['Escape'])
    root.dataset.fullscreenEscapeLock = 'locked'
  } catch {
    root.dataset.fullscreenEscapeLock = 'unavailable'
  }
}

function releaseFullscreenEscapeLock() {
  const keyboard = navigator.keyboard
  if (keyboard && typeof keyboard.unlock === 'function') keyboard.unlock()
  root.dataset.fullscreenEscapeLock = 'off'
}

function syncFullscreenShortcutHint() {
  if (!(fullscreenButton instanceof HTMLButtonElement)) return
  fullscreenButton.title = 'Fullscreen (F)'
  fullscreenButton.dataset.tooltip = 'Fullscreen (F)'
  fullscreenButton.setAttribute('aria-label', 'Toggle fullscreen')
  fullscreenButton.setAttribute('aria-keyshortcuts', 'F')
}

function shortcutTargetIsEditable(target) {
  if (!(target instanceof Element)) return false
  return Boolean(target.closest('input, textarea, select, [contenteditable="true"], [role="textbox"]'))
}
