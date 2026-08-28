/*
 * Z7 compositor prewarm adapter.
 *
 * The accepted Z7 interaction is owned by cockpit-reintegration.js. This file
 * does not replace that state machine. It delays the first animated click by
 * two animation frames so the browser can promote the world and specialist
 * layers before the exact Z7 handler changes data-deep-focus to `entering`.
 * Reduced-motion mode bypasses the prewarm because there is no long animation.
 */

const html = document.documentElement
const deepDiveButton = document.querySelector('#deep-dive')

let redispatching = false

installDeepFocusPrewarm()
installDeepFocusRenderingState()

function installDeepFocusPrewarm() {
  if (!deepDiveButton) return

  deepDiveButton.addEventListener('click', (event) => {
    if (redispatching) return
    if (html.dataset.deepFocus !== 'false') return
    if (html.dataset.reduced === 'on' || window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) return

    event.preventDefault()
    event.stopImmediatePropagation()
    html.dataset.z7Rendering = 'preparing'

    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        if (html.dataset.deepFocus !== 'false') {
          html.dataset.z7Rendering = 'active'
          return
        }

        redispatching = true
        deepDiveButton.click()
        redispatching = false
      })
    })
  }, true)
}

function installDeepFocusRenderingState() {
  html.dataset.z7Rendering = 'idle'

  const observer = new MutationObserver((mutations) => {
    if (!mutations.some((mutation) => mutation.attributeName === 'data-deep-focus')) return

    const state = html.dataset.deepFocus || 'false'
    if (state === 'entering' || state === 'focused') {
      html.dataset.z7Rendering = 'active'
      return
    }

    if (state === 'false') {
      html.dataset.z7Rendering = 'idle'
    }
  })

  observer.observe(html, { attributes: true, attributeFilter: ['data-deep-focus'] })
}
