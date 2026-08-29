/*
 * Cockpit late-mounted whole-product study adapter.
 *
 * Three responsibilities currently live here because this module is loaded after
 * the product-surface controller has moved the real Cockpit controls into their
 * final stage-owned container:
 *
 *   1. preserve the historical Gen 2 fixed-edge grip correction when a Gen 2
 *      study is explicitly requested;
 *   2. mount the current flat Project Grid rail on the canonical no-query route;
 *   3. mount explicitly requested whole-product presentation studies that need
 *      the fully composed source-faithful Cockpit as their substrate.
 *
 * The second responsibility removes `?edge=angled` from the current product
 * review URL without reimplementing the rail. The existing historical angle
 * source is still reused as implementation plumbing, and Checkpoints 255/256
 * flatten it into the current normal-2D presentation. Explicit `edge=` and
 * `rail=` study routes remain untouched.
 *
 * The third responsibility is opt-in only. It must never silently change the
 * canonical no-query Cockpit.
 */

mountCurrentFlatRailOnCanonicalRoute()
mountOptionalConversationIntegrationStudy()

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

function mountCurrentFlatRailOnCanonicalRoute() {
  const params = new URLSearchParams(window.location.search)
  if (params.has('edge') || params.has('rail')) return
  if (document.querySelector('.cockpit-angled-rail-rig')) return

  if (!document.querySelector('link[data-current-flat-rail-source]')) {
    const link = document.createElement('link')
    link.rel = 'stylesheet'
    link.href = './cockpit-spatial-rail-study-angle.css'
    link.dataset.currentFlatRailSource = 'true'
    document.head.appendChild(link)
  }

  import('./cockpit-spatial-rail-study-angle.js').catch((error) => {
    console.error('Current flat Cockpit rail failed to load', error)
  })
}

function mountOptionalConversationIntegrationStudy() {
  const params = new URLSearchParams(window.location.search)
  if (params.get('conversation') !== 'adaptive-dock') return

  if (!document.querySelector('link[data-conversation-integration-study]')) {
    const link = document.createElement('link')
    link.rel = 'stylesheet'
    link.href = './cockpit-conversation-integration-study.css'
    link.dataset.conversationIntegrationStudy = 'adaptive-dock'
    document.head.appendChild(link)
  }

  import('./cockpit-conversation-integration-study.js').catch((error) => {
    console.error('Conversation integration study failed to load', error)
  })
}
