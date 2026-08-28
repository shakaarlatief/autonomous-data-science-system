/*
 * Phase-C reintegration completion adapter.
 *
 * This file closes confirmed fidelity omissions without replacing accepted
 * component sources. It is intentionally loaded after the existing composition
 * adapters so it can repair fixture-level regressions at the holistic boundary.
 */

const root = document.documentElement
const world = document.querySelector('#reintegration-world')
const relationSvg = document.querySelector('#reintegration-relations')
const appearancePanel = document.querySelector('#reintegration-appearance-panel')
const appearanceReset = document.querySelector('#appearance-reset')
const specialistLayer = document.querySelector('#reintegration-specialist-layer')
const specialistBarCopy = specialistLayer?.querySelector('.reintegration-specialist-bar > div')

const NODE_SELECTOR = '.expansion-practical-node'
const SVG_NS = 'http://www.w3.org/2000/svg'
const TERMINAL_OUTSET = 2

const l0Supplement = {
  q: {
    cause: 'Human target-definition decision is unresolved',
    activity: 'Human decision requested',
  },
  i: {
    cause: 'Resolve target definition',
    activity: 'Missingness profile generated',
  },
  v: {
    cause: 'Production prerequisites remain upstream',
    activity: 'Chronological split specification prepared',
  },
  m: {
    cause: 'Latest execution attempt failed',
    activity: 'Failure diagnostics available for inspection',
  },
  r: {
    cause: 'No blocking cause',
    activity: 'Schema profile is running',
  },
  e: {
    cause: 'Model comparison remains pending',
    activity: 'Calibration review deferred',
  },
}

root.dataset.relationPresentation = root.dataset.relationPresentation || 'class-tag'
root.dataset.connectorTerminal = root.dataset.connectorTerminal || 'arrows'
root.dataset.internalLayout = 'l0'

removeRejectedPointPackets()
repairH4PerimeterSweep()
restoreP7ToneBinding()
restoreBlocksRelationSemantics()
restoreL0WorkingLayout()
mountAppearancePresets()
mountRelationshipPresentationControls()
prepareConnectorTerminals()
installRelationshipHoverColor()
restoreConversationRailContainment()
installSpecialistCategoryIdentity()
syncCompletionControls()

/* -------------------------------------------------------------------------- */
/* G4: remove the two isolated green point packets rejected in holistic review */
/* -------------------------------------------------------------------------- */

function removeRejectedPointPackets() {
  if (!world) return
  world.querySelectorAll('.live-packet').forEach((element) => element.remove())

  /* Prevent a later fixture-level re-mount from bringing them back. */
  if ('MutationObserver' in window) {
    const observer = new MutationObserver(() => {
      world.querySelectorAll('.live-packet').forEach((element) => element.remove())
    })
    observer.observe(world, { childList: true, subtree: false })
  }
}

/* -------------------------------------------------------------------------- */
/* H4: exact accepted perimeter sweep target rather than node-level class bug  */
/* -------------------------------------------------------------------------- */

function repairH4PerimeterSweep() {
  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    if (node.dataset.h4SweepRecovery === 'true') continue
    node.dataset.h4SweepRecovery = 'true'

    node.addEventListener('pointerenter', () => {
      if (root.dataset.reduced === 'on') return
      const sweep = node.querySelector('.perimeter-sweep')
      if (!sweep) return

      sweep.classList.remove('sweep-active')
      /* Accepted H4 intentionally restarts the one-shot sweep on entry. */
      void sweep.getBoundingClientRect().width
      sweep.classList.add('sweep-active')
      window.setTimeout(() => sweep.classList.remove('sweep-active'), 900)
    })
  }
}

/* -------------------------------------------------------------------------- */
/* P7: the selected design is Neutral Tag + Tone, not Neutral Tag alone       */
/* -------------------------------------------------------------------------- */

function restoreP7ToneBinding() {
  root.dataset.dispositionEncoding = 'p7'
}

/* -------------------------------------------------------------------------- */
/* BLOCKER -> BLOCKS -> BLOCKED                                               */
/* -------------------------------------------------------------------------- */

function restoreBlocksRelationSemantics() {
  const group = relationSvg?.querySelector('.reintegration-relation[data-relation-id="q-i"]')
  if (!group) return

  group.dataset.relationClass = 'blocks'
  group.style.setProperty('--class-rgb', '237, 112, 105')
  const text = group.querySelector('.semantic-tag-text')
  if (text) text.textContent = 'BLOCKS'
}

/* -------------------------------------------------------------------------- */
/* L0 provisional working internal layout                                     */
/* -------------------------------------------------------------------------- */

