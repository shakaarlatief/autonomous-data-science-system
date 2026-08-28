/*
 * Source-faithful Conversation Workspace integration controller.
 *
 * Held sources:
 *   M19 Quiet Graphite
 *     c66f72a74e681f89fd52ba591a1387ea50f0e959
 *   M20 scope, Boxes/Text and A6 no-floating-card refinement
 *     606e027f281b35c2dfc93d059a1681df23bc2b73
 *   M21 Grid/X5/Deep-Dive access and source-state preservation
 *     db31970d6885ce785609f9c3300f22123130d821
 *
 * The exact co-present width, transition choreography, conversation persistence
 * schema and production component API remain intentionally provisional.
 */

const html = document.documentElement
const shell = document.querySelector('#reintegration-shell')
const stage = document.querySelector('#reintegration-stage')
const specialistLayer = document.querySelector('#reintegration-specialist-layer')
const appearanceToggle = document.querySelector('#appearance-controls-toggle')
const compactConversationButton = document.querySelector('#conversation-expand')
const provisionalNote = document.querySelector('.reintegration-provisional-note')

const NODE_SELECTOR = '.expansion-practical-node'
const RAIL_STORAGE_KEY = 'ads-conversation-sidebar-view'

let conversationLayer = null
let activeScope = 'project'
let activeWorkKey = null
let returnFocusElement = null
let sourceMutationObserver = null

installConversationWorkspace()

function installConversationWorkspace() {
  if (!shell || document.querySelector('#reintegration-conversation-layer')) return

  html.dataset.conversationOpen = 'false'
  html.dataset.conversationPresentation = 'full'
  html.dataset.conversationScope = 'project'
  html.dataset.conversationRail = readInitialRailMode()
  html.dataset.conversationA6Expanded = 'false'
  html.dataset.conversationSource = 'grid'

  conversationLayer = document.createElement('section')
  conversationLayer.id = 'reintegration-conversation-layer'
  conversationLayer.className = 'reintegration-conversation-layer'
  conversationLayer.setAttribute('aria-label', 'Conversation Workspace')
  conversationLayer.setAttribute('aria-hidden', 'true')
  conversationLayer.innerHTML = conversationMarkup()
  shell.appendChild(conversationLayer)

  mountGlobalConversationAction()
  mountX5ConversationActions()
  mountDeepConversationActions()
  bindConversationEvents()
  renderConversationThreads()
  setConversationThread('project')
  syncConversationPresentationControl()
  syncRailControls()
  installSourceStateObserver()
}

