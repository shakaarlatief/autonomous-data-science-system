const html = document.documentElement

requestAnimationFrame(() => {
  const x5Button = document.querySelector('button[data-expansion-style="x5"]')
  if (x5Button) {
    x5Button.textContent = 'X5 Two-Axis Expansion'
    x5Button.click()
  }

  const x5Tile = document.querySelector('.expansion-tile[data-variant="x5"]')
  if (x5Tile) {
    const title = x5Tile.querySelector('.expansion-tile-copy strong')
    const description = x5Tile.querySelector('.expansion-tile-copy small')
    if (title) title.textContent = 'Two-Axis Expansion'
    if (description) description.textContent = 'The selected work unit expands in both width and height as one balanced object while the surrounding project map remains at normal salience.'
  }

  html.dataset.expansionStyle = 'x5'
})
