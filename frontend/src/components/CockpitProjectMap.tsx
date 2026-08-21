import {
  useEffect,
  useMemo,
  useRef,
  useState,
  type CSSProperties,
  type KeyboardEvent as ReactKeyboardEvent,
  type ReactNode,
} from 'react'
import {
  ArrowUpRight,
  BarChart3,
  BrainCircuit,
  Check,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  ChevronUp,
  Crosshair,
  Database,
  FlaskConical,
  Gauge,
  LocateFixed,
  Move,
  PanelRightOpen,
  Play,
  RotateCcw,
  Search,
  Target,
  TriangleAlert,
  X,
  ZoomIn,
  ZoomOut,
} from 'lucide-react'
import { useWorkspace } from '../appState'

export type ProjectMapFocus = 'data' | 'eda' | 'missingness'

type ProjectMapProps = {
  onFocus: (focus: ProjectMapFocus) => void
}

type NodeId =
  | 'objective'
  | 'data'
  | 'prediction'
  | 'missingness'
  | 'eda'
  | 'validation'
  | 'baseline'
  | 'rf'
  | 'evaluation'
  | 'review'

type NodeStatus = 'complete' | 'blocked' | 'attention' | 'ready' | 'selected' | 'deferred' | 'future'

type NodeDefinition = {
  nodeId: NodeId
  className: string
  kicker: string
  title: string
  description: string
  status: NodeStatus
  icon: ReactNode
  focus?: ProjectMapFocus
}

const CANVAS_WIDTH = 2260
const CANVAS_HEIGHT = 1180
const PAN_GUTTER = 420
const MIN_SCROLL_RANGE = 360
const GRID_SIDE_GUTTER = 150
const FIT_PADDING = 72
const MIN_ZOOM = 0.45
const MAX_ZOOM = 1.6
const ZOOM_STEP = 0.1
const PINCH_SENSITIVITY = 0.00135
const MAX_PINCH_DELTA_PER_FRAME = 64

const CONNECTOR_PATHS = [
  'M250 205 C300 205 300 175 350 175',
  'M550 175 C680 175 690 170 830 170',
  'M450 225 C450 305 470 340 480 430',
  'M520 520 C650 520 700 420 880 420',
  'M930 225 C930 280 945 315 960 360',
  'M1080 420 C1160 420 1175 315 1260 315',
  'M1080 455 C1170 480 1180 625 1260 625',
  'M1460 315 C1540 315 1540 480 1600 480',
  'M1460 625 C1540 625 1540 510 1600 510',
  'M520 760 C820 760 1120 780 1600 780',
]

const STAGES: Array<{ label: string; nodeId: NodeId }> = [
  { label: 'Framing', nodeId: 'objective' },
  { label: 'Data & exploration', nodeId: 'data' },
  { label: 'Validation', nodeId: 'validation' },
  { label: 'Modeling', nodeId: 'baseline' },
  { label: 'Evaluation', nodeId: 'evaluation' },
]

const clampZoom = (value: number) => Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, value))
const clampScroll = (value: number, maximum: number) => Math.min(Math.max(0, value), Math.max(0, maximum))
const clampPinchDelta = (value: number) => Math.min(MAX_PINCH_DELTA_PER_FRAME, Math.max(-MAX_PINCH_DELTA_PER_FRAME, value))

