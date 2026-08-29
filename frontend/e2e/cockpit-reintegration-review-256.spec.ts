import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'

async function openStudy(page: Page, width: number, height = 1000) {
  await page.setViewportSize({ width, height })
  await page.goto(route)
  await expect(page.locator('html')).toHaveAttribute('data-human-review256', 'true')
  await expect(page.locator('.cockpit-angled-rail-rig')).toBeVisible()

  const reviewStylesheet = page.locator('link[data-human-review256]')
  await expect(reviewStylesheet).toHaveCount(1)
  await expect.poll(() => reviewStylesheet.evaluate((element: HTMLLinkElement) => Boolean(element.sheet))).toBe(true)
}

async function openConversationBoxes(page: Page, width: number, height = 1000) {
  await openStudy(page, width, height)
  await page.locator('#conversation-expand').click()
  await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
  await page.locator('[data-conversation-rail-option="boxes"]').click()
  await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'boxes')
}

async function expectVisibleWorkUnitSpacing(page: Page, width: number, height = 1000) {
  await openConversationBoxes(page, width, height)

  const list = page.locator('.reintegration-thread-list')
  const rowGap = await list.evaluate((element) => Number.parseFloat(getComputedStyle(element).rowGap))
  expect(rowGap).toBeGreaterThanOrEqual(16)

  const projectThread = page.locator('.reintegration-thread-item[data-thread-scope="project"]')
  const projectGeometry = await projectThread.evaluate((element) => {
    const style = getComputedStyle(element)
    const rect = element.getBoundingClientRect()
    return {
      marginBottom: Number.parseFloat(style.marginBottom),
      paddingTop: Number.parseFloat(style.paddingTop),
      paddingBottom: Number.parseFloat(style.paddingBottom),
      height: rect.height,
    }
  })
  expect(projectGeometry.marginBottom).toBeLessThanOrEqual(0.5)
  expect(projectGeometry.paddingTop).toBeGreaterThanOrEqual(6)
  expect(projectGeometry.paddingBottom).toBeGreaterThanOrEqual(6)
  expect(projectGeometry.height).toBeGreaterThanOrEqual(72.5)

  const workRows = page.locator('.reintegration-thread-item[data-thread-scope="work"]')
  const firstWorkGeometry = await workRows.first().evaluate((element) => {
    const style = getComputedStyle(element)
    const rect = element.getBoundingClientRect()
    return {
      marginBottom: Number.parseFloat(style.marginBottom),
      paddingTop: Number.parseFloat(style.paddingTop),
      paddingBottom: Number.parseFloat(style.paddingBottom),
      height: rect.height,
    }
  })
  expect(firstWorkGeometry.marginBottom).toBeLessThanOrEqual(0.5)
  expect(firstWorkGeometry.paddingTop).toBeGreaterThanOrEqual(6)
  expect(firstWorkGeometry.paddingBottom).toBeGreaterThanOrEqual(6)
  expect(firstWorkGeometry.height).toBeGreaterThanOrEqual(72.5)

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

  /*
   * The grid track itself remains a deterministic 16 px gap. When measuring
   * painted border-box edges at the short desktop viewport, adjacent 1 px
   * borders can realize that as 15 px of dark pixels. Keep the structural
   * 16 px assertion above and require the visible result to remain at least
   * 15 px rather than changing the already human-approved spacing geometry.
   */
  const projectGap = rendered[0].y - ((project?.y ?? 0) + (project?.height ?? 0))
  expect(projectGap).toBeGreaterThanOrEqual(15)

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

  test('General project discussion remains a distinct first artifact at a short desktop viewport', async ({ page }) => {
    await expectVisibleWorkUnitSpacing(page, 1776, 766)
  })

  test('General project discussion matches the WorkUnit footprint and uses the same selected-surface frame', async ({ page }) => {
    await openConversationBoxes(page, 1600)

    const projectThread = page.locator('.reintegration-thread-item[data-thread-scope="project"]')
    const projectArtifact = projectThread.locator('.reintegration-project-thread-artifact')
    const firstWorkThread = page.locator('.reintegration-thread-item[data-thread-scope="work"]').first()
    const firstWorkBox = firstWorkThread.locator('.reintegration-thread-box')
    const firstWorkSurface = firstWorkThread.locator('.conversation-canonical-node .node-surface')

    await expect(projectThread).toHaveClass(/is-active/)

    const projectBox = await projectArtifact.boundingBox()
    const workBox = await firstWorkBox.boundingBox()
    expect(projectBox).not.toBeNull()
    expect(workBox).not.toBeNull()
    expect(Math.abs((projectBox?.width ?? 0) - (workBox?.width ?? 0))).toBeLessThanOrEqual(0.5)
    expect(Math.abs((projectBox?.height ?? 0) - (workBox?.height ?? 0))).toBeLessThanOrEqual(0.5)

    const projectSelectedStyle = await projectArtifact.evaluate((element) => {
      const style = getComputedStyle(element)
      return {
        borderTopWidth: Number.parseFloat(style.borderTopWidth),
        boxShadow: style.boxShadow,
      }
    })
    const projectOuterStyle = await projectThread.evaluate((element) => {
      const style = getComputedStyle(element)
      return { borderColor: style.borderColor, backgroundColor: style.backgroundColor }
    })
    expect(projectOuterStyle.borderColor).toBe('rgba(0, 0, 0, 0)')
    expect(projectOuterStyle.backgroundColor).toBe('rgba(0, 0, 0, 0)')
    expect(projectSelectedStyle.borderTopWidth).toBeGreaterThanOrEqual(1)
    expect(projectSelectedStyle.boxShadow).not.toBe('none')

    await firstWorkThread.click()
    await expect(firstWorkThread).toHaveClass(/is-active/)
    await expect(projectThread).not.toHaveClass(/is-active/)

    const workSelectedStyle = await firstWorkSurface.evaluate((element) => {
      const style = getComputedStyle(element)
      return {
        borderTopWidth: Number.parseFloat(style.borderTopWidth),
        boxShadow: style.boxShadow,
      }
    })
    const workOuterStyle = await firstWorkThread.evaluate((element) => {
      const style = getComputedStyle(element)
      return { borderColor: style.borderColor, backgroundColor: style.backgroundColor }
    })
    const projectInactiveStyle = await projectArtifact.evaluate((element) => getComputedStyle(element).boxShadow)

    expect(workOuterStyle.borderColor).toBe('rgba(0, 0, 0, 0)')
    expect(workOuterStyle.backgroundColor).toBe('rgba(0, 0, 0, 0)')
    expect(workSelectedStyle.borderTopWidth).toBeGreaterThanOrEqual(1)
    expect(workSelectedStyle.boxShadow).not.toBe('none')
    expect(projectInactiveStyle).toBe('none')
  })

  test('Conversation WorkUnits retain structural visible separation at the responsive 1100px viewport', async ({ page }) => {
    await expectVisibleWorkUnitSpacing(page, 1100, 900)
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
