/*
 * Source-faithful M09 integration adapter.
 *
 * Accepted source:
 *   da115b74de526fca05ed6f468bef39bdb801355c
 *   frontend/design-lab/work-unit-process-focus.{html,css,js}
 *
 * This adapter ports the accepted current-process focus lens onto the canonical
 * integrated WorkUnit DOM rather than rebuilding a second WorkUnit fixture.
 * Focus membership remains view composition only. It never mutates category,
 * project disposition, operational status, attention, SEL2 selection or X5.
 *
 * The small panel used to exercise the capability is provisional shell glue.
 * Persistence is intentionally omitted because production ownership remains
 * unfrozen and the accepted fixture's localStorage was proof-of-concept only.
 */

const root = document.documentElement
const stage = document.querySelector('#reintegration-stage')
const tools = document.querySelector('.reintegration-tools')
const relationSvg = document.querySelector('#reintegration-relations')
const nodeContainer = document.querySelector('#expansion-practical-nodes')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const appearanceToggle = document.querySelector('#appearance-controls-toggle')

const NODE_SELECTOR = '.expansion-practical-node'
const DEFAULT_FOCUS_KEYS = new Set(['q', 'i', 'v'])
const focusMembership = new Set(DEFAULT_FOCUS_KEYS)

root.dataset.processFocus = root.dataset.processFocus || 'context'
root.dataset.focusEdit = root.dataset.focusEdit || 'off'

installStylesheet()
mountFocusControl()
applyDefaultMembership()
installMembershipControls()
syncRelationFocusClasses()
syncFocusUi()

/*
 * The stylesheet is now statically linked by the integrated browser so focus
 * presentation is ready before interaction. Keep this installer as a defensive
 * fallback for historical or isolated fixture entry points.
 */
function installStylesheet() {
  if (document.querySelector('link[href="./cockpit-reintegration-process-focus.css"]')) return
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = './cockpit-reintegration-process-focus.css'
  document.head.appendChild(link)
}

function mountFocusControl() {
  if (!stage || !tools || document.querySelector('#process-focus-toggle')) return

  const toggle = document.createElement('button')
  toggle.type = 'button'
  toggle.id = 'process-focus-toggle'
  toggle.textContent = 'Focus'
  toggle.setAttribute('aria-expanded', 'false')
  toggle.setAttribute('aria-controls', 'reintegration-process-focus-panel')

  const appearance = tools.querySelector('#appearance-controls-toggle')
  tools.insertBefore(toggle, appearance || null)

  const panel = document.createElement('aside')
  panel.id = 'reintegration-process-focus-panel'
  panel.className = 'reintegration-process-focus-panel'
  panel.hidden = true
  panel.setAttribute('aria-label', 'Current process focus lens')
  panel.innerHTML = `
    <div class="reintegration-focus-head">
      <div>
        <span>ACCEPTED VIEW CAPABILITY · PROVISIONAL PANEL</span>
        <strong>Current process focus</strong>
      </div>
      <button type="button" id="process-focus-close" aria-label="Close current process focus controls">×</button>
    </div>
    <p>Disposition, focus membership and semantic state remain independent. The focus set below changes only the current view composition.</p>
    <div class="reintegration-focus-modes" role="group" aria-label="Current process focus mode">
      <button type="button" data-process-focus-mode="context" aria-pressed="true">Context visible</button>
      <button type="button" data-process-focus-mode="focused" aria-pressed="false">Focus current process</button>
    </div>
    <div class="reintegration-focus-edit-row">
      <div>
        <strong>Edit focus set</strong>
        <small>Reveal a membership control on each WorkUnit. Membership changes do not change the WorkUnit itself.</small>
      </div>
      <button type="button" id="process-focus-edit" aria-pressed="false">Edit focus set</button>
    </div>
    <div class="reintegration-focus-summary">
      <span>CURRENT LENS</span>
      <strong id="process-focus-summary">Context visible</strong>
      <small id="process-focus-membership-summary">3 in focus · 3 context</small>
    </div>
    <button type="button" id="process-focus-reset">Reset example membership</button>
  `
  stage.appendChild(panel)

  toggle.addEventListener('click', () => setFocusPanelOpen(panel.hidden))
  panel.querySelector('#process-focus-close')?.addEventListener('click', () => setFocusPanelOpen(false))

  for (const button of panel.querySelectorAll('[data-process-focus-mode]')) {
    button.addEventListener('click', () => {
      root.dataset.processFocus = button.dataset.processFocusMode === 'focused' ? 'focused' : 'context'
      syncNodeFocusMembership()
      syncRelationFocusClasses()
      syncFocusUi()
    })
  }

  panel.querySelector('#process-focus-edit')?.addEventListener('click', () => {
    root.dataset.focusEdit = root.dataset.focusEdit === 'on' ? 'off' : 'on'
    syncFocusUi()
  })

  panel.querySelector('#process-focus-reset')?.addEventListener('click', () => {
    applyDefaultMembership()
    syncRelationFocusClasses()
    syncFocusUi()
  })
}

function setFocusPanelOpen(open) {
  const panel = document.querySelector('#reintegration-process-focus-panel')
  const toggle = document.querySelector('#process-focus-toggle')
  if (!panel || !toggle) return

  panel.hidden = !open
  toggle.setAttribute('aria-expanded', String(open))

  if (open && appearancePanel && !appearancePanel.hidden) {
    appearancePanel.hidden = true
    appearanceToggle?.setAttribute('aria-expanded', 'false')
  }
}