export function CockpitProjectMap({ onFocus }: ProjectMapProps) {
  const { workspace } = useWorkspace()
  const viewportRef = useRef<HTMLElement>(null)
  const stageRulerTrackRef = useRef<HTMLElement>(null)
  const zoomRef = useRef(1)
  const pinchDeltaRef = useRef(0)
  const pinchAnchorRef = useRef({ x: 0, y: 0 })
  const pinchFrameRef = useRef<number | null>(null)
  const zoomLayoutFrameRef = useRef<number | null>(null)
  const [isHudExpanded, setIsHudExpanded] = useState(false)
  const [isContextOpen, setIsContextOpen] = useState(false)
  const [isJumpOpen, setIsJumpOpen] = useState(false)
  const [isToolbarCollapsed, setIsToolbarCollapsed] = useState(false)
  const [jumpQuery, setJumpQuery] = useState('')
  const [zoom, setZoom] = useState(1)

  const blocker = workspace.recommendations.find((item) => item.status === 'BLOCKING')
  const missingness = workspace.recommendations.find((item) => item.title.toLowerCase().includes('missing'))

  const nodes = useMemo<NodeDefinition[]>(() => [
    {
      nodeId: 'objective',
      className: 'node-objective',
      kicker: 'Framing',
      title: 'Objective defined',
      description: 'Predict customer churn with decisions usable before retention intervention.',
      status: 'complete',
      icon: <Target size={17} />,
    },
    {
      nodeId: 'data',
      className: 'node-data',
      kicker: 'Dataset',
      title: 'Data understanding',
      description: '7,043 rows · 21 source columns · semantic roles mapped',
      status: 'complete',
      icon: <Database size={17} />,
      focus: 'data',
    },
    {
      nodeId: 'prediction',
      className: 'node-prediction',
      kicker: 'Question',
      title: 'Resolve prediction moment',
      description: blocker?.summary ?? 'Feature eligibility cannot be finalized until the prediction moment is explicit.',
      status: 'blocked',
      icon: <TriangleAlert size={17} />,
    },
    {
      nodeId: 'missingness',
      className: 'node-missingness',
      kicker: 'Investigation',
      title: 'Production missingness',
      description: missingness?.summary ?? 'Support-ticket completeness needs production-time investigation.',
      status: 'attention',
      icon: <FlaskConical size={17} />,
      focus: 'missingness',
    },
    {
      nodeId: 'eda',
      className: 'node-eda',
      kicker: 'Exploration',
      title: 'EDA evidence',
      description: 'Distribution and cohort signals are available for focused inspection.',
      status: 'ready',
      icon: <BarChart3 size={17} />,
      focus: 'eda',
    },
    {
      nodeId: 'validation',
      className: 'node-validation',
      kicker: 'Decision',
      title: 'Chronological validation',
      description: 'Temporal ordering selected as the current validation design.',
      status: 'selected',
      icon: <Check size={17} />,
    },
    {
      nodeId: 'baseline',
      className: 'node-baseline',
      kicker: 'Modeling',
      title: 'Logistic baseline',
      description: 'Reference model completed and available for comparison.',
      status: 'complete',
      icon: <Play size={17} />,
    },
    {
      nodeId: 'rf',
      className: 'node-rf',
      kicker: 'Modeling',
      title: 'Random Forest benchmark',
      description: 'Deferred until prediction-time feature eligibility is resolved.',
      status: 'deferred',
      icon: <BrainCircuit size={17} />,
    },
    {
      nodeId: 'evaluation',
      className: 'node-evaluation',
      kicker: 'Downstream',
      title: 'Evaluation & calibration',
      description: 'Waiting on the active validation and modeling path.',
      status: 'future',
      icon: <Gauge size={17} />,
    },
    {
      nodeId: 'review',
      className: 'node-review',
      kicker: 'Evaluation',
      title: 'Subgroup review',
      description: 'Reserved downstream work demonstrates lower project-space growth without promoting a final stage taxonomy.',
      status: 'future',
      icon: <BarChart3 size={17} />,
    },
  ], [blocker?.summary, missingness?.summary])

  const filteredJumpTargets = useMemo(() => {
    const query = jumpQuery.trim().toLowerCase()
    if (!query) return nodes
    return nodes.filter((node) => `${node.title} ${node.kicker}`.toLowerCase().includes(query))
  }, [jumpQuery, nodes])

  const scrollBehavior = (): ScrollBehavior =>
    window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'

  const scrollLimits = (viewport: HTMLElement) => ({
    maximumLeft: Math.max(0, viewport.scrollWidth - viewport.clientWidth),
    maximumTop: Math.max(0, viewport.scrollHeight - viewport.clientHeight),
  })

  const canvasGeometry = (viewport: HTMLElement) => {
    const canvas = viewport.querySelector<HTMLElement>('.project-canvas')
    if (!canvas) return null

    const viewportRect = viewport.getBoundingClientRect()
    const canvasRect = canvas.getBoundingClientRect()
    return {
      viewportRect,
      canvasRect,
      originLeft: viewport.scrollLeft + canvasRect.left - viewportRect.left,
      originTop: viewport.scrollTop + canvasRect.top - viewportRect.top,
      centerLeft: viewport.scrollLeft + canvasRect.left - viewportRect.left + canvasRect.width / 2,
      centerTop: viewport.scrollTop + canvasRect.top - viewportRect.top + canvasRect.height / 2,
    }
  }

  const setZoomState = (nextZoom: number) => {
    zoomRef.current = nextZoom
    setZoom(nextZoom)
  }

  const zoomAround = (nextZoom: number, anchorX?: number, anchorY?: number) => {
    const viewport = viewportRef.current
    if (!viewport) return

    const currentZoom = zoomRef.current
    const boundedZoom = clampZoom(nextZoom)
    if (Math.abs(boundedZoom - currentZoom) < 0.0005) return

    const geometry = canvasGeometry(viewport)
    if (!geometry) return

    const x = anchorX ?? viewport.clientWidth / 2
    const y = anchorY ?? viewport.clientHeight / 2
    const canvasLeftInViewport = geometry.canvasRect.left - geometry.viewportRect.left
    const canvasTopInViewport = geometry.canvasRect.top - geometry.viewportRect.top
    const logicalX = (x - canvasLeftInViewport) / currentZoom
    const logicalY = (y - canvasTopInViewport) / currentZoom

    setZoomState(boundedZoom)

    if (zoomLayoutFrameRef.current !== null) {
      window.cancelAnimationFrame(zoomLayoutFrameRef.current)
    }
    zoomLayoutFrameRef.current = window.requestAnimationFrame(() => {
      zoomLayoutFrameRef.current = null
      const nextGeometry = canvasGeometry(viewport)
      if (!nextGeometry) return
      const limits = scrollLimits(viewport)
      viewport.scrollTo({
        left: clampScroll(nextGeometry.originLeft + logicalX * boundedZoom - x, limits.maximumLeft),
        top: clampScroll(nextGeometry.originTop + logicalY * boundedZoom - y, limits.maximumTop),
        behavior: 'auto',
      })
    })
  }

  const resetViewport = () => {
    const viewport = viewportRef.current
    if (!viewport) return

    setZoomState(1)
    window.requestAnimationFrame(() => {
      const geometry = canvasGeometry(viewport)
      if (!geometry) return
      const limits = scrollLimits(viewport)
      viewport.scrollTo({
        left: clampScroll(geometry.originLeft, limits.maximumLeft),
        top: clampScroll(geometry.originTop, limits.maximumTop),
        behavior: scrollBehavior(),
      })
      viewport.focus({ preventScroll: true })
    })
  }

  const fitProject = () => {
    const viewport = viewportRef.current
    if (!viewport) return

    const horizontalFit = (viewport.clientWidth - FIT_PADDING * 2) / CANVAS_WIDTH
    const verticalFit = (viewport.clientHeight - FIT_PADDING * 2) / CANVAS_HEIGHT
    const nextZoom = clampZoom(Math.min(horizontalFit, verticalFit, 1))

    setZoomState(nextZoom)
    window.requestAnimationFrame(() => {
      const geometry = canvasGeometry(viewport)
      if (!geometry) return
      const limits = scrollLimits(viewport)
      viewport.scrollTo({
        left: clampScroll(geometry.centerLeft - viewport.clientWidth / 2, limits.maximumLeft),
        top: clampScroll(geometry.centerTop - viewport.clientHeight / 2, limits.maximumTop),
        behavior: scrollBehavior(),
      })
      viewport.focus({ preventScroll: true })
    })
  }

  const jumpToNode = (nodeId: NodeId) => {
    const viewport = viewportRef.current
    const node = viewport?.querySelector<HTMLElement>(`[data-cockpit-node="${nodeId}"]`)
    if (!viewport || !node) return

    const viewportRect = viewport.getBoundingClientRect()
    const nodeRect = node.getBoundingClientRect()
    const limits = scrollLimits(viewport)
    const nodeCenterLeft = viewport.scrollLeft + nodeRect.left - viewportRect.left + nodeRect.width / 2
    const nodeCenterTop = viewport.scrollTop + nodeRect.top - viewportRect.top + nodeRect.height / 2

    viewport.scrollTo({
      left: clampScroll(nodeCenterLeft - viewport.clientWidth / 2, limits.maximumLeft),
      top: clampScroll(nodeCenterTop - viewport.clientHeight / 2, limits.maximumTop),
      behavior: scrollBehavior(),
    })
    window.requestAnimationFrame(() => node.focus({ preventScroll: true }))
    setIsJumpOpen(false)
    setJumpQuery('')
  }

  useEffect(() => {
    window.requestAnimationFrame(() => {
      const viewport = viewportRef.current
      if (!viewport) return
      const geometry = canvasGeometry(viewport)
      if (!geometry) return
      viewport.scrollTo({ left: geometry.originLeft, top: geometry.originTop, behavior: 'auto' })
    })
  }, [])

  useEffect(() => {
    const viewport = viewportRef.current
    const rulerTrack = stageRulerTrackRef.current
    if (!viewport || !rulerTrack) return undefined

    let frame = 0
    const syncRuler = () => {
      const framing = viewport.querySelector<HTMLElement>('.stage-framing')
      const evaluation = viewport.querySelector<HTMLElement>('.stage-evaluation')
      if (!framing || !evaluation) return

      const viewportRect = viewport.getBoundingClientRect()
      const framingRect = framing.getBoundingClientRect()
      const evaluationRect = evaluation.getBoundingClientRect()
      const semanticLeft = framingRect.left - viewportRect.left
      const semanticWidth = evaluationRect.right - framingRect.left

      rulerTrack.style.width = `${semanticWidth}px`
      rulerTrack.style.transform = `translate3d(${semanticLeft}px, 0, 0)`
    }
    const scheduleSync = () => {
      window.cancelAnimationFrame(frame)
      frame = window.requestAnimationFrame(syncRuler)
    }

    scheduleSync()
    viewport.addEventListener('scroll', scheduleSync, { passive: true })
    window.addEventListener('resize', scheduleSync)
    return () => {
      window.cancelAnimationFrame(frame)
      viewport.removeEventListener('scroll', scheduleSync)
      window.removeEventListener('resize', scheduleSync)
    }
  }, [zoom])

  useEffect(() => {
    const viewport = viewportRef.current
    if (!viewport) return undefined

    const handlePinchZoom = (event: WheelEvent) => {
      if (!event.ctrlKey) return
      event.preventDefault()

      const rect = viewport.getBoundingClientRect()
      const deltaModeScale = event.deltaMode === 1
        ? 16
        : event.deltaMode === 2
          ? viewport.clientHeight
          : 1
      pinchDeltaRef.current += event.deltaY * deltaModeScale
      pinchAnchorRef.current = {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top,
      }

      if (pinchFrameRef.current !== null) return

      pinchFrameRef.current = window.requestAnimationFrame(() => {
        pinchFrameRef.current = null
        const delta = clampPinchDelta(pinchDeltaRef.current)
        pinchDeltaRef.current = 0
        if (Math.abs(delta) < 0.01) return

        const factor = Math.exp(-delta * PINCH_SENSITIVITY)
        const anchor = pinchAnchorRef.current
        zoomAround(zoomRef.current * factor, anchor.x, anchor.y)
      })
    }

    viewport.addEventListener('wheel', handlePinchZoom, { passive: false })
    return () => {
      viewport.removeEventListener('wheel', handlePinchZoom)
      if (pinchFrameRef.current !== null) {
        window.cancelAnimationFrame(pinchFrameRef.current)
        pinchFrameRef.current = null
      }
      if (zoomLayoutFrameRef.current !== null) {
        window.cancelAnimationFrame(zoomLayoutFrameRef.current)
        zoomLayoutFrameRef.current = null
      }
    }
  }, [])

  useEffect(() => {
    if (!isJumpOpen) return undefined
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setIsJumpOpen(false)
    }
    window.addEventListener('keydown', closeOnEscape)
    return () => window.removeEventListener('keydown', closeOnEscape)
  }, [isJumpOpen])

  const handleViewportKeyDown = (event: ReactKeyboardEvent<HTMLElement>) => {
    const viewport = viewportRef.current
    if (!viewport || event.target !== viewport) return

    const step = event.shiftKey ? 320 : 150
    const movement = {
      ArrowLeft: [-step, 0],
      ArrowRight: [step, 0],
      ArrowUp: [0, -step],
      ArrowDown: [0, step],
    }[event.key]

    if (movement) {
      event.preventDefault()
      viewport.scrollBy({ left: movement[0], top: movement[1], behavior: scrollBehavior() })
      return
    }

    if (event.key === 'Home') {
      event.preventDefault()
      resetViewport()
      return
    }

    if (event.key === '+' || event.key === '=') {
      event.preventDefault()
      zoomAround(zoomRef.current + ZOOM_STEP)
      return
    }

    if (event.key === '-') {
      event.preventDefault()
      zoomAround(zoomRef.current - ZOOM_STEP)
      return
    }

    if (event.key === '0') {
      event.preventDefault()
      zoomAround(1)
      return
    }

    if (event.key.toLowerCase() === 'f') {
      event.preventDefault()
      fitProject()
    }
  }

  const canvasStyle = {
    zoom,
    '--cockpit-zoom': zoom,
  } as CSSProperties
  const worldStyle = {
    width: `max(${CANVAS_WIDTH * zoom + PAN_GUTTER * 2}px, calc(100% + ${MIN_SCROLL_RANGE}px))`,
    height: `max(${CANVAS_HEIGHT * zoom + PAN_GUTTER * 2}px, calc(100% + ${MIN_SCROLL_RANGE}px))`,
    '--cockpit-zoom': zoom,
  } as CSSProperties
  const zoomPercent = Math.round(zoom * 100)

  const collapseToolbar = () => {
    setIsJumpOpen(false)
    setIsToolbarCollapsed(true)
  }

  return (
    <main className="cockpit-stage cockpit-map-stage" aria-labelledby="cockpit-map-title">
      <h1 id="cockpit-map-title" className="cockpit-visually-hidden">
        {workspace.project.name} project operating map
      </h1>

      <div className="cockpit-map-layout">
        <section
          ref={viewportRef}
          className="project-viewport"
          aria-label="Living data science project map"
          aria-description="Two-dimensional finite grid workspace with symmetric pan reserve around the semantic project plane. Two-finger trackpad movement pans. Trackpad pinch zooms smoothly around the gesture anchor. Arrow keys pan, plus and minus zoom, F fits the project, and Home resets."
          aria-keyshortcuts="ArrowLeft ArrowRight ArrowUp ArrowDown Home + - 0 F"
          tabIndex={0}
          onKeyDown={handleViewportKeyDown}
        >
          <div className="project-world" style={worldStyle}>
            <div className="project-canvas" style={canvasStyle}>
              <div className="stage-zone stage-framing" aria-hidden="true" />
              <div className="stage-zone stage-exploration" aria-hidden="true" />
              <div className="stage-zone stage-validation" aria-hidden="true" />
              <div className="stage-zone stage-modeling" aria-hidden="true" />
              <div className="stage-zone stage-evaluation" aria-hidden="true" />

              <svg className="project-connectors" viewBox={`0 0 ${CANVAS_WIDTH} ${CANVAS_HEIGHT}`} aria-hidden="true" preserveAspectRatio="none">
                <g transform={`translate(${GRID_SIDE_GUTTER} 0)`}>
                  {CONNECTOR_PATHS.map((path, index) => (
                    <path key={path} className={index === 8 ? 'connector-deferred' : undefined} d={path} />
                  ))}
                </g>
              </svg>

              {nodes.map((node) => (
                <CockpitNode
                  key={node.nodeId}
                  {...node}
                  onActivate={node.focus ? () => onFocus(node.focus as ProjectMapFocus) : undefined}
                />
              ))}
            </div>
          </div>
        </section>

        <div className="cockpit-stage-ruler" aria-label="Visible project stage ruler">
          <nav ref={stageRulerTrackRef} className="cockpit-stage-ruler-track" aria-label="Project stages">
            {STAGES.map((stage) => (
              <button type="button" key={stage.nodeId} onClick={() => jumpToNode(stage.nodeId)}>{stage.label}</button>
            ))}
          </nav>
        </div>

        {!isToolbarCollapsed ? (
          <div className="cockpit-map-toolbar" role="group" aria-label="Project map controls">
            <button
              type="button"
              className="cockpit-toolbar-labelled"
              onClick={() => setIsHudExpanded((value) => !value)}
              aria-expanded={isHudExpanded}
              aria-label="Details"
              data-tooltip="Project details"
              title="Project details"
            >
              {isHudExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
              Details
            </button>

            <div className="cockpit-zoom-controls" aria-label="Project map zoom controls">
              <button type="button" onClick={() => zoomAround(zoomRef.current - ZOOM_STEP)} aria-label="Zoom out project map" title="Zoom out">
                <ZoomOut size={14} />
              </button>
              <button
                type="button"
                className="cockpit-zoom-level"
                onClick={() => zoomAround(1)}
                aria-label={`Zoom level ${zoomPercent} percent. Reset to 100 percent`}
                title="Reset zoom to 100%"
              >
                {zoomPercent}%
              </button>
              <button type="button" onClick={() => zoomAround(zoomRef.current + ZOOM_STEP)} aria-label="Zoom in project map" title="Zoom in">
                <ZoomIn size={14} />
              </button>
            </div>

            <button type="button" onClick={fitProject} aria-label="Fit project to viewport" data-tooltip="Fit project" title="Fit project">
              <LocateFixed size={14} />
            </button>
            <button type="button" onClick={resetViewport} aria-label="Reset project view" data-tooltip="Reset view" title="Reset pan and zoom">
              <RotateCcw size={14} />
            </button>

            <div className="cockpit-jump-menu">
              <button
                type="button"
                className="cockpit-toolbar-labelled"
                onClick={() => setIsJumpOpen((value) => !value)}
                aria-expanded={isJumpOpen}
                aria-haspopup="dialog"
                aria-label="Jump to project work"
                data-tooltip="Jump to project work"
                title="Jump to project work"
              >
                <Crosshair size={14} /> Jump to <ChevronDown size={12} />
              </button>

              {isJumpOpen && (
                <div className="cockpit-jump-popover" role="dialog" aria-label="Jump to project work">
                  <div className="cockpit-jump-quick" aria-label="Quick project jumps">
                    <button type="button" onClick={() => jumpToNode('missingness')}>Active work</button>
                    <button type="button" onClick={() => jumpToNode('prediction')}>Blocker</button>
                    <button type="button" onClick={() => jumpToNode('missingness')}>Investigation</button>
                    <button type="button" onClick={() => jumpToNode('evaluation')}>Evaluation</button>
                  </div>
                  <label className="cockpit-jump-search">
                    <Search size={14} />
                    <span className="cockpit-visually-hidden">Search project work</span>
                    <input
                      autoFocus
                      value={jumpQuery}
                      onChange={(event) => setJumpQuery(event.target.value)}
                      placeholder="Search project work…"
                      aria-label="Search project work"
                    />
                  </label>
                  <div className="cockpit-jump-results">
                    {filteredJumpTargets.map((node) => (
                      <button type="button" key={node.nodeId} onClick={() => jumpToNode(node.nodeId)}>
                        <span>{node.title}</span>
                        <small>{node.kicker}</small>
                      </button>
                    ))}
                    {filteredJumpTargets.length === 0 && <p>No matching project work.</p>}
                  </div>
                </div>
              )}
            </div>

            <button
              type="button"
              className="cockpit-toolbar-labelled"
              onClick={() => setIsContextOpen((value) => !value)}
              aria-expanded={isContextOpen}
              aria-label="System focus"
              data-tooltip="System focus"
              title="System focus"
            >
              <PanelRightOpen size={14} /> System focus
            </button>
            <button
              type="button"
              className="cockpit-toolbar-fold"
              onClick={collapseToolbar}
              aria-label="Hide project map controls"
              data-tooltip="Hide controls"
              title="Fold controls to the right"
            >
              <ChevronRight size={15} />
            </button>
          </div>
        ) : (
          <button
            type="button"
            className="cockpit-map-toolbar-reveal"
            onClick={() => setIsToolbarCollapsed(false)}
            aria-label="Show project map controls"
            title="Show project map controls"
          >
            <ChevronLeft size={15} />
          </button>
        )}

        {isHudExpanded && (
          <section className="cockpit-project-hud" aria-label="Expanded project details">
            <div>
              <span className="cockpit-kicker">{workspace.project.name}</span>
              <strong>{workspace.project.objective}</strong>
            </div>
            <div className="cockpit-project-hud-stats">
              <span><strong>1</strong> blocking question</span>
              <span><strong>1</strong> approval waiting</span>
              <span><strong>3</strong> established milestones</span>
            </div>
          </section>
        )}

        {isContextOpen && (
          <aside className="cockpit-context-drawer" aria-label="Current system focus">
            <div className="cockpit-context-drawer-header">
              <div>
                <span className="cockpit-kicker">System focus</span>
                <strong>Resolve validity before expanding model search.</strong>
              </div>
              <button type="button" onClick={() => setIsContextOpen(false)} aria-label="Close system focus">
                <X size={15} />
              </button>
            </div>
            <p>The current blocker affects feature eligibility, validation legitimacy and what evidence later model comparisons can support.</p>
            <div className="cockpit-now-actions">
              <button type="button" onClick={() => onFocus('missingness')}>Open active investigation</button>
              <button type="button" onClick={() => onFocus('data')}>Inspect data</button>
            </div>
          </aside>
        )}

        <div className="cockpit-navigation-hint" aria-hidden="true">
          <Move size={13} /> Two-finger move pans · pinch zooms · arrows move · +/- zoom · F fits · Home resets
        </div>
      </div>
    </main>
  )
}

function CockpitNode({
  nodeId,
  className,
  kicker,
  title,
  description,
  status,
  icon,
  onActivate,
}: NodeDefinition & { onActivate?: () => void }) {
  const body = (
    <>
      <span className={`cockpit-node-icon ${status}`}>{icon}</span>
      <span className="cockpit-node-copy">
        <span className="cockpit-node-kicker">{kicker}</span>
        <strong>{title}</strong>
        <small>{description}</small>
      </span>
      {onActivate && <ArrowUpRight className="cockpit-node-open" size={15} />}
    </>
  )

  if (onActivate) {
    return (
      <button
        type="button"
        data-cockpit-node={nodeId}
        className={`cockpit-node ${status} ${className}`}
        onClick={onActivate}
        aria-label={`Open ${title}`}
      >
        {body}
      </button>
    )
  }

  return (
    <article data-cockpit-node={nodeId} tabIndex={-1} className={`cockpit-node ${status} ${className}`}>
      {body}
    </article>
  )
}
