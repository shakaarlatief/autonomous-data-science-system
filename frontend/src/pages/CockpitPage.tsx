import {
  useEffect,
  useMemo,
  useRef,
  useState,
  type FormEvent,
  type KeyboardEvent as ReactKeyboardEvent,
  type ReactNode,
} from 'react'
import { Link } from '@tanstack/react-router'
import {
  Activity,
  ArrowLeft,
  ArrowUpRight,
  BarChart3,
  BrainCircuit,
  Check,
  ChevronDown,
  ChevronUp,
  CircleDot,
  Crosshair,
  Database,
  FlaskConical,
  Gauge,
  Maximize2,
  MessageSquareText,
  Minimize2,
  Move,
  PanelRightOpen,
  Play,
  RotateCcw,
  Send,
  Sparkles,
  Target,
  TriangleAlert,
  Workflow,
  X,
} from 'lucide-react'
import { useWorkspace } from '../appState'
import { DataPage } from './DataPage'
import { EdaPage } from './EdaPage'

export type CockpitFocus = 'map' | 'data' | 'eda' | 'missingness'

type CockpitPageProps = {
  focus: CockpitFocus
  selectedColumn: string
  filter: string
  selectedView: 'distribution' | 'trend'
  onFocusChange: (focus: CockpitFocus) => void | Promise<void>
  onSelectColumn: (column: string) => void | Promise<void>
  onSearchChange: (filter: string) => void | Promise<void>
  onViewChange: (view: 'distribution' | 'trend') => void | Promise<void>
}

export function CockpitPage({
  focus,
  selectedColumn,
  filter,
  selectedView,
  onFocusChange,
  onSelectColumn,
  onSearchChange,
  onViewChange,
}: CockpitPageProps) {
  const { workspace, runs } = useWorkspace()
  const [lastDirection, setLastDirection] = useState<string | null>(null)
  const [isFullscreen, setIsFullscreen] = useState(false)
  const [fullscreenMessage, setFullscreenMessage] = useState<string | null>(null)
  const shellRef = useRef<HTMLDivElement>(null)

  const activeRuns = runs.filter((run) => run.status === 'RUNNING').length
  const approvals = runs.filter((run) => run.status === 'WAITING_FOR_APPROVAL').length

  const transitionTo = (nextFocus: CockpitFocus) => {
    const apply = () => Promise.resolve(onFocusChange(nextFocus))
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const transitionDocument = document as Document & {
      startViewTransition?: (callback: () => void | Promise<void>) => unknown
    }

    if (!reducedMotion && transitionDocument.startViewTransition) {
      transitionDocument.startViewTransition(apply)
      return
    }

    void apply()
  }

  useEffect(() => {
    if (focus === 'map') return undefined
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') transitionTo('map')
    }
    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [focus])

  useEffect(() => {
    const syncFullscreenState = () => {
      setIsFullscreen(document.fullscreenElement === shellRef.current)
    }

    document.addEventListener('fullscreenchange', syncFullscreenState)
    syncFullscreenState()
    return () => document.removeEventListener('fullscreenchange', syncFullscreenState)
  }, [])

  const toggleFullscreen = async () => {
    setFullscreenMessage(null)

    try {
      if (document.fullscreenElement) {
        await document.exitFullscreen()
        return
      }

      if (!shellRef.current?.requestFullscreen || document.fullscreenEnabled === false) {
        setFullscreenMessage('Browser fullscreen is unavailable. The immersive Cockpit remains active.')
        return
      }

      await shellRef.current.requestFullscreen()
    } catch {
      setFullscreenMessage('Browser fullscreen was not granted. The immersive Cockpit remains active.')
    }
  }

  const submitDirection = (message: string) => {
    setLastDirection(message)
  }

  return (
    <div ref={shellRef} className={`cockpit-shell focus-${focus}${isFullscreen ? ' is-fullscreen' : ''}`}>
      <header className="cockpit-topbar">
        <div className="cockpit-brand-cluster">
          <div className="cockpit-brand-mark" aria-hidden="true">A</div>
          <div>
            <span className="cockpit-product-name">ADS</span>
            <span className="cockpit-project-name">{workspace.project.name}</span>
          </div>
        </div>

        <div className="cockpit-status-cluster" aria-label="Project execution status">
          <span className="cockpit-status"><Activity size={14} /> {activeRuns} running</span>
          {approvals > 0 && <span className="cockpit-status attention"><CircleDot size={13} /> {approvals} approval</span>}
          <span className="cockpit-status stage"><Workflow size={14} /> {workspace.project.stage}</span>
        </div>

        <div className="cockpit-topbar-actions">
          <button
            type="button"
            className="cockpit-icon-action"
            onClick={() => void toggleFullscreen()}
            aria-label={isFullscreen ? 'Exit fullscreen' : 'Enter fullscreen'}
            title={isFullscreen ? 'Exit fullscreen' : 'Enter fullscreen'}
          >
            {isFullscreen ? <Minimize2 size={15} /> : <Maximize2 size={15} />}
          </button>
          <Link to="/" className="cockpit-project-views-link">
            Project views <ArrowUpRight size={14} />
          </Link>
        </div>
      </header>

      {fullscreenMessage && (
        <div className="cockpit-fullscreen-message" role="status">
          {fullscreenMessage}
        </div>
      )}

      {focus === 'map' ? (
        <ProjectMap onFocus={transitionTo} />
      ) : (
        <FocusHost
          focus={focus}
          selectedColumn={selectedColumn}
          filter={filter}
          selectedView={selectedView}
          onBack={() => transitionTo('map')}
          onOpenData={() => transitionTo('data')}
          onSelectColumn={onSelectColumn}
          onSearchChange={onSearchChange}
          onViewChange={onViewChange}
        />
      )}

      <CockpitComposer focus={focus} lastDirection={lastDirection} onSubmit={submitDirection} />
    </div>
  )
}

