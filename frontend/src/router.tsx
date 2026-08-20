import {
  createRootRoute,
  createRoute,
  createRouter,
} from '@tanstack/react-router'
import { AppShell } from './components/AppShell'
import { CockpitPage, type CockpitFocus } from './pages/CockpitPage'
import { OverviewPage } from './pages/OverviewPage'
import { DataPage } from './pages/DataPage'
import { EdaPage } from './pages/EdaPage'
import { HistoryPage } from './pages/HistoryPage'

const rootRoute = createRootRoute({ component: AppShell })

const overviewRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/',
  component: OverviewPage,
})

const cockpitRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/cockpit',
  validateSearch: (search: Record<string, unknown>) => ({
    focus: isCockpitFocus(search.focus) ? search.focus : 'map',
    column: typeof search.column === 'string' ? search.column : 'support_tickets',
    filter: typeof search.filter === 'string' ? search.filter : '',
    view: search.view === 'trend' ? 'trend' as const : 'distribution' as const,
  }),
  component: CockpitRouteComponent,
})

function CockpitRouteComponent() {
  const search = cockpitRoute.useSearch()
  const navigate = cockpitRoute.useNavigate()

  return (
    <CockpitPage
      focus={search.focus}
      selectedColumn={search.column}
      filter={search.filter}
      selectedView={search.view}
      onFocusChange={(focus) => navigate({ search: (current) => ({ ...current, focus }) })}
      onSelectColumn={(column) => navigate({ search: (current) => ({ ...current, column }), replace: true })}
      onSearchChange={(filter) => navigate({ search: (current) => ({ ...current, filter }), replace: true })}
      onViewChange={(view) => navigate({ search: (current) => ({ ...current, view }), replace: true })}
    />
  )
}

const dataRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/data',
  validateSearch: (search: Record<string, unknown>) => ({
    column: typeof search.column === 'string' ? search.column : 'tenure_months',
    filter: typeof search.filter === 'string' ? search.filter : '',
  }),
  component: DataRouteComponent,
})

function DataRouteComponent() {
  const search = dataRoute.useSearch()
  const navigate = dataRoute.useNavigate()
  return (
    <DataPage
      selectedColumn={search.column}
      filter={search.filter}
      onSelectColumn={(column) => navigate({ search: (current) => ({ ...current, column }), replace: true })}
      onSearchChange={(filter) => navigate({ search: (current) => ({ ...current, filter }), replace: true })}
    />
  )
}

const edaRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/eda',
  validateSearch: (search: Record<string, unknown>) => ({
    view: search.view === 'trend' ? 'trend' : 'distribution',
  }),
  component: EdaRouteComponent,
})

function EdaRouteComponent() {
  const search = edaRoute.useSearch()
  const navigate = edaRoute.useNavigate()
  return (
    <EdaPage
      selectedView={search.view}
      onViewChange={(view) => navigate({ search: { view: view === 'trend' ? 'trend' : 'distribution' }, replace: true })}
    />
  )
}

const historyRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/history',
  component: HistoryPage,
})

const routeTree = rootRoute.addChildren([
  overviewRoute,
  cockpitRoute,
  dataRoute,
  edaRoute,
  historyRoute,
])

export const router = createRouter({ routeTree })

function isCockpitFocus(value: unknown): value is CockpitFocus {
  return value === 'map' || value === 'data' || value === 'eda' || value === 'missingness'
}

declare module '@tanstack/react-router' {
  interface Register {
    router: typeof router
  }
}
