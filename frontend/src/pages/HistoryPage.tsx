import {
  ArrowRight,
  CheckCircle2,
  GitBranch,
  History,
  MessageCircleQuestion,
  Quote,
} from 'lucide-react'
import { useWorkspace } from '../appState'

export function HistoryPage() {
  const { workspace } = useWorkspace()
  const decision = workspace.decisions[0]

  return (
    <div className="page-stack history-page">
      <header className="page-header">
        <div>
          <span className="eyebrow">Traceable project memory</span>
          <h1>Decisions & History</h1>
          <p>Inspect not only the current project state, but why it changed, which alternatives were considered and what evidence supported consequential choices.</p>
        </div>
        <div className="history-summary"><History size={18} /><span>Representative event projection</span></div>
      </header>

      <section className="decision-object panel">
        <div className="decision-accent"><GitBranch size={19} /></div>
        <div className="decision-main">
          <div className="decision-header">
            <div><span className="eyebrow">Decision · {decision.status.replaceAll('_', ' ').toLowerCase()}</span><h2>{decision.title}</h2></div>
            <span className="decision-date">{new Date(decision.decidedAt).toLocaleString()}</span>
          </div>
          <div className="selected-option">
            <span className="selected-icon"><CheckCircle2 size={15} /></span>
            <div><span>Selected option</span><strong>{decision.selected}</strong></div>
          </div>
          <div className="decision-grid">
            <div>
              <span className="detail-label"><Quote size={14} /> Rationale</span>
              <p>{decision.rationale}</p>
            </div>
            <div>
              <span className="detail-label"><GitBranch size={14} /> Alternatives considered</span>
              <ul className="alternative-list">{decision.alternatives.map((item) => <li key={item}>{item}</li>)}</ul>
            </div>
          </div>
          <div className="supporting-evidence">
            <span className="detail-label">Supporting project objects</span>
            {decision.supportingFindings.map((id) => {
              const finding = workspace.findings.find((item) => item.id === id)
              return finding ? <button className="evidence-reference" type="button" key={id}><CheckCircle2 size={14} /><span><strong>{finding.title}</strong><small>{finding.statement}</small></span><ArrowRight size={13} /></button> : null
            })}
          </div>
        </div>
      </section>

      <section className="history-timeline panel">
        <div className="panel-heading compact">
          <div><span className="eyebrow">Event history</span><h2>Recent reasoning trail</h2></div>
          <span className="count-chip">5</span>
        </div>
        <div className="history-events">
          <HistoryEvent time="10:31" kind="Question" icon={<MessageCircleQuestion size={15} />} title="Production missingness question opened" detail="Support-ticket availability at scoring time remains unresolved." />
          <HistoryEvent time="10:18" kind="Decision" icon={<GitBranch size={15} />} title="Chronological validation selected as baseline" detail="Multiple historical cutoffs will be compared before protected evaluation." />
          <HistoryEvent time="10:06" kind="Finding" icon={<CheckCircle2 size={15} />} title="Temporal coverage finding accepted" detail="Recent cohorts show higher churn prevalence than older cohorts." />
          <HistoryEvent time="09:52" kind="Finding" icon={<CheckCircle2 size={15} />} title="Target imbalance finding accepted" detail="Churn prevalence is 26.4%; accuracy alone is insufficient." />
          <HistoryEvent time="09:22" kind="Run" icon={<History size={15} />} title="Logistic regression baseline completed" detail="Run remains evidence under the current development split, pending validation refinement." />
        </div>
      </section>
    </div>
  )
}

function HistoryEvent({ time, kind, icon, title, detail }: { time: string; kind: string; icon: React.ReactNode; title: string; detail: string }) {
  return (
    <article className="history-event">
      <time>{time}</time>
      <span className="history-event-icon">{icon}</span>
      <div><span className="eyebrow">{kind}</span><h3>{title}</h3><p>{detail}</p></div>
    </article>
  )
}
