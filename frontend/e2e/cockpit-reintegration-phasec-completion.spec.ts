import { expect, test, type Locator, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'
const nodeSelector = '.expansion-practical-node'

async function semanticSnapshot(page: Page) {
  return page.locator(nodeSelector).evaluateAll((nodes) => nodes.map((node) => {
    const element = node as HTMLElement
    return {
      key: element.dataset.nodeKey,
      disposition: element.dataset.state,
      statusSource: element.dataset.statusSource,
      statusCode: element.dataset.statusCode,
      priority: element.dataset.priority,
      selected: element.dataset.selected,
      category: [...element.classList].find((name) => name.startsWith('category-')),
    }
  }))
}

async function relationSemanticSnapshot(relation: Locator) {
  return relation.evaluate((element: HTMLElement) => ({
    id: element.dataset.relationId,
    source: element.dataset.source,
    target: element.dataset.target,
    direction: element.dataset.direction,
    relationClass: element.dataset.relationClass || '',
  }))
}

test.describe('Phase-C holistic fidelity completion', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('script[src="./cockpit-reintegration-phasec-completion.js"]')).toHaveCount(1)
  })

  test('H4 pointer entry executes the accepted perimeter sweep on the perimeter element', async ({ page }) => {
    const node = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const sweep = node.locator('.perimeter-sweep')

    await node.hover()
    await expect(sweep).toHaveClass(/sweep-active/)
    await expect.poll(async () => sweep.evaluate((element) => getComputedStyle(element).animationName)).toContain('perimeter-sweep')

    await expect(node).toHaveCSS('transform', /matrix/)
    await expect(node.locator('.hover-light')).toHaveCSS('opacity', '1')
    await expect(node.locator('.hover-world-light')).toHaveCSS('opacity', '1')
    await expect(node.locator('.pointer-light')).toHaveCSS('opacity', '1')
  })

  test('G4 retains fields and stochastic world activity without the rejected isolated green packets', async ({ page }) => {
    const world = page.locator('#reintegration-world')
    await expect(world.locator('.activity-field')).toHaveCount(2)
    await expect(world.locator('.live-packet')).toHaveCount(0)
    await expect(page.locator('#reintegration-ambient-runtime-layer')).toHaveCount(1)
    await expect.poll(async () => page.locator('#reintegration-ambient-runtime-layer .runtime-current').count(), { timeout: 1800 }).toBeGreaterThanOrEqual(1)
  })

  test('relationship presentation switches between E5 hue+tag and neutral hover without changing semantics', async ({ page }) => {
    const relation = page.locator('.reintegration-relation[data-relation-id="i-v"]')
    const node = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const before = await relationSemanticSnapshot(relation)

    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-relation-presentation-option="neutral-hover"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-relation-presentation', 'neutral-hover')
    await expect(relation.locator('.semantic-tag')).toHaveCSS('visibility', 'hidden')

    const restingStroke = await relation.locator('.semantic-path').evaluate((element) => getComputedStyle(element).stroke)
    expect(restingStroke).toBe('rgba(153, 170, 193, 0.31)')

    const nodeRgb = await node.evaluate((element) => getComputedStyle(element).getPropertyValue('--node-rgb').trim())
    await node.hover()
    await expect(relation).toHaveClass(/is-related/)
    const hoverRgb = await relation.evaluate((element) => getComputedStyle(element).getPropertyValue('--hover-rgb').trim())
    expect(hoverRgb).toBe(nodeRgb)
    expect(await relationSemanticSnapshot(relation)).toEqual(before)

    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-relation-presentation-option="class-tag"]').click()
    await expect(relation.locator('.semantic-tag')).toHaveCSS('visibility', 'visible')
    expect(await relationSemanticSnapshot(relation)).toEqual(before)
  })

  test('connector endpoint preference activates exactly one treatment while D0-D3 semantics remain untouched', async ({ page }) => {
    const relation = page.locator('.reintegration-relation[data-relation-id="i-v"]')
    const before = await relationSemanticSnapshot(relation)
    await page.locator('#appearance-controls-toggle').click()

    for (const mode of ['clean', 'dots', 'sockets', 'arrows']) {
      await page.locator(`[data-connector-terminal-option="${mode}"]`).click()
      await expect(page.locator('html')).toHaveAttribute('data-connector-terminal', mode)

      const visibility = await relation.evaluate((element) => {
        const visible = (selector: string) => [...element.querySelectorAll(selector)]
          .filter((candidate) => getComputedStyle(candidate).visibility !== 'hidden' && Number(getComputedStyle(candidate).opacity) > 0)
          .length
        return {
          dots: visible('.reintegration-terminal-dot'),
          sockets: visible('.reintegration-terminal-socket'),
          arrows: visible('.semantic-arrow-start, .semantic-arrow-end'),
        }
      })

      if (mode === 'clean') expect(visibility).toEqual({ dots: 0, sockets: 0, arrows: 0 })
      if (mode === 'dots') expect(visibility).toEqual({ dots: 2, sockets: 0, arrows: 0 })
      if (mode === 'sockets') expect(visibility).toEqual({ dots: 0, sockets: 2, arrows: 0 })
      if (mode === 'arrows') expect(visibility).toEqual({ dots: 0, sockets: 0, arrows: 1 })
      expect(await relationSemanticSnapshot(relation)).toEqual(before)
    }
  })

  test('BLOCKER cause uses the confirmed BLOCKS relationship into the BLOCKED WorkUnit', async ({ page }) => {
    const source = page.locator(`${nodeSelector}[data-node-key="q"]`)
    const target = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const relation = page.locator('.reintegration-relation[data-relation-id="q-i"]')

    await expect(source).toHaveClass(/category-question/)
    await expect(target).toHaveAttribute('data-status-code', 'BLOCKED')
    await expect(relation).toHaveAttribute('data-relation-class', 'blocks')
    await expect(relation.locator('.semantic-tag-text')).toHaveText('BLOCKS')
  })

  test('L0 is the provisional X5 working layout with six held fields', async ({ page }) => {
    await expect(page.locator('html')).toHaveAttribute('data-internal-layout', 'l0')
    await page.locator('#toggle-detail').click()

    const selected = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await expect(selected).toHaveAttribute('data-expanded', 'true')
    const labels = await selected.locator('.detail-inline .detail-cell > span').allTextContents()
    expect(labels).toEqual([
      'Purpose',
      'Constraint / state',
      'Evidence',
      'Next action',
      'Blocking cause',
      'Recent activity',
    ])
  })

  test('P7 includes selective disposition tone and hover hue without changing disposition state', async ({ page }) => {
    await expect(page.locator('html')).toHaveAttribute('data-disposition-encoding', 'p7')
    const deferred = page.locator(`${nodeSelector}[data-node-key="e"]`)
    const before = await deferred.getAttribute('data-state')

    await expect(deferred.locator('.node-surface')).toHaveCSS('opacity', '0.78')
    await deferred.hover()
    const badgeColor = await deferred.locator('.disposition-state-badge').evaluate((element) => getComputedStyle(element).color)
    expect(badgeColor).not.toBe('rgba(0, 0, 0, 0)')
    expect(await deferred.getAttribute('data-state')).toBe(before)
  })

  test('Z7 destination retains the selected WorkUnit category identity', async ({ page }) => {
    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2400 })

    const category = page.locator('.reintegration-specialist-category')
    await expect(category).toContainText('Investigation')
    await expect(category.locator('.category-glyph rect')).toHaveCount(1)
    await expect(page.locator('#specialist-title')).toHaveText('Production missingness')
  })

  test('appearance presets reproduce the accepted Clean Structured and Rich combinations without semantic mutation', async ({ page }) => {
    const before = await semanticSnapshot(page)
    await page.locator('#appearance-controls-toggle').click()

    await page.locator('[data-appearance-preset="clean"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-shape-style', 'normal')
    await expect(page.locator('html')).toHaveAttribute('data-surface-style', 'none')

    await page.locator('[data-appearance-preset="structured"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-shape-style', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-surface-style', 'none')

    await page.locator('[data-appearance-preset="rich"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-shape-style', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-surface-style', 'material')
    expect(await semanticSnapshot(page)).toEqual(before)
  })

  test('Conversation Boxes rail uses accepted compact canonical WorkUnit containment and bounded search typography', async ({ page }) => {
    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')

    const search = page.locator('.reintegration-conversation-search > span')
    await expect(search).toHaveText('Search conversations…')
    const searchMetrics = await search.evaluate((element) => ({
      height: element.getBoundingClientRect().height,
      fontSize: parseFloat(getComputedStyle(element).fontSize),
      whiteSpace: getComputedStyle(element).whiteSpace,
    }))
    expect(searchMetrics.fontSize).toBeLessThanOrEqual(9)
    expect(searchMetrics.height).toBeLessThan(14)
    expect(searchMetrics.whiteSpace).toBe('nowrap')

    const workRows = page.locator('.reintegration-thread-item.is-workunit-thread')
    await expect(workRows).toHaveCount(6)

    for (const row of await workRows.all()) {
      const node = row.locator('.conversation-canonical-node')
      const transform = await node.evaluate((element) => getComputedStyle(element).transform)
      expect(transform).not.toBe('none')
      const rowBox = await row.boundingBox()
      expect(rowBox?.height).toBeCloseTo(92, 0)

      const visibleStatus = row.locator('.status-tag-carrier:visible, .status-dot-carrier:visible')
      if (await visibleStatus.count()) {
        const rowBounds = await row.boundingBox()
        const statusBounds = await visibleStatus.first().boundingBox()
        expect(rowBounds).not.toBeNull()
        expect(statusBounds).not.toBeNull()
        expect((statusBounds?.x ?? 0) + (statusBounds?.width ?? 0)).toBeLessThanOrEqual((rowBounds?.x ?? 0) + (rowBounds?.width ?? 0) + 1)
        expect((statusBounds?.y ?? 0) + (statusBounds?.height ?? 0)).toBeLessThanOrEqual((rowBounds?.y ?? 0) + (rowBounds?.height ?? 0) + 1)
      }
    }
  })
})
