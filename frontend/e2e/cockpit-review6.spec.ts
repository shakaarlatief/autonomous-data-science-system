import { expect, test } from '@playwright/test'

test.describe('ADS Cockpit sixth human-review repair iteration', () => {
  test('ambient depth belongs to the full finite grid world without a clipped project-plane glow', async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 900 })
    await page.goto('/cockpit')

    for (let index = 0; index < 6; index += 1) {
      await page.getByRole('button', { name: 'Zoom out project map' }).click()
    }
    await expect(page.getByRole('button', { name: /Zoom level 45 percent/i })).toBeVisible()

    const world = page.locator('.project-world')
    const canvas = page.locator('.project-canvas')
    const geometry = await Promise.all([world.boundingBox(), canvas.boundingBox()])
    const [worldBox, canvasBox] = geometry
    expect(worldBox).not.toBeNull()
    expect(canvasBox).not.toBeNull()
    expect(worldBox?.width ?? 0).toBeGreaterThan((canvasBox?.width ?? 0) + 500)
    expect(worldBox?.height ?? 0).toBeGreaterThan((canvasBox?.height ?? 0) + 500)

    const worldAmbient = await world.evaluate((element) => getComputedStyle(element, '::before').backgroundImage)
    const canvasAmbient = await canvas.evaluate((element) => ({
      content: getComputedStyle(element, '::before').content,
      backgroundImage: getComputedStyle(element, '::before').backgroundImage,
    }))

    expect(worldAmbient).toContain('radial-gradient')
    expect(canvasAmbient.content === 'none' || canvasAmbient.backgroundImage === 'none').toBe(true)
  })

  test('stage ruler begins and ends with the rendered semantic stage regions at minimum zoom', async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 900 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/cockpit')

    for (let index = 0; index < 6; index += 1) {
      await page.getByRole('button', { name: 'Zoom out project map' }).click()
    }
    await expect(page.getByRole('button', { name: /Zoom level 45 percent/i })).toBeVisible()

    const track = page.locator('.cockpit-stage-ruler-track')
    const framingZone = page.locator('.stage-framing')
    const evaluationZone = page.locator('.stage-evaluation')
    const framingButton = page.getByRole('button', { name: 'Framing', exact: true })
    const evaluationButton = page.getByRole('button', { name: 'Evaluation', exact: true })

    await expect.poll(async () => {
      const [trackBox, framingBox] = await Promise.all([track.boundingBox(), framingZone.boundingBox()])
      if (!trackBox || !framingBox) return 999
      return Math.abs(trackBox.x - framingBox.x)
    }).toBeLessThan(2)

    await expect.poll(async () => {
      const [trackBox, evaluationBox] = await Promise.all([track.boundingBox(), evaluationZone.boundingBox()])
      if (!trackBox || !evaluationBox) return 999
      return Math.abs((trackBox.x + trackBox.width) - (evaluationBox.x + evaluationBox.width))
    }).toBeLessThan(2)

    const edgeStyles = await Promise.all([
      framingButton.evaluate((element) => ({
        textAlign: getComputedStyle(element).textAlign,
        lineLeft: getComputedStyle(element, '::after').left,
        lineRight: getComputedStyle(element, '::after').right,
      })),
      evaluationButton.evaluate((element) => ({
        textAlign: getComputedStyle(element).textAlign,
        lineLeft: getComputedStyle(element, '::after').left,
        lineRight: getComputedStyle(element, '::after').right,
      })),
    ])
    expect(edgeStyles[0]).toEqual(edgeStyles[1])
    expect(edgeStyles[0].textAlign).toBe('left')
  })

  test('trackpad-style pinch zoom uses faster anchored frame-coalesced progression', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    const dataNode = page.locator('[data-cockpit-node="data"]')
    const canvas = page.locator('.project-canvas')
    const nodeBefore = await dataNode.boundingBox()
    expect(nodeBefore).not.toBeNull()

    const anchorX = (nodeBefore?.x ?? 0) + (nodeBefore?.width ?? 0) / 2
    const anchorY = (nodeBefore?.y ?? 0) + (nodeBefore?.height ?? 0) / 2

    await viewport.dispatchEvent('wheel', {
      ctrlKey: true,
      deltaY: -18,
      deltaMode: 0,
      clientX: anchorX,
      clientY: anchorY,
    })

    await expect.poll(async () => Number.parseFloat(await canvas.evaluate((element) => element.style.zoom || '1'))).toBeGreaterThan(1)
    const firstZoom = Number.parseFloat(await canvas.evaluate((element) => element.style.zoom || '1'))
    expect(firstZoom).toBeLessThanOrEqual(1.06)

    const nodeAfter = await dataNode.boundingBox()
    expect(nodeAfter).not.toBeNull()
    const afterCenterX = (nodeAfter?.x ?? 0) + (nodeAfter?.width ?? 0) / 2
    const afterCenterY = (nodeAfter?.y ?? 0) + (nodeAfter?.height ?? 0) / 2
    expect(Math.abs(afterCenterX - anchorX)).toBeLessThan(10)
    expect(Math.abs(afterCenterY - anchorY)).toBeLessThan(10)

    for (let index = 0; index < 5; index += 1) {
      await viewport.dispatchEvent('wheel', {
        ctrlKey: true,
        deltaY: -18,
        deltaMode: 0,
        clientX: anchorX,
        clientY: anchorY,
      })
      await page.waitForTimeout(35)
    }

    await expect.poll(async () => Number.parseFloat(await canvas.evaluate((element) => element.style.zoom || '1'))).toBeGreaterThan(firstZoom + 0.12)
    const finalZoom = Number.parseFloat(await canvas.evaluate((element) => element.style.zoom || '1'))
    expect(finalZoom).toBeLessThan(1.35)

    const nodeFinal = await dataNode.boundingBox()
    expect(nodeFinal).not.toBeNull()
    const finalCenterX = (nodeFinal?.x ?? 0) + (nodeFinal?.width ?? 0) / 2
    const finalCenterY = (nodeFinal?.y ?? 0) + (nodeFinal?.height ?? 0) / 2
    expect(Math.abs(finalCenterX - anchorX)).toBeLessThan(18)
    expect(Math.abs(finalCenterY - anchorY)).toBeLessThan(18)
  })

  test('Jump to palette re-clamps above the composer when leaving a tall/fullscreen-like viewport', async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 900 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/cockpit')

    await page.getByRole('button', { name: 'Jump to project work' }).click()
    const palette = page.getByRole('dialog', { name: 'Jump to project work' })
    const composer = page.getByRole('textbox', { name: 'Ask or direct the system' }).locator('xpath=ancestor::form')
    await expect(palette).toBeVisible()

    await page.setViewportSize({ width: 1600, height: 720 })

    await expect.poll(async () => {
      const [paletteBox, composerBox] = await Promise.all([palette.boundingBox(), composer.boundingBox()])
      if (!paletteBox || !composerBox) return -999
      return composerBox.y - (paletteBox.y + paletteBox.height)
    }).toBeGreaterThanOrEqual(8)

    const results = page.locator('.cockpit-jump-results')
    await results.evaluate((element) => element.scrollTo({ top: element.scrollHeight }))
    const lastResult = page.getByRole('button', { name: /Subgroup review/i })
    await lastResult.scrollIntoViewIfNeeded()
    await expect(lastResult).toBeVisible()
    await lastResult.click()

    await expect(palette).toHaveCount(0)
    await expect(page.locator('[data-cockpit-node="review"]')).toBeInViewport()
  })
})