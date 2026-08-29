import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'

async function openStudy(page: Page, width: number, height = 1000) {
  await page.setViewportSize({ width, height })
  await page.goto(route)
  await expect(page.locator('html')).toHaveAttribute('data-human-review256', 'true')
  await expect(page.locator('.cockpit-angled-rail-rig')).toBeVisible()
}

async function expectVisibleWorkUnitSpacing(page: Page, width: number) {
  await openStudy(page, width)
  await page.locator('#conversation-expand').click()
  await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
  await page.locator('[data-conversation-rail-option="boxes"]').click()
  await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'boxes')

  const list = page.locator('.reintegration-thread-list')
  const rowGap = await list.evaluate((element) => Number.parseFloat(getComputedStyle(element).rowGap))
  expect(rowGap).toBeLessThanOrEqual(0.5)

  const projectThread = page.locator('.reintegration-thread-item[data-thread-scope="project"]')
  const projectMargin = await projectThread.evaluate((element) => Number.parseFloat(getComputedStyle(element).marginBottom))
  expect(projectMargin).toBeGreaterThanOrEqual(16)

  const workRows = page.locator('.reintegration-thread-item[data-thread-scope="work"]')
  const firstWorkMargin = await workRows.first().evaluate((element) => Number.parseFloat(getComputedStyle(element).marginBottom))
  expect(firstWorkMargin).toBeGreaterThanOrEqual(16)

  const project = await page.locator('.reintegration-project-thread-artifact').boundingBox()
  const surfaces = page.locator('.reintegration-thread-item[data-thread-scope="work"] .conversation-canonical-node .node-surface')
  const count = await surfaces.count()
  expect(project).not.toBeNull()
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
    const visibleGap = current.y - (previous.y + previous.height)
    expect(visibleGap).toBeGreaterThanOrEqual(20)
  }
}

test.describe('Checkpoint 256 review corrections on the canonical Cockpit route', () => {
  test('Conversation WorkUnits have structural visible separation at the normal desktop viewport', async ({ page }) => {
    await expectVisibleWorkUnitSpacing(page, 1600)
  })

  test('Conversation WorkUnits retain structural visible separation at the narrow review viewport', async ({ page }) => {
    await expectVisibleWorkUnitSpacing(page, 760)
  })

  test('the current flat rail restores Fullscreen and removes the two rejected rail controls', async ({ page }) => {
    await openStudy(page, 1600)

    await expect(page.locator('#fullscreen-world')).toBeVisible()
    await expect(page.locator('#toggle-detail')).toBeHidden()
    await expect(page.locator('#hud-hide')).toBeHidden()

    await page.locator('.cockpit-angled-rail-clarity').click()
    await expect(page.locator('.cockpit-angled-rail-rig')).toHaveAttribute('data-clarity', 'expanded')
    await expect(page.locator('#fullscreen-world')).toBeVisible()
    await expect(page.locator('#fullscreen-world')).toHaveAttribute('data-tooltip', 'Fullscreen')
    await expect(page.locator('#toggle-detail')).toBeHidden()
    await expect(page.locator('#hud-hide')).toBeHidden()
  })
})
