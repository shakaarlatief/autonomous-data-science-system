import {
  createContext,
  useContext,
  useMemo,
  useState,
  type PropsWithChildren,
} from 'react'
import { useQuery } from '@tanstack/react-query'
import type { ProjectWorkspace, RunSummary } from './domain'
import { mockDataSource, mockInteractionStream } from './mockData'

interface WorkspaceState {
  workspace: ProjectWorkspace
  runs: RunSummary[]
  approveRun: (runId: string) => void
  rejectRun: (runId: string) => void
}

const WorkspaceContext = createContext<WorkspaceState | null>(null)

export function WorkspaceProvider({ children }: PropsWithChildren) {
  const query = useQuery({
    queryKey: ['workspace', 'project-churn-v1'],
    queryFn: () => mockDataSource.getWorkspace('project-churn-v1'),
    staleTime: Number.POSITIVE_INFINITY,
  })

  if (query.isPending) {
    return (
      <div className="app-state app-state-loading" role="status" aria-live="polite">
        <div className="skeleton skeleton-title" />
        <div className="skeleton skeleton-line" />
        <div className="skeleton skeleton-line short" />
        <span className="sr-only">Loading project workspace</span>
      </div>
    )
  }

  if (query.isError || !query.data) {
    return (
      <div className="app-state app-state-error" role="alert">
        <strong>Project workspace unavailable</strong>
        <p>The representative data source could not be loaded. Refresh to retry.</p>
      </div>
    )
  }

  return <LoadedWorkspace workspace={query.data}>{children}</LoadedWorkspace>
}

function LoadedWorkspace({ workspace, children }: PropsWithChildren<{ workspace: ProjectWorkspace }>) {
  const [runs, setRuns] = useState<RunSummary[]>(workspace.runs)

  const updateRun = (runId: string, approved: boolean) => {
    setRuns((current) =>
      current.map((run) =>
        run.id === runId
          ? {
              ...run,
              status: approved ? 'RUNNING' : 'FAILED',
              detail: approved
                ? `${run.detail} Approval recorded; execution resumed.`
                : `${run.detail} Rejected by user; no project write was performed.`,
            }
          : run,
      ),
    )
    mockInteractionStream.emit({ type: 'approval.resolved', runId, approved })
    mockInteractionStream.emit({
      type: 'run.status_changed',
      runId,
      status: approved ? 'RUNNING' : 'FAILED',
    })
  }

  const value = useMemo<WorkspaceState>(
    () => ({
      workspace,
      runs,
      approveRun: (runId) => updateRun(runId, true),
      rejectRun: (runId) => updateRun(runId, false),
    }),
    [workspace, runs],
  )

  return <WorkspaceContext.Provider value={value}>{children}</WorkspaceContext.Provider>
}

export function useWorkspace(): WorkspaceState {
  const context = useContext(WorkspaceContext)
  if (!context) throw new Error('useWorkspace must be used within WorkspaceProvider')
  return context
}
