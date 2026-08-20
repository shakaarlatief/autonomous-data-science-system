import {
  AlertTriangle,
  ArrowRight,
  CheckCircle2,
  Clock3,
  Database,
  FileCheck2,
  MessageCircleQuestion,
  PlayCircle,
  Radio,
} from 'lucide-react'
import { Link } from '@tanstack/react-router'
import { useWorkspace } from '../appState'
import { StatusLabel } from '../components/MethodologyPanel'

export function OverviewPage() {
  const { workspace, runs } = useWorkspace()
  const blocking = workspace.recommendations.filter((item) => item.status === 'BLOCKING')
  const openQuestions = workspace.questions.filter((item) => item.status === 'OPEN')
  const running = runs.filter((run) => run.status === 'RUNNING')

  return (
    <div className="page-stack overview-page">
      <header className="page-header hero-header">
        <div>
          <span className="eyebrow">{workspace.project.stage}</span>
          <h1>{workspace.project.name}</h1>
          <p>{workspace.project.objective}</p>
        </div>
        <div className="project-meta-card">
          <span className="meta-label">Target</span>
          <strong>{workspace.project.target}</strong>
          <span className="meta-separator" />
          <span className="meta-label">Prediction context</span>
          <span>{workspace.project.predictionContext}</span>
        </div>
      </header>

      <section className="metric-strip" aria-label="Project state summary">
        <Metric icon={<AlertTriangle size={17} />} value={blocking.length} label="blocking concern" tone="critical" />
        <Metric icon={<MessageCircleQuestion size={17} />} value={openQuestions.length} label="open questions" tone="attention" />
        <Metric icon={<FileCheck2 size={17} />} value={workspace.findings.length} label="accepted findings" tone="neutral" />
        <Metric icon={<Radio size={17} />} value={running.length} label="active run" tone="good" />
      </section>

      <div className="overview-grid">
        <section className="panel priority-panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">Priority</span>
              <h2>Current analytical state</h2>
            </div>
            <Link to="/eda" className="text-link">Open EDA <ArrowRight size={14} /></Link>
          </div>
          <div className="priority-list">
            {workspace.recommendations.slice(0, 3).map((item, index) => (
              <article className="priority-item" key={item.id}>
                <div className="priority-index">0{index + 1}</div>
                <div>
                  <StatusLabel status={item.status} />
                  <h3>{item.title}</h3>
                  <p>{item.summary}</p>
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="panel object-panel question-panel">
          <div className="panel-heading compact">
            <div>
              <span className="eyebrow">Questions</span>
              <h2>Needs clarification</h2>
            </div>
            <span className="count-chip">{openQuestions.length}</span>
          </div>
          {openQuestions.map((question) => (
            <article className="question-object" key={question.id}>
              <div className="question-glyph">?</div>
              <div>
                <span className={`importance ${question.importance}`}>{question.importance}</span>
                <h3>{question.prompt}</h3>
                <p>{question.rationale}</p>
                <button className="text-button" type="button">Answer or discuss <ArrowRight size={13} /></button>
              </div>
            </article>
          ))}
        </section>

        <section className="panel object-panel finding-panel">
          <div className="panel-heading compact">
            <div>
              <span className="eyebrow">Findings</span>
              <h2>Evidence-backed state</h2>
            </div>
            <CheckCircle2 size={18} />
          </div>
          {workspace.findings.map((finding) => (
            <article className="finding-object" key={finding.id}>
              <div className="finding-rail" />
              <div>
                <div className="finding-meta"><span>{finding.confidence} confidence</span><span>{finding.evidence.length} evidence refs</span></div>
                <h3>{finding.title}</h3>
                <p>{finding.statement}</p>
              </div>
            </article>
          ))}
        </section>

        <section className="panel activity-panel">
          <div className="panel-heading compact">
            <div>
              <span className="eyebrow">Execution</span>
              <h2>Runs & activity</h2>
            </div>
            <PlayCircle size={18} />
          </div>
          <div className="run-list">
            {runs.map((run) => (
              <div className="run-row" key={run.id}>
                <RunDot status={run.status} />
                <div className="run-copy">
                  <strong>{run.title}</strong>
                  <span>{run.detail}</span>
                </div>
                <span className={`run-status ${run.status.toLowerCase()}`}>{run.status.replaceAll('_', ' ')}</span>
              </div>
            ))}
          </div>
        </section>

        <section className="panel recent-panel">
          <div className="panel-heading compact">
            <div>
              <span className="eyebrow">Project memory</span>
              <h2>Recent changes</h2>
            </div>
            <Clock3 size={18} />
          </div>
          <div className="timeline">
            {workspace.recentChanges.map((change) => (
              <div className="timeline-row" key={change.id}>
                <span className="timeline-dot" />
                <div><strong>{change.label}</strong><span>{change.kind} · {change.when}</span></div>
              </div>
            ))}
          </div>
          <Link to="/history" className="button secondary full-width">Open decision history</Link>
        </section>

        <section className="panel dataset-panel">
          <div className="dataset-icon"><Database size={20} /></div>
          <div>
            <span className="eyebrow">Primary dataset</span>
            <h2>customer_churn.csv</h2>
            <p>7,043 rows · 7 profiled fields in this representative slice</p>
          </div>
          <Link to="/data" className="icon-button" aria-label="Open dataset"><ArrowRight size={16} /></Link>
        </section>
      </div>
    </div>
  )
}

function Metric({ icon, value, label, tone }: { icon: React.ReactNode; value: number; label: string; tone: string }) {
  return <div className={`metric-item ${tone}`}>{icon}<strong>{value}</strong><span>{label}</span></div>
}

function RunDot({ status }: { status: string }) {
  if (status === 'COMPLETED') return <CheckCircle2 className="run-dot completed" size={16} />
  if (status === 'WAITING_FOR_APPROVAL') return <Clock3 className="run-dot waiting" size={16} />
  return <span className={`run-dot pulse-dot ${status.toLowerCase()}`} />
}
