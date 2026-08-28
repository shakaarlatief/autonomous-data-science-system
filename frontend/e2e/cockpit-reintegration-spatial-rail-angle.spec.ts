import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html?edge=angled'

async function openStudy(page: Page, width = 1600, height = 1000) {
  await page.setViewportSize({ width, height })
  await page.goto(route)
  await expect(page.locator('html')).toHaveAttribute('data-spatial-rail-angle', 'angled')
  await expect(page.locator('html')).toHaveAttribute('data-human-review255', 'true')
  await expect(page.locator('.cockpit-angled-rail-rig')).toBeVisible()
  await expect(page.locator('.cockpit-angled-rail-rig')).toHaveAttribute('data-clarity', 'compact')
  await expect(page.locator('#map-tools-fold')).toBeHidden()
}

async function selectedWorkKey(page: Page) {
  return page.locator('.expansion-practical-node[data-selected="true"]').getAttribute('data-node-key')
}

test.describe('Checkpoint 255 whole-Cockpit human-review corrections', () => {
  test('the current compact right-side rail keeps its composition but is normal 2D', async ({ page }) => {
    await openStudy(page)

    const rig = page.locator('.cockpit-angled-rail-rig')
    const shell = page.locator('.cockpit-angled-rail-shell')
    const compactWidth = await shell.evaluate((element) => element.getBoundingClientRect().width)

    await expect.poll(() => rig.evaluate((element) => getComputedStyle(element).perspective)).toBe('none')
    await expect.poll(() => shell.evaluate((element) => getComputedStyle(element).transform)).toBe('none')
    await expect(page.locator('.cockpit-angled-rail-back')).toBeHidden()
    await expect(page.locator('.cockpit-angled-rail-spine')).toBeHidden()
    expect(compactWidth).toBeLessThan(100)
    await expect(page.locator('.cockpit-edge-grip')).toHaveCount(0)
    await expect(page.locator('.cockpit-angled-rail-rig [role="slider"]')).toHaveCount(0)
  })

  test('clarity expansion reveals labels without changing the flat rail or project state', async ({ page }) => {
    await openStudy(page)

    const shell = page.locator('.cockpit-angled-rail-shell')
    const selectedBefore = await selectedWorkKey(page)
    const cameraBefore = await page.locator('#reintegration-world-plane').evaluate((element) => element.style.transform)

    await page.locator('.cockpit-angled-rail-clarity').click()
    await expect(page.locator('.cockpit-angled-rail-rig')).toHaveAttribute('data-clarity', 'expanded')
    await expect(page.locator('.cockpit-angled-rail-clarity')).toHaveAttribute('aria-expanded', 'true')

    await page.waitForTimeout(220)
    const expandedWidth = await shell.evaluate((element) => element.getBoundingClientRect().width)
    const transformAfter = await shell.evaluate((element) => getComputedStyle(element).transform)
    const labelOpacity = await page.locator('#product-jump-toggle').evaluate((element) => getComputedStyle(element, '::after').opacity)
    const cameraAfter = await page.locator('#reintegration-world-plane').evaluate((element) => element.style.transform)

    expect(expandedWidth).toBeGreaterThan(180)
    expect(transformAfter).toBe('none')
    expect(Number(labelOpacity)).toBeGreaterThan(0.9)
    expect(cameraAfter).toBe(cameraBefore)
    expect(await selectedWorkKey(page)).toBe(selectedBefore)
  })

  test('the flat rail still reuses the real Cockpit controls and yields full-stage ownership', async ({ page }) => {
    await openStudy(page)

    await page.locator('#product-jump-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'true')
    await expect(page.locator('#jump-input')).toBeFocused()
    await page.keyboard.press('Escape')

    await page.locator('#appearance-controls-toggle').click()
    await expect(page.locator('#reintegration-appearance-panel')).toBeVisible()
    await page.keyboard.press('Escape')

    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('.cockpit-angled-rail-rig')).toBeHidden()
    await page.keyboard.press('Escape')
    await expect(page.locator('.cockpit-angled-rail-rig')).toBeVisible()

    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })
    await expect(page.locator('.cockpit-angled-rail-rig')).toBeHidden()
  })

  test('Conversation Boxes mode keeps clearly visible separation between every WorkUnit at narrow review width', async ({ page }) => {
    await openStudy(page, 760, 1000)
    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')

    await page.locator('[data-conversation-rail-option="boxes"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'boxes')

    const rowGap = await page.locator('.reintegration-thread-list').evaluate((element) => getComputedStyle(element).rowGap)
    expect(Number.parseFloat(rowGap)).toBeGreaterThanOrEqual(16)

    const project = await page.locator('.reintegration-project-thread-artifact').boundingBox()
    const workSurfaces = page.locator('.reintegration-thread-item[data-thread-scope="work"] .conversation-canonical-node .node-surface')
    const count = await workSurfaces.count()
    expect(project).not.toBeNull()
    expect(count).toBeGreaterThan(1)

    const surfaces = []
    for (let index = 0; index < count; index += 1) {
      const box = await workSurfaces.nth(index).boundingBox()
      expect(box).not.toBeNull()
      if (box) surfaces.push(box)
    }

    const projectGap = surfaces[0].y - ((project?.y ?? 0) + (project?.height ?? 0))
    expect(projectGap).toBeGreaterThanOrEqual(14)

    for (let index = 1; index < surfaces.length; index += 1) {
      const previous = surfaces[index - 1]
      const current = surfaces[index]
      const visibleGap = current.y - (previous.y + previous.height)
      expect(visibleGap).toBeGreaterThanOrEqual(14)
    }
  })

  test('the Z7 compass is one clean live topology instrument tied to the actual selected WorkUnit', async ({ page }) => {
    await openStudy(page)
    const selectedBefore = await selectedWorkKey(page)
    expect(selectedBefore).not.toBeNull()

    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })
    await expect(page.locator('html')).toHaveAttribute('data-topology-compass', 'live')

    const compass = page.locator('.reintegration-topology-compass')
    const miniMap = page.locator('.reintegration-mini-map')
    await expect(compass).toBeVisible()
    await expect(compass).toHaveAttribute('data-current-work', selectedBefore || '')

    const projectNodeCount = await page.locator('.expansion-practical-node').count()
    await expect(miniMap.locator('.mini-dot')).toHaveCount(projectNodeCount)
    await expect(miniMap.locator('.mini-dot.is-current')).toHaveCount(1)
    await expect(miniMap.locator('.mini-dot.is-current')).toHaveAttribute('data-node-key', selectedBefore || '')

    const relationCount = await page.locator('#reintegration-relations .reintegration-relation').count()
    await expect(miniMap.locator('.reintegration-mini-map-links line')).toHaveCount(relationCount)

    const compassBorder = await compass.evaluate((element) => getComputedStyle(element).borderTopWidth)
    const miniMapBorder = await miniMap.evaluate((element) => getComputedStyle(element).borderTopWidth)
    expect(Number.parseFloat(compassBorder)).toBeGreaterThan(0)
    expect(Number.parseFloat(miniMapBorder)).toBe(0)

    const compassBox = await compass.boundingBox()
    const firstSidePanel = await page.locator('.reintegration-specialist-side .reintegration-specialist-panel').first().boundingBox()
    expect(compassBox).not.toBeNull()
    expect(firstSidePanel).not.toBeNull()
    expect((firstSidePanel?.y ?? 0) - ((compassBox?.y ?? 0) + (compassBox?.height ?? 0))).toBeGreaterThan(8)

    await page.locator('#return-to-project').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'false')

    const alternateKey = selectedBefore === 'q' ? 'r' : 'q'
    const alternate = page.locator(`.expansion-practical-node[data-node-key="${alternateKey}"]`)
    await alternate.click()
    await expect(alternate).toHaveAttribute('data-selected', 'true')
    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })
    await expect(compass).toHaveAttribute('data-current-work', alternateKey)
    await expect(miniMap.locator('.mini-dot.is-current')).toHaveAttribute('data-node-key', alternateKey)
  })
})
