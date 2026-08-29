import { expect, test, type Locator, type Page } from '@playwright/test'

const canonicalRoute = '/design-lab/cockpit-reintegration.html'
const adaptiveWorkRoute = '/design-lab/cockpit-reintegration.html?conversation=adaptive-dock&focus=work&work=i&depth=x5'
const nodeSelector = '.expansion-practical-node'

async function opacity(locator: Locator) {
  return locator.evaluate((element) => Number.parseFloat(getComputedStyle(element).opacity))
}

async function expectWorkUnitRailSpacing(page: Page) {
  const list = page.locator('.reintegration-thread-list')
  await expect(list).toBeVisible()

  /*
   * The visible separation is carried by an explicit grid track gap. Live
   * browser geometry at Checkpoint 262 proved that a margin on a stretched grid
   * item can be absorbed by the auto track while a transformed canonical node
   * keeps painting outside the shrunken item.
   */
  const rowGap = await list.evaluate((element) => Number.parseFloat(getComputedStyle(element).rowGap))
  expect(rowGap).toBeGreaterThanOrEqual(16)

  const projectThread = page.locator('.reintegration-thread-item[data-thread-scope="project"]')
  const projectMargin = await projectThread.evaluate((element) => Number.parseFloat(getComputedStyle(element).marginBottom))
  expect(projectMargin).toBeLessThanOrEqual(0.5)

  const rows = page.locator('.reintegration-thread-item[data-thread-scope="work"]')
  const rowCount = await rows.count()
  expect(rowCount).toBeGreaterThan(1)

  const firstGeometry = await rows.first().evaluate((element) => {
    const style = getComputedStyle(element)
    const rect = element.getBoundingClientRect()
    return {
      top: Number.parseFloat(style.paddingTop),
      bottom: Number.parseFloat(style.paddingBottom),
      marginBottom: Number.parseFloat(style.marginBottom),
      height: rect.height,
    }
  })
  expect(firstGeometry.top).toBeGreaterThanOrEqual(6)
  expect(firstGeometry.bottom).toBeGreaterThanOrEqual(6)
  expect(firstGeometry.marginBottom).toBeLessThanOrEqual(0.5)
  expect(firstGeometry.height).toBeGreaterThanOrEqual(72.5)

  const lastMargin = await rows.last().evaluate((element) => Number.parseFloat(getComputedStyle(element).marginBottom))
  expect(lastMargin).toBeLessThanOrEqual(0.5)

  const project = await page.locator('.reintegration-project-thread-artifact').boundingBox()
  expect(project).not.toBeNull()

  const surfaces = page.locator('.reintegration-thread-item[data-thread-scope="work"] .conversation-canonical-node .node-surface')
  const count = await surfaces.count()
  expect(count).toBeGreaterThan(1)

  const rendered = []
  for (let index = 0; index < count; index += 1) {
    const box = await surfaces.nth(index).boundingBox()
    expect(box).not.toBeNull()
    if (box) rendered.push(box)
  }

  const projectGap = rendered[0].y - ((project?.y ?? 0) + (project?.height ?? 0))
  expect(projectGap).toBeGreaterThanOrEqual(16)

  for (let index = 1; index < rendered.length; index += 1) {
    const previous = rendered[index - 1]
    const current = rendered[index]
    expect(current.y - (previous.y + previous.height)).toBeGreaterThanOrEqual(20)
  }
}

