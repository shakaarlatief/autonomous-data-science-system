import { expect, test } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'

test.describe('Cockpit human-review fidelity corrections', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator('.expansion-practical-node')).toHaveCount(6)
  })

  test('Conversation Boxes rail restores the accepted canonical WorkUnit footprint beside the project artifact', async ({ page }) => {
    await page.locator('#global-conversations').click()

    const rail = page.locator('.reintegration-conversation-rail')
    const projectThread = page.locator('.reintegration-thread-item[data-thread-scope="project"]')
    const artifact = projectThread.locator('.reintegration-project-thread-artifact')
    const glyph = artifact.locator('.reintegration-project-thread-glyph')
    const copy = artifact.locator('.reintegration-project-thread-copy')
    const workThread = page.locator('.reintegration-thread-item.is-workunit-thread').first()
    const workSlot = workThread.locator('.reintegration-thread-box')
    const workNode = workSlot.locator('.conversation-canonical-node')

    await expect(projectThread).toBeVisible()
    await expect(glyph).toHaveText('P')
    await expect(copy.locator('small')).toHaveText('PROJECT')
    await expect(copy.locator('strong')).toHaveText('General project discussion')
    await expect(projectThread.locator('.conversation-canonical-node')).toHaveCount(0)

    const geometry = await page.evaluate(() => {
      const railElement = document.querySelector<HTMLElement>('.reintegration-conversation-rail')!
      const projectArtifact = document.querySelector<HTMLElement>('.reintegration-project-thread-artifact')!
      const projectCopy = document.querySelector<HTMLElement>('.reintegration-project-thread-copy')!
      const workSlotElement = document.querySelector<HTMLElement>('.reintegration-thread-item.is-workunit-thread .reintegration-thread-box')!
      const workNodeElement = workSlotElement.querySelector<HTMLElement>('.conversation-canonical-node')!
      const projectRect = projectArtifact.getBoundingClientRect()
      const slotRect = workSlotElement.getBoundingClientRect()
      const nodeRect = workNodeElement.getBoundingClientRect()
      return {
        railWidth: railElement.getBoundingClientRect().width,
        projectWidth: projectRect.width,
        projectHeight: projectRect.height,
        workSlotWidth: slotRect.width,
        workSlotHeight: slotRect.height,
        workNodeWidth: nodeRect.width,
        workNodeHeight: nodeRect.height,
        workNodeCssWidth: getComputedStyle(workNodeElement).width,
        workNodeCssHeight: getComputedStyle(workNodeElement).height,
        projectCopyBorder: getComputedStyle(projectCopy).borderTopWidth,
      }
    })

    expect(geometry.railWidth).toBeCloseTo(270, 0)
    expect(geometry.workSlotWidth).toBeCloseTo(232, 0)
    expect(geometry.workSlotHeight).toBeCloseTo(74, 0)
    expect(geometry.workNodeWidth).toBeCloseTo(232, 0)
    expect(geometry.workNodeHeight).toBeCloseTo(73.6, 0)
    expect(geometry.workNodeCssWidth).toBe('290px')
    expect(geometry.workNodeCssHeight).toBe('92px')
    expect(Math.abs(geometry.projectWidth - geometry.workSlotWidth)).toBeLessThanOrEqual(12)
    expect(geometry.projectHeight).toBeGreaterThanOrEqual(56)
    expect(geometry.projectCopyBorder).toBe('0px')

    await page.locator('[data-conversation-rail-option="text"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'text')
    await expect(artifact).toBeHidden()
    await expect(workSlot).toBeHidden()
    await expect(projectThread.locator('.reintegration-thread-text')).toBeVisible()
  })

  test('Micro dots use the accepted side-normal 2 px outset in the above-node overlay', async ({ page }) => {
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
    await expect(overlay.locator('.reintegration-port-socket')).toHaveCount(0)

    const layers = await page.evaluate(() => ({
      relations: Number(getComputedStyle(document.querySelector('#reintegration-relations')!).zIndex),
      nodes: Number(getComputedStyle(document.querySelector('#expansion-practical-nodes')!).zIndex),
      ports: Number(getComputedStyle(document.querySelector('#reintegration-port-overlay')!).zIndex),
    }))
    expect(layers.relations).toBeLessThan(layers.nodes)
    expect(layers.ports).toBeGreaterThan(layers.nodes)

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
      const end = path.getPointAtLength(path.getTotalLength())
      const overlayGroup = document.querySelector<SVGGElement>('.reintegration-port-group[data-relation-id="q-i"]')!
      const sourceDot = overlayGroup.querySelector<SVGCircleElement>('.reintegration-port-source-dot')!
      const targetDot = overlayGroup.querySelector<SVGCircleElement>('.reintegration-port-target-dot')!
      return {
        sourceDx: Number(sourceDot.getAttribute('cx')) - start.x,
        sourceDy: Number(sourceDot.getAttribute('cy')) - start.y,
        targetDx: Number(targetDot.getAttribute('cx')) - end.x,
        targetDy: Number(targetDot.getAttribute('cy')) - end.y,
      }
    })

    /* q -> i is right-side source to left-side target in this fixture. */
    expect(docking.sourceDx).toBeCloseTo(2, 1)
    expect(docking.sourceDy).toBeCloseTo(0, 1)
    expect(docking.targetDx).toBeCloseTo(-2, 1)
    expect(docking.targetDy).toBeCloseTo(0, 1)

    await expect(page.locator('#reintegration-relations .reintegration-terminal-dot').first()).toHaveCSS('display', 'none')
  })

  test('Frame sockets remain in the accepted under-node frame-integrated layer', async ({ page }) => {
    await page.locator('#appearance-controls-toggle').click()
    await page.locator('[data-connector-terminal-option="sockets"]').click()

    await expect(page.locator('html')).toHaveAttribute('data-connector-terminal', 'sockets')
    await expect(page.locator('#reintegration-port-overlay .reintegration-port-socket')).toHaveCount(0)
    await expect(page.locator('#reintegration-port-overlay .reintegration-port-dot').first()).toHaveCSS('visibility', 'hidden')

    const relation = page.locator('.reintegration-relation[data-relation-id="q-i"]')
    const sourceSocket = relation.locator('.reintegration-source-socket')
    const targetSocket = relation.locator('.reintegration-target-socket')
    await expect(sourceSocket).toHaveCSS('visibility', 'visible')
    await expect(targetSocket).toHaveCSS('visibility', 'visible')
    await expect(sourceSocket).toHaveCSS('opacity', '0.92')

    const geometry = await relation.evaluate((element) => {
      const path = element.querySelector<SVGPathElement>('.semantic-path')!
      const start = path.getPointAtLength(0)
      const end = path.getPointAtLength(path.getTotalLength())
      const source = element.querySelector<SVGRectElement>('.reintegration-source-socket')!
      const target = element.querySelector<SVGRectElement>('.reintegration-target-socket')!
      return {
        start: { x: start.x, y: start.y },
        end: { x: end.x, y: end.y },
        sourceCenter: {
          x: Number(source.getAttribute('x')) + Number(source.getAttribute('width')) / 2,
          y: Number(source.getAttribute('y')) + Number(source.getAttribute('height')) / 2,
        },
        targetCenter: {
          x: Number(target.getAttribute('x')) + Number(target.getAttribute('width')) / 2,
          y: Number(target.getAttribute('y')) + Number(target.getAttribute('height')) / 2,
        },
        relationsZ: Number(getComputedStyle(document.querySelector('#reintegration-relations')!).zIndex),
        nodesZ: Number(getComputedStyle(document.querySelector('#expansion-practical-nodes')!).zIndex),
      }
    })

    expect(geometry.sourceCenter.x).toBeCloseTo(geometry.start.x, 1)
    expect(geometry.sourceCenter.y).toBeCloseTo(geometry.start.y, 1)
    expect(geometry.targetCenter.x).toBeCloseTo(geometry.end.x, 1)
    expect(geometry.targetCenter.y).toBeCloseTo(geometry.end.y, 1)
    expect(geometry.relationsZ).toBeLessThan(geometry.nodesZ)
  })
})
