import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'
const nodeSelector = '.expansion-practical-node'

async function dispatchWheel(
  page: Page,
  options: { deltaX?: number; deltaY?: number; ctrlKey?: boolean; shiftKey?: boolean; clientX?: number; clientY?: number },
  target = '#reintegration-stage',
) {
  await page.locator(target).evaluate((element, init) => {
    const rect = element.getBoundingClientRect()
    element.dispatchEvent(new WheelEvent('wheel', {
      bubbles: true,
      cancelable: true,
      deltaX: init.deltaX ?? 0,
      deltaY: init.deltaY ?? 0,
      ctrlKey: init.ctrlKey ?? false,
      shiftKey: init.shiftKey ?? false,
      clientX: init.clientX ?? rect.left + rect.width / 2,
      clientY: init.clientY ?? rect.top + rect.height / 2,
    }))
  }, options)
  await page.waitForTimeout(190)
}

async function nodeSemanticSnapshot(page: Page) {
  return page.locator(nodeSelector).evaluateAll((nodes) => nodes.map((node) => {
    const element = node as HTMLElement
    return {
      key: element.dataset.nodeKey,
      disposition: element.dataset.state,
      statusSource: element.dataset.statusSource,
      statusCode: element.dataset.statusCode,
      priority: element.dataset.priority,
      selected: element.dataset.selected,
      selectionStyle: element.dataset.selectionStyle,
      category: [...element.classList].find((value) => value.startsWith('category-')),
    }
  }))
}

