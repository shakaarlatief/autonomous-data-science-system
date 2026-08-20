import { useState } from 'react'
import {
  AlertTriangle,
  ArrowUpRight,
  BrainCircuit,
  Check,
  ChevronDown,
  CircleHelp,
  Clock3,
  Info,
  PanelRightClose,
  PanelRightOpen,
  Play,
  Sparkles,
  X,
} from 'lucide-react'
import { useWorkspace } from '../appState'
import type { MethodologicalStatus, Recommendation, RunSummary } from '../domain'

export function MethodologyPanel({ collapsed, onToggle }: { collapsed: boolean; onToggle: () => void }) {
  const { workspace, runs, approveRun, rejectRun } = useWorkspace()
  const [selected, setSelected] = useState<Recommendation | null>(workspace.recommendations[0] ?? null)
  const waiting = runs.find((run) => run.status === 'WAITING_FOR_APPROVAL')

  if (collapsed) {
    return (
      <aside className="context-panel context-panel-collapsed" aria-label="Methodological guidance">
        <button className="context-panel-toggle collapsed-toggle" type="button" aria-label="Expand methodological guidance" onClick={onToggle}>
          <PanelRightOpen size={18} />
        </button>
        <span className="collapsed-system-mark" aria-hidden="true"><BrainCircuit size={17} /></span>
        {waiting && <span className="collapsed-attention-dot" aria-label="Approval required" />}
      </aside>
    )
  }

  return (
    <aside className="context-panel" aria-label="Methodological guidance">
      <div className="context-panel-header">
        <div>
          <span className="eyebrow">System</span>
          <h2>What matters now</h2>
        </div>
        <div className="context-panel-header-actions">
          <BrainCircuit size={19} />
          <button className="context-panel-toggle" type="button" aria-label="Collapse methodological guidance" onClick={onToggle}>
            <PanelRightClose size={17} />
          </button>
        </div>
      </div>

      {waiting && (
        <ApprovalCard run={waiting} onApprove={() => approveRun(waiting.id)} onReject={() => rejectRun(waiting.id)} />
      )}

      <section className="context-section" aria-labelledby="guidance-heading">
        <div className="section-heading-row">
          <h3 id="guidance-heading">Methodological guidance</h3>
          <span className="count-chip">{workspace.recommendations.length}</span>
        </div>
        <div className="recommendation-list">
          {workspace.recommendations.map((recommendation) => (
            <button
              type="button"
              key={recommendation.id}
              className={`recommendation-row ${selected?.id === recommendation.id ? 'selected' : ''}`}
              onClick={() => setSelected(recommendation)}
            >
              <StatusMark status={recommendation.status} />
              <span className="recommendation-row-copy">
                <span className="recommendation-title">{recommendation.title}</span>
                <span className="recommendation-summary">{recommendation.summary}</span>
              </span>
              <ArrowUpRight size={14} />
            </button>
          ))}
        </div>
      </section>

      {selected && (
        <section className="recommendation-detail" aria-live="polite">
          <div className="detail-title-row">
            <StatusLabel status={selected.status} />
            <button className="icon-button quiet" type="button" aria-label="Close recommendation detail" onClick={() => setSelected(null)}>
              <X size={14} />
            </button>
          </div>
          <h3>{selected.title}</h3>
          <DetailBlock icon={<Info size={14} />} label="Why this is here" text={selected.why} />
          <DetailBlock icon={<Check size={14} />} label="What it can establish" text={selected.establishes} />
          <DetailBlock icon={<AlertTriangle size={14} />} label="If skipped" text={selected.ifSkipped} />
          <div className="detail-list">
            <span className="detail-label"><CircleHelp size={14} /> Depends on</span>
            <ul>{selected.dependsOn.map((item) => <li key={item}>{item}</li>)}</ul>
          </div>
          <div className="detail-list">
            <span className="detail-label"><Sparkles size={14} /> Alternatives / complements</span>
            <ul>{selected.alternatives.map((item) => <li key={item}>{item}</li>)}</ul>
          </div>
        </section>
      )}
    </aside>
  )
}

function ApprovalCard({ run, onApprove, onReject }: { run: RunSummary; onApprove: () => void; onReject: () => void }) {
  const [expanded, setExpanded] = useState(true)
  return (
    <section className="approval-card" aria-labelledby="approval-title">
      <button className="approval-heading" type="button" onClick={() => setExpanded((value) => !value)} aria-expanded={expanded}>
        <span className="approval-icon"><Clock3 size={15} /></span>
        <span>
          <span className="eyebrow">Approval required</span>
          <strong id="approval-title">{run.title}</strong>
        </span>
        <ChevronDown size={15} className={expanded ? 'rotate' : ''} />
      </button>
      {expanded && (
        <div className="approval-body">
          <p>{run.detail}</p>
          <dl className="compact-definition-list">
            <div><dt>Effect</dt><dd>{run.sideEffect}</dd></div>
            {Object.entries(run.parameters).map(([key, value]) => <div key={key}><dt>{key}</dt><dd>{value}</dd></div>)}
          </dl>
          <p className="approval-explainer">Approve resumes the proposed investigation. Reject leaves project state unchanged and records the rejection in the interaction stream.</p>
          <div className="approval-actions">
            <button className="button primary" type="button" onClick={onApprove}><Play size={14} /> Approve & run</button>
            <button className="button secondary" type="button" onClick={onReject}>Reject</button>
          </div>
        </div>
      )}
    </section>
  )
}

function DetailBlock({ icon, label, text }: { icon: React.ReactNode; label: string; text: string }) {
  return (
    <div className="detail-block">
      <span className="detail-label">{icon}{label}</span>
      <p>{text}</p>
    </div>
  )
}

export function StatusLabel({ status }: { status: MethodologicalStatus }) {
  return <span className={`method-status ${status.toLowerCase()}`}><StatusMark status={status} />{statusLabel(status)}</span>
}

function StatusMark({ status }: { status: MethodologicalStatus }) {
  const symbol = status === 'BLOCKING' ? '!' : status === 'RECOMMENDED' ? '↑' : status === 'RELEVANT' ? '•' : '○'
  return <span className={`status-mark ${status.toLowerCase()}`} aria-hidden="true">{symbol}</span>
}

function statusLabel(status: MethodologicalStatus) {
  if (status === 'BLOCKING') return 'Required / blocking'
  if (status === 'RECOMMENDED') return 'Recommended'
  if (status === 'RELEVANT') return 'Relevant'
  return 'Deferred'
}
