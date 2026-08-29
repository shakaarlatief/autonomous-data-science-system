import { expect, test, type Page } from '@playwright/test'

const adaptiveRoute = '/design-lab/cockpit-reintegration.html?conversation=adaptive-dock'
const canonicalRoute = '/design-lab/cockpit-reintegration.html'

async function openAdaptiveConversation(page: Page) {
  await page.goto(adaptiveRoute)
  await expect(page.locator('#global-conversations')).toBeVisible()
  await page.locator('#global-conversations').click()
  await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
  await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
}

async function projectRailGeometry(page: Page) {
  return page.evaluate(() => {
    const rig = document.querySelector('.cockpit-angled-rail-rig')?.getBoundingClientRect()
    const shell = document.querySelector('.cockpit-angled-rail-shell')?.getBoundingClientRect()
    const dock = document.querySelector('#reintegration-conversation-layer')?.getBoundingClientRect()
    const shellElement = document.querySelector('.cockpit-angled-rail-shell')
    const shellStyle = shellElement ? getComputedStyle(shellElement) : null

    if (!rig || !shell || !dock || !shellStyle) return null

    return {
      viewportWidth: innerWidth,
      viewportHeight: innerHeight,
      rigLeft: rig.left,
      rigRight: rig.right,
      rigTop: rig.top,
      rigBottom: rig.bottom,
      rigWidth: rig.width,
      shellLeft: shell.left,
      shellRight: shell.right,
      shellTop: shell.top,
      shellBottom: shell.bottom,
      shellWidth: shell.width,
      dockRight: dock.right,
      borderRadius: shellStyle.borderRadius,
      borderLeftWidth: Number.parseFloat(shellStyle.borderLeftWidth),
    }
  })
}

test.describe('Adaptive Conversation project-tool edge integration', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
  })

  test('turns the co-present project rail into a flush edge utility strip', async ({ page }) => {
    await openAdaptiveConversation(page)

    const rig = page.locator('.cockpit-angled-rail-rig')
    const shell = page.locator('.cockpit-angled-rail-shell')
    await expect(rig).toBeVisible()
    await expect(shell).toBeVisible()
    await expect(rig).toHaveAttribute('data-clarity', 'compact')

    const geometry = await projectRailGeometry(page)
    expect(geometry).not.toBeNull()
    expect(Math.abs(geometry!.rigRight - geometry!.viewportWidth)).toBeLessThanOrEqual(1)
    expect(Math.abs(geometry!.rigTop)).toBeLessThanOrEqual(1)
    expect(Math.abs(geometry!.rigBottom - geometry!.viewportHeight)).toBeLessThanOrEqual(1)
    expect(geometry!.rigWidth).toBeGreaterThanOrEqual(55)
    expect(geometry!.rigWidth).toBeLessThanOrEqual(57)
    expect(Math.abs(geometry!.dockRight - geometry!.shellLeft)).toBeLessThanOrEqual(2)
    expect(geometry!.borderRadius).toBe('0px')
    expect(geometry!.borderLeftWidth).toBeGreaterThanOrEqual(1)

    const toolButton = page.locator('.cockpit-angled-rail-shell .reintegration-tools button:visible').first()
    const buttonHeight = await toolButton.evaluate((element) => element.getBoundingClientRect().height)
    expect(buttonHeight).toBeGreaterThanOrEqual(37)
  })

  test('clarity expansion remains usable and the Conversation dock tracks the widened edge strip', async ({ page }) => {
    await openAdaptiveConversation(page)

    await page.locator('.cockpit-angled-rail-clarity').click()
    const rig = page.locator('.cockpit-angled-rail-rig')
    await expect(rig).toHaveAttribute('data-clarity', 'expanded')

    await expect.poll(async () => {
      const geometry = await projectRailGeometry(page)
      return geometry?.rigWidth ?? 0
    }).toBeGreaterThan(190)

    const geometry = await projectRailGeometry(page)
    expect(geometry).not.toBeNull()
    expect(geometry!.rigWidth).toBeLessThanOrEqual(197)
    expect(Math.abs(geometry!.dockRight - geometry!.shellLeft)).toBeLessThanOrEqual(2)
    expect(Math.abs(geometry!.rigRight - geometry!.viewportWidth)).toBeLessThanOrEqual(1)

    await expect(page.locator('.cockpit-angled-rail-mark span')).toBeVisible()
    await expect(page.locator('.cockpit-angled-rail-clarity-label')).toBeVisible()
  })

  test('leaves the standalone canonical Project Grid rail presentation unchanged', async ({ page }) => {
    await page.goto(canonicalRoute)
    const rig = page.locator('.cockpit-angled-rail-rig')
    await expect(rig).toBeVisible()

    const geometry = await projectRailGeometry(page)
    expect(geometry).not.toBeNull()
    expect(geometry!.rigTop).toBeGreaterThan(60)
    expect(geometry!.rigWidth).toBeGreaterThan(80)
    expect(geometry!.borderRadius).not.toBe('0px')
  })
})
