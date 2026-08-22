import { expect, test } from '@playwright/test'

test.describe('ADS V1 visual regression', () => {
  test.skip(process.env.VISUAL_REGRESSION !== '1', 'Visual regression runs in the dedicated canonical screenshot step.')
  test.skip(process.platform !== 'linux', 'Canonical visual baselines use Linux Chromium to avoid operating-system font rasterization drift.')

  test.use({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    colorScheme: 'light',
    locale: 'en-US',
    timezoneId: 'UTC',
  })

  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem('ads-theme', 'light')
    })
    await page.emulateMedia({ colorScheme: 'light', reducedMotion: 'reduce' })
  })

  test('overview workspace remains visually stable', async ({ page }) => {
    await page.goto('/')
    await expect(page.getByRole('heading', { name: 'Customer Churn Prediction' })).toBeVisible()

    await expect(page).toHaveScreenshot('overview-light.png', {
      fullPage: true,
      animations: 'disabled',
      caret: 'hide',
      maxDiffPixelRatio: 0.002,
    })
  })

  test('data inspection workspace remains visually stable', async ({ page }) => {
    await page.goto('/data?column=support_tickets&filter=month')
    await expect(page.getByRole('heading', { name: 'support_tickets' })).toBeVisible()
    await expect(page.getByPlaceholder('Filter preview rows')).toHaveValue('month')

    await expect(page).toHaveScreenshot('data-support-tickets-light.png', {
      fullPage: true,
      animations: 'disabled',
      caret: 'hide',
      maxDiffPixelRatio: 0.002,
    })
  })

  test('EDA distribution workspace remains visually stable', async ({ page }) => {
    await page.goto('/eda')
    await expect(page.getByRole('heading', { name: 'Tenure distribution' })).toBeVisible()
    await expect(page.locator('.chart-stage')).toHaveAttribute('data-chart-engine', 'echarts')
    await expect(page.locator('.chart-stage canvas')).toBeVisible()

    await expect(page).toHaveScreenshot('eda-distribution-light.png', {
      fullPage: true,
      animations: 'disabled',
      caret: 'hide',
      maxDiffPixelRatio: 0.002,
    })
  })

  test('decision history workspace remains visually stable', async ({ page }) => {
    await page.goto('/history')
    await expect(page.getByRole('heading', { name: 'Decisions & History' })).toBeVisible()
    await expect(page.getByRole('heading', { name: 'Recent reasoning trail' })).toBeVisible()

    await expect(page).toHaveScreenshot('history-light.png', {
      fullPage: true,
      animations: 'disabled',
      caret: 'hide',
      maxDiffPixelRatio: 0.002,
    })
  })
})