function conversationMarkup() {
  return `
    <aside class="reintegration-conversation-rail" aria-label="Conversation navigation">
      <div class="reintegration-conversation-brand">
        <span class="reintegration-conversation-brand-mark">A</span>
        <div>
          <strong>Autonomous Data Science</strong>
          <small>Telco churn project</small>
        </div>
      </div>

      <button class="reintegration-conversation-search" type="button">
        <span>⌕</span>
        <span>Search conversations</span>
        <kbd>⌘ K</kbd>
      </button>

      <div class="reintegration-conversation-view-switch" role="group" aria-label="Conversation sidebar view">
        <button type="button" data-conversation-rail-option="boxes">Boxes</button>
        <button type="button" data-conversation-rail-option="text">Text</button>
      </div>

      <div class="reintegration-conversation-rail-heading">
        <span>Project conversations</span>
        <button type="button" aria-label="New conversation">+</button>
      </div>

      <div class="reintegration-thread-list" id="reintegration-thread-list"></div>

      <div class="reintegration-conversation-rail-footer">
        <i></i>
        <span>Project state synchronized</span>
      </div>
    </aside>

    <section class="reintegration-conversation-main">
      <header class="reintegration-conversation-header">
        <div class="reintegration-conversation-title">
          <button class="reintegration-conversation-close" id="reintegration-conversation-close" type="button" aria-label="Return to work context">←</button>
          <div class="reintegration-conversation-title-copy">
            <div class="reintegration-conversation-title-row">
              <h2 id="reintegration-conversation-title">General project discussion</h2>
              <span class="reintegration-conversation-scope-pill" id="reintegration-conversation-scope-pill">PROJECT GENERAL</span>
            </div>
            <p class="reintegration-conversation-subtitle" id="reintegration-conversation-subtitle">Project-level conversation with no single WorkUnit home.</p>
          </div>
        </div>

        <div class="reintegration-conversation-actions">
          <button type="button">Find</button>
          <button type="button">Outline</button>
          <button type="button" id="reintegration-conversation-presentation-toggle">Co-present</button>
          <button type="button" id="reintegration-conversation-expand-box">Expand box</button>
          <button type="button" aria-label="More conversation actions">•••</button>
        </div>
      </header>

      <div class="reintegration-conversation-transcript-scroll" id="reintegration-conversation-transcript-scroll">
        <div class="reintegration-conversation-transcript">
          <div class="reintegration-date-divider">Today · current session</div>

          <article class="reintegration-conversation-turn">
            <div class="reintegration-turn-anchor">U</div>
            <div class="reintegration-turn-body">
              <div class="reintegration-turn-meta"><strong>You</strong><span>now</span></div>
              <div class="reintegration-user-message" id="reintegration-conversation-user-message"></div>
              <div class="reintegration-turn-tools"><button type="button">Copy</button><button type="button">Link</button></div>
            </div>
          </article>

          <article class="reintegration-conversation-turn">
            <div class="reintegration-turn-anchor is-ads">A</div>
            <div class="reintegration-turn-body">
              <div class="reintegration-turn-meta"><strong>ADS</strong><span>now</span><span>Reasoning</span></div>
              <div class="reintegration-ads-message">
                <p id="reintegration-conversation-ads-primary"></p>
                <p>Conversation ownership is separate from temporary per-turn context, and opening this workspace does not reset the work surface underneath it.</p>
                <div class="reintegration-project-reference-row">
                  <button class="reintegration-project-ref" type="button"><span>◇</span><span><small>PROJECT OBJECT</small><strong id="reintegration-conversation-primary-ref">Autonomous Data Science</strong></span></button>
                  <button class="reintegration-project-ref" type="button"><span>△</span><span><small>VALIDATION</small><strong>Chronological validation</strong></span></button>
                </div>
                <h3>Current interaction contract</h3>
                <ol>
                  <li>Conversation may take full focus or coexist with the active work surface.</li>
                  <li>Switching threads does not mutate Grid selection, X5 expansion or Deep Dive state.</li>
                  <li>Consequential project truth remains separate from conversational prose.</li>
                </ol>
              </div>
              <div class="reintegration-turn-tools"><button type="button">Copy</button><button type="button">Discuss selection</button><button type="button">•••</button></div>
            </div>
          </article>

          <section class="reintegration-project-change" aria-label="Structured project change">
            <span>↳</span>
            <div>
              <small>PROJECT STATE</small>
              <strong>Underlying work context preserved</strong>
              <p>Conversation presentation does not silently change the project work state.</p>
            </div>
            <button type="button">Open state</button>
          </section>

          <article class="reintegration-conversation-turn">
            <div class="reintegration-turn-anchor">U</div>
            <div class="reintegration-turn-body">
              <div class="reintegration-turn-meta"><strong>You</strong><span>now</span></div>
              <div class="reintegration-user-message">Can I keep working while this conversation remains available?</div>
            </div>
          </article>

          <article class="reintegration-conversation-turn">
            <div class="reintegration-turn-anchor is-ads">A</div>
            <div class="reintegration-turn-body">
              <div class="reintegration-turn-meta"><strong>ADS</strong><span>now</span></div>
              <div class="reintegration-ads-message"><p>Yes. Co-present mode keeps the underlying Grid or specialist workspace mounted and usable, while full-focus mode temporarily gives Conversation the stage.</p></div>
              <details class="reintegration-activity-row"><summary>2 project-aware context actions available</summary></details>
            </div>
          </article>
        </div>
      </div>

      <footer class="reintegration-full-composer">
        <div class="reintegration-full-composer-context">
          <span>HOME</span>
          <button type="button" id="reintegration-conversation-home-chip">Autonomous Data Science project</button>
          <span>WORK CONTEXT PRESERVED</span>
        </div>
        <div class="reintegration-full-composer-shell">
          <textarea rows="2" placeholder="Continue this discussion, bring in evidence, or update project state…"></textarea>
          <div class="reintegration-full-composer-actions">
            <div><button type="button">＋</button><button type="button">Commands</button></div>
            <div><span class="reintegration-full-composer-status"><i></i> Project-aware</span><button class="reintegration-conversation-send" type="button" aria-label="Send">↑</button></div>
          </div>
        </div>
      </footer>
    </section>

    <aside class="reintegration-a6-inspector" id="reintegration-a6-inspector" aria-label="Home WorkUnit inspector">
      <div class="reintegration-a6-head">
        <div><small>HOME WORK UNIT</small><strong id="reintegration-a6-title">WorkUnit context</strong></div>
        <button type="button" id="reintegration-a6-close" aria-label="Collapse WorkUnit inspector">×</button>
      </div>
      <div class="reintegration-a6-home-box" id="reintegration-a6-home-box"></div>
      <section class="reintegration-a6-section"><span>Conversation ownership</span><p>This conversation belongs to this WorkUnit. Referencing another project object does not silently re-home the thread.</p></section>
      <section class="reintegration-a6-section"><span>Contextual detail</span><p id="reintegration-a6-detail">The richer WorkUnit view is available on demand while the reading field stays clean at rest.</p></section>
      <section class="reintegration-a6-section"><span>Integration boundary</span><p class="reintegration-a6-provisional">Exact production inspector internals and persistence remain unfrozen. A6 ownership, explicit expansion and the no-floating-card resting state are held.</p></section>
    </aside>
  `
}

