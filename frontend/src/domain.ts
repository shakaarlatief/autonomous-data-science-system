export type MethodologicalStatus =
  | 'BLOCKING'
  | 'RECOMMENDED'
  | 'RELEVANT'
  | 'DEFERRED'

export type RunStatus =
  | 'RUNNING'
  | 'WAITING_FOR_APPROVAL'
  | 'COMPLETED'
  | 'FAILED'

export type SemanticType =
  | 'numeric'
  | 'categorical'
  | 'identifier'
  | 'temporal'
  | 'target'

export interface ProjectSummary {
  id: string
  name: string
  objective: string
  target: string
  predictionContext: string
  stage: string
  updatedAt: string
}

export interface Recommendation {
  id: string
  title: string
  status: MethodologicalStatus
  summary: string
  why: string
  establishes: string
  dependsOn: string[]
  ifSkipped: string
  alternatives: string[]
}

export interface Question {
  id: string
  prompt: string
  importance: 'critical' | 'high' | 'normal'
  status: 'OPEN' | 'ANSWERED'
  rationale: string
}

export interface Finding {
  id: string
  title: string
  statement: string
  confidence: 'high' | 'medium' | 'low'
  evidence: string[]
  createdAt: string
}

export interface Decision {
  id: string
  title: string
  selected: string
  alternatives: string[]
  rationale: string
  supportingFindings: string[]
  status: 'ACCEPTED' | 'REVISIT_IF_CONTEXT_CHANGES'
  decidedAt: string
}

export interface VariableSummary {
  name: string
  semanticType: SemanticType
  storedType: string
  missingPercent: number
  unique: number
  preview: string
}

export interface DataRow {
  customerId: string
  tenureMonths: number
  monthlyCharges: number
  contract: string
  supportTickets: number | null
  signupDate: string
  churn: 'Yes' | 'No'
}

export interface RunSummary {
  id: string
  title: string
  status: RunStatus
  detail: string
  startedAt: string
  sideEffect: 'read-only' | 'project-write' | 'external'
  parameters: Record<string, string>
}

export interface TrendPoint {
  label: string
  value: number
}

export interface DistributionBin {
  label: string
  count: number
}

export interface ProjectWorkspace {
  project: ProjectSummary
  recommendations: Recommendation[]
  questions: Question[]
  findings: Finding[]
  decisions: Decision[]
  variables: VariableSummary[]
  rows: DataRow[]
  runs: RunSummary[]
  churnTrend: TrendPoint[]
  tenureDistribution: DistributionBin[]
  recentChanges: Array<{ id: string; label: string; when: string; kind: string }>
}

export interface FrontendDataSource {
  getWorkspace(projectId: string): Promise<ProjectWorkspace>
}

export type AdsInteractionEvent =
  | { type: 'run.started'; runId: string }
  | { type: 'run.status_changed'; runId: string; status: RunStatus }
  | { type: 'message.delta'; runId: string; delta: string }
  | { type: 'message.completed'; runId: string; message: string }
  | { type: 'tool.started'; runId: string; toolName: string }
  | { type: 'tool.completed'; runId: string; toolName: string }
  | { type: 'approval.requested'; runId: string }
  | { type: 'approval.resolved'; runId: string; approved: boolean }
  | { type: 'artifact.created'; runId: string; artifactId: string }

export interface InteractionStream {
  subscribe(listener: (event: AdsInteractionEvent) => void): () => void
}