/*
 * Membership is owned by one explicit set rather than by whichever DOM nodes
 * happen to be mounted at the moment. This matters because the integrated
 * Cockpit can rebuild WorkUnit DOM while preserving project semantics. Newly
 * mounted nodes must immediately recover the same view-composition membership.
 */
function applyDefaultMembership() {
  focusMembership.clear()
  for (const key of DEFAULT_FOCUS_KEYS) focusMembership.add(key)
  syncNodeFocusMembership()
}

function syncNodeFocusMembership() {
  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    const key = node.dataset.nodeKey || ''
    node.dataset.processScope = focusMembership.has(key) ? 'current' : 'context'
    syncMembershipControl(node)
  }
}

function installMembershipControls() {
  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    if (node.querySelector('.reintegration-focus-membership-toggle')) continue
    const surface = node.querySelector('.node-surface')
    if (!surface) continue

    const button = document.createElement('button')
    button.type = 'button'
    button.className = 'reintegration-focus-membership-toggle'
    button.dataset.focusMembershipToggle = node.dataset.nodeKey || ''
    surface.appendChild(button)
    syncMembershipControl(node)

    button.addEventListener('pointerdown', (event) => event.stopPropagation())
    button.addEventListener('click', (event) => {
      event.stopPropagation()
      const key = node.dataset.nodeKey || ''
      if (!key) return

      if (focusMembership.has(key)) focusMembership.delete(key)
      else focusMembership.add(key)

      syncNodeFocusMembership()
      syncRelationFocusClasses()
      syncFocusUi()
    })
  }
}

function syncMembershipControl(node) {
  const button = node.querySelector('.reintegration-focus-membership-toggle')
  if (!button) return

  const title = node.querySelector('.node-surface > strong')?.textContent?.trim() || 'WorkUnit'
  const inFocus = node.dataset.processScope === 'current'
  button.textContent = inFocus ? '− FOCUS' : '+ FOCUS'
  button.setAttribute('aria-label', `${inFocus ? 'Remove' : 'Add'} ${title} ${inFocus ? 'from' : 'to'} current focus`)
  button.title = inFocus ? 'Remove from current focus' : 'Add to current focus'
}

function syncRelationFocusClasses() {
  if (!relationSvg) return

  for (const relation of relationSvg.querySelectorAll('.reintegration-relation')) {
    const source = document.querySelector(`${NODE_SELECTOR}[data-node-key="${relation.dataset.source}"]`)
    const target = document.querySelector(`${NODE_SELECTOR}[data-node-key="${relation.dataset.target}"]`)
    const contextEdge = source?.dataset.processScope === 'context' || target?.dataset.processScope === 'context'
    relation.classList.toggle('is-context-edge', Boolean(contextEdge))
    relation.classList.toggle('is-current-edge', !contextEdge)
  }
}

function syncFocusUi() {
  const focused = root.dataset.processFocus === 'focused'
  const editing = root.dataset.focusEdit === 'on'

  for (const button of document.querySelectorAll('[data-process-focus-mode]')) {
    button.setAttribute('aria-pressed', String(button.dataset.processFocusMode === (focused ? 'focused' : 'context')))
  }

  const editButton = document.querySelector('#process-focus-edit')
  if (editButton) {
    editButton.setAttribute('aria-pressed', String(editing))
    editButton.textContent = editing ? 'Done editing' : 'Edit focus set'
  }

  const summary = document.querySelector('#process-focus-summary')
  if (summary) summary.textContent = focused ? 'Focus current process' : 'Context visible'

  const nodes = [...document.querySelectorAll(NODE_SELECTOR)]
  const currentCount = nodes.filter((node) => node.dataset.processScope === 'current').length
  const membershipSummary = document.querySelector('#process-focus-membership-summary')
  if (membershipSummary) membershipSummary.textContent = `${currentCount} in focus · ${nodes.length - currentCount} context`
}

/*
 * Accepted M09 focus recession must remain synchronized with E5 relation
 * composition. Existing relation geometry can be regenerated by other adapters,
 * so classify newly mounted relation groups without taking ownership of their
 * semantic direction or relation class.
 */
if (relationSvg && 'MutationObserver' in window) {
  const relationObserver = new MutationObserver(() => syncRelationFocusClasses())
  relationObserver.observe(relationSvg, { childList: true, subtree: false })
}

/*
 * WorkUnit carriers may also be replaced while the project state itself remains
 * unchanged. Recover focus scope and membership controls whenever that happens,
 * then resynchronize relation recession from the repaired node state.
 */
if (nodeContainer && 'MutationObserver' in window) {
  const nodeObserver = new MutationObserver(() => {
    syncNodeFocusMembership()
    installMembershipControls()
    syncRelationFocusClasses()
    syncFocusUi()
  })
  nodeObserver.observe(nodeContainer, { childList: true, subtree: false })
}

/* Panels are bounded view surfaces. Deep focus or Conversation takes ownership. */
if ('MutationObserver' in window) {
  const ownershipObserver = new MutationObserver(() => {
    if (root.dataset.deepFocus !== 'false' || root.dataset.conversationOpen === 'true') {
      setFocusPanelOpen(false)
      root.dataset.focusEdit = 'off'
      syncFocusUi()
    }
  })
  ownershipObserver.observe(root, {
    attributes: true,
    attributeFilter: ['data-deep-focus', 'data-conversation-open'],
  })
}
