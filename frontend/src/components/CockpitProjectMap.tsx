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

type JumpTarget = {
  nodeId: string
  label: string
  category: string
}

const CANVAS_WIDTH = 2260
const CANVAS_HEIGHT = 1180
const MIN_ZOOM = 0.45
const MAX_ZOOM = 1.6
const ZOOM_STEP = 0.1

const clampZoom = (value: number) => Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, value))

export function CockpitProjectMap({ onFocus }: ProjectMapProps) {
  const { workspace } = useWorkspace()
  const viewportRef = useRef<HTMLElement>(null)
  const [isHudExpanded, setIsHudExpanded] = useState(false)
  const [isContextOpen, setIsContextOpen] = useState(false)
  const [isJumpOpen, setIsJumpOpen] = useState(false)
  const [jumpQuery, setJumpQuery] = useState('')
  const [zoom, setZoom] = useState(1)

  const blocker = workspace.recommendations.find((item) => item.status === 'BLOCKING')
  const missingness = workspace.recommendations.find((item) => item.title.toLowerCase().includes('missing'))

  const jumpTargets = useMemo<JumpTarget[]>(() => [
    { nodeId: 'objective', label: 'Objective defined', category: 'Framing' },
    { nodeId: 'data', label: 'Data understanding', category: 'Dataset' },
    { nodeId: 'prediction', label: 'Resolve prediction moment', category: 'Blocker' },
    { nodeId: 'missingness', label: 'Production missingness', category: 'Investigation' },
    { nodeId: 'eda', label: 'EDA evidence', category: 'Exploration' },
    { nodeId: 'validation', label: 'Chronological validation', category: 'Decision' },
    { nodeId: 'baseline', label: 'Logistic baseline', category: 'Modeling' },
    { nodeId: 'rf', label: 'Random Forest benchmark', category: 'Modeling' },
    { nodeId: 'evaluation', label: 'Evaluation & calibration', category: 'Evaluation' },
    { nodeId: 'review', label: 'Subgroup review', category: 'Evaluation' },
  ], [])

  const filteredJumpTargets = useMemo(() => {
    const query = jumpQuery.trim().toLowerCase()
    if (!query) return jumpTargets
    return jumpTargets.filter((target) =>
      `${target.label} ${target.category}`.toLowerCase().includes(query),
    )
  }, [jumpQuery, jumpTargets])

  const scrollBehavior = (): ScrollBehavior =>
    window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'

  const zoomAround = (nextZoom: number, anchorX?: number, anchorY?: number) => {
    const viewport = viewportRef.current
    if (!viewport) return

    const boundedZoom = clampZoom(nextZoom)
    if (Math.abs(boundedZoom - zoom) < 0.001) return

    const x = anchorX ?? viewport.clientWidth / 2
    const y = anchorY ?? viewport.clientHeight / 2
    const worldX = (viewport.scrollLeft + x) / zoom
    const worldY = (viewport.scrollTop + y) / zoom

    setZoom(boundedZoom)
    window.requestAnimationFrame(() => {
      viewport.scrollTo({
        left: Math.max(0, worldX * boundedZoom - x),
        top: Math.max(0, worldY * boundedZoom - y),
        behavior: 'auto',
      })
    })
  }

  const resetViewport = () => {
    setZoom(1)
    window.requestAnimationFrame(() => {
      viewportRef.current?.scrollTo({ left: 0, top: 0, behavior: scrollBehavior() })
      viewportRef.current?.focus({ preventScroll: true })
    })
  }

  const fitProject = () => {
    const viewport = viewportRef.current
    if (!viewport) return

    const horizontalFit = (viewport.clientWidth - 24) / CANVAS_WIDTH
    const verticalFit = (viewport.clientHeight - 24) / CANVAS_HEIGHT
    const nextZoom = clampZoom(Math.min(horizontalFit, verticalFit, 1))
    setZoom(nextZoom)
    window.requestAnimationFrame(() => {
      viewport.scrollTo({ left: 0, top: 0, behavior: scrollBehavior() })
      viewport.focus({ preventScroll: true })
    })
  }

  const jumpToNode = (nodeId: string) => {
    const viewport = viewportRef.current
    const node = viewport?.querySelector<HTMLElement>(`[data-cockpit-node="${nodeId}"]`)
    if (!node) return

    node.scrollIntoView({ behavior: scrollBehavior(), block: 'center', inline: 'center' })
    window.requestAnimationFrame(() => node.focus({ preventScroll: true }))
    setIsJumpOpen(false)
    setJumpQuery('')
  }

  useEffect(() => {
    const viewport = viewportRef.current
    if (!viewport) return undefined

    const handlePinchZoom = (event: WheelEvent) => {
      if (!event.ctrlKey) return
      event.preventDefault()
      const rect = viewport.getBoundingClientRect()
      const factor = Math.exp(-event.deltaY * 0.004)
      zoomAround(zoom * factor, event.clientX - rect.left, event.clientY - rect.top)
    }

    viewport.addEventListener('wheel', handlePinchZoom, { passive: false })
    return () => viewport.removeEventListener('wheel', handlePinchZoom)
  }, [zoom])

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
      zoomAround(zoom + ZOOM_STEP)
      return
    }

    if (event.key === '-') {
      event.preventDefault()
      zoomAround(zoom - ZOOM_STEP)
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

  const canvasStyle = { zoom } as CSSProperties
  const zoomPercent = Math.round(zoom * 100)

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
          aria-description="Two-dimensional project space. Two-finger trackpad movement pans. Trackpad pinch zooms. Arrow keys pan, plus and minus zoom, F fits the project, and Home resets."
          aria-keyshortcuts="ArrowLeft ArrowRight ArrowUp ArrowDown Home + - 0 F"
          tabIndex={0}
          onKeyDown={handleViewportKeyDown}
        >
          <div className="project-canvas" style={canvasStyle}>
            <nav className="cockpit-stage-strip" aria-label="Project stages">
              <button type="button" onClick={() => jumpToNode('objective')}>Framing</button>
              <button type="button" onClick={() => jumpToNode('data')}>Data & exploration</button>
              <button type="button" onClick={() => jumpToNode('validation')}>Validation</button>
              <button type="button" onClick={() => jumpToNode('baseline')}>Modeling</button>
              <button type="button" onClick={() => jumpToNode('evaluation')}>Evaluation</button>
            </nav>

            <div className="stage-zone stage-framing" aria-hidden="true" />
            <div className="stage-zone stage-exploration" aria-hidden="true" />
            <div className="stage-zone stage-validation" aria-hidden="true" />
            <div className="stage-zone stage-modeling" aria-hidden="true" />
            <div className="stage-zone stage-evaluation" aria-hidden="true" />

            <svg className="project-connectors" viewBox={`0 0 ${CANVAS_WIDTH} ${CANVAS_HEIGHT}`} aria-hidden="true" preserveAspectRatio="none">
              <path d="M250 205 C300 205 300 175 350 175" />
              <path d="M550 175 C680 175 690 170 830 170" />
              <path d="M450 225 C450 305 470 340 480 430" />
              <path d="M520 520 C650 520 700 420 880 420" />
              <path d="M930 225 C930 280 945 315 960 360" />
              <path d="M1080 420 C1160 420 1175 315 1260 315" />
              <path d="M1080 455 C1170 480 1180 625 1260 625" />
              <path d="M1460 315 C1540 315 1540 480 1600 480" />
              <path className="connector-deferred" d="M1460 625 C1540 625 1540 510 1600 510" />
              <path d="M520 760 C820 760 1120 780 1600 780" />
            </svg>

            <CockpitNode
              nodeId="objective"
              className="node-objective"
              kicker="Framing"
              title="Objective defined"
              description="Predict customer churn with decisions usable before retention intervention."
              status="complete"
              icon={<Target size={17} />}
            />

            <CockpitNode
              nodeId="data"
              className="node-data"
              kicker="Dataset"
              title="Data understanding"
              description="7,043 rows · 21 source columns · semantic roles mapped"
              status="complete"
              icon={<Database size={17} />}
              onActivate={() => onFocus('data')}
            />

            <CockpitNode
              nodeId="prediction"
              className="node-prediction"
              kicker="Question"
              title="Resolve prediction moment"
              description={blocker?.summary ?? 'Feature eligibility cannot be finalized until the prediction moment is explicit.'}
              status="blocked"
              icon={<TriangleAlert size={17} />}
            />

            <CockpitNode
              nodeId="missingness"
              className="node-missingness"
              kicker="Investigation"
              title="Production missingness"
              description={missingness?.summary ?? 'Support-ticket completeness needs production-time investigation.'}
              status="attention"
              icon={<FlaskConical size={17} />}
              onActivate={() => onFocus('missingness')}
            />

            <CockpitNode
              nodeId="eda"
              className="node-eda"
              kicker="Exploration"
              title="EDA evidence"
              description="Distribution and cohort signals are available for focused inspection."
              status="ready"
              icon={<BarChart3 size={17} />}
              onActivate={() => onFocus('eda')}
            />

            <CockpitNode
              nodeId="validation"
              className="node-validation"
              kicker="Decision"
              title="Chronological validation"
              description="Temporal ordering selected as the current validation design."
              status="selected"
              icon={<Check size={17} />}
            />

            <CockpitNode
              nodeId="baseline"
              className="node-baseline"
              kicker="Modeling"
              title="Logistic baseline"
              description="Reference model completed and available for comparison."
              status="complete"
              icon={<Play size={17} />}
            />

            <CockpitNode
              nodeId="rf"
              className="node-rf"
              kicker="Modeling"
              title="Random Forest benchmark"
              description="Deferred until prediction-time feature eligibility is resolved."
              status="deferred"
              icon={<BrainCircuit size={17} />}
            />

            <CockpitNode
              nodeId="evaluation"
              className="node-evaluation"
              kicker="Downstream"
              title="Evaluation & calibration"
              description="Waiting on the active validation and modeling path."
              status="future"
              icon={<Gauge size={17} />}
            />

            <CockpitNode
              nodeId="review"
              className="node-review"
              kicker="Evaluation"
              title="Subgroup review"
              description="Reserved downstream work demonstrates lower project-space growth without promoting a final stage taxonomy."
              status="future"
              icon={<BarChart3 size={17} />}
            />
          </div>
        </section>

        <div className="cockpit-map-toolbar" aria-label="Project map controls">
          <button
            type="button"
            className="cockpit-toolbar-labelled"
            onClick={() => setIsHudExpanded((value) => !value)}
            aria-expanded={isHudExpanded}
          >
            {isHudExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
            Details
          </button>

          <div className="cockpit-zoom-controls" aria-label="Project map zoom controls">
            <button type="button" onClick={() => zoomAround(zoom - ZOOM_STEP)} aria-label="Zoom out project map" title="Zoom out">
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
            <button type="button" onClick={() => zoomAround(zoom + ZOOM_STEP)} aria-label="Zoom in project map" title="Zoom in">
              <ZoomIn size={14} />
            </button>
          </div>

          <button type="button" onClick={fitProject} aria-label="Fit project to viewport" title="Fit project">
            <LocateFixed size={14} />
          </button>
          <button type="button" onClick={resetViewport} aria-label="Reset project view" title="Reset pan and zoom">
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
                  {filteredJumpTargets.map((target) => (
                    <button type="button" key={`${target.nodeId}-${target.category}`} onClick={() => jumpToNode(target.nodeId)}>
                      <span>{target.label}</span>
                      <small>{target.category}</small>
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
          >
            <PanelRightOpen size={14} /> System focus
          </button>
        </div>

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
}: {
  nodeId: string
  className: string
  kicker: string
  title: string
  description: string
  status: 'complete' | 'blocked' | 'attention' | 'ready' | 'selected' | 'deferred' | 'future'
  icon: ReactNode
  onActivate?: () => void
}) {
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