function restoreL0WorkingLayout() {
  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    const supplement = l0Supplement[node.dataset.nodeKey || '']
    if (!supplement) continue

    node.dataset.internalLayout = 'l0'
    for (const grid of node.querySelectorAll('.detail-grid')) {
      if (grid.querySelector('[data-l0-field="blocking-cause"]')) continue
      grid.insertAdjacentHTML('beforeend', `
        <div class="detail-cell" data-l0-field="blocking-cause"><span>Blocking cause</span><strong>${escapeHtml(supplement.cause)}</strong></div>
        <div class="detail-cell" data-l0-field="recent-activity"><span>Recent activity</span><strong>${escapeHtml(supplement.activity)}</strong></div>
      `)
    }
  }
}

/* -------------------------------------------------------------------------- */
/* Foundation 023 appearance presets                                          */
/* -------------------------------------------------------------------------- */

function mountAppearancePresets() {
  if (!appearancePanel || appearancePanel.querySelector('[data-integration-setting="appearance-presets"]')) return

  const fieldset = document.createElement('fieldset')
  fieldset.className = 'reintegration-setting'
  fieldset.dataset.integrationSetting = 'appearance-presets'
  fieldset.innerHTML = `
    <legend>Appearance preset</legend>
    <div class="reintegration-setting-options">
      <button type="button" data-appearance-preset="clean" aria-pressed="false">Clean</button>
      <button type="button" data-appearance-preset="structured" aria-pressed="false">Structured</button>
      <button type="button" data-appearance-preset="rich" aria-pressed="true">Rich</button>
    </div>
    <small class="reintegration-setting-note">Clean = Normal + None · Structured = Subtle shape + None · Rich = Subtle shape + Material.</small>
  `

  const firstSetting = appearancePanel.querySelector('.reintegration-setting')
  appearancePanel.insertBefore(fieldset, firstSetting || appearanceReset)

  fieldset.querySelectorAll('[data-appearance-preset]').forEach((button) => {
    button.addEventListener('click', () => applyAppearancePreset(button.dataset.appearancePreset || 'rich'))
  })

  appearanceReset?.addEventListener('click', () => window.setTimeout(syncAppearancePresetControl, 0))
}

function applyAppearancePreset(preset) {
  const values = {
    clean: { shape: 'normal', surface: 'none' },
    structured: { shape: 'true', surface: 'none' },
    rich: { shape: 'true', surface: 'material' },
  }[preset] || { shape: 'true', surface: 'material' }

  root.dataset.shapeStyle = values.shape
  root.dataset.surfaceStyle = values.surface
  syncNativeAppearanceButtons()
  syncAppearancePresetControl()
}

function syncNativeAppearanceButtons() {
  document.querySelectorAll('[data-shape-option]').forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.shapeOption === root.dataset.shapeStyle))
  })
  document.querySelectorAll('[data-surface-option]').forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.surfaceOption === root.dataset.surfaceStyle))
  })
}

function syncAppearancePresetControl() {
  const preset = root.dataset.shapeStyle === 'normal' && root.dataset.surfaceStyle === 'none'
    ? 'clean'
    : root.dataset.shapeStyle === 'true' && root.dataset.surfaceStyle === 'none'
      ? 'structured'
      : root.dataset.shapeStyle === 'true' && root.dataset.surfaceStyle === 'material'
        ? 'rich'
        : ''

  document.querySelectorAll('[data-appearance-preset]').forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.appearancePreset === preset))
  })
}

/* -------------------------------------------------------------------------- */
/* Relation-class presentation + connector terminal presentation              */
/* -------------------------------------------------------------------------- */

