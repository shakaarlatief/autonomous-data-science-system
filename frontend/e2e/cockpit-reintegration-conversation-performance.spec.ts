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

test.describe('Conversation integration and source-faithful Z7 rendering', () => {
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

  test('Z7 preserves the selected Pull-Back Then Dive choreography while suppressing decorative world work', async ({ page }) => {
    const source = page.locator(`${nodeSelector}[data-node-key="i"]`)
    await page.locator('#toggle-detail').click()
    await expect(source).toHaveAttribute('data-expanded', 'true')

    /*
     * Capture the rendering contract at the exact mutation boundary instead of
     * sampling a transient 780 ms state from the test runner. In addition to
     * state-machine behavior, this deliberately inspects the live animation
     * objects so a later performance adapter cannot silently replace the
     * accepted Z7 visual choreography again.
     */
    await page.evaluate(() => {
      const root = document.documentElement
      ;(window as typeof window & { __z7RenderingCapture?: Promise<Record<string, string | null>> }).__z7RenderingCapture = new Promise((resolve) => {
        const observer = new MutationObserver(() => {
          if (root.dataset.deepFocus !== 'entering') return

          const worldTransition = document.querySelector('#reintegration-world-transition-layer') as HTMLElement | null
          const specialist = document.querySelector('#reintegration-specialist-layer') as HTMLElement | null
          const ambient = document.querySelector('#reintegration-ambient-runtime-layer')
          const activity = document.querySelector('.activity-field')
          const selected = document.querySelector(`${nodeSelector}[data-selected="true"]`) as HTMLElement | null
          const stage = document.querySelector('#reintegration-stage') as HTMLElement | null
          const worldStyle = worldTransition ? getComputedStyle(worldTransition) : null
          const specialistStyle = specialist ? getComputedStyle(specialist) : null
          const rootStyle = getComputedStyle(root)
          const worldAnimation = worldTransition?.getAnimations()[0]
          const specialistAnimation = specialist?.getAnimations()[0]
          const worldKeyframes = (worldAnimation?.effect as KeyframeEffect | null)?.getKeyframes() ?? []
          const specialistKeyframes = (specialistAnimation?.effect as KeyframeEffect | null)?.getKeyframes() ?? []
          const nodeRect = selected?.getBoundingClientRect()
          const stageRect = stage?.getBoundingClientRect()
          const expectedOriginX = nodeRect && stageRect ? nodeRect.left - stageRect.left + nodeRect.width / 2 : null
          const expectedOriginY = nodeRect && stageRect ? nodeRect.top - stageRect.top + nodeRect.height / 2 : null

          observer.disconnect()
          resolve({
            state: root.dataset.deepFocus || null,
            z7Rendering: root.dataset.z7Rendering || null,
            worldAnimation: worldStyle?.animationName ?? null,
            worldDuration: worldStyle?.animationDuration ?? null,
            worldTiming: worldStyle?.animationTimingFunction ?? null,
            worldWillChange: worldStyle?.willChange ?? null,
            worldKeyframes: JSON.stringify(worldKeyframes.map((frame) => ({
              offset: frame.offset,
              opacity: frame.opacity,
              transform: frame.transform,
              filter: frame.filter,
            }))),
            specialistAnimation: specialistStyle?.animationName ?? null,
            specialistDuration: specialistStyle?.animationDuration ?? null,
            specialistTiming: specialistStyle?.animationTimingFunction ?? null,
            specialistKeyframes: JSON.stringify(specialistKeyframes.map((frame) => ({
              offset: frame.offset,
              opacity: frame.opacity,
              transform: frame.transform,
            }))),
            originX: rootStyle.getPropertyValue('--deep-origin-x').trim() || null,
            originY: rootStyle.getPropertyValue('--deep-origin-y').trim() || null,
            expectedOriginX: expectedOriginX === null ? null : String(expectedOriginX),
            expectedOriginY: expectedOriginY === null ? null : String(expectedOriginY),
            ambientDisplay: ambient ? getComputedStyle(ambient).display : null,
            activityDisplay: activity ? getComputedStyle(activity).display : null,
          })
        })

        observer.observe(root, { attributes: true, attributeFilter: ['data-deep-focus'] })
      })
    })

    await page.locator('#deep-dive').click()

    const rendering = await page.evaluate(async () => {
      const capture = (window as typeof window & { __z7RenderingCapture?: Promise<Record<string, string | null>> }).__z7RenderingCapture
      if (!capture) throw new Error('Z7 rendering capture was not installed')
      return capture
    })

    expect(rendering.state).toBe('entering')
    expect(rendering.z7Rendering).toBe('active')
    expect(rendering.worldAnimation).toBe('reintegration-z7-world-dive')
    expect(rendering.specialistAnimation).toBe('reintegration-z7-workspace-arrive')
    expect(rendering.worldDuration).toBe('0.78s')
    expect(rendering.specialistDuration).toBe('0.78s')
    expect(rendering.worldTiming).toBe('cubic-bezier(0.16, 1, 0.3, 1)')
    expect(rendering.specialistTiming).toBe('cubic-bezier(0.16, 1, 0.3, 1)')
    expect(rendering.worldWillChange).toContain('transform')
    expect(rendering.worldWillChange).toContain('filter')

    const worldKeyframes = JSON.parse(rendering.worldKeyframes || '[]') as Array<Record<string, string | number | null>>
    expect(worldKeyframes).toHaveLength(3)
    expect(worldKeyframes.map((frame) => frame.offset)).toEqual([0, 0.24, 1])
    expect(worldKeyframes.map((frame) => frame.filter)).toEqual(['none', 'saturate(0.78)', 'blur(1.4px)'])
    expect(worldKeyframes.map((frame) => frame.transform)).toEqual(['scale(1)', 'scale(0.86)', 'scale(5.3)'])
    expect(worldKeyframes.map((frame) => frame.opacity)).toEqual(['1', '1', '0'])

    const specialistKeyframes = JSON.parse(rendering.specialistKeyframes || '[]') as Array<Record<string, string | number | null>>
    expect(specialistKeyframes).toHaveLength(3)
    expect(specialistKeyframes.map((frame) => frame.offset)).toEqual([0, 0.3, 1])
    expect(specialistKeyframes.map((frame) => frame.transform)).toEqual(['scale(0.62)', 'scale(0.62)', 'scale(1)'])
    expect(specialistKeyframes.map((frame) => frame.opacity)).toEqual(['0', '0', '1'])

    expect(Math.abs(parseFloat(rendering.originX || 'NaN') - parseFloat(rendering.expectedOriginX || 'NaN'))).toBeLessThanOrEqual(1)
    expect(Math.abs(parseFloat(rendering.originY || 'NaN') - parseFloat(rendering.expectedOriginY || 'NaN'))).toBeLessThanOrEqual(1)
    expect(rendering.ambientDisplay).toBe('none')
    expect(rendering.activityDisplay).toBe('none')

    await expect(page.locator('html')).toHaveAttribute('data-deep-focus', 'focused', { timeout: 2200 })
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