function mountGlobalConversationAction() {
  if (document.querySelector('#global-conversations')) return
  const button = document.createElement('button')
  button.type = 'button'
  button.id = 'global-conversations'
  button.textContent = 'Conversations'
  button.setAttribute('aria-label', 'Open project conversations')
  appearanceToggle?.insertAdjacentElement('beforebegin', button)

  button.addEventListener('click', () => {
    openConversation({ scope: 'project', presentation: 'full', origin: 'grid', trigger: button })
  })
}

function mountX5ConversationActions() {
  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    if (node.querySelector(':scope > .reintegration-x5-chat-action')) continue
    const key = node.dataset.nodeKey
    if (!key) continue

    const button = document.createElement('button')
    button.type = 'button'
    button.className = 'reintegration-x5-chat-action'
    button.dataset.workConversationKey = key
    button.textContent = 'Open conversation'
    button.setAttribute('aria-label', `Open conversation for ${nodeTitle(node)}`)
    button.addEventListener('click', (event) => {
      event.preventDefault()
      event.stopPropagation()
      openConversation({ scope: 'work', nodeKey: key, presentation: 'copresent', origin: 'grid', trigger: button })
    })
    node.appendChild(button)
  }
}

function mountDeepConversationActions() {
  const bar = specialistLayer?.querySelector('.reintegration-specialist-bar')
  const returnButton = document.querySelector('#return-to-project')
  if (!bar || !returnButton || bar.querySelector('.reintegration-deep-conversation-actions')) return

  const actions = document.createElement('div')
  actions.className = 'reintegration-deep-conversation-actions'
  actions.innerHTML = `
    <button type="button" id="deep-global-conversations">Conversations</button>
    <button type="button" id="deep-work-conversation">Chat about this work</button>
  `
  returnButton.insertAdjacentElement('beforebegin', actions)

  actions.querySelector('#deep-global-conversations')?.addEventListener('click', (event) => {
    openConversation({ scope: 'project', presentation: 'copresent', origin: 'deep', trigger: event.currentTarget })
  })
  actions.querySelector('#deep-work-conversation')?.addEventListener('click', (event) => {
    const selected = currentSelectedNode()
    openConversation({
      scope: 'work',
      nodeKey: selected?.dataset.nodeKey || null,
      presentation: 'copresent',
      origin: 'deep',
      trigger: event.currentTarget,
    })
  })
}

function bindConversationEvents() {
  conversationLayer?.querySelector('#reintegration-conversation-close')?.addEventListener('click', closeConversation)
  conversationLayer?.querySelector('#reintegration-conversation-presentation-toggle')?.addEventListener('click', toggleConversationPresentation)
  conversationLayer?.querySelector('#reintegration-conversation-expand-box')?.addEventListener('click', toggleA6Inspector)
  conversationLayer?.querySelector('#reintegration-a6-close')?.addEventListener('click', () => setA6Expanded(false))

  for (const button of conversationLayer?.querySelectorAll('[data-conversation-rail-option]') || []) {
    button.addEventListener('click', () => setRailMode(button.dataset.conversationRailOption || 'boxes', true))
  }

  compactConversationButton?.addEventListener('click', () => {
    openConversation({ scope: 'project', presentation: 'full', origin: 'grid', trigger: compactConversationButton })
  })

  window.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape' || html.dataset.conversationOpen !== 'true') return
    event.preventDefault()
    event.stopImmediatePropagation()
    closeConversation()
  }, true)
}

