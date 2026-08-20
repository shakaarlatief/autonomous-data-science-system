import { useEffect, useMemo, useState, type FormEvent, type ReactNode } from 'react'
import { Link } from '@tanstack/react-router'
import {
  Activity,
  ArrowLeft,
  ArrowUpRight,
  BarChart3,
  BrainCircuit,
  Check,
  CircleDot,
  Database,
  FlaskConical,
  Gauge,
  MessageSquareText,
  Play,
  Send,
  Sparkles,
  Target,
  TriangleAlert,
  Workflow,
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

  const submitDirection = (message: string) => {
    setLastDirection(message)
  }

  return (
    <div className={`cockpit-shell focus-${focus}`}>
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

        <Link to="/" className="cockpit-project-views-link">
          Project views <ArrowUpRight size={14} />
        </Link>
      </header>

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
  const blocker = workspace.recommendations.find((item) => item.status === 'BLOCKING')
  const missingness = workspace.recommendations.find((item) => item.title.toLowerCase().includes('missing'))

  return (
    <main className="cockpit-stage cockpit-map-stage" aria-labelledby="cockpit-map-title">
      <div className="cockpit-map-intro">
        <div>
          <span className="cockpit-kicker">Project operating map</span>
          <h1 id="cockpit-map-title">{workspace.project.name}</h1>
          <p>{workspace.project.objective}</p>
        </div>
        <div className="cockpit-map-summary">
          <span><strong>1</strong> blocking question</span>
          <span><strong>1</strong> approval waiting</span>
          <span><strong>3</strong> established milestones</span>
        </div>
      </div>

      <section className="project-canvas" aria-label="Living data science project map">
        <div className="stage-zone stage-framing"><span>Framing</span></div>
        <div className="stage-zone stage-exploration"><span>Data & exploration</span></div>
        <div className="stage-zone stage-validation"><span>Validation</span></div>
        <div className="stage-zone stage-modeling"><span>Modeling</span></div>
        <div className="stage-zone stage-evaluation"><span>Evaluation</span></div>

        <svg className="project-connectors" viewBox="0 0 1200 610" aria-hidden="true" preserveAspectRatio="none">
          <path d="M145 210 C220 210 225 170 300 170" />
          <path d="M420 170 C485 170 480 170 545 170" />
          <path d="M360 220 C360 285 360 300 360 350" />
          <path d="M420 390 C500 390 500 295 575 295" />
          <path d="M655 215 C655 245 655 260 655 278" />
          <path d="M735 300 C795 300 805 240 860 240" />
          <path d="M735 330 C800 340 795 415 860 420" />
          <path d="M980 240 C1035 240 1035 320 1085 320" />
          <path className="connector-deferred" d="M980 420 C1035 420 1035 345 1085 345" />
        </svg>

        <CockpitNode
          className="node-objective"
          kicker="Framing"
          title="Objective defined"
          description="Predict customer churn with decisions usable before retention intervention."
          status="complete"
          icon={<Target size={17} />}
        />

        <CockpitNode
          className="node-data"
          kicker="Dataset"
          title="Data understanding"
          description="7,043 rows · 21 source columns · semantic roles mapped"
          status="complete"
          icon={<Database size={17} />}
          onActivate={() => onFocus('data')}
        />

        <CockpitNode
          className="node-prediction"
          kicker="Question"
          title="Resolve prediction moment"
          description={blocker?.summary ?? 'Feature eligibility cannot be finalized until the prediction moment is explicit.'}
          status="blocked"
          icon={<TriangleAlert size={17} />}
        />

        <CockpitNode
          className="node-missingness"
          kicker="Investigation"
          title="Production missingness"
          description={missingness?.summary ?? 'Support-ticket completeness needs production-time investigation.'}
          status="attention"
          icon={<FlaskConical size={17} />}
          onActivate={() => onFocus('missingness')}
        />

        <CockpitNode
          className="node-eda"
          kicker="Exploration"
          title="EDA evidence"
          description="Distribution and cohort signals are available for focused inspection."
          status="ready"
          icon={<BarChart3 size={17} />}
          onActivate={() => onFocus('eda')}
        />

        <CockpitNode
          className="node-validation"
          kicker="Decision"
          title="Chronological validation"
          description="Temporal ordering selected as the current validation design."
          status="selected"
          icon={<Check size={17} />}
        />

        <CockpitNode
          className="node-baseline"
          kicker="Modeling"
          title="Logistic baseline"
          description="Reference model completed and available for comparison."
          status="complete"
          icon={<Play size={17} />}
        />

        <CockpitNode
          className="node-rf"
          kicker="Modeling"
          title="Random Forest benchmark"
          description="Deferred until prediction-time feature eligibility is resolved."
          status="deferred"
          icon={<BrainCircuit size={17} />}
        />

        <CockpitNode
          className="node-evaluation"
          kicker="Downstream"
          title="Evaluation & calibration"
          description="Waiting on the active validation and modeling path."
          status="future"
          icon={<Gauge size={17} />}
        />

        <aside className="cockpit-now-card" aria-label="Current system focus">
          <span className="cockpit-kicker">System focus</span>
          <strong>Resolve validity before expanding model search.</strong>
          <p>The current blocker affects feature eligibility, validation legitimacy and what evidence later model comparisons can support.</p>
          <div className="cockpit-now-actions">
            <button type="button" onClick={() => onFocus('missingness')}>Open active investigation</button>
            <button type="button" onClick={() => onFocus('data')}>Inspect data</button>
          </div>
        </aside>
      </section>
    </main>
  )
}

function CockpitNode({
  className,
  kicker,
  title,
  description,
  status,
  icon,
  onActivate,
}: {
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
      <button type="button" className={`cockpit-node ${status} ${className}`} onClick={onActivate} aria-label={`Open ${title}`}>
        {body}
      </button>
    )
  }

  return <article className={`cockpit-node ${status} ${className}`}>{body}</article>
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
