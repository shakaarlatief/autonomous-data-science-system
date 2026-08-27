const SVG_NS = 'http://www.w3.org/2000/svg'

function installRuntimeTagPerimeterTraces() {
  for (const tag of document.querySelectorAll('.runtime-tag-carrier')) {
    if (tag.querySelector('.runtime-tag-trace')) continue

    const svg = document.createElementNS(SVG_NS, 'svg')
    svg.classList.add('runtime-tag-trace')
    svg.setAttribute('viewBox', '0 0 100 36')
    svg.setAttribute('preserveAspectRatio', 'none')
    svg.setAttribute('aria-hidden', 'true')

    const runner = document.createElementNS(SVG_NS, 'rect')
    runner.classList.add('runtime-tag-trace-runner')
    runner.setAttribute('x', '1.5')
    runner.setAttribute('y', '1.5')
    runner.setAttribute('width', '97')
    runner.setAttribute('height', '33')
    runner.setAttribute('rx', '11')
    runner.setAttribute('ry', '11')
    runner.setAttribute('pathLength', '100')

    svg.append(runner)
    tag.prepend(svg)
  }
}

installRuntimeTagPerimeterTraces()
