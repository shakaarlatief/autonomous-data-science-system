import { useEffect, useState } from 'react'
import { Link, Outlet, useRouterState } from '@tanstack/react-router'
import {
  Activity,
  BarChart3,
  Boxes,
  BrainCircuit,
  ChevronRight,
  CircleDot,
  ClipboardCheck,
  Database,
  FileText,
  FlaskConical,
  Gauge,
  GitBranch,
  History,
  Home,
  Layers3,
  Moon,
  Search,
  Settings2,
  ShieldCheck,
  Sun,
} from 'lucide-react'
import { useWorkspace } from '../appState'
import { MethodologyPanel } from './MethodologyPanel'

const primaryNavigation = [
  { to: '/', label: 'Overview', icon: Home, enabled: true },
  { to: '/data', label: 'Data', icon: Database, enabled: true },
  { to: '/eda', label: 'EDA', icon: BarChart3, enabled: true },
  { to: '/history', label: 'Decisions & History', icon: History, enabled: true },
]

const futureNavigation = [
  ['Validation', ShieldCheck],
  ['Features', Layers3],
  ['Models', BrainCircuit],
  ['Experiments', FlaskConical],
  ['Evaluation', Gauge],
  ['Report', FileText],
] as const

export function AppShell() {
  const { workspace, runs } = useWorkspace()
  const pathname = useRouterState({ select: (state) => state.location.pathname })
  const [theme, setTheme] = useState<'light' | 'dark'>(() => {
    const stored = localStorage.getItem('ads-theme')
    if (stored === 'light' || stored === 'dark') return stored
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  })

  useEffect(() => {
    document.documentElement.dataset.theme = theme
    localStorage.setItem('ads-theme', theme)
  }, [theme])

  const activeRunCount = runs.filter((run) => run.status === 'RUNNING').length
  const approvalCount = runs.filter((run) => run.status === 'WAITING_FOR_APPROVAL').length

  return (
    <div className="app-shell">
      <aside className="sidebar" aria-label="Project navigation">
        <div className="brand-block">
          <div className="brand-mark" aria-hidden="true">A</div>
          <div>
            <div className="brand-name">ADS</div>
            <div className="brand-caption">Autonomous Data Science</div>
          </div>
        </div>

        <button className="project-switcher" type="button" aria-label="Current project">
          <div className="project-switcher-icon"><Boxes size={16} /></div>
          <div className="project-switcher-copy">
            <span className="eyebrow">Project</span>
            <strong>{workspace.project.name}</strong>
          </div>
          <ChevronRight size={15} />
        </button>

        <nav className="nav-section" aria-label="Workspace">
          <span className="nav-heading">Workspace</span>
          {primaryNavigation.map(({ to, label, icon: Icon }) => {
            const active = to === '/' ? pathname === '/' : pathname.startsWith(to)
            return (
              <Link key={to} to={to} className={`nav-item ${active ? 'active' : ''}`}>
                <Icon size={17} strokeWidth={1.8} />
                <span>{label}</span>
              </Link>
            )
          })}
        </nav>

        <nav className="nav-section future-section" aria-label="Planned workspace sections">
          <span className="nav-heading">Later in V1</span>
          {futureNavigation.map(([label, Icon]) => (
            <div key={label} className="nav-item disabled" aria-disabled="true">
              <Icon size={17} strokeWidth={1.7} />
              <span>{label}</span>
              <span className="nav-soon">soon</span>
            </div>
          ))}
        </nav>

        <div className="sidebar-footer">
          <div className="system-health">
            <span className="health-dot" aria-hidden="true" />
            <span>Local workspace healthy</span>
          </div>
          <button className="icon-text-button" type="button">
            <Settings2 size={16} /> Settings
          </button>
        </div>
      </aside>

      <div className="workspace-column">
        <header className="topbar">
          <div className="breadcrumbs" aria-label="Breadcrumb">
            <span>{workspace.project.name}</span>
            <ChevronRight size={14} />
            <strong>{sectionName(pathname)}</strong>
          </div>
          <div className="topbar-actions">
            <button className="search-control" type="button" aria-label="Search project">
              <Search size={16} />
              <span>Search project</span>
              <kbd>⌘ K</kbd>
            </button>
            <div className="run-indicators" aria-label="Execution status">
              <span className="status-inline"><Activity size={15} /> {activeRunCount} running</span>
              {approvalCount > 0 && <span className="status-inline attention"><CircleDot size={14} /> {approvalCount} approval</span>}
            </div>
            <button
              className="icon-button"
              type="button"
              aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`}
              onClick={() => setTheme((value) => (value === 'dark' ? 'light' : 'dark'))}
            >
              {theme === 'dark' ? <Sun size={17} /> : <Moon size={17} />}
            </button>
          </div>
        </header>

        <div className="main-grid">
          <main className="content-area" id="main-content">
            <Outlet />
          </main>
          <MethodologyPanel />
        </div>
      </div>
    </div>
  )
}

function sectionName(pathname: string): string {
  if (pathname.startsWith('/data')) return 'Data'
  if (pathname.startsWith('/eda')) return 'EDA'
  if (pathname.startsWith('/history')) return 'Decisions & History'
  return 'Overview'
}
