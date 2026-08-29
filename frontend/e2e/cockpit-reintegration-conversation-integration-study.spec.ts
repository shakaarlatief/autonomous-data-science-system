import { expect, test, type Page } from '@playwright/test'

const adaptiveRoute = '/design-lab/cockpit-reintegration.html?conversation=adaptive-dock'
const canonicalRoute = '/design-lab/cockpit-reintegration.html'
const nodeSelector = '.expansion-practical-node'

async function selectedSnapshot(page: Page) {
  return page.locator(`${nodeSelector}[data-selected="true"]`).evaluate((node: HTMLElement) => ({
    key: node.dataset.nodeKey,
    selected: node.dataset.selected,
    expanded: node.dataset.expanded,
  }))
}

test.describe('Professional Conversation co-presence study', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
  })

  test('keeps the canonical no-query Cockpit outside the opt-in adaptive study', async ({ page }) => {
    await page.goto(canonicalRoute)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('#reintegration-conversation-layer')).toHaveCount(1)
    await expect(page.locator('html')).not.toHaveAttribute('data-conversation-integration', 'adaptive-dock')
    await expect(page.locator('#adaptive-conversation-threads')).toHaveCount(0)
    await expect(page.locator('#adaptive-conversation-resize-handle')).toHaveCount(0)
  })

  test('turns co-present Conversation into a compact secondary dock with invoked thread navigation', async ({ page }) => {
    await page.goto(adaptiveRoute)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('html')).toHaveAttribute('data-conversation-integration', 'adaptive-dock')

    const before = await selectedSnapshot(page)

    await expect(page.locator('#global-conversations')).toBeVisible()
    await page.locator('#global-conversations').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('.reintegration-conversation-rail')).toBeVisible()
    await expect(page.locator('#adaptive-conversation-threads')).toBeHidden()

    await page.locator('#reintegration-conversation-presentation-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    await expect(page.locator('#adaptive-conversation-threads')).toBeVisible()
    await expect(page.locator('#adaptive-conversation-resize-handle')).toBeVisible()
    await expect(page.locator('.reintegration-conversation-rail')).toBeHidden()

    const geometry = await page.locator('#reintegration-conversation-layer').evaluate((element: HTMLElement) => {
      const rect = element.getBoundingClientRect()
      return { width: rect.width, right: window.innerWidth - rect.right, viewport: window.innerWidth }
    })
    expect(geometry.width).toBeGreaterThanOrEqual(500)
    expect(geometry.width).toBeLessThanOrEqual(660)
    expect(geometry.width / geometry.viewport).toBeLessThanOrEqual(0.42)
    expect(Math.abs(geometry.right)).toBeLessThanOrEqual(1)

    await page.locator('#adaptive-conversation-threads').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'open')
    await expect(page.locator('.reintegration-conversation-rail')).toBeVisible()
    await expect(page.locator('[data-conversation-rail-option="boxes"]')).toBeVisible()
    await expect(page.locator('[data-conversation-rail-option="text"]')).toBeVisible()

    await page.locator('[data-conversation-rail-option="text"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'text')
    await page.locator('.adaptive-conversation-drawer-close').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'closed')
    await expect(page.locator('.reintegration-conversation-rail')).toBeHidden()

    expect(await selectedSnapshot(page)).toEqual(before)
  })

  test('resizes the dock without changing project state and restores the persistent rail in full focus', async ({ page }) => {
    await page.goto(adaptiveRoute)
    await expect(page.locator('#global-conversations')).toBeVisible()
    const before = await selectedSnapshot(page)

    await page.locator('#global-conversations').click()
    await page.locator('#reintegration-conversation-presentation-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')

    const layer = page.locator('#reintegration-conversation-layer')
    const handle = page.locator('#adaptive-conversation-resize-handle')
    const initialWidth = await layer.evaluate((element: HTMLElement) => element.getBoundingClientRect().width)

    await handle.focus()
    await handle.press('ArrowLeft')
    const wider = await layer.evaluate((element: HTMLElement) => element.getBoundingClientRect().width)
    expect(wider).toBeGreaterThan(initialWidth + 20)
    expect(wider).toBeLessThanOrEqual(760.5)
    expect(await selectedSnapshot(page)).toEqual(before)

    await page.locator('#reintegration-conversation-presentation-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('.reintegration-conversation-rail')).toBeVisible()
    await expect(page.locator('#adaptive-conversation-threads')).toBeHidden()
    expect(await selectedSnapshot(page)).toEqual(before)

    await page.locator('#reintegration-conversation-close').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'false')
    expect(await selectedSnapshot(page)).toEqual(before)
  })
})
