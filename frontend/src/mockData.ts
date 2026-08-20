import type {
  AdsInteractionEvent,
  FrontendDataSource,
  InteractionStream,
  ProjectWorkspace,
} from './domain'

const workspace: ProjectWorkspace = {
  project: {
    id: 'project-churn-v1',
    name: 'Customer Churn Prediction',
    objective: 'Build a reliable binary prediction workflow for customers at risk of churn while preserving deployment-valid evidence.',
    target: 'churn',
    predictionContext: 'Monthly account review; exact prediction moment remains unresolved.',
    stage: 'EDA and validation design',
    updatedAt: '2026-08-20T10:45:00Z',
  },
  recommendations: [
    {
      id: 'rec-prediction-moment',
      title: 'Resolve prediction moment',
      status: 'BLOCKING',
      summary: 'Feature eligibility and validation legitimacy cannot be finalized until the represented prediction moment is explicit.',
      why: 'Several candidate variables may contain information that is only available after the intended scoring moment.',
      establishes: 'A defensible information boundary for feature eligibility and evaluation.',
      dependsOn: ['Deployment workflow', 'Target window', 'Feature source timing'],
      ifSkipped: 'Later model evidence may look strong while being invalid for the intended deployment process.',
      alternatives: ['Clarify operational scoring contract', 'Temporarily mark affected features unresolved'],
    },
    {
      id: 'rec-missingness',
      title: 'Investigate production missingness',
      status: 'RECOMMENDED',
      summary: 'Support-ticket data are incomplete and may remain incomplete at prediction time.',
      why: 'The missingness mechanism affects preprocessing, deployment robustness and whether missingness itself is informative.',
      establishes: 'Whether the missing-data strategy should represent real production missingness.',
      dependsOn: ['Source-system behavior', 'Production data contract'],
      ifSkipped: 'Validation may overstate performance or the production pipeline may fail on expected missing values.',
      alternatives: ['Missingness indicator', 'Native model handling', 'Median/imputation pipeline'],
    },
    {
      id: 'rec-temporal',
      title: 'Compare temporal validation cutoffs',
      status: 'RELEVANT',
      summary: 'Signup and churn behavior show time structure that may make a single split fragile.',
      why: 'The intended claim is about future customers, so performance stability across historical cutoffs is informative.',
      establishes: 'Sensitivity of model comparison to the chosen historical evaluation window.',
      dependsOn: ['Prediction horizon', 'Retraining cadence'],
      ifSkipped: 'One favorable cutoff could hide temporal instability.',
      alternatives: ['Rolling-origin evaluation', 'Multiple chronological holdouts'],
    },
    {
      id: 'rec-random-forest',
      title: 'Random Forest nonlinear benchmark',
      status: 'DEFERRED',
      summary: 'A flexible tree ensemble remains useful, but validation semantics should be settled before model expansion.',
      why: 'It can benchmark nonlinearities and interactions after the evaluation design becomes legitimate.',
      establishes: 'Whether a flexible nonlinear model materially outperforms simpler baselines.',
      dependsOn: ['Validated feature set', 'Validation design'],
      ifSkipped: 'The project can still proceed with simpler baselines; this is not currently blocking.',
      alternatives: ['Gradient-boosted trees', 'Regularized logistic regression'],
    },
  ],
  questions: [
    {
      id: 'q-prediction-moment',
      prompt: 'At exactly what point in the monthly workflow should a churn prediction be considered available?',
      importance: 'critical',
      status: 'OPEN',
      rationale: 'The answer governs prediction-time feature eligibility and temporal validation.',
    },
    {
      id: 'q-production-missing',
      prompt: 'Can support-ticket counts still be missing when the production scorer runs?',
      importance: 'high',
      status: 'OPEN',
      rationale: 'The answer determines whether realistic missingness must be preserved throughout validation.',
    },
  ],
  findings: [
    {
      id: 'f-imbalance',
      title: 'Target is moderately imbalanced',
      statement: 'Churn prevalence is 26.4%, so accuracy alone would be an incomplete model-selection metric.',
      confidence: 'high',
      evidence: ['dataset summary', 'target-frequency table'],
      createdAt: '2026-08-20T09:52:00Z',
    },
    {
      id: 'f-temporal-coverage',
      title: 'Customer acquisition spans multiple regimes',
      statement: 'Signup dates span 41 months and recent cohorts have a higher churn rate than the oldest cohorts.',
      confidence: 'medium',
      evidence: ['signup-date distribution', 'cohort churn trend'],
      createdAt: '2026-08-20T10:06:00Z',
    },
  ],
  decisions: [
    {
      id: 'd-validation',
      title: 'Use chronological validation as current baseline',
      selected: 'Chronological holdout with multiple candidate cutoffs before protected final evaluation',
      alternatives: ['Random stratified split', 'Single chronological holdout', 'Rolling-origin validation'],
      rationale: 'The project currently targets future-customer generalization and already shows meaningful temporal structure.',
      supportingFindings: ['f-temporal-coverage'],
      status: 'REVISIT_IF_CONTEXT_CHANGES',
      decidedAt: '2026-08-20T10:18:00Z',
    },
  ],
  variables: [
    { name: 'customer_id', semanticType: 'identifier', storedType: 'string', missingPercent: 0, unique: 7043, preview: '7590-VHVEG' },
    { name: 'tenure_months', semanticType: 'numeric', storedType: 'int64', missingPercent: 0, unique: 73, preview: '1, 34, 2, 45' },
    { name: 'monthly_charges', semanticType: 'numeric', storedType: 'float64', missingPercent: 0, unique: 1585, preview: '29.85, 56.95, 53.85' },
    { name: 'contract', semanticType: 'categorical', storedType: 'string', missingPercent: 0, unique: 3, preview: 'Month-to-month' },
    { name: 'support_tickets', semanticType: 'numeric', storedType: 'float64', missingPercent: 6.8, unique: 17, preview: '0, 2, missing, 1' },
    { name: 'signup_date', semanticType: 'temporal', storedType: 'date', missingPercent: 0, unique: 1188, preview: '2023-03-14' },
    { name: 'churn', semanticType: 'target', storedType: 'string', missingPercent: 0, unique: 2, preview: 'Yes / No' },
  ],
  rows: [
    { customerId: '7590-VHVEG', tenureMonths: 1, monthlyCharges: 29.85, contract: 'Month-to-month', supportTickets: 2, signupDate: '2026-06-04', churn: 'No' },
    { customerId: '5575-GNVDE', tenureMonths: 34, monthlyCharges: 56.95, contract: 'One year', supportTickets: 0, signupDate: '2023-09-18', churn: 'No' },
    { customerId: '3668-QPYBK', tenureMonths: 2, monthlyCharges: 53.85, contract: 'Month-to-month', supportTickets: null, signupDate: '2026-05-01', churn: 'Yes' },
    { customerId: '7795-CFOCW', tenureMonths: 45, monthlyCharges: 42.30, contract: 'One year', supportTickets: 1, signupDate: '2022-11-22', churn: 'No' },
    { customerId: '9237-HQITU', tenureMonths: 2, monthlyCharges: 70.70, contract: 'Month-to-month', supportTickets: 3, signupDate: '2026-05-09', churn: 'Yes' },
    { customerId: '9305-CDSKC', tenureMonths: 8, monthlyCharges: 99.65, contract: 'Month-to-month', supportTickets: null, signupDate: '2025-11-27', churn: 'Yes' },
    { customerId: '1452-KIOVK', tenureMonths: 22, monthlyCharges: 89.10, contract: 'Month-to-month', supportTickets: 1, signupDate: '2024-09-14', churn: 'No' },
    { customerId: '6713-OKOMC', tenureMonths: 10, monthlyCharges: 29.75, contract: 'Month-to-month', supportTickets: 0, signupDate: '2025-09-02', churn: 'No' },
    { customerId: '7892-POOKP', tenureMonths: 28, monthlyCharges: 104.80, contract: 'Month-to-month', supportTickets: 4, signupDate: '2024-03-10', churn: 'Yes' },
    { customerId: '6388-TABGU', tenureMonths: 62, monthlyCharges: 56.15, contract: 'One year', supportTickets: 0, signupDate: '2021-04-18', churn: 'No' },
    { customerId: '9763-GRSKD', tenureMonths: 13, monthlyCharges: 49.95, contract: 'Month-to-month', supportTickets: 1, signupDate: '2025-06-03', churn: 'No' },
    { customerId: '7469-LKBCI', tenureMonths: 16, monthlyCharges: 18.95, contract: 'Two year', supportTickets: 0, signupDate: '2025-03-17', churn: 'No' },
  ],
  runs: [
    {
      id: 'run-missingness',
      title: 'Missingness pattern investigation',
      status: 'WAITING_FOR_APPROVAL',
      detail: 'Compare missingness by target and signup cohort, then persist evidence tables to project artifacts.',
      startedAt: '2026-08-20T10:31:00Z',
      sideEffect: 'project-write',
      parameters: { scope: 'support_tickets', output: 'evidence + finding candidates' },
    },
    {
      id: 'run-baseline',
      title: 'Logistic regression baseline',
      status: 'COMPLETED',
      detail: 'Baseline fitted on the current chronological development split.',
      startedAt: '2026-08-20T09:22:00Z',
      sideEffect: 'read-only',
      parameters: { metric: 'PR-AUC', split: 'chronological-v0' },
    },
    {
      id: 'run-profile',
      title: 'Dataset profile refresh',
      status: 'RUNNING',
      detail: 'Refreshing lightweight dataset summaries after source metadata update.',
      startedAt: '2026-08-20T10:43:00Z',
      sideEffect: 'read-only',
      parameters: { dataset: 'customers', mode: 'incremental' },
    },
  ],
  churnTrend: [
    { label: '2025 Q3', value: 21.8 },
    { label: '2025 Q4', value: 23.1 },
    { label: '2026 Q1', value: 25.4 },
    { label: '2026 Q2', value: 27.0 },
    { label: '2026 Q3', value: 29.2 },
  ],
  tenureDistribution: [
    { label: '0-6', count: 1460 },
    { label: '7-12', count: 910 },
    { label: '13-24', count: 1220 },
    { label: '25-36', count: 1030 },
    { label: '37-48', count: 880 },
    { label: '49-60', count: 730 },
    { label: '61-72', count: 813 },
  ],
  recentChanges: [
    { id: 'change-1', label: 'Temporal coverage finding added', when: '12 min ago', kind: 'Finding' },
    { id: 'change-2', label: 'Validation baseline decision updated', when: '18 min ago', kind: 'Decision' },
    { id: 'change-3', label: 'Production missingness question opened', when: '31 min ago', kind: 'Question' },
  ],
}

export class TypedMockDataSource implements FrontendDataSource {
  async getWorkspace(projectId: string): Promise<ProjectWorkspace> {
    if (projectId !== workspace.project.id) {
      throw new Error(`Unknown project: ${projectId}`)
    }
    return structuredClone(workspace)
  }
}

export class MockInteractionStream implements InteractionStream {
  private listeners = new Set<(event: AdsInteractionEvent) => void>()

  subscribe(listener: (event: AdsInteractionEvent) => void): () => void {
    this.listeners.add(listener)
    return () => this.listeners.delete(listener)
  }

  emit(event: AdsInteractionEvent): void {
    for (const listener of this.listeners) listener(event)
  }
}

export const mockDataSource = new TypedMockDataSource()
export const mockInteractionStream = new MockInteractionStream()