function mountRelationshipPresentationControls() {
  if (!appearancePanel || appearancePanel.querySelector('[data-integration-setting="relationship-presentation"]')) return

  const relationFieldset = document.createElement('fieldset')
  relationFieldset.className = 'reintegration-setting'
  relationFieldset.dataset.integrationSetting = 'relationship-presentation'
  relationFieldset.innerHTML = `
    <legend>Relationship lines</legend>
    <div class="reintegration-setting-options two">
      <button type="button" data-relation-presentation-option="neutral-hover" aria-pressed="false">Neutral + hover</button>
      <button type="button" data-relation-presentation-option="class-tag" aria-pressed="true">Hue + tags</button>
    </div>
    <small class="reintegration-setting-note">Neutral + hover removes relation-class color and tags at rest. Hovering a WorkUnit colors its related lines with that WorkUnit's category color. Relationship meaning is unchanged.</small>
  `

  const terminalFieldset = document.createElement('fieldset')
  terminalFieldset.className = 'reintegration-setting'
  terminalFieldset.dataset.integrationSetting = 'connector-terminal'
  terminalFieldset.innerHTML = `
    <legend>Connector endpoint treatment</legend>
    <div class="reintegration-setting-options two">
      <button type="button" data-connector-terminal-option="clean" aria-pressed="false">Clean</button>
      <button type="button" data-connector-terminal-option="dots" aria-pressed="false">Micro dots</button>
      <button type="button" data-connector-terminal-option="sockets" aria-pressed="false">Frame sockets</button>
      <button type="button" data-connector-terminal-option="arrows" aria-pressed="true">Direction arrows</button>
    </div>
    <small class="reintegration-setting-note">Exactly one endpoint treatment is active. Directionality remains system-owned even when visual arrows are hidden.</small>
  `

  const pendingConnector = [...appearancePanel.querySelectorAll('.reintegration-pending-setting')]
    .find((element) => element.querySelector('strong')?.textContent?.includes('Connector presentation'))

  if (pendingConnector) {
    pendingConnector.before(relationFieldset, terminalFieldset)
    pendingConnector.remove()
  } else {
    appearancePanel.insertBefore(relationFieldset, appearanceReset)
    appearancePanel.insertBefore(terminalFieldset, appearanceReset)
  }

  relationFieldset.querySelectorAll('[data-relation-presentation-option]').forEach((button) => {
    button.addEventListener('click', () => {
      root.dataset.relationPresentation = button.dataset.relationPresentationOption || 'class-tag'
      syncRelationshipControls()
    })
  })

  terminalFieldset.querySelectorAll('[data-connector-terminal-option]').forEach((button) => {
    button.addEventListener('click', () => {
      root.dataset.connectorTerminal = button.dataset.connectorTerminalOption || 'arrows'
      syncRelationshipControls()
    })
  })

  appearanceReset?.addEventListener('click', () => {
    root.dataset.relationPresentation = 'class-tag'
    root.dataset.connectorTerminal = 'arrows'
    syncRelationshipControls()
  })
}

function prepareConnectorTerminals() {
  if (!relationSvg) return

  for (const group of relationSvg.querySelectorAll('.reintegration-relation')) {
    if (!group.querySelector('.reintegration-source-dot')) {
      const sourceDot = document.createElementNS(SVG_NS, 'circle')
      sourceDot.classList.add('reintegration-terminal-dot', 'reintegration-source-dot')
      sourceDot.setAttribute('r', '2.6')

      const targetDot = document.createElementNS(SVG_NS, 'circle')
      targetDot.classList.add('reintegration-terminal-dot', 'reintegration-target-dot')
      targetDot.setAttribute('r', '2.6')

      const sourceSocket = document.createElementNS(SVG_NS, 'rect')
      sourceSocket.classList.add('reintegration-terminal-socket', 'reintegration-source-socket')
      sourceSocket.setAttribute('width', '5.2')
      sourceSocket.setAttribute('height', '5.2')
      sourceSocket.setAttribute('rx', '1.1')

      const targetSocket = document.createElementNS(SVG_NS, 'rect')
      targetSocket.classList.add('reintegration-terminal-socket', 'reintegration-target-socket')
      targetSocket.setAttribute('width', '5.2')
      targetSocket.setAttribute('height', '5.2')
      targetSocket.setAttribute('rx', '1.1')

      const tag = group.querySelector('.semantic-tag')
      group.insertBefore(sourceDot, tag || null)
      group.insertBefore(targetDot, tag || null)
      group.insertBefore(sourceSocket, tag || null)
      group.insertBefore(targetSocket, tag || null)
    }

    syncConnectorTerminalGeometry(group)
  }

  if ('MutationObserver' in window) {
    const observer = new MutationObserver((mutations) => {
      const groups = new Set()
      for (const mutation of mutations) {
        if (!(mutation.target instanceof Element)) continue
        if (mutation.attributeName !== 'd' || !mutation.target.matches('.semantic-path')) continue
        const group = mutation.target.closest('.reintegration-relation')
        if (group) groups.add(group)
      }
      groups.forEach((group) => syncConnectorTerminalGeometry(group))
    })
    observer.observe(relationSvg, { subtree: true, attributes: true, attributeFilter: ['d'] })
  }
}

