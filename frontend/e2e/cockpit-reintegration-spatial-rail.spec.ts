import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'

async function openVariant(page: Page, variant: 'blade' | 'deck' | 'float') {
  await page.setViewportSize({ width: 1600, height: 1000 })
  await page.goto(`${route}?rail=${variant}`)
  await expect(page.locator('html')).toHaveAttribute('data-spatial-rail-study', variant)
  await expect(page.locator('.spatial-rail-rig')).toBeVisible()
  await expect(page.locator('.spatial-rail-grip')).toBeVisible()
  await expect(page.locator('#map-tools-fold')).toBeHidden()
}

async function dragGrip(page: Page, deltaX: number, deltaY = 0) {
  const grip = page.locator('.spatial-rail-grip')
  const box = await grip.boundingBox()
  expect(box).not.toBeNull()
  const x = (box?.x ?? 0) + (box?.width ?? 0) / 2
  const y = (box?.y ?? 0) + (box?.height ?? 0) / 2

  await page.mouse.move(x, y)
  await page.mouse.down()
  await page.mouse.move(x + deltaX, y + deltaY, { steps: 8 })
  await page.mouse.up()
}

async function selectedWorkKey(page: Page) {
  return page.locator('.expansion-practical-node[data-selected="true"]').getAttribute('data-node-key')
}

test.describe('advanced spatial edge-rail studies', () => {
  test('A Extruded Blade pulls into the Cockpit and reveals a labelled tool surface without changing project selection', async ({ page }) => {
    await openVariant(page, 'blade')
    const beforeSelection = await selectedWorkKey(page)

    const compactWidth = await page.locator('.reintegration-tools').evaluate((element) => element.getBoundingClientRect().width)
    expect(compactWidth).toBeLessThan(60)

    await dragGrip(page, -155)

    const rig = page.locator('.spatial-rail-rig')
    await expect(rig).toHaveAttribute('data-state', 'open')
    await expect(rig).toHaveAttribute('data-open', 'true')

    const openWidth = await page.locator('.reintegration-tools').evaluate((element) => element.getBoundingClientRect().width)
    expect(openWidth).toBeGreaterThan(180)

    const navigationLabel = page.locator('.spatial-rail-layer[data-layer="navigation"] .spatial-rail-layer-label')
    await expect(navigationLabel).toHaveText('Navigation')
    await expect.poll(async () => navigationLabel.evaluate((element) => Number(getComputedStyle(element).opacity))).toBeGreaterThan(0.9)

    expect(await selectedWorkKey(page)).toBe(beforeSelection)

    /* The real search command remains live inside the pulled blade. */
    await page.locator('#product-jump-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'true')
    await expect(page.locator('#jump-input')).toBeFocused()
  })

  test('B Layered Deck fans navigation, work and system controls into separate depth planes while preserving semantics', async ({ page }) => {
    await openVariant(page, 'deck')
    const beforeSelection = await selectedWorkKey(page)

    await expect(page.locator('.spatial-rail-layer')).toHaveCount(3)
    await dragGrip(page, -150)

    const rig = page.locator('.spatial-rail-rig')
    await expect(rig).toHaveAttribute('data-state', 'open')
    await expect(rig).toHaveAttribute('data-open', 'true')

    const nav = await page.locator('.spatial-rail-layer[data-layer="navigation"]').boundingBox()
    const work = await page.locator('.spatial-rail-layer[data-layer="work"]').boundingBox()
    const system = await page.locator('.spatial-rail-layer[data-layer="system"]').boundingBox()
    expect(nav).not.toBeNull()
    expect(work).not.toBeNull()
    expect(system).not.toBeNull()

    expect((work?.x ?? 0)).toBeLessThan((nav?.x ?? 0) - 40)
    expect((system?.x ?? 0)).toBeLessThan((work?.x ?? 0) - 40)

    const workOpacity = await page.locator('.spatial-rail-layer[data-layer="work"]').evaluate((element) => Number(getComputedStyle(element).opacity))
    const systemOpacity = await page.locator('.spatial-rail-layer[data-layer="system"]').evaluate((element) => Number(getComputedStyle(element).opacity))
    expect(workOpacity).toBeGreaterThan(0.9)
    expect(systemOpacity).toBeGreaterThan(0.9)

    expect(await selectedWorkKey(page)).toBe(beforeSelection)

    /* A real secondary control is usable only after the layers fan open. */
    await page.locator('#appearance-controls-toggle').click()
    await expect(page.locator('#reintegration-appearance-panel')).toBeVisible()
  })

  test('C Dock and Float detaches into the project world, moves freely, and snaps back to the edge without work-state mutation', async ({ page }) => {
    await openVariant(page, 'float')
    const beforeSelection = await selectedWorkKey(page)
    const rig = page.locator('.spatial-rail-rig')

    const docked = await rig.boundingBox()
    expect(docked).not.toBeNull()

    await dragGrip(page, -135, 16)
    await expect(rig).toHaveAttribute('data-state', 'floating')

    const detached = await rig.boundingBox()
    expect(detached).not.toBeNull()
    expect((detached?.x ?? 0)).toBeLessThan((docked?.x ?? 0) - 90)

    await dragGrip(page, -180, 85)
    const moved = await rig.boundingBox()
    expect(moved).not.toBeNull()
    expect((moved?.x ?? 0)).toBeLessThan((detached?.x ?? 0) - 120)
    expect((moved?.y ?? 0)).toBeGreaterThan((detached?.y ?? 0) + 40)

    /* Opening a real floating-rail command anchors its surface beside the rail. */
    await page.locator('#product-jump-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'true')
    const search = await page.locator('.reintegration-search').boundingBox()
    expect(search).not.toBeNull()
    expect((search?.right ?? ((search?.x ?? 0) + (search?.width ?? 0)))).toBeLessThanOrEqual((moved?.x ?? 0) + 6)
    await page.keyboard.press('Escape')

    /* Move the floating object back into the right-edge snap zone. */
    const floatingBox = await rig.boundingBox()
    expect(floatingBox).not.toBeNull()
    const gripBox = await page.locator('.spatial-rail-grip').boundingBox()
    expect(gripBox).not.toBeNull()
    const startX = (gripBox?.x ?? 0) + (gripBox?.width ?? 0) / 2
    const startY = (gripBox?.y ?? 0) + (gripBox?.height ?? 0) / 2
    const stageBox = await page.locator('#reintegration-stage').boundingBox()
    expect(stageBox).not.toBeNull()
    const targetX = (stageBox?.x ?? 0) + (stageBox?.width ?? 0) - 30

    await page.mouse.move(startX, startY)
    await page.mouse.down()
    await page.mouse.move(targetX, startY, { steps: 12 })
    await page.mouse.up()

    await expect(rig).toHaveAttribute('data-state', 'docked')
    const redocked = await rig.boundingBox()
    expect(redocked).not.toBeNull()
    expect(Math.abs((redocked?.x ?? 0) - (docked?.x ?? 0))).toBeLessThan(3)
    expect(await selectedWorkKey(page)).toBe(beforeSelection)
  })

  test('direct-manipulation studies disappear for full-focus Conversation and do not replace accepted focus ownership', async ({ page }) => {
    await openVariant(page, 'blade')
    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('.spatial-rail-rig')).toBeHidden()
    await expect(page.locator('.spatial-rail-study-switcher')).toBeHidden()
  })
})
