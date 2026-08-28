import { expect, test } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'

test.describe('source-faithful Cockpit reintegration', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator('.selection-practical-node')).toHaveCount(6)
  })

  test('mounts canonical WorkUnit geometry and accepted semantic carriers', async ({ page }) => {
    const nodes = page.locator('.selection-practical-node')

    for (let index = 0; index < 6; index += 1) {
      const box = await nodes.nth(index).boundingBox()
      expect(box).not.toBeNull()
      expect(box?.width).toBeCloseTo(176, 0)
      expect(box?.height).toBeCloseTo(92, 0)
    }

    const selected = page.locator('.selection-practical-node[data-node-key="i"]')
    await expect(selected).toHaveAttribute('data-selected', 'true')
    await expect(selected).toHaveAttribute('data-selection-style', 'sel2')

    const selectedCorners = selected.locator('.selection-corners')
    await expect(selectedCorners).toHaveCSS('opacity', '1')

    await expect(page.locator('.priority-signal-bars')).toHaveCount(3)
    await expect(page.locator('[data-status-code="BLOCKED"]')).toHaveCount(1)
    await expect(page.locator('[data-status-code="FAIL"]')).toHaveCount(1)
    await expect(page.locator('[data-status-code="RUN"]')).toHaveCount(1)
  })

  test('retains exact scientific marker categories', async ({ page }) => {
    await expect(page.locator('.category-question .category-glyph circle')).toHaveCount(1)
    await expect(page.locator('.category-investigation .category-glyph rect')).toHaveCount(2)
    await expect(page.locator('.category-validation .category-glyph path')).toHaveCount(1)
    await expect(page.locator('.category-model .category-glyph path')).toHaveCount(1)
    await expect(page.locator('.category-evaluation .category-glyph path')).toHaveCount(1)
  })

  test('mounts E5 Hue plus Tag relations with D1 target arrows', async ({ page }) => {
    await expect(page.locator('html')).toHaveAttribute('data-relation-encoding', 'e5')
    await expect(page.locator('.reintegration-relation')).toHaveCount(4)

    const relations = page.locator('.reintegration-relation')
    for (let index = 0; index < 4; index += 1) {
      await expect(relations.nth(index).locator('.semantic-path')).not.toHaveAttribute('d', '')
      await expect(relations.nth(index).locator('.semantic-arrow')).not.toHaveAttribute('d', '')
      await expect(relations.nth(index).locator('.semantic-tag')).toHaveCSS('opacity', '1')
    }

    await expect(page.locator('.semantic-tag-text')).toHaveText(['DEP', 'EVID', 'LINE', 'CAUSE'])
  })

  test('initializes G4 ambient grid behavior from the accepted source module', async ({ page }) => {
    const currents = page.locator('.ambient-current')
    await expect(currents).toHaveCount(4)

    for (let index = 0; index < 4; index += 1) {
      await expect(currents.nth(index)).toHaveAttribute('data-orientation', /horizontal|vertical/)
      const position = await currents.nth(index).evaluate((element) =>
        getComputedStyle(element).getPropertyValue('--ambient-position').trim(),
      )
      expect(position).toMatch(/^\d+px$/)
    }

    const glints = page.locator('.ambient-glint')
    await expect(glints).toHaveCount(3)
    for (let index = 0; index < 3; index += 1) {
      const position = await glints.nth(index).evaluate((element: HTMLElement) => ({
        left: element.style.left,
        top: element.style.top,
      }))
      expect(Number.parseInt(position.left, 10) % 100).toBe(0)
      expect(Number.parseInt(position.top, 10) % 100).toBe(0)
    }
  })

  test('supports Specification 008 map recovery primitives without mutating WorkUnit state', async ({ page }) => {
    const initialTransform = await page.locator('#reintegration-world-plane').evaluate((element: HTMLElement) => element.style.transform)

    await page.locator('#zoom-in').click()
    await expect(page.locator('#zoom-readout')).not.toHaveText('100%')

    const zoomedTransform = await page.locator('#reintegration-world-plane').evaluate((element: HTMLElement) => element.style.transform)
    expect(zoomedTransform).not.toBe(initialTransform)

    await page.locator('#reset-world').click()
    await expect(page.locator('#zoom-readout')).toHaveText('100%')

    await page.locator('#jump-input').fill('Boosted candidate')
    await page.locator('#jump-button').click()
    await expect(page.locator('.selection-practical-node[data-node-key="m"]')).toHaveAttribute('data-selected', 'true')
    await expect(page.locator('#selected-work-label')).toContainText('Boosted candidate')

    await expect(page.locator('.selection-practical-node[data-node-key="m"]')).toHaveAttribute('data-status-code', 'FAIL')
    await expect(page.locator('.selection-practical-node[data-node-key="m"]')).toHaveAttribute('data-priority', 'high')
  })

  test('does not silently substitute a fake Conversation Workspace', async ({ page }) => {
    await page.locator('#conversation-expand').click()
    await expect(page.locator('.reintegration-provisional-note')).toContainText('next exact-source reintegration layer')
    await expect(page.locator('body')).not.toContainText('Deep Navy')
  })
})
