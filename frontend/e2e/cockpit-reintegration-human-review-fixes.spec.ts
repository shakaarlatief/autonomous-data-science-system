import { expect, test } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'

test.describe('Cockpit human-review fidelity corrections', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator('.expansion-practical-node')).toHaveCount(6)
  })

  test('project-general thread uses the accepted neutral project artifact without boxing its text wrapper', async ({ page }) => {
    await page.locator('#global-conversations').click()

    const projectThread = page.locator('.reintegration-thread-item[data-thread-scope="project"]')
    const artifact = projectThread.locator('.reintegration-project-thread-artifact')
    const glyph = artifact.locator('.reintegration-project-thread-glyph')
    const copy = artifact.locator('.reintegration-project-thread-copy')

    await expect(projectThread).toBeVisible()
    await expect(glyph).toHaveText('P')
    await expect(copy.locator('small')).toHaveText('PROJECT')
    await expect(copy.locator('strong')).toHaveText('General project discussion')
    await expect(projectThread.locator('.conversation-canonical-node')).toHaveCount(0)

    const geometry = await artifact.evaluate((element) => {
      const glyphElement = element.querySelector<HTMLElement>('.reintegration-project-thread-glyph')!
      const copyElement = element.querySelector<HTMLElement>('.reintegration-project-thread-copy')!
      const glyphRect = glyphElement.getBoundingClientRect()
      const copyRect = copyElement.getBoundingClientRect()
      const copyStyle = getComputedStyle(copyElement)
      return {
        glyphWidth: glyphRect.width,
        glyphHeight: glyphRect.height,
        copyWidth: copyRect.width,
        copyHeight: copyRect.height,
        copyBorderTopWidth: copyStyle.borderTopWidth,
        copyDisplay: copyStyle.display,
      }
    })

    expect(geometry.glyphWidth).toBeCloseTo(26, 0)
    expect(geometry.glyphHeight).toBeCloseTo(26, 0)
    expect(geometry.copyWidth).toBeGreaterThan(80)
    expect(geometry.copyHeight).toBeLessThan(40)
    expect(geometry.copyBorderTopWidth).toBe('0px')
    expect(geometry.copyDisplay).toBe('block')

    await page.locator('[data-conversation-rail-option="text"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'text')
    await expect(artifact).toBeHidden()
    await expect(projectThread.locator('.reintegration-thread-text')).toBeVisible()
  })

  test('Micro dots use a dedicated above-node endpoint overlay with accepted geometry', async ({ page }) => {
    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-connector-terminal-option="dots"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-connector-terminal', 'dots')
    await expect(page.locator('html')).toHaveAttribute('data-port-overlay-recovered', 'true')

    const overlay = page.locator('#reintegration-port-overlay')
    const groups = overlay.locator('.reintegration-port-group')
    const dots = overlay.locator('.reintegration-port-dot')

    await expect(overlay).toHaveCount(1)
    await expect(groups).toHaveCount(4)
    await expect(dots).toHaveCount(8)

    const layers = await page.evaluate(() => ({
      relations: Number(getComputedStyle(document.querySelector('#reintegration-relations')!).zIndex),
      ports: Number(getComputedStyle(document.querySelector('#reintegration-port-overlay')!).zIndex),
    }))
    expect(layers.ports).toBeGreaterThan(layers.relations)

    const visibleDots = await dots.evaluateAll((elements) => elements.map((element) => ({
      radius: element.getAttribute('r'),
      opacity: getComputedStyle(element).opacity,
      visibility: getComputedStyle(element).visibility,
    })))
    for (const dot of visibleDots) {
      expect(dot.radius).toBe('2.6')
      expect(dot.opacity).toBe('0.88')
      expect(dot.visibility).toBe('visible')
    }

    const docking = await page.locator('.reintegration-relation[data-relation-id="q-i"]').evaluate((relation) => {
      const path = relation.querySelector<SVGPathElement>('.semantic-path')!
      const start = path.getPointAtLength(0)
      const overlayGroup = document.querySelector<SVGGElement>('.reintegration-port-group[data-relation-id="q-i"]')!
      const dot = overlayGroup.querySelector<SVGCircleElement>('.reintegration-port-source-dot')!
      const dx = Number(dot.getAttribute('cx')) - start.x
      const dy = Number(dot.getAttribute('cy')) - start.y
      return Math.hypot(dx, dy)
    })
    expect(docking).toBeCloseTo(2, 1)

    const underlayEndpoints = page.locator('#reintegration-relations .reintegration-terminal-dot')
    await expect(underlayEndpoints.first()).toHaveCSS('display', 'none')
  })

  test('Frame sockets share the restored endpoint overlay and remain mutually exclusive with Micro dots', async ({ page }) => {
    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-connector-terminal-option="sockets"]').click()

    await expect(page.locator('html')).toHaveAttribute('data-connector-terminal', 'sockets')
    await expect(page.locator('#reintegration-port-overlay .reintegration-port-socket').first()).toHaveCSS('visibility', 'visible')
    await expect(page.locator('#reintegration-port-overlay .reintegration-port-dot').first()).toHaveCSS('visibility', 'hidden')
  })
})
