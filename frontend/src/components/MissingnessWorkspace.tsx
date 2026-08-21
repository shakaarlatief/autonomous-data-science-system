import { useMemo } from 'react'
import {
  ArrowUpRight,
  BrainCircuit,
  Check,
  Database,
  MessageSquareText,
  Play,
  Sparkles,
  TriangleAlert,
} from 'lucide-react'
import { useWorkspace } from '../appState'

type MissingnessWorkspaceProps = {
  onOpenData: () => void
  onSelectColumn: (column: string) => void | Promise<void>
}

export function MissingnessWorkspace({
  onOpenData,
  onSelectColumn,
}: MissingnessWorkspaceProps) {
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