function ProjectMap({ onFocus }: { onFocus: (focus: CockpitFocus) => void }) {
  const { workspace } = useWorkspace()
  const viewportRef = useRef<HTMLElement>(null)
  const [isHudExpanded, setIsHudExpanded] = useState(false)
  const [isContextOpen, setIsContextOpen] = useState(false)
  const blocker = workspace.recommendations.find((item) => item.status === 'BLOCKING')
  const missingness = workspace.recommendations.find((item) => item.title.toLowerCase().includes('missing'))

  const scrollBehavior = (): ScrollBehavior =>
    window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'

  const resetViewport = () => {
    viewportRef.current?.scrollTo({ left: 0, top: 0, behavior: scrollBehavior() })
    viewportRef.current?.focus({ preventScroll: true })
  }

  const jumpToNode = (nodeId: string) => {
    const viewport = viewportRef.current
    const node = viewport?.querySelector<HTMLElement>(`[data-cockpit-node="${nodeId}"]`)
    if (!node) return

    node.scrollIntoView({ behavior: scrollBehavior(), block: 'center', inline: 'center' })
    window.requestAnimationFrame(() => node.focus({ preventScroll: true }))
  }

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
    }
  }

  return (
    <main className="cockpit-stage cockpit-map-stage" aria-labelledby="cockpit-map-title">
      <div className="cockpit-map-control-row">
        <div className="cockpit-map-identity">
          <span className="cockpit-kicker">Project operating map</span>
          <h1 id="cockpit-map-title">{workspace.project.name}</h1>
        </div>

        <div className="cockpit-map-controls" aria-label="Project map controls">
          <button type="button" onClick={() => setIsHudExpanded((value) => !value)} aria-expanded={isHudExpanded}>
            {isHudExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
            {isHudExpanded ? 'Hide project details' : 'Show project details'}
          </button>
          <button type="button" onClick={resetViewport} aria-label="Reset project view">
            <RotateCcw size={14} /> Reset
          </button>
          <button type="button" onClick={() => jumpToNode('prediction')}>
            <Crosshair size={14} /> Jump to blocker
          </button>
          <button type="button" onClick={() => jumpToNode('evaluation')}>
            <Crosshair size={14} /> Jump to evaluation
          </button>
          <button type="button" onClick={() => setIsContextOpen((value) => !value)} aria-expanded={isContextOpen}>
            <PanelRightOpen size={14} /> System focus
          </button>
        </div>
      </div>

      {isHudExpanded && (
        <section className="cockpit-project-hud" aria-label="Expanded project details">
          <div>
            <span className="cockpit-kicker">Objective</span>
            <strong>{workspace.project.objective}</strong>
          </div>
          <div className="cockpit-project-hud-stats">
            <span><strong>1</strong> blocking question</span>
            <span><strong>1</strong> approval waiting</span>
            <span><strong>3</strong> established milestones</span>
          </div>
        </section>
      )}

      <div className={`cockpit-map-layout${isContextOpen ? ' context-open' : ''}`}>
        <section
          ref={viewportRef}
          className="project-viewport"
          aria-label="Living data science project map"
          aria-description="Two-dimensional project space. Use scrolling or trackpad movement, arrow keys to pan, Home to reset, or the jump controls above."
          aria-keyshortcuts="ArrowLeft ArrowRight ArrowUp ArrowDown Home"
          tabIndex={0}
          onKeyDown={handleViewportKeyDown}
        >
          <div className="project-canvas">
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

            <svg className="project-connectors" viewBox="0 0 1960 980" aria-hidden="true" preserveAspectRatio="none">
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
      </div>

      <div className="cockpit-navigation-hint" aria-hidden="true">
        <Move size={13} /> Pan with scroll or trackpad · Arrow keys move · Shift + Arrow moves farther · Home resets
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

function FocusHost({
  focus,
  selectedColumn,
  filter,
  selectedView,
  onBack,
  onOpenData,
  onSelectColumn,
  onSearchChange,
  onViewChange,
}: {
  focus: Exclude<CockpitFocus, 'map'>
  selectedColumn: string
  filter: string
  selectedView: 'distribution' | 'trend'
  onBack: () => void
  onOpenData: () => void
  onSelectColumn: (column: string) => void | Promise<void>
  onSearchChange: (filter: string) => void | Promise<void>
  onViewChange: (view: 'distribution' | 'trend') => void | Promise<void>
}) {
  const focusMeta = {
    data: ['Data & exploration', 'Data understanding'],
    eda: ['Data & exploration', 'EDA evidence'],
    missingness: ['Data & exploration', 'Production missingness'],
  }[focus]

  return (
    <main className="cockpit-stage cockpit-focus-stage" aria-label={`${focusMeta[1]} focused workspace`}>
      <header className="cockpit-focus-header">
        <button type="button" className="cockpit-back-button" onClick={onBack} aria-label="Return to project map">
          <ArrowLeft size={17} /> Project map
        </button>
        <div className="cockpit-focus-breadcrumb">
          <span>{focusMeta[0]}</span>
          <span>/</span>
          <strong>{focusMeta[1]}</strong>
        </div>
        <span className="cockpit-focus-hint">Esc to zoom out</span>
      </header>

      <div className="cockpit-focus-content">
        {focus === 'data' && (
          <DataPage
            selectedColumn={selectedColumn}
            filter={filter}
            onSelectColumn={(column) => void onSelectColumn(column)}
            onSearchChange={(value) => void onSearchChange(value)}
          />
        )}
        {focus === 'eda' && (
          <EdaPage
            selectedView={selectedView}
            onViewChange={(view) => void onViewChange(view === 'trend' ? 'trend' : 'distribution')}
          />
        )}
        {focus === 'missingness' && <MissingnessWorkspace onOpenData={onOpenData} onSelectColumn={onSelectColumn} />}
      </div>
    </main>
  )
}

function MissingnessWorkspace({
  onOpenData,
  onSelectColumn,
}: {
  onOpenData: () => void
  onSelectColumn: (column: string) => void | Promise<void>
}) {
  const { workspace } = useWorkspace()
  const supportTickets = workspace.variables.find((variable) => variable.name === 'support_tickets')
  const missingRows = workspace.rows.filter((row) => row.supportTickets === null)

  const contractStats = useMemo(() => {
    const groups = new Map<string, { total: number; missing: number }>()
    workspace.rows.forEach((row) => {
      const current = groups.get(row.contract) ?? { total: 0, missing: 0 }
      current.total += 1
      if (row.supportTickets === null) current.missing += 1
      groups.set(row.contract, current)
    })
    return Array.from(groups.entries()).map(([label, value]) => ({
      label,
      percent: value.total ? Math.round((value.missing / value.total) * 100) : 0,
      missing: value.missing,
      total: value.total,
    }))
  }, [workspace.rows])

  const openSupportTickets = async () => {
    await Promise.resolve(onSelectColumn('support_tickets'))
    onOpenData()
  }

  return (
    <div className="missingness-workspace">
      <header className="missingness-hero">
        <div>
          <span className="cockpit-kicker">Focused investigation</span>
          <h1>Production missingness investigation</h1>
          <p>Determine whether support-ticket data is complete enough, and available early enough, to support defensible production features.</p>
        </div>
        <div className="missingness-hero-stats">
          <div><strong>{supportTickets?.missingPercent ?? 6.8}%</strong><span>stored missing</span></div>
          <div><strong>{missingRows.length}</strong><span>missing in preview</span></div>
          <div><strong>1</strong><span>linked blocker</span></div>
        </div>
      </header>

      <section className="missingness-grid">
        <article className="cockpit-focus-panel missingness-pattern-panel">
          <div className="cockpit-panel-heading">
            <div><span className="cockpit-kicker">Representative preview</span><h2>Missingness by contract</h2></div>
            <Database size={18} />
          </div>
          <div className="missingness-bars">
            {contractStats.map((item) => (
              <div className="missingness-bar-row" key={item.label}>
                <div><strong>{item.label}</strong><span>{item.missing}/{item.total} preview rows</span></div>
                <div className="missingness-bar-track"><span style={{ width: `${Math.max(item.percent, item.missing ? 8 : 0)}%` }} /></div>
                <strong>{item.percent}%</strong>
              </div>
            ))}
          </div>
          <p className="cockpit-panel-note">This preview is intentionally not treated as production evidence. The real investigation must query production-time completeness by target/cohort and prediction moment.</p>
        </article>

        <aside className="cockpit-focus-panel missingness-method-panel">
          <div className="cockpit-panel-heading">
            <div><span className="cockpit-kicker">Methodological context</span><h2>Why this work matters</h2></div>
            <BrainCircuit size={18} />
          </div>
          <div className="method-context-item blocking">
            <TriangleAlert size={16} />
            <div><strong>Prediction moment unresolved</strong><p>Availability cannot be assessed without an explicit prediction time.</p></div>
          </div>
          <div className="method-context-item recommended">
            <Sparkles size={16} />
            <div><strong>Compare production missingness</strong><p>Stratify completeness by target, signup cohort and the eventual prediction-time boundary.</p></div>
          </div>
          <div className="method-context-item evidence">
            <Check size={16} />
            <div><strong>Expected output</strong><p>Evidence and Finding candidates that can constrain feature eligibility.</p></div>
          </div>
        </aside>

        <article className="cockpit-focus-panel missingness-rows-panel">
          <div className="cockpit-panel-heading">
            <div><span className="cockpit-kicker">Evidence inspection</span><h2>Rows with missing support tickets</h2></div>
            <button type="button" className="cockpit-inline-action" onClick={() => void openSupportTickets()}>
              Open full Data workspace <ArrowUpRight size={14} />
            </button>
          </div>
          <div className="missingness-table-scroll">
            <table className="missingness-table">
              <thead><tr><th>Customer</th><th>Tenure</th><th>Contract</th><th>Signup</th><th>Churn</th><th>Support tickets</th></tr></thead>
              <tbody>
                {missingRows.map((row) => (
                  <tr key={row.customerId}>
                    <td>{row.customerId}</td><td>{row.tenureMonths} mo</td><td>{row.contract}</td><td>{row.signupDate}</td><td>{row.churn}</td><td><span className="missing-value">missing</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </article>

        <article className="cockpit-focus-panel missingness-next-panel">
          <span className="cockpit-kicker">System proposal</span>
          <h2>Next evidence-producing step</h2>
          <p>Once the prediction moment is explicit, compare support-ticket completeness at that cutoff across churn outcome and signup cohorts. Persist resulting evidence before deciding whether derived support features are admissible.</p>
          <div className="missingness-next-actions">
            <button type="button" className="cockpit-primary-action"><Play size={14} /> Prepare investigation</button>
            <button type="button" className="cockpit-secondary-action"><MessageSquareText size={14} /> Ask why</button>
          </div>
        </article>
      </section>
    </div>
  )
}

function CockpitComposer({
  focus,
  lastDirection,
  onSubmit,
}: {
  focus: CockpitFocus
  lastDirection: string | null
  onSubmit: (message: string) => void
}) {
  const [message, setMessage] = useState('')

  const submit = (event: FormEvent) => {
    event.preventDefault()
    const trimmed = message.trim()
    if (!trimmed) return
    onSubmit(trimmed)
    setMessage('')
  }

  return (
    <div className="cockpit-composer-wrap">
      {lastDirection && (
        <div className="cockpit-prototype-response" role="status">
          <Sparkles size={13} /> Prototype direction captured: “{lastDirection}”
        </div>
      )}
      <form className="cockpit-composer" onSubmit={submit}>
        <span className="cockpit-composer-context">
          <BrainCircuit size={17} />
          {focus === 'map' ? 'Project context' : `${focusLabel(focus)} context`}
        </span>
        <input
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          placeholder={focus === 'map' ? 'Ask or direct the system across this project…' : `Ask or direct the system about ${focusLabel(focus).toLowerCase()}…`}
          aria-label="Ask or direct the system"
        />
        <button type="submit" aria-label="Send direction"><Send size={16} /></button>
      </form>
    </div>
  )
}

function focusLabel(focus: CockpitFocus): string {
  if (focus === 'data') return 'Data'
  if (focus === 'eda') return 'EDA'
  if (focus === 'missingness') return 'Missingness investigation'
  return 'Project'
}