function syncConnectorTerminalGeometry(group) {
  const path = group.querySelector('.semantic-path')
  if (!path) return

  let length = 0
  try {
    length = path.getTotalLength()
  } catch {
    return
  }
  if (!Number.isFinite(length) || length <= 0) return

  const start = path.getPointAtLength(0)
  const startTangent = path.getPointAtLength(Math.min(8, length))
  const end = path.getPointAtLength(length)
  const endTangent = path.getPointAtLength(Math.max(0, length - Math.min(8, length)))

  const sourceVector = normalize(start.x - startTangent.x, start.y - startTangent.y)
  const targetVector = normalize(end.x - endTangent.x, end.y - endTangent.y)
  const sourceDot = {
    x: start.x + sourceVector.x * TERMINAL_OUTSET,
    y: start.y + sourceVector.y * TERMINAL_OUTSET,
  }
  const targetDot = {
    x: end.x + targetVector.x * TERMINAL_OUTSET,
    y: end.y + targetVector.y * TERMINAL_OUTSET,
  }

  positionCircle(group.querySelector('.reintegration-source-dot'), sourceDot)
  positionCircle(group.querySelector('.reintegration-target-dot'), targetDot)
  positionSocket(group.querySelector('.reintegration-source-socket'), start)
  positionSocket(group.querySelector('.reintegration-target-socket'), end)
}

function installRelationshipHoverColor() {
  if (!relationSvg) return

  for (const node of document.querySelectorAll(NODE_SELECTOR)) {
    if (node.dataset.relationHoverCompletion === 'true') continue
    node.dataset.relationHoverCompletion = 'true'

    node.addEventListener('pointerenter', () => {
      const key = node.dataset.nodeKey || ''
      const rgb = getComputedStyle(node).getPropertyValue('--node-rgb').trim() || node.style.getPropertyValue('--node-rgb').trim()
      if (!key || !rgb) return

      for (const group of relationSvg.querySelectorAll('.reintegration-relation')) {
        if (group.dataset.source === key || group.dataset.target === key) {
          group.style.setProperty('--hover-rgb', rgb)
        }
      }
    })

    node.addEventListener('pointerleave', () => {
      const key = node.dataset.nodeKey || ''
      for (const group of relationSvg.querySelectorAll('.reintegration-relation')) {
        if (group.dataset.source === key || group.dataset.target === key) {
          group.style.removeProperty('--hover-rgb')
        }
      }
    })
  }
}

function syncRelationshipControls() {
  document.querySelectorAll('[data-relation-presentation-option]').forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.relationPresentationOption === root.dataset.relationPresentation))
  })
  document.querySelectorAll('[data-connector-terminal-option]').forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.connectorTerminalOption === root.dataset.connectorTerminal))
  })
}

/* -------------------------------------------------------------------------- */
/* Quiet Graphite / A6 canonical Boxes rail                                   */
/* -------------------------------------------------------------------------- */

function restoreConversationRailContainment() {
  document.querySelectorAll('.reintegration-thread-item').forEach((item) => {
    if (item.querySelector('.reintegration-thread-box')) item.classList.add('is-workunit-thread')
  })

  const search = document.querySelector('.reintegration-conversation-search > span')
  if (search) search.textContent = 'Search conversations…'
}

/* -------------------------------------------------------------------------- */
/* Z7 specialist destination category identity                               */
/* -------------------------------------------------------------------------- */

function installSpecialistCategoryIdentity() {
  if (!specialistBarCopy) return

  let category = specialistBarCopy.querySelector('.reintegration-specialist-category')
  if (!category) {
    category = document.createElement('div')
    category.className = 'reintegration-specialist-category'
    specialistBarCopy.prepend(category)
  }

  const sync = () => {
    if (root.dataset.deepFocus === 'false') return
    const selected = document.querySelector(`${NODE_SELECTOR}[data-selected="true"]`)
    if (!selected) return

    const glyph = selected.querySelector('.category-glyph')?.innerHTML || ''
    const kind = selected.querySelector('.unit-kind')?.textContent?.trim() || 'Work unit'
    const rgb = getComputedStyle(selected).getPropertyValue('--node-rgb').trim() || selected.style.getPropertyValue('--node-rgb').trim() || '142, 169, 255'
    category.style.setProperty('--specialist-category-rgb', rgb)
    category.innerHTML = `<span class="category-glyph" aria-hidden="true">${glyph}</span><span>${escapeHtml(kind)}</span>`
  }

  sync()
  if ('MutationObserver' in window) {
    const observer = new MutationObserver(sync)
    observer.observe(root, { attributes: true, attributeFilter: ['data-deep-focus'] })
  }
}

function syncCompletionControls() {
  syncAppearancePresetControl()
  syncRelationshipControls()
}

function positionCircle(element, point) {
  if (!element) return
  element.setAttribute('cx', format(point.x))
  element.setAttribute('cy', format(point.y))
}

function positionSocket(element, point) {
  if (!element) return
  element.setAttribute('x', format(point.x - 2.6))
  element.setAttribute('y', format(point.y - 2.6))
}

function normalize(x, y) {
  const magnitude = Math.hypot(x, y) || 1
  return { x: x / magnitude, y: y / magnitude }
}

function format(value) {
  return Number(value.toFixed(2)).toString()
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;')
}