test.describe('source-faithful Cockpit reintegration', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
  })

  test('loads every local reintegration dependency without page errors', async ({ page }) => {
    const failedResponses: string[] = []
    const pageErrors: string[] = []

    page.on('response', (response) => {
      const pathname = new URL(response.url()).pathname
      if (pathname.includes('/design-lab/') && response.status() >= 400) {
        failedResponses.push(`${response.status()} ${pathname}`)
      }
    })
    page.on('pageerror', (error) => pageErrors.push(error.message))

    await page.goto(route)
    await page.waitForLoadState('networkidle')

    expect(failedResponses).toEqual([])
    expect(pageErrors).toEqual([])
    await expect(page.locator('link[href="./cockpit-reintegration-z7.css"]')).toHaveCount(1)
    await expect(page.locator('link[href="./cockpit-reintegration-review-controls.css"]')).toHaveCount(1)
    await expect(page.locator('link[href="./cockpit-reintegration-conversation.css"]')).toHaveCount(1)
    await expect(page.locator('link[href="./cockpit-reintegration-deep-performance.css"]')).toHaveCount(1)
  })

  test('mounts canonical compact WorkUnit geometry and accepted semantic carriers', async ({ page }) => {
    const nodes = page.locator(nodeSelector)
    const world = page.locator('#reintegration-world')

    for (let index = 0; index < 6; index += 1) {
      const box = await nodes.nth(index).boundingBox()
      expect(box).not.toBeNull()
      expect(box?.width).toBeCloseTo(176, 0)
      expect(box?.height).toBeCloseTo(92, 0)
    }

    const selected = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await expect(selected).toHaveAttribute('data-selected', 'true')
    await expect(selected).toHaveAttribute('data-selection-style', 'sel2')
    await expect(selected.locator('.selection-corners')).toHaveCSS('opacity', '1')

    await expect(world.locator('.priority-signal-bars')).toHaveCount(3)
    await expect(world.locator('[data-status-code="BLOCKED"]')).toHaveCount(1)
    await expect(world.locator('[data-status-code="FAIL"]')).toHaveCount(1)
    await expect(world.locator('[data-status-code="RUN"]')).toHaveCount(1)
  })

  test('retains exact scientific marker categories in the Project Grid', async ({ page }) => {
    const world = page.locator('#reintegration-world')
    await expect(world.locator('.category-question .category-glyph circle')).toHaveCount(1)
    await expect(world.locator('.category-investigation .category-glyph rect')).toHaveCount(2)
    await expect(world.locator('.category-validation .category-glyph path')).toHaveCount(1)
    await expect(world.locator('.category-model .category-glyph path')).toHaveCount(1)
    await expect(world.locator('.category-evaluation .category-glyph path')).toHaveCount(1)
  })

  test('mounts E5 Hue plus Tag relations with persistent D1 target direction', async ({ page }) => {
    await expect(page.locator('html')).toHaveAttribute('data-relation-encoding', 'e5')
    await expect(page.locator('.reintegration-relation')).toHaveCount(4)

    const relations = page.locator('.reintegration-relation')
    for (let index = 0; index < 4; index += 1) {
      await expect(relations.nth(index)).toHaveAttribute('data-direction', 'forward')
      await expect(relations.nth(index).locator('.semantic-path')).not.toHaveAttribute('d', '')
      await expect(relations.nth(index).locator('.semantic-arrow')).not.toHaveAttribute('d', '')
      await expect(relations.nth(index).locator('.semantic-tag')).toHaveCSS('opacity', '1')
    }

    await expect(page.locator('.semantic-tag-text')).toHaveText(['BLOCKS', 'EVID', 'LINE', 'CAUSE'])
  })

  test('mounts the latest stochastic G4 scheduler instead of the superseded fixed ambient fixture', async ({ page }) => {
    const world = page.locator('#reintegration-world')
    const runtimeLayer = page.locator('#reintegration-ambient-runtime-layer')

    await expect(page.locator('html')).toHaveAttribute('data-ambient-cadence', 'lively')
    await expect(world).toHaveClass(/variant-g4/)
    await expect(runtimeLayer).toHaveCount(1)

    await expect(world.locator(':scope > .ambient-current')).toHaveCount(0)
    await expect(world.locator(':scope > .ambient-glint')).toHaveCount(0)
    await expect(world.locator(':scope > .ambient-drift')).toHaveCount(0)

    await expect.poll(async () => runtimeLayer.locator('.runtime-current').count(), { timeout: 1800 }).toBeGreaterThanOrEqual(1)
    const current = runtimeLayer.locator('.runtime-current').first()
    await expect(current).toHaveAttribute('data-orientation', /horizontal|vertical/)
    const coordinate = Number(await current.getAttribute('data-grid-coordinate'))
    expect(coordinate % 20).toBe(0)

    await expect(world.locator('.activity-field')).toHaveCount(2)
    await expect(world.locator('.live-packet')).toHaveCount(2)
  })

  test('reuses accepted X5 two-axis expansion without context recession', async ({ page }) => {
    const selected = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await expect(selected).toHaveAttribute('data-expanded', 'false')

    await page.locator('#toggle-detail').click()
    await expect(selected).toHaveAttribute('data-expanded', 'true')
    await expect(selected).toHaveCSS('width', '390px')
    await expect(selected).toHaveCSS('height', '210px')

    await expect(page.locator(`${nodeSelector}[data-node-key="q"]`)).toHaveCSS('opacity', '1')
    await expect(page.locator('.reintegration-relations')).toHaveCSS('opacity', '1')
    await expect(page.locator('#detail-state-label')).toContainText('X5 expanded')
  })

  test('ordinary two-finger wheel movement pans while ctrl-wheel pinch zooms around its anchor', async ({ page }) => {
    await page.locator('#reset-world').click()
    await expect(page.locator('#zoom-readout')).toHaveText('100%')

    const plane = page.locator('#reintegration-world-plane')
    const initialTransform = await plane.evaluate((element: HTMLElement) => element.style.transform)

    await dispatchWheel(page, { deltaX: 70, deltaY: 120 })
    await expect(page.locator('#zoom-readout')).toHaveText('100%')
    const pannedTransform = await plane.evaluate((element: HTMLElement) => element.style.transform)
    expect(pannedTransform).not.toBe(initialTransform)

    await page.locator('#reset-world').click()
    const anchorNode = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const before = await anchorNode.boundingBox()
    expect(before).not.toBeNull()
    const anchorX = (before?.x ?? 0) + (before?.width ?? 0) / 2
    const anchorY = (before?.y ?? 0) + (before?.height ?? 0) / 2

    await dispatchWheel(page, { deltaY: -80, ctrlKey: true, clientX: anchorX, clientY: anchorY })
    await expect(page.locator('#zoom-readout')).not.toHaveText('100%')

    const after = await anchorNode.boundingBox()
    expect(after).not.toBeNull()
    const afterX = (after?.x ?? 0) + (after?.width ?? 0) / 2
    const afterY = (after?.y ?? 0) + (after?.height ?? 0) / 2
    expect(Math.abs(afterX - anchorX)).toBeLessThan(2)
    expect(Math.abs(afterY - anchorY)).toBeLessThan(2)
  })

  test('pointer drag remains an alternate pan and keyboard recovery can move and reset the world', async ({ page }) => {
    const plane = page.locator('#reintegration-world-plane')
    const stage = page.locator('#reintegration-stage')
    const initialTransform = await plane.evaluate((element: HTMLElement) => element.style.transform)

    await page.mouse.move(300, 500)
    await page.mouse.down()
    await page.mouse.move(380, 565, { steps: 5 })
    await page.mouse.up()
    const draggedTransform = await plane.evaluate((element: HTMLElement) => element.style.transform)
    expect(draggedTransform).not.toBe(initialTransform)

    await stage.focus()
    await expect(stage).toBeFocused()
    await page.keyboard.press('ArrowRight')
    await page.waitForTimeout(50)
    const keyboardTransform = await plane.evaluate((element: HTMLElement) => element.style.transform)
    expect(keyboardTransform).not.toBe(draggedTransform)

    await page.keyboard.press('0')
    await page.waitForTimeout(50)
    await expect(page.locator('#zoom-readout')).toHaveText('100%')
    expect(await plane.evaluate((element: HTMLElement) => element.style.transform)).toBe(initialTransform)
  })

  test('releases navigation compositing after gestures and keeps rendered translation device-pixel aligned', async ({ page }) => {
    await dispatchWheel(page, { deltaX: 37.4, deltaY: 81.7 })

    const rendered = await page.locator('#reintegration-world-plane').evaluate((element: HTMLElement) => ({
      transform: element.style.transform,
      dpr: window.devicePixelRatio || 1,
      willChange: getComputedStyle(element).willChange,
    }))

    const match = rendered.transform.match(/translate3d\(([-\d.]+)px, ([-\d.]+)px/)
    expect(match).not.toBeNull()
    const x = Number(match?.[1])
    const y = Number(match?.[2])
    expect(Math.abs(x * rendered.dpr - Math.round(x * rendered.dpr))).toBeLessThan(0.001)
    expect(Math.abs(y * rendered.dpr - Math.round(y * rendered.dpr))).toBeLessThan(0.001)
    expect(rendered.willChange).toBe('auto')
    await expect(page.locator('#reintegration-stage')).not.toHaveClass(/is-navigating/)
  })

  test('Jump remains a recovery action after pan and pinch and does not corrupt WorkUnit semantics', async ({ page }) => {
    await dispatchWheel(page, { deltaX: 160, deltaY: -110 })
    await dispatchWheel(page, { deltaY: -52, ctrlKey: true, clientX: 760, clientY: 500 })

    await page.locator('#jump-input').fill('Boosted candidate')
    await page.locator('#jump-button').click()

    const selected = page.locator(`${nodeSelector}[data-node-key="m"]`)
    await expect(selected).toHaveAttribute('data-selected', 'true')
    await expect(selected).toHaveAttribute('data-status-code', 'FAIL')
    await expect(selected).toHaveAttribute('data-priority', 'high')
    await expect(selected).toHaveAttribute('data-expanded', 'false')
    await expect(page.locator('#selected-work-label')).toContainText('Boosted candidate')

    const stageBox = await page.locator('#reintegration-stage').boundingBox()
    const nodeBox = await selected.boundingBox()
    expect(stageBox).not.toBeNull()
    expect(nodeBox).not.toBeNull()
    const stageCenterX = (stageBox?.x ?? 0) + (stageBox?.width ?? 0) / 2
    const stageCenterY = (stageBox?.y ?? 0) + (stageBox?.height ?? 0) / 2
    const nodeCenterX = (nodeBox?.x ?? 0) + (nodeBox?.width ?? 0) / 2
    const nodeCenterY = (nodeBox?.y ?? 0) + (nodeBox?.height ?? 0) / 2
    expect(Math.abs(nodeCenterX - stageCenterX)).toBeLessThan(3)
    expect(Math.abs(nodeCenterY - stageCenterY)).toBeLessThan(3)

    for (const path of await page.locator('.semantic-path').all()) {
      await expect(path).not.toHaveAttribute('d', '')
    }
  })

  test('approved appearance controls change presentation without mutating semantics and keep relation geometry synchronized', async ({ page }) => {
    const beforeSemantics = await nodeSemanticSnapshot(page)
    const beforePath = await page.locator('.reintegration-relation[data-relation-id="i-v"] .semantic-path').getAttribute('d')

    await page.locator('#appearance-controls-toggle').click()
    await expect(page.locator('#reintegration-appearance-panel')).toBeVisible()

    await page.locator('[data-shape-option="normal"]').click()
    await page.locator('[data-surface-option="lumen"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-shape-style', 'normal')
    await expect(page.locator('html')).toHaveAttribute('data-surface-style', 'lumen')

    await page.waitForTimeout(180)
    expect(await nodeSemanticSnapshot(page)).toEqual(beforeSemantics)

    const afterPath = await page.locator('.reintegration-relation[data-relation-id="i-v"] .semantic-path').getAttribute('d')
    expect(afterPath).not.toBeNull()
    expect(afterPath).not.toBe(beforePath)

    for (const relation of await page.locator('.reintegration-relation').all()) {
      await expect(relation).toHaveAttribute('data-direction', 'forward')
      await expect(relation.locator('.semantic-arrow')).not.toHaveAttribute('d', '')
    }
  })

  test('settings overlay does not steal wheel input for the project world', async ({ page }) => {
    await page.locator('#appearance-controls-toggle').click()
    const beforeTransform = await page.locator('#reintegration-world-plane').evaluate((element: HTMLElement) => element.style.transform)
    const beforeZoom = await page.locator('#zoom-readout').textContent()

    await dispatchWheel(page, { deltaX: 90, deltaY: 120 }, '#reintegration-appearance-panel')

    const afterTransform = await page.locator('#reintegration-world-plane').evaluate((element: HTMLElement) => element.style.transform)
    const afterZoom = await page.locator('#zoom-readout').textContent()
    expect(afterTransform).toBe(beforeTransform)
    expect(afterZoom).toBe(beforeZoom)
  })

  test('X5 expanded source enters exact Z7 full-stage focus and returns with project state preserved', async ({ page }) => {
    const selected = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const plane = page.locator('#reintegration-world-plane')
    const transformBefore = await plane.evaluate((element: HTMLElement) => element.style.transform)

    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2200 })
    await expect(selected).toHaveAttribute('data-expanded', 'true')
    await expect(selected).toHaveAttribute('data-selected', 'true')
    await expect(page.locator('#reintegration-specialist-layer')).toHaveAttribute('aria-hidden', 'false')
    await expect(page.locator('.reintegration-topology-compass')).toHaveCSS('opacity', '1')
    await expect(page.locator('#specialist-title')).toHaveText('Production missingness')

    const transformDuringFocus = await plane.evaluate((element: HTMLElement) => element.style.transform)
    await dispatchWheel(page, { deltaX: 120, deltaY: 120 })
    expect(await plane.evaluate((element: HTMLElement) => element.style.transform)).toBe(transformDuringFocus)

    await page.locator('#return-to-project').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'false')
    await expect(page.locator('#reintegration-specialist-layer')).toHaveAttribute('aria-hidden', 'true')
    await expect(selected).toHaveAttribute('data-expanded', 'true')
    await expect(selected).toHaveAttribute('data-selected', 'true')
    expect(await plane.evaluate((element: HTMLElement) => element.style.transform)).toBe(transformBefore)
  })

  test('reduced motion reaches the same Z7 semantic end state without waiting for animated choreography', async ({ page }) => {
    await page.locator('#appearance-controls-toggle').click()
    await page.locator('#reduced-motion-toggle').check()
    await expect(page.locator('html')).toHaveAttribute('data-reduced', 'on')

    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 500 })
    await expect(page.locator(`${nodeSelector}[data-node-key="i"]`)).toHaveAttribute('data-expanded', 'true')
    await expect(page.locator('#reintegration-specialist-layer')).toHaveAttribute('aria-hidden', 'false')

    await page.locator('#return-to-project').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'false')
    await expect(page.locator(`${nodeSelector}[data-node-key="i"]`)).toHaveAttribute('data-expanded', 'true')
  })

  test('combined pan pinch select expand appearance and Z7 sequence preserves independent carriers', async ({ page }) => {
    await dispatchWheel(page, { deltaX: -95, deltaY: 125 })
    await dispatchWheel(page, { deltaY: -60, ctrlKey: true, clientX: 720, clientY: 460 })

    await page.locator('#jump-input').fill('Resolve target definition')
    await page.locator('#jump-button').click()
    const selected = page.locator(`${nodeSelector}[data-node-key="q"]`)
    await expect(selected).toHaveAttribute('data-selected', 'true')
    await expect(selected).toHaveAttribute('data-status-code', 'HUMAN')
    await expect(selected).toHaveAttribute('data-priority', 'high')

    await page.locator('#toggle-detail').click()
    await expect(selected).toHaveAttribute('data-expanded', 'true')

    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-shape-option="normal"]').click()
    await page.locator('[data-surface-option="none"]').click()
    await page.locator('#appearance-controls-close').click()

    await expect(selected).toHaveAttribute('data-selected', 'true')
    await expect(selected).toHaveAttribute('data-status-code', 'HUMAN')
    await expect(selected).toHaveAttribute('data-priority', 'high')
    await expect(selected.locator('.selection-corners')).toHaveCSS('opacity', '1')

    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 1800 })
    await expect(page.locator('#specialist-title')).toHaveText('Resolve target definition')

    await page.locator('#return-to-project').click()
    await expect(selected).toHaveAttribute('data-expanded', 'true')
    await expect(selected).toHaveAttribute('data-selected', 'true')
    await expect(selected).toHaveAttribute('data-status-code', 'HUMAN')
    await expect(selected).toHaveAttribute('data-priority', 'high')

    for (const path of await page.locator('.semantic-path').all()) {
      await expect(path).not.toHaveAttribute('d', '')
    }
  })

  test('opens the real source-faithful Conversation Workspace without reviving rejected visual systems', async ({ page }) => {
    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('#reintegration-conversation-layer')).toHaveAttribute('aria-hidden', 'false')
    await expect(page.locator('#reintegration-conversation-title')).toHaveText('General project discussion')
    await expect(page.locator('body')).not.toContainText('Deep Navy')
    await expect(page.locator('#reintegration-appearance-panel')).toContainText('Conversation rail Boxes / Text')
  })
})
