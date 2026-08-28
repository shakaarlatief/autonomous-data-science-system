import { expect, test, type Page } from '@playwright/test'

const route = '/design-lab/cockpit-reintegration.html'
const nodeSelector = '.expansion-practical-node'

async function selectedSnapshot(page: Page) {
  return page.locator(`${nodeSelector}[data-selected="true"]`).evaluate((node: HTMLElement) => ({
    key: node.dataset.nodeKey,
    selected: node.dataset.selected,
    expanded: node.dataset.expanded,
    statusCode: node.dataset.statusCode,
    priority: node.dataset.priority,
  }))
}

test.describe('Conversation integration and Z7 rendering performance', () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 1000 })
    await page.goto(route)
    await expect(page.locator(nodeSelector)).toHaveCount(6)
    await expect(page.locator('#reintegration-conversation-layer')).toHaveCount(1)
  })

  test('mounts the held Quiet Graphite Conversation Workspace as a real full-focus project conversation', async ({ page }) => {
    const beforeSelection = await selectedSnapshot(page)
    const beforeTransform = await page.locator('#reintegration-world-plane').evaluate((element: HTMLElement) => element.style.transform)

    await page.locator('#global-conversations').click()

    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-scope', 'project')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    await expect(page.locator('#reintegration-conversation-layer')).toHaveAttribute('aria-hidden', 'false')
    await expect(page.locator('#reintegration-conversation-title')).toHaveText('General project discussion')
    await expect(page.locator('#reintegration-conversation-scope-pill')).toHaveText('PROJECT GENERAL')
    await expect(page.locator('#reintegration-conversation-expand-box')).toBeHidden()

    const quietGraphite = await page.locator('#reintegration-conversation-layer').evaluate((element) => {
      const style = getComputedStyle(element)
      const transcript = document.querySelector('.reintegration-conversation-transcript')?.getBoundingClientRect()
      return {
        background: style.backgroundColor,
        accent: style.getPropertyValue('--cq-accent').trim(),
        transcriptWidth: transcript?.width ?? 0,
      }
    })
    expect(quietGraphite.background).toBe('rgb(7, 10, 15)')
    expect(quietGraphite.accent.toLowerCase()).toBe('#69d9c2')
    expect(quietGraphite.transcriptWidth).toBeGreaterThan(600)
    expect(quietGraphite.transcriptWidth).toBeLessThanOrEqual(850.5)

    await page.locator('#reintegration-conversation-close').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'false')
    expect(await selectedSnapshot(page)).toEqual(beforeSelection)
    expect(await page.locator('#reintegration-world-plane').evaluate((element: HTMLElement) => element.style.transform)).toBe(beforeTransform)
  })

  test('opens an X5 WorkUnit conversation without confusing conversation ownership with SEL2 selection', async ({ page }) => {
    const source = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await expect(source).toHaveAttribute('data-selected', 'true')
    await page.locator('#toggle-detail').click()
    await expect(source).toHaveAttribute('data-expanded', 'true')

    const sourceState = await selectedSnapshot(page)
    const action = source.locator(':scope > .reintegration-x5-chat-action')
    await expect(action).toBeVisible()
    await action.click()

    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-scope', 'work')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    await expect(page.locator('#reintegration-conversation-title')).toHaveText('Production missingness')
    await expect(page.locator('#reintegration-conversation-scope-pill')).toHaveText('WORK UNIT')

    const activeRailNode = page.locator('.reintegration-thread-item.is-active .conversation-canonical-node')
    await expect(activeRailNode).toHaveCount(1)
    await expect(activeRailNode).toHaveAttribute('data-selected', 'false')
    await expect(activeRailNode.locator('.selection-corners')).toHaveCSS('display', 'none')

    expect(await selectedSnapshot(page)).toEqual(sourceState)

    await page.locator('[data-conversation-rail-option="text"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'text')
    await expect(page.locator('.reintegration-thread-item.is-active .reintegration-thread-text')).toBeVisible()
    await expect(page.locator('.reintegration-thread-item.is-active .reintegration-thread-box')).toBeHidden()

    await page.locator('[data-conversation-rail-option="boxes"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-rail', 'boxes')
    await expect(page.locator('.reintegration-thread-item.is-active .reintegration-thread-box')).toBeVisible()

    await page.locator('#reintegration-conversation-expand-box').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-a6-expanded', 'true')
    await expect(page.locator('#reintegration-a6-inspector')).toHaveCSS('opacity', '1')
    await expect(page.locator('#reintegration-a6-home-box .conversation-canonical-node')).toHaveAttribute('data-selected', 'false')
    await expect(page.locator('.reintegration-conversation-floating-home')).toHaveCount(0)

    await page.locator('.reintegration-thread-item[data-thread-scope="project"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-scope', 'project')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-a6-expanded', 'false')
    expect(await selectedSnapshot(page)).toEqual(sourceState)

    await page.locator('#reintegration-conversation-close').click()
    expect(await selectedSnapshot(page)).toEqual(sourceState)
  })

  test('keeps Deep Dive mounted when Conversation opens, switches thread or closes', async ({ page }) => {
    const source = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await page.locator('#toggle-detail').click()
    await expect(source).toHaveAttribute('data-expanded', 'true')

    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2200 })
    await expect(page.locator('#deep-work-conversation')).toBeVisible()
    await expect(page.locator('#deep-global-conversations')).toBeVisible()

    await page.locator('#deep-work-conversation').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-scope', 'work')
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused')

    await page.locator('.reintegration-thread-item[data-thread-scope="project"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-scope', 'project')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused')

    await page.locator('#reintegration-conversation-close').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'false')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused')
    await expect(source).toHaveAttribute('data-selected', 'true')
    await expect(source).toHaveAttribute('data-expanded', 'true')

    await page.locator('#return-to-project').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'false')
    await expect(source).toHaveAttribute('data-selected', 'true')
    await expect(source).toHaveAttribute('data-expanded', 'true')
  })

  test('full-focus and co-present Conversation are presentation states, not work-state mutations', async ({ page }) => {
    const source = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await page.locator('#toggle-detail').click()
    await expect(source).toHaveAttribute('data-expanded', 'true')
    const before = await selectedSnapshot(page)

    await source.locator(':scope > .reintegration-x5-chat-action').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')

    await page.locator('#reintegration-conversation-presentation-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'full')
    expect(await selectedSnapshot(page)).toEqual(before)

    await page.locator('#reintegration-conversation-presentation-toggle').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-presentation', 'copresent')
    expect(await selectedSnapshot(page)).toEqual(before)
  })

  test('Z7 uses a prewarmed transform-opacity compositor path and suppresses decorative world work during the dive', async ({ page }) => {
    const source = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await page.locator('#toggle-detail').click()
    await expect(source).toHaveAttribute('data-expanded', 'true')

    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-z7-rendering', /preparing|active/)
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'entering', { timeout: 700 })

    const rendering = await page.evaluate(() => {
      const worldTransition = document.querySelector('#reintegration-world-transition-layer')
      const specialist = document.querySelector('#reintegration-specialist-layer')
      const ambient = document.querySelector('#reintegration-ambient-runtime-layer')
      const activity = document.querySelector('.activity-field')
      return {
        worldFilter: worldTransition ? getComputedStyle(worldTransition).filter : null,
        worldAnimation: worldTransition ? getComputedStyle(worldTransition).animationName : null,
        worldWillChange: worldTransition ? getComputedStyle(worldTransition).willChange : null,
        specialistFilter: specialist ? getComputedStyle(specialist).filter : null,
        specialistAnimation: specialist ? getComputedStyle(specialist).animationName : null,
        ambientDisplay: ambient ? getComputedStyle(ambient).display : null,
        activityDisplay: activity ? getComputedStyle(activity).display : null,
      }
    })

    expect(rendering.worldFilter).toBe('none')
    expect(rendering.specialistFilter).toBe('none')
    expect(rendering.worldAnimation).toBe('reintegration-z7-world-dive-smooth')
    expect(rendering.specialistAnimation).toBe('reintegration-z7-workspace-arrive-smooth')
    expect(rendering.worldWillChange).toContain('transform')
    expect(rendering.ambientDisplay).toBe('none')
    expect(rendering.activityDisplay).toBe('none')

    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 1500 })
    await page.locator('#return-to-project').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'false')
    await expect(page.locator('html')).toHaveAttribute('data-z7-rendering', 'idle')
    await expect(page.locator('#reintegration-ambient-runtime-layer')).not.toHaveCSS('display', 'none')
  })

  test('Escape closes Conversation before it can collapse the preserved Deep Dive source state', async ({ page }) => {
    await page.locator('#toggle-detail').click()
    await page.locator('#deep-dive').click()
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2200 })

    await page.locator('#deep-global-conversations').click()
    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'true')
    await page.keyboard.press('Escape')

    await expect(page.locator('html')).toHaveAttribute('data-conversation-open', 'false')
    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused')
  })
})
