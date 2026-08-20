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

    await expect(page.getByText('Project operating map')).toBeVisible()
    await expect(page.getByRole('navigation', { name: 'Workspace', exact: true })).toHaveCount(0)
    await expect(page.getByRole('link', { name: /Project views/i })).toBeVisible()

    await page.getByRole('button', { name: 'Open Data understanding' }).click()
    await expect(page.getByRole('heading', { name: 'Data' })).toBeVisible()
    await expect(page.getByRole('heading', { name: 'support_tickets' })).toBeVisible()
    await expect(page).toHaveURL(/focus=data/)

    await page.getByRole('button', { name: 'Return to project map' }).click()
    await expect(page.getByText('Project operating map')).toBeVisible()
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
    await expect(page.getByText('Project operating map')).toBeVisible()
  })

  test('cockpit exposes a genuinely larger two-dimensional project space with keyboard recovery', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/cockpit')

    const viewport = page.getByRole('region', { name: 'Living data science project map' })
    await expect(viewport).toBeVisible()

    const extent = await viewport.evaluate((element) => ({
      clientWidth: element.clientWidth,
      clientHeight: element.clientHeight,
      scrollWidth: element.scrollWidth,
      scrollHeight: element.scrollHeight,
    }))
    expect(extent.scrollWidth).toBeGreaterThan(extent.clientWidth)
    expect(extent.scrollHeight).toBeGreaterThan(extent.clientHeight)

    await viewport.focus()
    await viewport.press('ArrowRight')
    await viewport.press('ArrowDown')
    await expect.poll(async () => viewport.evaluate((element) => element.scrollLeft)).toBeGreaterThan(0)
    await expect.poll(async () => viewport.evaluate((element) => element.scrollTop)).toBeGreaterThan(0)

    await page.getByRole('button', { name: 'Reset project view' }).click()
    await expect.poll(async () => viewport.evaluate((element) => element.scrollLeft)).toBe(0)
    await expect.poll(async () => viewport.evaluate((element) => element.scrollTop)).toBe(0)

    await page.getByRole('button', { name: 'Jump to evaluation' }).click()
    await expect(page.getByText('Evaluation & calibration')).toBeInViewport()
  })

  test('cockpit keeps project details and system focus collapsible instead of permanently consuming the map', async ({ page }) => {
    await page.goto('/cockpit')

    const details = page.getByRole('region', { name: 'Expanded project details' })
    await expect(details).toHaveCount(0)
    await page.getByRole('button', { name: 'Show project details' }).click()
    await expect(details).toBeVisible()
    await expect(details).toContainText('Predict churn')
    await page.getByRole('button', { name: 'Hide project details' }).click()
    await expect(details).toHaveCount(0)

    const systemFocus = page.getByRole('complementary', { name: 'Current system focus' })
    await expect(systemFocus).toHaveCount(0)
    await page.getByRole('button', { name: 'System focus' }).click()
    await expect(systemFocus).toBeVisible()
    await page.getByRole('button', { name: 'Close system focus' }).click()
    await expect(systemFocus).toHaveCount(0)
  })

  test('cockpit map viewport remains clear of the docked composer at desktop scale', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 })
    await page.goto('/cockpit')

    const viewportBox = await page.getByRole('region', { name: 'Living data science project map' }).boundingBox()
    const composerBox = await page.getByRole('textbox', { name: 'Ask or direct the system' }).locator('xpath=ancestor::form').boundingBox()

    expect(viewportBox).not.toBeNull()
    expect(composerBox).not.toBeNull()
    expect((viewportBox?.y ?? 0) + (viewportBox?.height ?? 0)).toBeLessThanOrEqual((composerBox?.y ?? 0) + 1)
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
    await expect(page.getByText('Project operating map')).toBeVisible()

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
