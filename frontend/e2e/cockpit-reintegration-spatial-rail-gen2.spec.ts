import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'

type Variant = 'hinge' | 'stack' | 'console'

async function openVariant(page: Page, variant: Variant) {
  await page.setViewportSize({ width: 1600, height: 1000 })
  await page.goto(`${route}?edge=${variant}`)
  await expect(page.locator('html')).toHaveAttribute('data-spatial-rail-gen2', variant)
  await expect(page.locator('.cockpit-edge-rig')).toBeVisible()
  await expect(page.locator('.cockpit-edge-grip')).toBeVisible()
  await expect(page.locator('#map-tools-fold')).toBeHidden()
}

async function dragGrip(page: Page, deltaX: number) {
  const grip = page.locator('.cockpit-edge-grip')
  const box = await grip.boundingBox()
  expect(box).not.toBeNull()
  const x = (box?.x ?? 0) + (box?.width ?? 0) / 2
  const y = (box?.y ?? 0) + (box?.height ?? 0) / 2

  await page.mouse.move(x, y)
  await page.mouse.down()
  await page.mouse.move(x + deltaX, y, { steps: 10 })
  await page.mouse.up()
}

async function selectedWorkKey(page: Page) {
  return page.locator('.expansion-practical-node[data-selected="true"]').getAttribute('data-node-key')
}

test.describe('second-generation architectural Cockpit edge studies', () => {
  test('A Hinged Instrument Panel pivots into the world as an actual depth surface while preserving selection', async ({ page }) => {
    await openVariant(page, 'hinge')
    const beforeSelection = await selectedWorkKey(page)
    const shell = page.locator('.cockpit-edge-shell')

    const compactWidth = await shell.evaluate((element) => element.getBoundingClientRect().width)
    expect(compactWidth).toBeLessThan(85)

    await dragGrip(page, -220)
    await expect(page.locator('.cockpit-edge-rig')).toHaveAttribute('data-state', 'open')

    const openWidth = await shell.evaluate((element) => element.getBoundingClientRect().width)
    expect(openWidth).toBeGreaterThan(240)

    const transform = await shell.evaluate((element) => getComputedStyle(element).transform)
    expect(transform).not.toBe('none')

    await expect(page.locator('.cockpit-edge-bank-label')).toHaveCount(3)
    await expect(page.locator('#cockpit-edge-context-title')).not.toHaveText('Project controls')
    expect(await selectedWorkKey(page)).toBe(beforeSelection)

    await page.locator('#product-jump-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-product-search-open', 'true')
    await expect(page.locator('#jump-input')).toBeFocused()
  })

  test('B Telescoping Layer Stack creates three separately displaced functional instrument planes', async ({ page }) => {
    await openVariant(page, 'stack')
    const beforeSelection = await selectedWorkKey(page)

    await expect(page.locator('.cockpit-edge-bank')).toHaveCount(3)
    await dragGrip(page, -255)
    await expect(page.locator('.cockpit-edge-rig')).toHaveAttribute('data-state', 'open')

    const nav = await page.locator('.cockpit-edge-bank[data-bank="navigation"]').boundingBox()
    const work = await page.locator('.cockpit-edge-bank[data-bank="work"]').boundingBox()
    const system = await page.locator('.cockpit-edge-bank[data-bank="system"]').boundingBox()
    expect(nav).not.toBeNull()
    expect(work).not.toBeNull()
    expect(system).not.toBeNull()

    expect(nav?.x ?? 0).toBeLessThan((work?.x ?? 0) - 40)
    expect(work?.x ?? 0).toBeLessThan((system?.x ?? 0) - 40)

    const transforms = await page.locator('.cockpit-edge-bank').evaluateAll((elements) =>
      elements.map((element) => getComputedStyle(element).transform),
    )
    expect(new Set(transforms).size).toBe(3)
    expect(await selectedWorkKey(page)).toBe(beforeSelection)

    await page.locator('#appearance-controls-toggle').click()
    await expect(page.locator('#reintegration-appearance-panel')).toBeVisible()
  })

  test('C Spatial Command Console grows into a deep context-aware command surface using the real selected WorkUnit', async ({ page }) => {
    await openVariant(page, 'console')
    const beforeSelection = await selectedWorkKey(page)

    await dragGrip(page, -300)
    const rig = page.locator('.cockpit-edge-rig')
    await expect(rig).toHaveAttribute('data-state', 'open')

    const shellWidth = await page.locator('.cockpit-edge-shell').evaluate((element) => element.getBoundingClientRect().width)
    expect(shellWidth).toBeGreaterThan(315)

    await expect(page.locator('.cockpit-edge-header')).toBeVisible()
    const initialContext = await page.locator('#cockpit-edge-context-title').textContent()
    expect(initialContext?.trim().length ?? 0).toBeGreaterThan(3)

    const question = page.locator('.expansion-practical-node[data-node-key="q"]')
    await question.click()
    await expect(question).toHaveAttribute('data-selected', 'true')
    await expect(page.locator('#cockpit-edge-context-title')).toHaveText('Resolve target definition')
    expect(await selectedWorkKey(page)).toBe('q')
    expect(await selectedWorkKey(page)).not.toBe(beforeSelection)

    await page.locator('#process-focus-toggle').click()
    await expect(page.locator('#reintegration-process-focus-panel')).toBeVisible()
  })

  test('architectural edge studies yield full-stage ownership to Conversation and Deep Dive', async ({ page }) => {
    await openVariant(page, 'hinge')

    await page.locator('#conversation-expand').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('.cockpit-edge-rig')).toBeHidden()
    await expect(page.locator('.cockpit-edge-switcher')).toBeHidden()

    await page.keyboard.press('Escape')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'false')
    await expect(page.locator('.cockpit-edge-rig')).toBeVisible()

    const selected = page.locator('.expansion-practical-node[data-selected="true"]')
    if (await selected.getAttribute('data-expanded') !== 'true') await selected.click()
    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2500 })
    await expect(page.locator('.cockpit-edge-rig')).toBeHidden()
  })
})
