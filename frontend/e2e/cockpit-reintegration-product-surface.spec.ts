import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html?edge=none'
const nodeSelector = '.expansion-practical-node'

async function numericFontSize(page: Page, selector: string) {
  return page.locator(selector).first().evaluate((element) => parseFloat(getComputedStyle(element).fontSize))
}

test.describe('advanced integrated Cockpit product-surface study A', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('html')).toHaveAttribute('data-product-surface-study', 'a')
  })

  test('continuous grid owns the viewport while the semantic project plane no longer reads as a smaller card', async ({ page }) => {
    const stage = page.locator('#reintegration-stage')
    const world = page.locator('#reintegration-world')

    const stageBackground = await stage.evaluate((element) => ({
      image: getComputedStyle(element).backgroundImage,
      minor: getComputedStyle(element).getPropertyValue('--product-grid-minor').trim(),
      major: getComputedStyle(element).getPropertyValue('--product-grid-major').trim(),
    }))
    expect(stageBackground.image).toContain('linear-gradient')
    expect(parseFloat(stageBackground.minor)).toBeGreaterThan(0)
    expect(parseFloat(stageBackground.major)).toBeGreaterThan(parseFloat(stageBackground.minor))

    await expect(world).toHaveCSS('border-top-width', '0px')
    await expect(world).toHaveCSS('box-shadow', 'none')
    await expect(page.locator('.reintegration-input-contract')).toBeHidden()
    await expect(page.locator('.reintegration-map-status')).toBeHidden()
    await expect(page.locator('.reintegration-zoom-rail')).toBeHidden()
    await expect(page.locator('.reintegration-provisional-note')).toBeHidden()

    const beforeMinor = parseFloat(stageBackground.minor)
    const beforePosition = await stage.evaluate((element) => getComputedStyle(element).backgroundPosition)
    await page.locator('#zoom-in').click()
    await expect.poll(async () => parseFloat(await stage.evaluate((element) => getComputedStyle(element).getPropertyValue('--product-grid-minor')))).toBeGreaterThan(beforeMinor)

    await stage.evaluate((element) => {
      element.dispatchEvent(new WheelEvent('wheel', { bubbles: true, cancelable: true, deltaX: 90, deltaY: 50 }))
    })
    await expect.poll(async () => stage.evaluate((element) => getComputedStyle(element).backgroundPosition)).not.toBe(beforePosition)
  })

  test('project chrome is compact and spatial tools live in a foldable right-side rail', async ({ page }) => {
    const hud = page.locator('.reintegration-hud')
    const tools = page.locator('.reintegration-tools')
    const hudBox = await hud.boundingBox()
    const toolsBox = await tools.boundingBox()

    expect(hudBox).not.toBeNull()
    expect(toolsBox).not.toBeNull()
    expect(hudBox?.width).toBeLessThan(260)
    expect(toolsBox?.width).toBeLessThanOrEqual(50)
    expect(toolsBox?.height).toBeGreaterThan(toolsBox?.width ?? 0)
    expect((toolsBox?.x ?? 0) + (toolsBox?.width ?? 0)).toBeGreaterThan(1540)

    await expect(page.locator('#product-jump-toggle')).toBeVisible()
    await expect(page.locator('#map-tools-fold')).toBeVisible()
    await page.locator('#map-tools-fold').click()
    await expect(tools).toHaveAttribute('data-folded', 'true')
    await expect(page.locator('#zoom-in')).toBeHidden()
    await page.locator('#map-tools-fold').click()
    await expect(page.locator('#zoom-in')).toBeVisible()
  })

  test('Jump/search is invoked from the spatial rail and keeps accepted recovery behavior', async ({ page }) => {
    const search = page.locator('.reintegration-search')
    const input = page.locator('#jump-input')

    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'false')
    await expect(search).toHaveCSS('opacity', '0')

    await page.locator('#product-jump-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'true')
    await expect(search).toHaveCSS('opacity', '1')
    await expect(input).toBeFocused()

    await input.fill('Boosted candidate')
    await page.locator('#jump-button').click()
    await expect(page.locator(`${nodeSelector}[data-node-key="m"]`)).toHaveAttribute('data-selected', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'false')
  })

  test('full Conversation uses normal application typography rather than micro type', async ({ page }) => {
    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')

    expect(await numericFontSize(page, '.reintegration-user-message')).toBeGreaterThanOrEqual(14)
    expect(await numericFontSize(page, '.reintegration-ads-message')).toBeGreaterThanOrEqual(14)
    expect(await numericFontSize(page, '.reintegration-conversation-title-row h2')).toBeGreaterThanOrEqual(16)
    expect(await numericFontSize(page, '.reintegration-conversation-actions button')).toBeGreaterThanOrEqual(10.5)
    expect(await numericFontSize(page, '.reintegration-conversation-search')).toBeGreaterThanOrEqual(11)
    expect(await numericFontSize(page, '.reintegration-full-composer textarea')).toBeGreaterThanOrEqual(14)
    expect(await numericFontSize(page, '.reintegration-full-composer-actions button')).toBeGreaterThanOrEqual(10.5)
    expect(await numericFontSize(page, '.reintegration-full-composer-status')).toBeGreaterThanOrEqual(10)
  })

  test('Conversation composer is compact while remaining a full-width readable input surface', async ({ page }) => {
    await page.locator('#conversation-expand').click()
    const footer = page.locator('.reintegration-full-composer')
    const shell = page.locator('.reintegration-full-composer-shell')
    const textarea = page.locator('.reintegration-full-composer textarea')

    const footerBox = await footer.boundingBox()
    const shellBox = await shell.boundingBox()
    const textareaBox = await textarea.boundingBox()

    expect(footerBox).not.toBeNull()
    expect(shellBox).not.toBeNull()
    expect(textareaBox).not.toBeNull()
    expect(footerBox?.height).toBeLessThan(105)
    expect(shellBox?.height).toBeLessThan(78)
    expect(textareaBox?.height).toBeLessThan(48)
    expect(shellBox?.width).toBeGreaterThan(800)
  })
})
