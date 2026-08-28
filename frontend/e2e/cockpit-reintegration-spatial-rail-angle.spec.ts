import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html?edge=angled'

async function openStudy(page: Page) {
  await page.setViewportSize({ width: 1600, height: 1000 })
  await page.goto(route)
  await expect(page.locator('html')).toHaveAttribute('data-spatial-rail-angle', 'angled')
  await expect(page.locator('.cockpit-angled-rail-rig')).toBeVisible()
  await expect(page.locator('.cockpit-angled-rail-rig')).toHaveAttribute('data-clarity', 'compact')
  await expect(page.locator('#map-tools-fold')).toBeHidden()
}

async function selectedWorkKey(page: Page) {
  return page.locator('.expansion-practical-node[data-selected="true"]').getAttribute('data-node-key')
}

test.describe('resting-angle Cockpit rail study', () => {
  test('the compact resting rail already carries perspective and visible depth without any drag state', async ({ page }) => {
    await openStudy(page)

    const shell = page.locator('.cockpit-angled-rail-shell')
    const back = page.locator('.cockpit-angled-rail-back')
    const compactWidth = await shell.evaluate((element) => element.getBoundingClientRect().width)
    const shellTransform = await shell.evaluate((element) => getComputedStyle(element).transform)
    const backTransform = await back.evaluate((element) => getComputedStyle(element).transform)

    expect(compactWidth).toBeLessThan(100)
    expect(shellTransform).not.toBe('none')
    expect(backTransform).not.toBe('none')
    await expect(page.locator('.cockpit-edge-grip')).toHaveCount(0)
    await expect(page.locator('.cockpit-angled-rail-rig [role="slider"]')).toHaveCount(0)
  })

  test('clarity expansion reveals labels without changing the rail perspective or project state', async ({ page }) => {
    await openStudy(page)

    const shell = page.locator('.cockpit-angled-rail-shell')
    const selectedBefore = await selectedWorkKey(page)
    const cameraBefore = await page.locator('#reintegration-world-plane').evaluate((element) => element.style.transform)
    const transformBefore = await shell.evaluate((element) => getComputedStyle(element).transform)

    await page.locator('.cockpit-angled-rail-clarity').click()
    await expect(page.locator('.cockpit-angled-rail-rig')).toHaveAttribute('data-clarity', 'expanded')
    await expect(page.locator('.cockpit-angled-rail-clarity')).toHaveAttribute('aria-expanded', 'true')

    await page.waitForTimeout(220)
    const expandedWidth = await shell.evaluate((element) => element.getBoundingClientRect().width)
    const transformAfter = await shell.evaluate((element) => getComputedStyle(element).transform)
    const labelOpacity = await page.locator('#product-jump-toggle').evaluate((element) => getComputedStyle(element, '::after').opacity)
    const cameraAfter = await page.locator('#reintegration-world-plane').evaluate((element) => element.style.transform)

    expect(expandedWidth).toBeGreaterThan(180)
    expect(transformAfter).toBe(transformBefore)
    expect(Number(labelOpacity)).toBeGreaterThan(0.9)
    expect(cameraAfter).toBe(cameraBefore)
    expect(await selectedWorkKey(page)).toBe(selectedBefore)
  })

  test('the angled shell reuses the real Cockpit controls', async ({ page }) => {
    await openStudy(page)

    await page.locator('#product-jump-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'true')
    await expect(page.locator('#jump-input')).toBeFocused()

    await page.keyboard.press('Escape')
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'false')

    await page.locator('#appearance-controls-toggle').click()
    await expect(page.locator('#reintegration-appearance-panel')).toBeVisible()
  })

  test('the angled rail yields stage ownership to full Conversation and Deep Dive', async ({ page }) => {
    await openStudy(page)

    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('.cockpit-angled-rail-rig')).toBeHidden()

    await page.keyboard.press('Escape')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'false')
    await expect(page.locator('.cockpit-angled-rail-rig')).toBeVisible()

    const selected = page.locator('.expansion-practical-node[data-selected="true"]')
    if (await selected.getAttribute('data-expanded') !== 'true') await selected.click()
    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })
    await expect(page.locator('.cockpit-angled-rail-rig')).toBeHidden()
  })
})
