/*
 * Cockpit top-layer Escape router.
 *
 * Loaded before the Conversation controller so browser fullscreen and invoked
 * Conversation sublayers get first refusal on Escape. This prevents one mode's
 * recovery handler from swallowing another mode's more immediate exit.
 *
 * It does not own Deep Dive or Conversation closing. If none of the priorities
 * below applies, the existing source controllers receive Escape unchanged.
 */

const root = document.documentElement

window.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return

  /* Browser fullscreen is outside the Cockpit's view-state stack. Do not call
   * preventDefault: the browser must retain its native Escape-to-exit behavior.
   * Stop only app-level listeners from interpreting the same keystroke. */
  if (document.fullscreenElement) {
    event.stopImmediatePropagation()
    return
  }

  if (root.dataset.conversationOpen !== 'true') return

  /* Temporary Conversation surfaces close before the Conversation itself. */
  if (root.dataset.conversationRailDrawer === 'open') {
    event.preventDefault()
    event.stopImmediatePropagation()
    const close = document.querySelector('.adaptive-conversation-drawer-close')
    if (close instanceof HTMLButtonElement) close.click()
    else document.querySelector('#adaptive-conversation-threads')?.click()
    return
  }

  if (root.dataset.conversationA6Expanded === 'true') {
    event.preventDefault()
    event.stopImmediatePropagation()
    document.querySelector('#reintegration-a6-close')?.click()
  }
}, true)