function renderConversationThreads() {
  const list = conversationLayer?.querySelector('#reintegration-thread-list')
  if (!list) return

  const workNodes = [...document.querySelectorAll(NODE_SELECTOR)]
  const projectButton = document.createElement('button')
  projectButton.type = 'button'
  projectButton.className = 'reintegration-thread-item'
  projectButton.dataset.threadScope = 'project'
  projectButton.innerHTML = `
    <span class="reintegration-project-thread-artifact"><span>P</span><span><small>PROJECT</small><strong>General project discussion</strong></span></span>
    <span class="reintegration-thread-text"><i></i><span><strong>General project discussion</strong><small>Project general</small></span></span>
  `
  projectButton.addEventListener('click', () => setConversationThread('project'))

  list.replaceChildren(projectButton)

  for (const node of workNodes) {
    const key = node.dataset.nodeKey
    if (!key) continue

    const button = document.createElement('button')
    button.type = 'button'
    button.className = 'reintegration-thread-item'
    button.dataset.threadScope = 'work'
    button.dataset.threadNodeKey = key

    const box = document.createElement('span')
    box.className = 'reintegration-thread-box'
    box.appendChild(canonicalConversationNode(node))

    const text = document.createElement('span')
    text.className = 'reintegration-thread-text'
    text.innerHTML = `<i></i><span><strong>${escapeHtml(nodeTitle(node))}</strong><small>${escapeHtml(nodeKind(node))} · ${escapeHtml(node.dataset.statusCode || 'NONE')}</small></span>`

    button.append(box, text)
    button.addEventListener('click', () => setConversationThread('work', key))
    list.appendChild(button)
  }

  syncActiveThreadUi()
}

function refreshCanonicalArtifacts() {
  if (!conversationLayer) return

  for (const button of conversationLayer.querySelectorAll('[data-thread-node-key]')) {
    const source = nodeByKey(button.dataset.threadNodeKey)
    const host = button.querySelector('.reintegration-thread-box')
    if (!source || !host) continue
    host.replaceChildren(canonicalConversationNode(source))

    const textStrong = button.querySelector('.reintegration-thread-text strong')
    const textSmall = button.querySelector('.reintegration-thread-text small')
    if (textStrong) textStrong.textContent = nodeTitle(source)
    if (textSmall) textSmall.textContent = `${nodeKind(source)} · ${source.dataset.statusCode || 'NONE'}`
  }

  if (activeScope === 'work') refreshA6HomeBox()
}

function canonicalConversationNode(source) {
  const clone = source.cloneNode(true)
  const categoryClass = [...source.classList].find((value) => value.startsWith('category-')) || ''
  clone.className = `grammar-node custom-node conversation-canonical-node ${categoryClass}`.trim()
  clone.removeAttribute('id')
  clone.removeAttribute('tabindex')
  clone.removeAttribute('role')
  clone.removeAttribute('aria-label')
  clone.dataset.selected = 'false'
  clone.dataset.expanded = 'false'
  clone.dataset.selectionStyle = 'sel2'
  clone.querySelectorAll('[id]').forEach((element) => element.removeAttribute('id'))
  clone.querySelectorAll('.reintegration-x5-chat-action').forEach((element) => element.remove())
  clone.querySelectorAll('button').forEach((button) => {
    button.tabIndex = -1
    button.setAttribute('aria-hidden', 'true')
  })
  return clone
}

function openConversation({ scope, nodeKey = null, presentation = 'full', origin = 'grid', trigger = null }) {
  if (!conversationLayer) return
  returnFocusElement = trigger instanceof HTMLElement ? trigger : document.activeElement
  html.dataset.conversationSource = origin === 'deep' || html.dataset.deepFocus === 'focused' ? 'deep' : 'grid'
  html.dataset.conversationPresentation = presentation === 'copresent' ? 'copresent' : 'full'
  html.dataset.conversationOpen = 'true'
  conversationLayer.setAttribute('aria-hidden', 'false')
  setA6Expanded(false)

  if (scope === 'work') {
    const resolved = nodeByKey(nodeKey) || currentSelectedNode()
    if (resolved) setConversationThread('work', resolved.dataset.nodeKey)
    else setConversationThread('project')
  } else {
    setConversationThread('project')
  }

  refreshCanonicalArtifacts()
  syncConversationPresentationControl()
  requestAnimationFrame(() => conversationLayer?.querySelector('#reintegration-conversation-close')?.focus({ preventScroll: true }))
}

