import { expect, test } from '@playwright/test'

test.describe('ADS Cockpit fifth human-review iteration', () => {
  test('continuous grid world keeps the semantic stage ruler pinned while the project plane moves beneath it', async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 900 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    const world = page.locator('.project-world')
    const canvas = page.locator('.project-canvas')
    const ruler = page.locator('.cockpit-stage-ruler')
    const rulerTrack = page.locator('.cockpit-stage-ruler-track')
    const stage = page.getByRole('button', { name: 'Data & exploration', exact: true })

    for (let index = 0; index < 6; index += 1) {
      await page.getByRole('button', { name: 'Zoom out project map' }).click()
    }
    await expect(page.getByRole('button', { name: /Zoom level 45 percent/i })).toBeVisible()

    const worldBackground = await world.evaluate((element) => getComputedStyle(element).backgroundImage)
    expect(worldBackground).toContain('linear-gradient')

    await viewport.evaluate((element) => element.scrollTo({ left: 0, top: 0 }))
    await expect.poll(async () => {
      const viewportBox = await viewport.boundingBox()
      const canvasBox = await canvas.boundingBox()
      const stageBox = await stage.boundingBox()
      const rulerBox = await ruler.boundingBox()
      if (!viewportBox || !canvasBox || !stageBox || !rulerBox) return null
      return {
        reserveAboveCanvas: canvasBox.y - viewportBox.y,
        rulerOffset: rulerBox.y - viewportBox.y,
        stageOffset: stageBox.y - viewportBox.y,
      }
    }).toEqual(expect.objectContaining({
      rulerOffset: expect.any(Number),
      stageOffset: expect.any(Number),
    }))

    const topGeometry = await Promise.all([
      viewport.boundingBox(),
      canvas.boundingBox(),
      ruler.boundingBox(),
      stage.boundingBox(),
    ])
    const [viewportBox, canvasBox, rulerBox, stageBox] = topGeometry
    expect(viewportBox).not.toBeNull()
    expect(canvasBox).not.toBeNull()
    expect(rulerBox).not.toBeNull()
    expect(stageBox).not.toBeNull()
    expect((canvasBox?.y ?? 0) - (viewportBox?.y ?? 0)).toBeGreaterThan(250)
    expect(Math.abs((rulerBox?.y ?? 0) - (viewportBox?.y ?? 0))).toBeLessThan(3)
    expect(Math.abs((stageBox?.y ?? 0) - (viewportBox?.y ?? 0))).toBeLessThan(4)

    await viewport.evaluate((element) => element.scrollTo({ left: 240, top: element.scrollHeight }))
    await expect.poll(async () => {
      const viewportRect = await viewport.boundingBox()
      const stageRect = await stage.boundingBox()
      if (!viewportRect || !stageRect) return 999
      return Math.abs(stageRect.y - viewportRect.y)
    }).toBeLessThan(4)

    await expect.poll(async () => {
      const canvasRect = await canvas.boundingBox()
      const trackRect = await rulerTrack.boundingBox()
      if (!canvasRect || !trackRect) return 999
      return Math.abs(canvasRect.x - trackRect.x)
    }).toBeLessThan(2)
  })

  test('project-map controls use a compact vertical rail and still fold into the right edge', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 })
    await page.goto('/cockpit')

    const toolbar = page.getByRole('group', { name: 'Project map controls' })
    await expect(toolbar).toBeVisible()

    const toolbarBox = await toolbar.boundingBox()
    const detailsBox = await page.getByRole('button', { name: 'Details' }).boundingBox()
    const zoomOutBox = await page.getByRole('button', { name: 'Zoom out project map' }).boundingBox()
    const fitBox = await page.getByRole('button', { name: 'Fit project to viewport' }).boundingBox()
    const jumpBox = await page.getByRole('button', { name: 'Jump to project work' }).boundingBox()
    const focusBox = await page.getByRole('button', { name: 'System focus' }).boundingBox()

    expect(toolbarBox).not.toBeNull()
    expect(detailsBox).not.toBeNull()
    expect(zoomOutBox).not.toBeNull()
    expect(fitBox).not.toBeNull()
    expect(jumpBox).not.toBeNull()
    expect(focusBox).not.toBeNull()
    expect(toolbarBox?.width ?? 999).toBeLessThan(70)
    expect(toolbarBox?.height ?? 0).toBeGreaterThan((toolbarBox?.width ?? 1) * 4)
    expect(zoomOutBox?.y ?? 0).toBeGreaterThan(detailsBox?.y ?? 0)
    expect(fitBox?.y ?? 0).toBeGreaterThan(zoomOutBox?.y ?? 0)
    expect(jumpBox?.y ?? 0).toBeGreaterThan(fitBox?.y ?? 0)
    expect(focusBox?.y ?? 0).toBeGreaterThan(jumpBox?.y ?? 0)
    expect(Math.abs((detailsBox?.x ?? 0) - (focusBox?.x ?? 0))).toBeLessThan(3)

    await page.getByRole('button', { name: 'Hide project map controls' }).click()
    await expect(toolbar).toHaveCount(0)
    await expect(page.getByRole('button', { name: 'Show project map controls' })).toBeVisible()
    await page.getByRole('button', { name: 'Show project map controls' }).click()
    await expect(page.getByRole('group', { name: 'Project map controls' })).toBeVisible()
  })
})
