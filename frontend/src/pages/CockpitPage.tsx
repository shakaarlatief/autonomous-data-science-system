import { useEffect, useRef, useState, type FormEvent } from 'react'
import { Link } from '@tanstack/react-router'
import {
  Activity,
  ArrowLeft,
  ArrowUpRight,
  BrainCircuit,
  ChevronDown,
  ChevronUp,
  CircleDot,
  Maximize2,
  Minimize2,
  Send,
  Sparkles,
  Workflow,
} from 'lucide-react'
import { useWorkspace } from '../appState'
import { CockpitProjectMap } from '../components/CockpitProjectMap'
import { MissingnessWorkspace } from '../components/MissingnessWorkspace'
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
  const [isHudCollapsed, setIsHudCollapsed] = useState(false)
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

  return (
    <div
      ref={shellRef}
      className={`cockpit-shell focus-${focus}${isFullscreen ? ' is-fullscreen' : ''}${isHudCollapsed ? ' hud-collapsed' : ''}`}
    >
      {!isHudCollapsed ? (
        <header className="cockpit-topbar" aria-label="Cockpit HUD">
          <div className="cockpit-brand-cluster">
            <div className="cockpit-brand-mark" aria-hidden="true">A</div>
            <div className="cockpit-brand-copy">
              <span className="cockpit-product-name">ADS</span>
              <span className="cockpit-brand-separator" aria-hidden="true">·</span>
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
              onClick={() => setIsHudCollapsed(true)}
              aria-label="Hide Cockpit HUD"
              title="Hide Cockpit HUD"
            >
              <ChevronUp size={15} />
            </button>
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
      ) : (
        <button
          type="button"
          className="cockpit-hud-reveal"
          onClick={() => setIsHudCollapsed(false)}
          aria-label="Show Cockpit HUD"
          title="Show Cockpit HUD"
        >
          <ChevronDown size={15} />
        </button>
      )}

      {fullscreenMessage && (
        <div className="cockpit-fullscreen-message" role="status">
          {fullscreenMessage}
        </div>
      )}

      {focus === 'map' ? (
        <CockpitProjectMap onFocus={transitionTo} />
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

      <CockpitComposer focus={focus} lastDirection={lastDirection} onSubmit={setLastDirection} />
    </div>
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