function closeConversation() {
  if (!conversationLayer || html.dataset.conversationOpen !== 'true') return
  html.dataset.conversationOpen = 'false'
  html.dataset.conversationA6Expanded = 'false'
  conversationLayer.setAttribute('aria-hidden', 'true')
  resetIntegrationBoundaryNote()

  requestAnimationFrame(() => {
    if (returnFocusElement instanceof HTMLElement && returnFocusElement.isConnected) {
      returnFocusElement.focus({ preventScroll: true })
    } else if (html.dataset.deepFocus === 'focused') {
      document.querySelector('#return-to-project')?.focus({ preventScroll: true })
    } else {
      stage?.focus({ preventScroll: true })
    }
  })
}

function setConversationThread(scope, nodeKey = null) {
  if (!conversationLayer) return
  const isWork = scope === 'work' && Boolean(nodeByKey(nodeKey))
  activeScope = isWork ? 'work' : 'project'
  activeWorkKey = isWork ? nodeKey : null
  html.dataset.conversationScope = activeScope
  setA6Expanded(false)

  const title = conversationLayer.querySelector('#reintegration-conversation-title')
  const subtitle = conversationLayer.querySelector('#reintegration-conversation-subtitle')
  const pill = conversationLayer.querySelector('#reintegration-conversation-scope-pill')
  const userMessage = conversationLayer.querySelector('#reintegration-conversation-user-message')
  const adsPrimary = conversationLayer.querySelector('#reintegration-conversation-ads-primary')
  const primaryRef = conversationLayer.querySelector('#reintegration-conversation-primary-ref')
  const homeChip = conversationLayer.querySelector('#reintegration-conversation-home-chip')
  const expandButton = conversationLayer.querySelector('#reintegration-conversation-expand-box')

  if (activeScope === 'work') {
    const node = nodeByKey(activeWorkKey)
    const name = node ? nodeTitle(node) : 'Current WorkUnit'
    if (title) title.textContent = name
    if (subtitle) subtitle.textContent = 'Conversation anchored to one WorkUnit. Other objects can be referenced without changing its home.'
    if (pill) pill.textContent = 'WORK UNIT'
    if (userMessage) userMessage.textContent = `I want to continue the ${name} discussion while preserving the work surface I came from.`
    if (adsPrimary) adsPrimary.innerHTML = `This thread has <strong>${escapeHtml(name)}</strong> as its persistent home. The active Grid or Deep Dive state remains preserved underneath Conversation.`
    if (primaryRef) primaryRef.textContent = name
    if (homeChip) homeChip.textContent = `◇ ${name}`
    if (expandButton) expandButton.hidden = false
    refreshA6HomeBox()
  } else {
    if (title) title.textContent = 'General project discussion'
    if (subtitle) subtitle.textContent = 'Project-level conversation with no single WorkUnit home.'
    if (pill) pill.textContent = 'PROJECT GENERAL'
    if (userMessage) userMessage.textContent = 'I want to discuss the project broadly without attaching this conversation to whichever WorkUnit is currently visible.'
    if (adsPrimary) adsPrimary.innerHTML = 'This is a <strong>project-general conversation</strong>. It may reference any WorkUnit without becoming owned by the current selection or Deep Dive source.'
    if (primaryRef) primaryRef.textContent = 'Autonomous Data Science'
    if (homeChip) homeChip.textContent = 'Autonomous Data Science project'
    if (expandButton) expandButton.hidden = true
    conversationLayer.querySelector('#reintegration-a6-home-box')?.replaceChildren()
  }

  syncActiveThreadUi()
}

function syncActiveThreadUi() {
  if (!conversationLayer) return
  for (const button of conversationLayer.querySelectorAll('.reintegration-thread-item')) {
    const active = activeScope === 'project'
      ? button.dataset.threadScope === 'project'
      : button.dataset.threadScope === 'work' && button.dataset.threadNodeKey === activeWorkKey
    button.classList.toggle('is-active', active)
  }
}

function toggleConversationPresentation() {
  const next = html.dataset.conversationPresentation === 'copresent' ? 'full' : 'copresent'
  html.dataset.conversationPresentation = next
  syncConversationPresentationControl()
}

function syncConversationPresentationControl() {
  const button = conversationLayer?.querySelector('#reintegration-conversation-presentation-toggle')
  if (!button) return
  const copresent = html.dataset.conversationPresentation === 'copresent'
  button.textContent = copresent ? 'Full focus' : 'Co-present'
  button.setAttribute('aria-pressed', String(copresent))
}