test.describe('Cockpit presentation-state integrity recovery', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
  })

  test('Conversation structural spacing survives direct co-present, Threads drawer and full-focus presentation changes', async ({ page }) => {
    await page.goto(adaptiveWorkRoute)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('html')).toHaveAttribute('data-conversation-integration', 'adaptive-dock')

    /* Adaptive Dock now treats co-presence as the normal one-click workbench entry. */
    await page.locator('#global-conversations').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    await page.locator('#adaptive-conversation-threads').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'open')

    await page.locator('[data-conversation-rail-option="boxes"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'boxes')
    await expectWorkUnitRailSpacing(page)

    await page.locator('[data-conversation-rail-option="text"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'text')
    await page.locator('[data-conversation-rail-option="boxes"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'boxes')
    await expectWorkUnitRailSpacing(page)

    await page.locator('.adaptive-conversation-drawer-close').click()
    await page.locator('#reintegration-conversation-presentation-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('.reintegration-conversation-rail')).toBeVisible()
    await expectWorkUnitRailSpacing(page)

    await page.locator('#reintegration-conversation-presentation-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    await page.locator('#adaptive-conversation-threads').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail-drawer', 'open')
    await expectWorkUnitRailSpacing(page)
  })

  test('Boxes separation survives the legacy artifact rail state at a responsive 1100px viewport', async ({ page }) => {
    await page.setViewportSize({ width: 1100, height: 900 })
    await page.goto(canonicalRoute)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await page.locator('#global-conversations').click()
    await page.locator('[data-conversation-rail-option="boxes"]').click()

    /*
     * Historical Conversation code used "artifact" for the same rail mode.
     * The current UI resolves every non-Text value as Boxes. This viewport also
     * enters the <=1450px responsive canonical-WorkUnit scale that reproduced
     * the project owner's live browser failure while DevTools was docked.
     */
    await page.evaluate(() => {
      document.documentElement.dataset.conversationRail = 'artifact'
    })
    await expect(page.locator('[data-conversation-rail-option="boxes"]')).toHaveAttribute('aria-pressed', 'true')
    await expectWorkUnitRailSpacing(page)
  })

  test('Boxes separation survives the legacy artifact rail state at a wide desktop viewport', async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(canonicalRoute)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await page.locator('#global-conversations').click()
    await page.locator('[data-conversation-rail-option="boxes"]').click()
    await page.evaluate(() => {
      document.documentElement.dataset.conversationRail = 'artifact'
    })
    await expect(page.locator('[data-conversation-rail-option="boxes"]')).toHaveAttribute('aria-pressed', 'true')
    await expectWorkUnitRailSpacing(page)
  })

  test('current-process focus keeps node and relation recession synchronized through repeated state changes and WorkUnit remounts', async ({ page }) => {
    await page.goto(canonicalRoute)
    await expect(page.locator(nodeSelector)).toHaveCount(6)

    const focusStylesheet = page.locator('link[href="./cockpit-reintegration-process-focus.css"]')
    await expect(focusStylesheet).toHaveCount(1)
    await expect.poll(() => focusStylesheet.evaluate((element: HTMLLinkElement) => Boolean(element.sheet))).toBe(true)

    const current = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const context = page.locator(`${nodeSelector}[data-node-key="m"]`)
    const contextRelation = page.locator('.reintegration-relation[data-relation-id="m-v"]')
    const currentRelation = page.locator('.reintegration-relation[data-relation-id="q-i"]')

    await expect(current).toHaveAttribute('data-process-scope', 'current')
    await expect(context).toHaveAttribute('data-process-scope', 'context')

    await page.locator('#process-focus-toggle').click()
    await page.locator('[data-process-focus-mode="focused"]').click()
    await page.mouse.move(20, 20)
    await expect(page.locator('html')).toHaveAttribute('data-process-focus', 'focused')
    await expect.poll(() => opacity(context)).toBeLessThan(0.4)
    await expect.poll(() => opacity(current)).toBeGreaterThan(0.9)
    await expect(contextRelation).toHaveClass(/is-context-edge/)
    await expect(currentRelation).toHaveClass(/is-current-edge/)
    await expect.poll(() => opacity(contextRelation)).toBeLessThan(0.5)
    await expect.poll(() => opacity(currentRelation)).toBeGreaterThan(0.9)

    for (let cycle = 0; cycle < 3; cycle += 1) {
      await page.locator('[data-process-focus-mode="context"]').click()
      await expect(page.locator('html')).toHaveAttribute('data-process-focus', 'context')
      await page.locator('[data-process-focus-mode="focused"]').click()
      await page.mouse.move(20, 20)
      await expect(page.locator('html')).toHaveAttribute('data-process-focus', 'focused')
      await expect.poll(() => opacity(context)).toBeLessThan(0.4)
      await expect.poll(() => opacity(current)).toBeGreaterThan(0.9)
    }

    await context.evaluate((element: HTMLElement) => {
      const replacement = element.cloneNode(true) as HTMLElement
      replacement.removeAttribute('data-process-scope')
      replacement.querySelector('.reintegration-focus-membership-toggle')?.remove()
      element.replaceWith(replacement)
    })

    await expect(context).toHaveAttribute('data-process-scope', 'context')
    await expect(context.locator('.reintegration-focus-membership-toggle')).toHaveCount(1)
    await page.mouse.move(20, 20)
    await expect.poll(() => opacity(context)).toBeLessThan(0.4)
    await expect(contextRelation).toHaveClass(/is-context-edge/)
    await expect.poll(() => opacity(contextRelation)).toBeLessThan(0.5)
  })
})
