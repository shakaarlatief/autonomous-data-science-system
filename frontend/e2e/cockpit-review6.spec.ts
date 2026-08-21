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

  test('stage ruler begins and ends exactly with the semantic stage regions at minimum zoom', async ({ page }) => {
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
      const [trackBox, framingBox, evaluationBox] = await Promise.all([
        track.boundingBox(),
        framingZone.boundingBox(),
        evaluationZone.boundingBox(),
      ])
      if (!trackBox || !framingBox || !evaluationBox) return null
      return {
        leftDelta: Math.abs(trackBox.x - framingBox.x),
        rightDelta: Math.abs((trackBox.x + trackBox.width) - (evaluationBox.x + evaluationBox.width)),
      }
    }).toEqual({ leftDelta: 0, rightDelta: 0 })

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

  test('trackpad-style pinch zoom advances in small anchored frame-coalesced steps', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    const dataNode = page.locator('[data-cockpit-node="data"]')
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

    await expect.poll(async () => {
      const text = await page.locator('.cockpit-zoom-level').textContent()
      return Number.parseInt(text ?? '0', 10)
    }).toBeGreaterThan(100)

    const firstZoom = Number.parseInt((await page.locator('.cockpit-zoom-level').textContent()) ?? '0', 10)
    expect(firstZoom).toBeLessThanOrEqual(104)

    const nodeAfter = await dataNode.boundingBox()
    expect(nodeAfter).not.toBeNull()
    const afterCenterX = (nodeAfter?.x ?? 0) + (nodeAfter?.width ?? 0) / 2
    const afterCenterY = (nodeAfter?.y ?? 0) + (nodeAfter?.height ?? 0) / 2
    expect(Math.abs(afterCenterX - anchorX)).toBeLessThan(10)
    expect(Math.abs(afterCenterY - anchorY)).toBeLessThan(10)

    let previousZoom = firstZoom
    for (let index = 0; index < 5; index += 1) {
      await viewport.dispatchEvent('wheel', {
        ctrlKey: true,
        deltaY: -18,
        deltaMode: 0,
        clientX: anchorX,
        clientY: anchorY,
      })
      await page.waitForTimeout(35)
      const currentZoom = Number.parseInt((await page.locator('.cockpit-zoom-level').textContent()) ?? '0', 10)
      expect(currentZoom).toBeGreaterThan(previousZoom)
      expect(currentZoom - previousZoom).toBeLessThanOrEqual(4)
      previousZoom = currentZoom
    }

    expect(previousZoom).toBeLessThan(125)
  })

  test('Jump to palette stays above the composer and keeps its lowest results selectable', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/cockpit')

    await page.getByRole('button', { name: 'Jump to project work' }).click()
    const palette = page.getByRole('dialog', { name: 'Jump to project work' })
    const composer = page.getByRole('textbox', { name: 'Ask or direct the system' }).locator('xpath=ancestor::form')
    await expect(palette).toBeVisible()

    const [paletteBox, composerBox] = await Promise.all([palette.boundingBox(), composer.boundingBox()])
    expect(paletteBox).not.toBeNull()
    expect(composerBox).not.toBeNull()
    expect((paletteBox?.y ?? 0) + (paletteBox?.height ?? 0)).toBeLessThan((composerBox?.y ?? 0) - 8)

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
