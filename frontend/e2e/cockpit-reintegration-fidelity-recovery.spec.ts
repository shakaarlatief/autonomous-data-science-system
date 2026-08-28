import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'
const nodeSelector = '.expansion-practical-node'

async function dispatchPinch(
  page: Page,
  deltaY: number,
  clientX = 800,
  clientY = 500,
) {
  await page.locator('#reintegration-stage').evaluate((element, init) => {
    element.dispatchEvent(new WheelEvent('wheel', {
      bubbles: true,
      cancelable: true,
      deltaY: init.deltaY,
      ctrlKey: true,
      clientX: init.clientX,
      clientY: init.clientY,
    }))
  }, { deltaY, clientX, clientY })
  await page.waitForTimeout(210)
}

test.describe('Cockpit integrated fidelity recovery', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('#reintegration-world-plane')).toHaveAttribute('data-raster-mode', /layout-zoom|transform-fallback/)
  })

  test('clicking one operational dot switches only that carrier and never selects the parent WorkUnit', async ({ page }) => {
    const initiallySelected = page.locator(`${nodeSelector}[data-node-key="i"]`)
    const runningNode = page.locator(`${nodeSelector}[data-node-key="r"]`)

    await expect(initiallySelected).toHaveAttribute('data-selected', 'true')
    await expect(runningNode).toHaveAttribute('data-selected', 'false')
    await expect(runningNode).toHaveAttribute('data-status-code', 'RUN')
    await expect(runningNode).toHaveAttribute('data-status-carrier', 'dot')

    const dot = runningNode.locator('.status-dot-carrier')
    await expect(dot).toBeVisible()
    await dot.click()

    await expect(runningNode).toHaveAttribute('data-status-carrier', 'tag')
    await expect(runningNode).toHaveAttribute('data-local-override', 'true')
    await expect(runningNode.locator('.status-tag-carrier')).toBeVisible()
    await expect(runningNode.locator('.status-tag-label')).toHaveText('RUN')

    /* The carrier interaction must not bubble into WorkUnit selection. */
    await expect(initiallySelected).toHaveAttribute('data-selected', 'true')
    await expect(runningNode).toHaveAttribute('data-selected', 'false')
    await expect(page.locator('#selected-work-label')).toContainText('Production missingness')

    await runningNode.locator('.status-tag-carrier').click()
    await expect(runningNode).toHaveAttribute('data-status-carrier', 'dot')
    await expect(runningNode).toHaveAttribute('data-local-override', 'false')
    await expect(runningNode.locator('.status-dot-carrier')).toBeVisible()
    await expect(initiallySelected).toHaveAttribute('data-selected', 'true')
  })

  test('global operational-carrier switching changes every active status and clears local overrides', async ({ page }) => {
    const runningNode = page.locator(`${nodeSelector}[data-node-key="r"]`)
    const noStatusNode = page.locator(`${nodeSelector}[data-node-key="e"]`)

    await page.locator('#appearance-controls-toggle').click()
    const globalTag = page.locator('[data-global-status-carrier="tag"]')
    const globalDot = page.locator('[data-global-status-carrier="dot"]')
    await expect(globalTag).toBeVisible()

    await globalTag.click()
    await expect(page.locator('html')).toHaveAttribute('data-global-status-carrier', 'tag')

    const activeNodes = page.locator(`${nodeSelector}:not([data-status-code="NONE"])`)
    const activeCount = await activeNodes.count()
    for (let index = 0; index < activeCount; index += 1) {
      await expect(activeNodes.nth(index)).toHaveAttribute('data-status-carrier', 'tag')
      await expect(activeNodes.nth(index)).toHaveAttribute('data-local-override', 'false')
      await expect(activeNodes.nth(index).locator('.status-tag-carrier')).toBeVisible()
    }

    await expect(noStatusNode.locator('.status-dot-carrier')).toHaveCount(0)
    await expect(noStatusNode.locator('.status-tag-carrier')).toHaveCount(0)

    /* A local click diverges only this WorkUnit from the global presentation. */
    await runningNode.locator('.status-tag-carrier').click()
    await expect(runningNode).toHaveAttribute('data-status-carrier', 'dot')
    await expect(runningNode).toHaveAttribute('data-local-override', 'true')

    /* Any new global choice clears local overrides, matching the accepted model. */
    await globalDot.click()
    await expect(page.locator('html')).toHaveAttribute('data-global-status-carrier', 'dot')
    for (let index = 0; index < activeCount; index += 1) {
      await expect(activeNodes.nth(index)).toHaveAttribute('data-status-carrier', 'dot')
      await expect(activeNodes.nth(index)).toHaveAttribute('data-local-override', 'false')
    }
  })

  test('BLOCKED and FAIL keep their selected compact ring distinction while sharing the switchable status slot', async ({ page }) => {
    const blockedRing = page.locator(`${nodeSelector}[data-status-code="BLOCKED"] .status-dot-ring`)
    const failRing = page.locator(`${nodeSelector}[data-status-code="FAIL"] .status-dot-ring`)

    await expect(blockedRing).toHaveCSS('border-radius', '5px')
    await expect(failRing).toHaveCSS('border-radius', '50%')

    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-global-status-carrier="tag"]').click()
    await expect(page.locator(`${nodeSelector}[data-status-code="BLOCKED"] .status-tag-label`)).toHaveText('BLOCKED')
    await expect(page.locator(`${nodeSelector}[data-status-code="FAIL"] .status-tag-label`)).toHaveText('FAIL')
  })

  test('G4 uses Lively stochastic grid currents plus independently quiet major-grid glints and localized semantic activity', async ({ page }) => {
    const world = page.locator('#reintegration-world')
    const runtimeLayer = page.locator('#reintegration-ambient-runtime-layer')

    await expect(page.locator('html')).toHaveAttribute('data-ambient-cadence', 'lively')
    await expect(world).toHaveClass(/variant-g4/)
    await expect(runtimeLayer).toHaveCount(1)

    /* The superseded repeating fixture is gone. */
    await expect(world.locator(':scope > .ambient-current')).toHaveCount(0)
    await expect(world.locator(':scope > .ambient-glint')).toHaveCount(0)
    await expect(world.locator(':scope > .ambient-drift')).toHaveCount(0)

    /* Localized semantic activity remains a separate, higher-level layer. */
    await expect(world.locator('.activity-field')).toHaveCount(2)
    await expect(world.locator('.live-packet')).toHaveCount(2)

    await expect.poll(async () => runtimeLayer.locator('.runtime-current').count(), { timeout: 2600 }).toBeGreaterThanOrEqual(2)
    const currents = runtimeLayer.locator('.runtime-current')
    expect(await currents.count()).toBeLessThanOrEqual(5)

    const currentCount = await currents.count()
    const gridCoordinates = new Set<number>()
    for (let index = 0; index < currentCount; index += 1) {
      const current = currents.nth(index)
      await expect(current).toHaveAttribute('data-orientation', /horizontal|vertical/)
      const coordinate = Number(await current.getAttribute('data-grid-coordinate'))
      expect(Number.isFinite(coordinate)).toBe(true)
      expect(coordinate % 20).toBe(0)
      gridCoordinates.add(coordinate)
    }
    expect(gridCoordinates.size).toBeGreaterThan(1)

    await expect.poll(async () => runtimeLayer.locator('.runtime-glint').count(), { timeout: 3200 }).toBeGreaterThanOrEqual(1)
    const glints = runtimeLayer.locator('.runtime-glint')
    expect(await glints.count()).toBeLessThanOrEqual(2)
    const glintCount = await glints.count()
    for (let index = 0; index < glintCount; index += 1) {
      const glint = glints.nth(index)
      const x = Number(await glint.getAttribute('data-major-x'))
      const y = Number(await glint.getAttribute('data-major-y'))
      expect(x % 100).toBe(0)
      expect(y % 100).toBe(0)
      expect(x).toBeGreaterThan(0)
      expect(y).toBeGreaterThan(0)
    }

    await expect.poll(async () => runtimeLayer.locator('.runtime-drift').count(), { timeout: 2200 }).toBeGreaterThanOrEqual(1)
  })

  test('reduced motion removes decorative G4 runtime activity while preserving static operational identity', async ({ page }) => {
    const runtimeLayer = page.locator('#reintegration-ambient-runtime-layer')
    const runningNode = page.locator(`${nodeSelector}[data-status-code="RUN"]`)

    await expect.poll(async () => runtimeLayer.locator('.runtime-current').count(), { timeout: 1800 }).toBeGreaterThanOrEqual(1)

    await page.locator('#appearance-controls-toggle').click()
    await page.locator('#reduced-motion-toggle').check()
    await expect(page.locator('html')).toHaveAttribute('data-reduced', 'on')
    await expect(runtimeLayer).toHaveCSS('display', 'none')
    await expect(runtimeLayer.locator('.runtime-current')).toHaveCount(0)
    await expect(runtimeLayer.locator('.runtime-glint')).toHaveCount(0)
    await expect(runtimeLayer.locator('.runtime-drift')).toHaveCount(0)

    await expect(runningNode.locator('.status-dot-core')).toBeVisible()
    await expect(runningNode).toHaveAttribute('data-status-code', 'RUN')

    await page.locator('#reduced-motion-toggle').uncheck()
    await expect(page.locator('html')).toHaveAttribute('data-reduced', 'off')
    await expect.poll(async () => runtimeLayer.locator('.runtime-current').count(), { timeout: 1800 }).toBeGreaterThanOrEqual(1)
  })

  test('Chromium geometric zoom rerasterizes the world instead of leaving text and grid inside a scaled compositor texture', async ({ page, browserName }) => {
    test.skip(browserName !== 'chromium', 'The design-lab layout-zoom fidelity adapter targets Chromium.')

    const plane = page.locator('#reintegration-world-plane')
    const world = page.locator('#reintegration-world')

    await page.locator('#reset-world').click()
    await page.waitForTimeout(180)
    await expect(plane).toHaveAttribute('data-raster-mode', 'layout-zoom')

    const initial = await plane.evaluate((element: HTMLElement) => ({
      transform: element.style.transform,
      zoom: (element.querySelector('#reintegration-world') as HTMLElement | null)?.style.getPropertyValue('zoom') || '',
    }))
    expect(initial.transform).not.toContain('scale(')
    expect(Number(initial.zoom)).toBeCloseTo(1, 5)

    const anchorNode = page.locator(`${nodeSelector}[data-node-key="r"]`)
    const before = await anchorNode.boundingBox()
    expect(before).not.toBeNull()
    const anchorX = (before?.x ?? 0) + (before?.width ?? 0) / 2
    const anchorY = (before?.y ?? 0) + (before?.height ?? 0) / 2

    await dispatchPinch(page, -82, anchorX, anchorY)
    await expect(page.locator('#zoom-readout')).not.toHaveText('100%')

    const after = await anchorNode.boundingBox()
    expect(after).not.toBeNull()
    const afterX = (after?.x ?? 0) + (after?.width ?? 0) / 2
    const afterY = (after?.y ?? 0) + (after?.height ?? 0) / 2
    expect(Math.abs(afterX - anchorX)).toBeLessThan(2)
    expect(Math.abs(afterY - anchorY)).toBeLessThan(2)

    const rendered = await plane.evaluate((element: HTMLElement) => {
      const worldElement = element.querySelector('#reintegration-world') as HTMLElement
      return {
        transform: element.style.transform,
        worldZoom: Number(worldElement.style.getPropertyValue('zoom')),
        gridHairline: Number.parseFloat(getComputedStyle(worldElement).getPropertyValue('--reintegration-grid-hairline')),
        minorGridSize: getComputedStyle(worldElement).backgroundSize,
        majorGridSize: getComputedStyle(worldElement.querySelector('.major-grid') as HTMLElement).backgroundSize,
        willChange: getComputedStyle(element).willChange,
      }
    })

    expect(rendered.transform).not.toContain('scale(')
    expect(rendered.worldZoom).toBeGreaterThan(1)
    expect(rendered.gridHairline * rendered.worldZoom).toBeCloseTo(1, 2)
    expect(rendered.minorGridSize).toContain('20px 20px')
    expect(rendered.majorGridSize).toContain('100px 100px')
    expect(rendered.willChange).toBe('auto')

    /* Repeated zoom changes must keep using rerasterized layout projection. */
    await dispatchPinch(page, 54, 640, 420)
    await dispatchPinch(page, -37, 970, 620)
    const finalProjection = await plane.evaluate((element: HTMLElement) => ({
      transform: element.style.transform,
      zoom: Number((element.querySelector('#reintegration-world') as HTMLElement).style.getPropertyValue('zoom')),
    }))
    expect(finalProjection.transform).not.toContain('scale(')
    expect(finalProjection.zoom).toBeGreaterThan(0.52)
    expect(finalProjection.zoom).toBeLessThan(1.42)
  })
})
