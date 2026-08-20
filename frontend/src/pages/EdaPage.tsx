import { useMemo, useState } from 'react'
import ReactECharts from 'echarts-for-react'
import Plot from 'react-plotly.js'
import {
  BarChart3,
  CircleHelp,
  Eye,
  Layers3,
  LineChart,
  Sparkles,
} from 'lucide-react'
import { useWorkspace } from '../appState'
import { StatusLabel } from '../components/MethodologyPanel'

export function EdaPage({ selectedView, onViewChange }: { selectedView: string; onViewChange: (value: string) => void }) {
  const { workspace } = useWorkspace()
  const [engine, setEngine] = useState<'echarts' | 'plotly'>('echarts')
  const view = selectedView === 'trend' ? 'trend' : 'distribution'

  return (
    <div className="page-stack eda-page">
      <header className="page-header">
        <div>
          <span className="eyebrow">Exploratory analysis</span>
          <h1>EDA</h1>
          <p>Explore evidence while keeping methodological options, validity concerns and follow-up questions visible in the same workspace.</p>
        </div>
        <div className="segmented-control" role="group" aria-label="EDA view">
          <button className={view === 'distribution' ? 'active' : ''} type="button" onClick={() => onViewChange('distribution')}><BarChart3 size={14} /> Distribution</button>
          <button className={view === 'trend' ? 'active' : ''} type="button" onClick={() => onViewChange('trend')}><LineChart size={14} /> Time trend</button>
        </div>
      </header>

      <section className="eda-layout">
        <div className="eda-analysis-stack">
          <section className="panel chart-panel">
            <div className="panel-heading chart-heading">
              <div>
                <span className="eyebrow">Analytical preview</span>
                <h2>{view === 'distribution' ? 'Tenure distribution' : 'Churn rate through time'}</h2>
                <p>{view === 'distribution' ? 'Customer tenure grouped into six-month bands.' : 'Quarterly churn prevalence in recent cohorts.'}</p>
              </div>
              <div className="chart-engine-control" role="group" aria-label="Chart renderer comparison">
                <button type="button" className={engine === 'echarts' ? 'active' : ''} onClick={() => setEngine('echarts')}>ECharts</button>
                <button type="button" className={engine === 'plotly' ? 'active' : ''} onClick={() => setEngine('plotly')}>Plotly</button>
              </div>
            </div>
            <div className="chart-stage" data-chart-engine={engine}>
              {engine === 'echarts'
                ? <EChartView view={view} />
                : <PlotlyView view={view} />}
            </div>
            <div className="chart-caption">
              <span><Eye size={14} /> Renderer bakeoff uses the same ADS data and visual intent.</span>
              <span>Selection is evaluation-only.</span>
            </div>
          </section>

          <section className="panel finding-callout">
            <div className="finding-callout-icon"><Sparkles size={18} /></div>
            <div>
              <span className="eyebrow">Candidate interpretation</span>
              <h3>{view === 'distribution' ? 'Short-tenure customers form the largest concentration.' : 'Recent cohorts show increasing churn prevalence.'}</h3>
              <p>{view === 'distribution'
                ? 'This pattern motivates segmented target analysis, but a histogram alone does not establish why short-tenure customers churn.'
                : 'The trend is relevant to validation design, but it does not by itself establish future drift or causal change.'}</p>
            </div>
            <button className="button secondary" type="button">Inspect evidence</button>
          </section>
        </div>

        <aside className="eda-methods panel" aria-label="EDA methods">
          <div className="panel-heading compact">
            <div><span className="eyebrow">Option space</span><h2>Analyses for this view</h2></div>
            <Layers3 size={18} />
          </div>
          <div className="method-stack">
            {workspace.recommendations.map((recommendation) => (
              <article className="method-card" key={recommendation.id}>
                <StatusLabel status={recommendation.status} />
                <h3>{recommendation.title}</h3>
                <p>{recommendation.summary}</p>
                <button type="button" className="text-button"><CircleHelp size={13} /> Why this status?</button>
              </article>
            ))}
          </div>
        </aside>
      </section>
    </div>
  )
}

function EChartView({ view }: { view: 'distribution' | 'trend' }) {
  const { workspace } = useWorkspace()
  const dark = document.documentElement.dataset.theme === 'dark'
  const data = view === 'distribution' ? workspace.tenureDistribution : workspace.churnTrend
  const option = useMemo(() => ({
    animationDuration: 350,
    grid: { left: 50, right: 24, top: 24, bottom: 42 },
    tooltip: { trigger: 'axis' },
    xAxis: {
      type: 'category',
      data: data.map((item) => item.label),
      axisLine: { lineStyle: { color: dark ? '#343a45' : '#d9dde5' } },
      axisLabel: { color: dark ? '#9199a8' : '#697181' },
    },
    yAxis: {
      type: 'value',
      name: view === 'distribution' ? 'Customers' : 'Churn %',
      nameTextStyle: { color: dark ? '#77808f' : '#7a8290' },
      axisLabel: { color: dark ? '#9199a8' : '#697181' },
      splitLine: { lineStyle: { color: dark ? '#20242b' : '#eef0f4' } },
    },
    series: [{
      data: data.map((item) => item.value ?? ('count' in item ? item.count : 0)),
      type: view === 'distribution' ? 'bar' : 'line',
      smooth: view === 'trend',
      symbolSize: 8,
      barMaxWidth: 48,
      itemStyle: { color: dark ? '#8da2fb' : '#566bd8', borderRadius: view === 'distribution' ? [5, 5, 1, 1] : undefined },
      lineStyle: { width: 2.5, color: dark ? '#8da2fb' : '#566bd8' },
      areaStyle: view === 'trend' ? { opacity: 0.08, color: dark ? '#8da2fb' : '#566bd8' } : undefined,
    }],
  }), [data, dark, view])

  return <ReactECharts option={option} style={{ height: 340, width: '100%' }} opts={{ renderer: 'canvas' }} />
}

function PlotlyView({ view }: { view: 'distribution' | 'trend' }) {
  const { workspace } = useWorkspace()
  const dark = document.documentElement.dataset.theme === 'dark'
  const data = view === 'distribution' ? workspace.tenureDistribution : workspace.churnTrend
  const x = data.map((item) => item.label)
  const y = data.map((item) => item.value ?? ('count' in item ? item.count : 0))
  const color = dark ? '#8da2fb' : '#566bd8'

  return (
    <Plot
      data={view === 'distribution'
        ? [{ type: 'bar', x, y, marker: { color } }]
        : [{ type: 'scatter', mode: 'lines+markers', x, y, line: { color, width: 3 }, marker: { color, size: 7 }, fill: 'tozeroy', fillcolor: dark ? 'rgba(141,162,251,0.08)' : 'rgba(86,107,216,0.08)' }]}
      layout={{
        autosize: true,
        height: 340,
        margin: { l: 55, r: 24, t: 20, b: 46 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: dark ? '#9199a8' : '#697181', family: 'Inter, ui-sans-serif, system-ui' },
        xaxis: { gridcolor: 'rgba(0,0,0,0)', zeroline: false },
        yaxis: { gridcolor: dark ? '#20242b' : '#eef0f4', zeroline: false, title: { text: view === 'distribution' ? 'Customers' : 'Churn %' } },
        showlegend: false,
      }}
      config={{ displayModeBar: false, responsive: true }}
      style={{ width: '100%', height: '340px' }}
      useResizeHandler
    />
  )
}
