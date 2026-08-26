import { expect, test } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'

test.describe('ADS V1 frontend spike', () => {
  test('renders the project shell and methodological state', async ({ page }) => {
    await page.goto('/')

    await expect(page.getByRole('heading', { name: 'Customer Churn Prediction' })).toBeVisible()
    await expect(page.getByText('Resolve prediction moment').first()).toBeVisible()
    await expect(page.locator('.method-status.blocking').first()).toContainText('Required / blocking')
    await expect(page.getByRole('navigation', { name: 'Workspace', exact: true })).toBeVisible()
    await expect(page.getByRole('complementary', { name: 'Methodological guidance' })).toBeVisible()
  })

  test('preserves Data view state in the URL', async ({ page }) => {
    await page.goto('/data?column=support_tickets&filter=month')

    await expect(page.getByRole('heading', { name: 'Data' })).toBeVisible()
    await expect(page.getByRole('heading', { name: 'support_tickets' })).toBeVisible()
    await expect(page.getByPlaceholder('Filter preview rows')).toHaveValue('month')
    await expect(page).toHaveURL(/column=support_tickets/)
    await expect(page).toHaveURL(/filter=month/)
  })

  test('keeps the data workspace inside its column and folds the context panel', async ({ page }) => {
    await page.goto('/data?column=tenure_months&filter=')

    const tableRegion = page.getByRole('region', { name: 'Representative dataset rows' })
    const contextPanel = page.getByRole('complementary', { name: 'Methodological guidance' })
    await expect(tableRegion).toBeVisible()
    await expect(contextPanel).toBeVisible()

    const expandedTableBox = await tableRegion.boundingBox()
    const expandedPanelBox = await contextPanel.boundingBox()
    expect(expandedTableBox).not.toBeNull()
    expect(expandedPanelBox).not.toBeNull()
    expect((expandedTableBox?.x ?? 0) + (expandedTableBox?.width ?? 0)).toBeLessThanOrEqual((expandedPanelBox?.x ?? 0) + 1)

    await page.getByRole('button', { name: 'Collapse methodological guidance' }).click()
    await expect(page.getByRole('button', { name: 'Expand methodological guidance' })).toBeVisible()
    await expect.poll(async () => (await contextPanel.boundingBox())?.width ?? 1000).toBeLessThanOrEqual(50)

    await page.getByRole('button', { name: 'Expand methodological guidance' }).click()
    await expect(page.getByRole('button', { name: 'Collapse methodological guidance' })).toBeVisible()
  })

  test('updates EDA view state without leaving the analytical workspace', async ({ page }) => {
    await page.goto('/eda')

    await expect(page.getByRole('heading', { name: 'Tenure distribution' })).toBeVisible()
    await page.getByRole('button', { name: 'Time trend' }).click()
    await expect(page.getByRole('heading', { name: 'Churn rate through time' })).toBeVisible()
    await expect(page).toHaveURL(/view=trend/)
  })

  test('cockpit is immersive and spatially focuses into the shared Data workspace', async ({ page }) => {
    await page.goto('/cockpit')

    await expect(page.getByRole('region', { name: 'Living data science project map' })).toBeVisible()
    await expect(page.getByRole('navigation', { name: 'Workspace', exact: true })).toHaveCount(0)
    await expect(page.getByRole('link', { name: /Project views/i })).toBeVisible()

    await page.getByRole('button', { name: 'Open Data understanding' }).click()
    await expect(page.getByRole('heading', { name: 'Data' })).toBeVisible()
    await expect(page.getByRole('heading', { name: 'support_tickets' })).toBeVisible()
    await expect(page).toHaveURL(/focus=data/)

    await page.getByRole('button', { name: 'Return to project map' }).click()
    await expect(page.getByRole('region', { name: 'Living data science project map' })).toBeVisible()
    await expect(page).toHaveURL(/focus=map/)
  })

  test('cockpit opens the missingness investigation and can hand off to full Data focus', async ({ page }) => {
    await page.goto('/cockpit')

    await page.getByRole('button', { name: 'Open Production missingness' }).click()
    await expect(page.getByRole('heading', { name: 'Production missingness investigation' })).toBeVisible()
    await expect(page.getByRole('heading', { name: 'Missingness by contract' })).toBeVisible()
    await expect(page).toHaveURL(/focus=missingness/)

    await page.getByRole('button', { name: /Open full Data workspace/i }).click()
    await expect(page.getByRole('heading', { name: 'Data' })).toBeVisible()
    await expect(page.getByRole('heading', { name: 'support_tickets' })).toBeVisible()
    await expect(page).toHaveURL(/focus=data/)
  })

  test('browser Back restores the prior cockpit project-map state', async ({ page }) => {
    await page.goto('/cockpit')
    await page.getByRole('button', { name: 'Open EDA evidence' }).click()
    await expect(page.getByRole('heading', { name: 'EDA' })).toBeVisible()
    await expect(page).toHaveURL(/focus=eda/)

    await page.goBack()
    await expect(page.getByRole('region', { name: 'Living data science project map' })).toBeVisible()
  })

  test('cockpit exposes a larger two-dimensional project space with recovery in every direction and searchable jumps', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    await expect(viewport).toBeVisible()

    const initial = await viewport.evaluate((element) => ({
      left: element.scrollLeft,
      top: element.scrollTop,
      clientWidth: element.clientWidth,
      clientHeight: element.clientHeight,
      scrollWidth: element.scrollWidth,
      scrollHeight: element.scrollHeight,
    }))
    expect(initial.scrollWidth).toBeGreaterThan(initial.clientWidth)
    expect(initial.scrollHeight).toBeGreaterThan(initial.clientHeight)
    expect(initial.left).toBeGreaterThan(0)
    expect(initial.top).toBeGreaterThan(0)

    await viewport.focus()
    await viewport.press('ArrowRight')
    await viewport.press('ArrowDown')
    await expect.poll(async () => viewport.evaluate((element) => element.scrollLeft)).toBeGreaterThan(initial.left)
    await expect.poll(async () => viewport.evaluate((element) => element.scrollTop)).toBeGreaterThan(initial.top)

    await page.getByRole('button', { name: 'Reset project view' }).click()
    await expect.poll(async () => viewport.evaluate((element) => ({ left: element.scrollLeft, top: element.scrollTop }))).toEqual({
      left: initial.left,
      top: initial.top,
    })

    await viewport.focus()
    await viewport.press('ArrowLeft')
    await viewport.press('ArrowUp')
    await expect.poll(async () => viewport.evaluate((element) => element.scrollLeft)).toBeLessThan(initial.left)
    await expect.poll(async () => viewport.evaluate((element) => element.scrollTop)).toBeLessThan(initial.top)

    await page.getByRole('button', { name: 'Jump to project work' }).click()
    await expect(page.getByRole('button', { name: 'Investigation', exact: true })).toBeVisible()
    await page.getByRole('textbox', { name: 'Search project work' }).fill('evaluation')
    await page.getByRole('button', { name: /Evaluation & calibration/i }).click()
    await expect(page.locator('[data-cockpit-node="evaluation"]')).toBeInViewport()
  })

  test('cockpit zoom works from controls, keyboard, fit command and trackpad-style pinch events', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    await expect(page.getByRole('button', { name: /Zoom level 100 percent/i })).toBeVisible()

    await page.getByRole('button', { name: 'Zoom out project map' }).click()
    await expect(page.getByRole('button', { name: /Zoom level 90 percent/i })).toBeVisible()

    await viewport.focus()
    await viewport.press('+')
    await expect(page.getByRole('button', { name: /Zoom level 100 percent/i })).toBeVisible()

    await viewport.evaluate((element) => element.scrollTo({ left: 760, top: 650 }))
    const beforePinch = await viewport.evaluate((element) => ({ left: element.scrollLeft, top: element.scrollTop }))
    await viewport.dispatchEvent('wheel', { ctrlKey: true, deltaY: 80, clientX: 500, clientY: 300 })
    await expect(page.getByRole('button', { name: /Zoom level 100 percent/i })).toHaveCount(0)
    const afterPinch = await viewport.evaluate((element) => ({ left: element.scrollLeft, top: element.scrollTop }))
    expect(afterPinch.left).not.toBe(420)
    expect(afterPinch.top).not.toBe(420)
    expect(Math.abs(afterPinch.left - beforePinch.left)).toBeLessThan(300)
    expect(Math.abs(afterPinch.top - beforePinch.top)).toBeLessThan(300)

    await page.getByRole('button', { name: 'Fit project to viewport' }).click()
    const fittedLabel = await page.locator('.cockpit-zoom-level').textContent()
    expect(fittedLabel).not.toBe('100%')
  })

  test('fully zoomed-out project plane stays centered inside an always-pannable symmetric world', async ({ page }) => {
    await page.setViewportSize({ width: 1920, height: 1000 })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    for (let index = 0; index < 6; index += 1) {
      await page.getByRole('button', { name: 'Zoom out project map' }).click()
    }
    await expect(page.getByRole('button', { name: /Zoom level 45 percent/i })).toBeVisible()

    const geometry = await viewport.evaluate((element) => {
      const world = element.querySelector<HTMLElement>('.project-world')
      const canvas = element.querySelector<HTMLElement>('.project-canvas')
      if (!world || !canvas) return null
      const worldRect = world.getBoundingClientRect()
      const canvasRect = canvas.getBoundingClientRect()
      return {
        left: canvasRect.left - worldRect.left,
        right: worldRect.right - canvasRect.right,
        top: canvasRect.top - worldRect.top,
        bottom: worldRect.bottom - canvasRect.bottom,
        maximumLeft: element.scrollWidth - element.clientWidth,
        maximumTop: element.scrollHeight - element.clientHeight,
      }
    })
    expect(geometry).not.toBeNull()
    expect(Math.abs((geometry?.left ?? 0) - (geometry?.right ?? 0))).toBeLessThan(2)
    expect(Math.abs((geometry?.top ?? 0) - (geometry?.bottom ?? 0))).toBeLessThan(2)
    expect(geometry?.left ?? 0).toBeGreaterThan(300)
    expect(geometry?.top ?? 0).toBeGreaterThan(300)
    expect(geometry?.maximumLeft ?? 0).toBeGreaterThanOrEqual(300)
    expect(geometry?.maximumTop ?? 0).toBeGreaterThanOrEqual(300)

    await viewport.evaluate((element) => element.scrollTo({ left: 0, top: 0 }))
    const startReserve = await viewport.evaluate((element) => {
      const canvas = element.querySelector<HTMLElement>('.project-canvas')
      if (!canvas) return null
      const viewportRect = element.getBoundingClientRect()
      const canvasRect = canvas.getBoundingClientRect()
      return { left: canvasRect.left - viewportRect.left, top: canvasRect.top - viewportRect.top }
    })
    expect(startReserve?.left ?? 0).toBeGreaterThan(300)
    expect(startReserve?.top ?? 0).toBeGreaterThan(300)

    await viewport.evaluate((element) => element.scrollTo({ left: element.scrollWidth, top: element.scrollHeight }))
    const endReserve = await viewport.evaluate((element) => {
      const canvas = element.querySelector<HTMLElement>('.project-canvas')
      if (!canvas) return null
      const viewportRect = element.getBoundingClientRect()
      const canvasRect = canvas.getBoundingClientRect()
      return { right: viewportRect.right - canvasRect.right, bottom: viewportRect.bottom - canvasRect.bottom }
    })
    expect(endReserve?.right ?? 0).toBeGreaterThan(300)
    expect(endReserve?.bottom ?? 0).toBeGreaterThan(300)

    const stageBox = await page.getByRole('button', { name: 'Data & exploration', exact: true }).boundingBox()
    expect(stageBox).not.toBeNull()
    expect(stageBox?.height ?? 0).toBeGreaterThan(32)
  })

  test('cockpit project details, system focus, map controls and primary HUD are explicitly collapsible', async ({ page }) => {
    await page.goto('/cockpit')

    const productBox = await page.locator('.cockpit-product-name').boundingBox()
    const projectBox = await page.locator('.cockpit-project-name').boundingBox()
    expect(productBox).not.toBeNull()
    expect(projectBox).not.toBeNull()
    expect(Math.abs((productBox?.y ?? 0) - (projectBox?.y ?? 0))).toBeLessThan(4)

    const details = page.getByRole('region', { name: 'Expanded project details' })
    await expect(details).toHaveCount(0)
    await page.getByRole('button', { name: 'Details' }).click()
    await expect(details).toBeVisible()
    await expect(details).toContainText('deployment-valid evidence')
    const detailsBox = await details.boundingBox()
    const viewportBox = await page.getByRole('region', { name: 'Living data science project map' }).boundingBox()
    expect(detailsBox).not.toBeNull()
    expect(viewportBox).not.toBeNull()
    expect((detailsBox?.y ?? 999) - (viewportBox?.y ?? 0)).toBeLessThan(70)
    await page.getByRole('button', { name: 'Details' }).click()
    await expect(details).toHaveCount(0)

    const systemFocus = page.getByRole('complementary', { name: 'Current system focus' })
    await expect(systemFocus).toHaveCount(0)
    await page.getByRole('button', { name: 'System focus' }).click()
    await expect(systemFocus).toBeVisible()
    await page.getByRole('button', { name: 'Close system focus' }).click()
    await expect(systemFocus).toHaveCount(0)

    await page.getByRole('button', { name: 'Hide project map controls' }).click()
    await expect(page.getByRole('button', { name: 'Show project map controls' })).toBeVisible()
    await expect(page.getByRole('group', { name: 'Project map controls' })).toHaveCount(0)
    await page.getByRole('button', { name: 'Show project map controls' }).click()
    await expect(page.getByRole('group', { name: 'Project map controls' })).toBeVisible()

    await page.getByRole('button', { name: 'Hide Cockpit HUD' }).click()
    await expect(page.getByRole('button', { name: 'Show Cockpit HUD' })).toBeVisible()
    await expect(page.getByRole('banner', { name: 'Cockpit HUD' })).toHaveCount(0)
    await page.getByRole('button', { name: 'Show Cockpit HUD' }).click()
    await expect(page.getByRole('banner', { name: 'Cockpit HUD' })).toBeVisible()
  })

  test('cockpit canvas visually continues behind the composer while lower work remains recoverable', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    const composer = page.getByRole('textbox', { name: 'Ask or direct the system' }).locator('xpath=ancestor::form')
    const viewportBox = await viewport.boundingBox()
    const composerBox = await composer.boundingBox()

    expect(viewportBox).not.toBeNull()
    expect(composerBox).not.toBeNull()
    expect((viewportBox?.y ?? 0) + (viewportBox?.height ?? 0)).toBeGreaterThan((composerBox?.y ?? 0) + 1)

    await page.getByRole('button', { name: 'Jump to project work' }).click()
    await page.getByRole('textbox', { name: 'Search project work' }).fill('subgroup')
    await page.getByRole('button', { name: /Subgroup review/i }).click()

    await expect.poll(async () => {
      const lowerNodeBox = await page.locator('[data-cockpit-node="review"]').boundingBox()
      const currentComposerBox = await composer.boundingBox()
      if (!lowerNodeBox || !currentComposerBox) return false
      return lowerNodeBox.y + lowerNodeBox.height < currentComposerBox.y - 4
    }).toBe(true)
  })

  test('cockpit fullscreen control synchronizes supported enter and exit behavior', async ({ page }) => {
    await page.addInitScript(() => {
      let fullscreenElement: Element | null = null
      Object.defineProperty(document, 'fullscreenEnabled', { configurable: true, get: () => true })
      Object.defineProperty(document, 'fullscreenElement', { configurable: true, get: () => fullscreenElement })
      HTMLElement.prototype.requestFullscreen = async function requestFullscreen() {
        fullscreenElement = this
        document.dispatchEvent(new Event('fullscreenchange'))
      }
      document.exitFullscreen = async () => {
        fullscreenElement = null
        document.dispatchEvent(new Event('fullscreenchange'))
      }
    })

    await page.goto('/cockpit')
    await page.getByRole('button', { name: 'Enter fullscreen' }).click()
    await expect(page.getByRole('button', { name: 'Exit fullscreen' })).toBeVisible()
    await page.getByRole('button', { name: 'Exit fullscreen' }).click()
    await expect(page.getByRole('button', { name: 'Enter fullscreen' })).toBeVisible()
  })

  test('cockpit core surface has no serious automated accessibility violations', async ({ page }) => {
    await page.goto('/cockpit')
    await expect(page.getByRole('region', { name: 'Living data science project map' })).toBeVisible()

    const results = await new AxeBuilder({ page }).analyze()
    const serious = results.violations.filter((violation) =>
      violation.impact === 'serious' || violation.impact === 'critical',
    )

    expect(serious).toEqual([])
  })

  test('approval action updates run state through the interaction boundary', async ({ page }) => {
    await page.goto('/')

    const approveButton = page.getByRole('button', { name: /Approve & run/i })
    await expect(approveButton).toBeVisible()
    await approveButton.click()
    await expect(page.getByRole('button', { name: /Approve & run/i })).toHaveCount(0)
    await expect(page.getByText('2 running')).toBeVisible()
  })

  test('theme switching is explicit and persisted', async ({ page }) => {
    await page.goto('/')

    const switcher = page.getByRole('button', { name: /Switch to .* theme/ })
    const before = await page.locator('html').getAttribute('data-theme')
    await switcher.click()
    const after = await page.locator('html').getAttribute('data-theme')

    expect(after).not.toBe(before)
    await page.reload()
    await expect(page.locator('html')).toHaveAttribute('data-theme', after ?? 'light')
  })

  test('core shell has no serious automated accessibility violations', async ({ page }) => {
    await page.goto('/')
    await expect(page.getByRole('heading', { name: 'Customer Churn Prediction' })).toBeVisible()

    const results = await new AxeBuilder({ page }).analyze()
    const serious = results.violations.filter((violation) =>
      violation.impact === 'serious' || violation.impact === 'critical',
    )

    expect(serious).toEqual([])
  })
})
