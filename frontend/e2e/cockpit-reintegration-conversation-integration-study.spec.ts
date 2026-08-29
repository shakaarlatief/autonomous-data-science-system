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

async function dockWidth(page: Page) {
  return page.locator('#reintegration-conversation-layer').evaluate((element: HTMLElement) => element.getBoundingClientRect().width)
}

async function openConversationFromRail(page: Page) {
  await expect(page.locator('#global-conversations')).toBeVisible()
  await page.locator('#global-conversations').click()
  await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
  await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
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
    await expect(page.locator('.adaptive-deep-dive-action')).toHaveCount(0)
  })

  test('opens directly into co-present, preserves the Project Grid rail, and keeps Threads invoked', async ({ page }) => {
    await page.goto(adaptiveRoute)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('html')).toHaveAttribute('data-conversation-integration', 'adaptive-dock')
    await expect(page.locator('.cockpit-angled-rail-shell')).toBeVisible()

    const before = await selectedSnapshot(page)
    await openConversationFromRail(page)

    await expect(page.locator('#adaptive-conversation-threads')).toBeVisible()
    await expect(page.locator('#adaptive-conversation-resize-handle')).toBeVisible()
    await expect(page.locator('.reintegration-conversation-rail')).toBeHidden()
    await expect(page.locator('.reintegration-conversation-subtitle')).toBeHidden()

    const geometry = await page.evaluate(() => {
      const dock = document.querySelector('#reintegration-conversation-layer')?.getBoundingClientRect()
      const rail = document.querySelector('.cockpit-angled-rail-shell')?.getBoundingClientRect()
      return dock && rail ? { dockRight: dock.right, railLeft: rail.left, dockWidth: dock.width } : null
    })
    expect(geometry).not.toBeNull()
    expect(geometry!.dockRight).toBeLessThanOrEqual(geometry!.railLeft - 4)
    expect(geometry!.dockWidth).toBeGreaterThanOrEqual(500)

    await page.locator('.cockpit-angled-rail-clarity').click()
    await expect(page.locator('.cockpit-angled-rail-rig')).toHaveAttribute('data-clarity', 'expanded')
    await expect.poll(async () => page.evaluate(() => {
      const dock = document.querySelector('#reintegration-conversation-layer')?.getBoundingClientRect()
      const rail = document.querySelector('.cockpit-angled-rail-shell')?.getBoundingClientRect()
      return dock && rail ? rail.left - dock.right : -1
    })).toBeGreaterThanOrEqual(4)

    await page.locator('#adaptive-conversation-threads').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'open')
    await expect(page.locator('.reintegration-conversation-rail')).toBeVisible()
    await expect(page.locator('[data-conversation-rail-option="boxes"]')).toBeVisible()
    await expect(page.locator('[data-conversation-rail-option="text"]')).toBeVisible()

    await page.locator('[data-conversation-rail-option="text"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'text')
    await page.locator('.adaptive-conversation-drawer-close').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'closed')
    expect(await selectedSnapshot(page)).toEqual(before)
  })

  test('supports a materially wider and narrower dock without mutating project state', async ({ page }) => {
    await page.goto(adaptiveRoute)
    const before = await selectedSnapshot(page)
    await openConversationFromRail(page)

    const handle = page.locator('#adaptive-conversation-resize-handle')
    const initialWidth = await dockWidth(page)

    await handle.focus()
    await handle.press('ArrowLeft')
    await handle.press('ArrowLeft')
    await expect.poll(() => dockWidth(page)).toBeGreaterThan(initialWidth + 60)
    const wider = await dockWidth(page)
    expect(wider).toBeLessThanOrEqual(900.5)

    for (let index = 0; index < 8; index += 1) await handle.press('ArrowRight')
    await expect.poll(() => dockWidth(page)).toBeLessThan(wider - 180)
    const narrower = await dockWidth(page)
    expect(narrower).toBeGreaterThanOrEqual(359.5)
    expect(await selectedSnapshot(page)).toEqual(before)

    await page.keyboard.press('Shift+C')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('.reintegration-conversation-rail')).toBeVisible()
    await page.keyboard.press('Shift+C')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    expect(await selectedSnapshot(page)).toEqual(before)
  })

  test('offers Deep Dive directly from expanded work and makes Deep Dive + Chat a real split workspace', async ({ page }) => {
    await page.goto(adaptiveRoute)
    const selected = page.locator(`${nodeSelector}[data-selected="true"]`)
    await expect(selected).toHaveCount(1)

    if (await selected.getAttribute('data-expanded') !== 'true') await selected.click()
    await expect(selected).toHaveAttribute('data-expanded', 'true')

    const directDeepDive = selected.locator(':scope > .adaptive-deep-dive-action')
    await expect(directDeepDive).toBeVisible()
    await directDeepDive.click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })

    const labelStyle = await page.locator('.reintegration-specialist-panel > span').first().evaluate((element) => {
      const style = getComputedStyle(element)
      return { fontSize: Number.parseFloat(style.fontSize), letterSpacing: style.letterSpacing, transform: style.textTransform }
    })
    expect(labelStyle.fontSize).toBeGreaterThanOrEqual(10.5)
    expect(labelStyle.transform).toBe('none')

    await page.locator('#deep-work-conversation').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-scope', 'work')

    const split = await page.evaluate(() => {
      const deep = document.querySelector('#reintegration-specialist-layer')?.getBoundingClientRect()
      const dock = document.querySelector('#reintegration-conversation-layer')?.getBoundingClientRect()
      return deep && dock ? { deepRight: deep.right, dockLeft: dock.left, dockRight: dock.right, viewport: innerWidth } : null
    })
    expect(split).not.toBeNull()
    expect(Math.abs(split!.deepRight - split!.dockLeft)).toBeLessThanOrEqual(2)
    expect(Math.abs(split!.dockRight - split!.viewport)).toBeLessThanOrEqual(2)

    const beforeResize = await dockWidth(page)
    const handle = page.locator('#adaptive-conversation-resize-handle')
    await handle.focus()
    await handle.press('ArrowLeft')
    await expect.poll(() => dockWidth(page)).toBeGreaterThan(beforeResize + 20)
    await expect.poll(async () => page.evaluate(() => {
      const deep = document.querySelector('#reintegration-specialist-layer')?.getBoundingClientRect()
      const dock = document.querySelector('#reintegration-conversation-layer')?.getBoundingClientRect()
      return deep && dock ? Math.abs(deep.right - dock.left) : 999
    })).toBeLessThanOrEqual(2)
  })

  test('uses practical keyboard recovery: drawer -> conversation -> Deep Dive', async ({ page }) => {
    await page.goto(adaptiveRoute)

    await page.keyboard.press('d')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })

    await page.keyboard.press('c')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-scope', 'work')

    await page.keyboard.press('t')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'open')

    await page.keyboard.press('Escape')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'closed')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused')

    await page.keyboard.press('Escape')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'false')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused')

    await page.keyboard.press('Escape')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'false')
  })
})