function toggleA6Inspector() {
  if (activeScope !== 'work') return
  setA6Expanded(html.dataset.conversationA6Expanded !== 'true')
}

function setA6Expanded(expanded) {
  const next = activeScope === 'work' && Boolean(expanded)
  html.dataset.conversationA6Expanded = String(next)
  const button = conversationLayer?.querySelector('#reintegration-conversation-expand-box')
  if (button) {
    button.textContent = next ? 'Collapse box' : 'Expand box'
    button.setAttribute('aria-pressed', String(next))
  }
  if (next) refreshA6HomeBox()
}

function refreshA6HomeBox() {
  if (!conversationLayer || activeScope !== 'work') return
  const node = nodeByKey(activeWorkKey)
  const host = conversationLayer.querySelector('#reintegration-a6-home-box')
  const title = conversationLayer.querySelector('#reintegration-a6-title')
  const detail = conversationLayer.querySelector('#reintegration-a6-detail')
  if (!node || !host) return

  host.replaceChildren(canonicalConversationNode(node))
  if (title) title.textContent = nodeTitle(node)

  const cells = [...node.querySelectorAll('.detail-layer .detail-cell strong')]
    .map((element) => element.textContent?.trim())
    .filter(Boolean)
  if (detail) detail.textContent = cells.length ? cells.join(' · ') : nodeSubtitle(node)
}

function setRailMode(mode, persist = false) {
  const resolved = mode === 'text' ? 'text' : 'boxes'
  html.dataset.conversationRail = resolved
  syncRailControls()

  if (persist) {
    try {
      window.localStorage.setItem(RAIL_STORAGE_KEY, resolved === 'text' ? 'text' : 'artifact')
    } catch {
      // Session-local fallback is sufficient for this design-lab integration.
    }
  }
}

function syncRailControls() {
  const resolved = html.dataset.conversationRail === 'text' ? 'text' : 'boxes'
  for (const button of conversationLayer?.querySelectorAll('[data-conversation-rail-option]') || []) {
    button.setAttribute('aria-pressed', String(button.dataset.conversationRailOption === resolved))
  }
}

function readInitialRailMode() {
  try {
    return window.localStorage.getItem(RAIL_STORAGE_KEY) === 'text' ? 'text' : 'boxes'
  } catch {
    return 'boxes'
  }
}

function installSourceStateObserver() {
  const host = document.querySelector('#expansion-practical-nodes')
  if (!host || !('MutationObserver' in window)) return

  sourceMutationObserver = new MutationObserver((mutations) => {
    if (!mutations.some((mutation) => mutation.type === 'attributes')) return
    refreshCanonicalArtifacts()
  })
  sourceMutationObserver.observe(host, {
    subtree: true,
    attributes: true,
    attributeFilter: [
      'data-selected',
      'data-expanded',
      'data-state',
      'data-status-code',
      'data-status-source',
      'data-status-carrier',
      'data-priority',
    ],
  })
}

function currentSelectedNode() {
  return document.querySelector(`${NODE_SELECTOR}[data-selected="true"]`)
}

function nodeByKey(key) {
  if (!key) return null
  return document.querySelector(`${NODE_SELECTOR}[data-node-key="${cssEscape(key)}"]`)
}

function nodeTitle(node) {
  return node?.querySelector('.node-surface > strong')?.textContent?.trim() || node?.dataset.nodeKey || 'WorkUnit'
}

function nodeKind(node) {
  return node?.querySelector('.unit-kind')?.textContent?.trim() || 'WorkUnit'
}

function nodeSubtitle(node) {
  return node?.querySelector('.node-surface > small')?.textContent?.trim() || 'Project work context'
}

function resetIntegrationBoundaryNote() {
  if (!provisionalNote) return
  const strong = provisionalNote.querySelector('strong')
  const small = provisionalNote.querySelector('small')
  if (strong) strong.textContent = 'Shell geometry is provisional'
  if (small) small.textContent = 'Accepted WorkUnit/world/X5/Z7/relation and Quiet Graphite Conversation sources are reused or exactly ported. HUD, stage size, controls and co-present width remain provisional.'
}

function cssEscape(value) {
  if (window.CSS?.escape) return window.CSS.escape(String(value))
  return String(value).replaceAll('"', '\\"')
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;')
}
