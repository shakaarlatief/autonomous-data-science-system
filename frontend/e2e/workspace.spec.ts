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

  test('updates EDA view state without leaving the analytical workspace', async ({ page }) => {
    await page.goto('/eda')

    await expect(page.getByRole('heading', { name: 'Tenure distribution' })).toBeVisible()
    await page.getByRole('button', { name: 'Time trend' }).click()
    await expect(page.getByRole('heading', { name: 'Churn rate through time' })).toBeVisible()
    await expect(page).toHaveURL(/view=trend/)
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
