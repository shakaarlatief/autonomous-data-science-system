/*
 * Cockpit top-layer keyboard router.
 *
 * The Adaptive Conversation Dock gives Escape one application meaning:
 * return from the currently open Conversation workspace. Browser fullscreen is
 * controlled explicitly with F instead of being treated as the first Cockpit
 * recovery layer. The browser may still expose its own native Escape behavior
 * for fullscreen, which web applications cannot disable reliably.
 *
 * Outside the opt-in Adaptive Dock route, the existing source controllers keep
 * their historical keyboard behavior unchanged.
 */

const root = document.documentElement
const params = new URLSearchParams(window.location.search)
const adaptiveDock = params.get('conversation') === 'adaptive-dock'
const fullscreenButton = document.querySelector('#fullscreen-world')

if (adaptiveDock && fullscreenButton instanceof HTMLButtonElement) {
  fullscreenButton.title = 'Fullscreen (F)'
  fullscreenButton.setAttribute('aria-keyshortcuts', 'F')
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

  if (event.key !== 'Escape' || root.dataset.conversationOpen !== 'true') return

  /*
   * Escape exits Conversation in one step, regardless of whether its Threads
   * drawer or A6 inspector is open and regardless of full-focus/co-present
   * presentation. Do not reserve Escape for browser fullscreen. When the
   * browser itself also exits native fullscreen on Escape, the same keystroke
   * still returns the user to the Cockpit instead of leaving Conversation open.
   */
  if (!document.fullscreenElement) event.preventDefault()
  event.stopImmediatePropagation()
  document.querySelector('#reintegration-conversation-close')?.click()
}, true)

function shortcutTargetIsEditable(target) {
  if (!(target instanceof Element)) return false
  return Boolean(target.closest('input, textarea, select, [contenteditable="true"], [role="textbox"]'))
}
