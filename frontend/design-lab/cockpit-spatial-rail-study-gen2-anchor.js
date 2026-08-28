/*
 * Keep the Gen 2 direct-manipulation grip attached to the stationary Cockpit
 * edge while the instrument surface deploys around it.
 *
 * Reparenting preserves the listeners already installed on the real grip.
 * A MutationObserver is used because the Gen 2 study itself is dynamically
 * imported by the product-surface controller.
 */

const mount = () => {
  const rig = document.querySelector('.cockpit-edge-rig')
  const grip = document.querySelector('.cockpit-edge-grip')
  if (!rig || !grip) return false

  if (grip.parentElement !== rig) rig.appendChild(grip)
  rig.dataset.gripAnchor = 'edge'
  return true
}

if (!mount() && 'MutationObserver' in window) {
  const observer = new MutationObserver(() => {
    if (!mount()) return
    observer.disconnect()
  })
  observer.observe(document.documentElement, { childList: true, subtree: true })
}
