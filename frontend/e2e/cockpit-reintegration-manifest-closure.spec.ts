import { expect, test, type Locator, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html?edge=none'
const nodeSelector = '.expansion-practical-node'

async function semanticSnapshot(node: Locator) {
  return node.evaluate((element: HTMLElement) => ({
    key: element.dataset.nodeKey,
    disposition: element.dataset.state,
    statusSource: element.dataset.statusSource,
    statusCode: element.dataset.statusCode,
    priority: element.dataset.priority,
    selected: element.dataset.selected,
    expanded: element.dataset.expanded,
    category: [...element.classList].find((name) => name.startsWith('category-')),
  }))
}

async function selectedKey(page: Page) {
  return page.locator(`${nodeSelector}[data-selected="true"]`).getAttribute('data-node-key')
}

async function arrowVisibility(group: Locator) {
  return group.evaluate((element) => {
    const start = element.querySelector('.semantic-arrow-start')
    const end = element.querySelector('.semantic-arrow-end')
    return {
      start: start ? getComputedStyle(start).visibility : null,
      end: end ? getComputedStyle(end).visibility : null,
    }
  })
}

test.describe('Cockpit accepted-implementation manifest closure', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('#process-focus-toggle')).toBeVisible()
  })

  test('M09 focus membership is editable view composition and never mutates WorkUnit semantics', async ({ page }) => {
    const current = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const context = page.locator(`${nodeSelector}[data-node-key="m"]`)
    const relation = page.locator('.reintegration-relation[data-relation-id="m-v"]')

    await expect(current).toHaveAttribute('data-process-scope', 'current')
    await expect(context).toHaveAttribute('data-process-scope', 'context')
    await expect(relation).toHaveClass(/is-context-edge/)

    const beforeContextSemantic = await semanticSnapshot(context)
    const beforeSelected = await selectedKey(page)

    await page.locator('#process-focus-toggle').click()
    await page.locator('[data-process-focus-mode="focused"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-process-focus', 'focused')

    /* Preserve the accepted recession transition and wait for its settled state. */
    await expect.poll(async () => Number(await context.evaluate((element) => getComputedStyle(element).opacity))).toBeLessThan(0.4)
    await expect.poll(async () => Number(await current.evaluate((element) => getComputedStyle(element).opacity))).toBeGreaterThan(0.9)

    await context.hover()
    await expect(context).toHaveClass(/is-hovered/)
    await expect.poll(async () => Number(await context.evaluate((element) => getComputedStyle(element).opacity))).toBeGreaterThan(0.6)

    await page.locator('#process-focus-edit').click()
    await expect(page.locator('html')).toHaveAttribute('data-focus-edit', 'on')
    const membership = context.locator('.reintegration-focus-membership-toggle')
    await expect(membership).toBeVisible()
    await membership.click()

    await expect(context).toHaveAttribute('data-process-scope', 'current')
    await expect(relation).toHaveClass(/is-current-edge/)
    expect(await semanticSnapshot(context)).toEqual(beforeContextSemantic)
    expect(await selectedKey(page)).toBe(beforeSelected)

    await page.locator('#process-focus-reset').click()
    await expect(context).toHaveAttribute('data-process-scope', 'context')
    await expect(relation).toHaveClass(/is-context-edge/)
  })

  test('M06 supports D0-D3 with one edge-docked arrow treatment and unchanged relation meaning', async ({ page }) => {
    const group = page.locator('.reintegration-relation[data-relation-id="q-i"]')
    await expect(group.locator('.semantic-arrow-start')).toHaveCount(1)
    await expect(group.locator('.semantic-arrow-end')).toHaveCount(1)

    const relationClassBefore = await group.evaluate((element: HTMLElement) => ({
      source: element.dataset.source,
      target: element.dataset.target,
      hue: element.style.getPropertyValue('--class-rgb'),
      tag: element.querySelector('.semantic-tag-text')?.textContent,
    }))

    const expected = [
      ['none', { start: 'hidden', end: 'hidden' }],
      ['forward', { start: 'hidden', end: 'visible' }],
      ['reverse', { start: 'visible', end: 'hidden' }],
      ['both', { start: 'visible', end: 'visible' }],
    ] as const

    for (const [direction, visibility] of expected) {
      await group.evaluate((element: HTMLElement, value) => { element.dataset.direction = value }, direction)
      await expect.poll(() => arrowVisibility(group)).toEqual(visibility)
    }

    const docking = await group.evaluate((element) => {
      const path = element.querySelector<SVGPathElement>('.semantic-path')!
      const startArrow = element.querySelector<SVGPathElement>('.semantic-arrow-start')!
      const endArrow = element.querySelector<SVGPathElement>('.semantic-arrow-end')!
      const pathStart = path.getPointAtLength(0)
      const pathEnd = path.getPointAtLength(path.getTotalLength())

      const parseTip = (arrow: SVGPathElement) => {
        const numbers = (arrow.getAttribute('d') || '').match(/-?\d+(?:\.\d+)?/g)?.map(Number) || []
        return { x: numbers[2], y: numbers[3] }
      }

      return {
        pathStart: { x: pathStart.x, y: pathStart.y },
        pathEnd: { x: pathEnd.x, y: pathEnd.y },
        startTip: parseTip(startArrow),
        endTip: parseTip(endArrow),
      }
    })

    expect(docking.startTip.x).toBeCloseTo(docking.pathStart.x, 1)
    expect(docking.startTip.y).toBeCloseTo(docking.pathStart.y, 1)
    expect(docking.endTip.x).toBeCloseTo(docking.pathEnd.x, 1)
    expect(docking.endTip.y).toBeCloseTo(docking.pathEnd.y, 1)

    const relationClassAfter = await group.evaluate((element: HTMLElement) => ({
      source: element.dataset.source,
      target: element.dataset.target,
      hue: element.style.getPropertyValue('--class-rgb'),
      tag: element.querySelector('.semantic-tag-text')?.textContent,
    }))
    expect(relationClassAfter).toEqual(relationClassBefore)

    const zLayers = await page.evaluate(() => ({
      relations: Number(getComputedStyle(document.querySelector('#reintegration-relations')!).zIndex),
      nodes: Number(getComputedStyle(document.querySelector('#expansion-practical-nodes')!).zIndex),
    }))
    expect(zLayers.relations).toBeLessThan(zLayers.nodes)
  })

  test('M11 shared tag carrier preserves the accepted soft-shade state texture and reduced-motion fallback', async ({ page }) => {
    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-global-status-carrier="tag"]').click()

    const running = page.locator(`${nodeSelector}[data-node-key="r"]`)
    await expect(running).toHaveAttribute('data-status-code', 'RUN')
    await expect(running).toHaveAttribute('data-status-carrier', 'tag')

    const tag = running.locator('.status-tag-carrier')
    await expect(tag).toBeVisible()
    await expect(tag.locator('.status-tag-label')).toHaveText('RUN')

    const animated = await tag.evaluate((element) => {
      const before = getComputedStyle(element, '::before')
      const after = getComputedStyle(element, '::after')
      return {
        beforeAnimation: before.animationName,
        beforeBackground: before.backgroundImage,
        afterBackground: after.backgroundImage,
      }
    })
    expect(animated.beforeAnimation).toContain('blocked-status-shade-orbit')
    expect(animated.beforeBackground).toContain('conic-gradient')
    expect(animated.afterBackground).toContain('conic-gradient')
    await expect(running.locator('[role="progressbar"]')).toHaveCount(0)

    await page.locator('#reduced-motion-toggle').check()
    await expect(page.locator('html')).toHaveAttribute('data-reduced', 'on')
    await expect.poll(async () => tag.evaluate((element) => getComputedStyle(element, '::before').animationName)).toBe('none')
    await expect(tag.locator('.status-tag-label')).toHaveText('RUN')
  })

  test('M01 fold-away chrome remains recoverable without mutating project state', async ({ page }) => {
    const before = await selectedKey(page)

    await page.locator('#map-tools-fold').click()
    await expect(page.locator('.reintegration-tools')).toHaveAttribute('data-folded', 'true')
    await expect(page.locator('#zoom-in')).toBeHidden()
    await expect(page.locator('#map-tools-fold')).toBeVisible()
    await page.locator('#map-tools-fold').click()
    await expect(page.locator('#zoom-in')).toBeVisible()

    await page.locator('#hud-hide').click()
    await expect(page.locator('html')).toHaveAttribute('data-hud-visibility', 'hidden')
    await expect(page.locator('#hud-restore')).toBeVisible()
    await page.locator('#hud-restore').click()
    await expect(page.locator('html')).toHaveAttribute('data-hud-visibility', 'visible')
    expect(await selectedKey(page)).toBe(before)
  })

  test('M01 deep focus is URL-reconstructable across refresh while the URL contract remains provisional', async ({ page }) => {
    const model = page.locator(`${nodeSelector}[data-node-key="m"]`)
    await model.click()
    await expect(model).toHaveAttribute('data-selected', 'true')
    await model.click()
    await expect(model).toHaveAttribute('data-expanded', 'true')
    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })

    await expect.poll(() => new URL(page.url()).searchParams.get('work')).toBe('m')
    expect(new URL(page.url()).searchParams.get('depth')).toBe('deep')
    expect(new URL(page.url()).searchParams.get('focus')).toBe('work')

    await page.reload()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 3500 })
    await expect(page.locator(`${nodeSelector}[data-node-key="m"]`)).toHaveAttribute('data-selected', 'true')
    await expect(page.locator(`${nodeSelector}[data-node-key="m"]`)).toHaveAttribute('data-expanded', 'true')

    await page.locator('#return-to-project').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'false')
    await expect.poll(() => new URL(page.url()).searchParams.get('depth')).toBe('x5')
  })

  test('M01 denied fullscreen degrades gracefully and floating controls remain bounded at laptop size', async ({ page }) => {
    await page.evaluate(() => {
      Object.defineProperty(document.documentElement, 'requestFullscreen', {
        configurable: true,
        value: async () => { throw new Error('test denial') },
      })
    })

    await page.locator('#fullscreen-world').click()
    await expect(page.locator('html')).toHaveAttribute('data-fullscreen', 'false')
    await expect(page.locator('.reintegration-provisional-note small')).toContainText('fullscreen was unavailable')

    await page.setViewportSize({ width: 1024, height: 768 })
    await page.locator('#process-focus-toggle').click()
    const bounds = await page.locator('#reintegration-process-focus-panel').evaluate((element) => {
      const rect = element.getBoundingClientRect()
      return { left: rect.left, top: rect.top, right: rect.right, bottom: rect.bottom }
    })
    expect(bounds.left).toBeGreaterThanOrEqual(0)
    expect(bounds.top).toBeGreaterThanOrEqual(0)
    expect(bounds.right).toBeLessThanOrEqual(1024)
    expect(bounds.bottom).toBeLessThanOrEqual(768)

    await page.locator('#appearance-controls-toggle').click()
    await expect(page.locator('#reintegration-process-focus-panel')).toBeHidden()
    await expect(page.locator('#reintegration-appearance-panel')).toBeVisible()
    await page.locator('#product-jump-toggle').click()
    await expect(page.locator('#reintegration-appearance-panel')).toBeHidden()
    await expect(page.locator('#jump-input')).toBeVisible()
    await expect(page.locator('#composer-input')).toBeVisible()
  })
})
