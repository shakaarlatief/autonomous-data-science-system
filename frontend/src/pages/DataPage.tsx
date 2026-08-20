import { useMemo, useState } from 'react'
import {
  ArrowDown,
  ArrowUp,
  Columns3,
  Database,
  Filter,
  Search,
  SlidersHorizontal,
} from 'lucide-react'
import {
  createSortedRowModel,
  rowSortingFeature,
  tableFeatures,
  useTable,
  type ColumnDef,
} from '@tanstack/react-table'
import { useWorkspace } from '../appState'
import type { DataRow, VariableSummary } from '../domain'

const features = tableFeatures({
  rowSortingFeature,
  sortedRowModel: createSortedRowModel(),
})

const columns: Array<ColumnDef<typeof features, DataRow>> = [
  { accessorKey: 'customerId', header: 'Customer ID' },
  { accessorKey: 'tenureMonths', header: 'Tenure', cell: (info) => `${info.getValue<number>()} mo` },
  { accessorKey: 'monthlyCharges', header: 'Monthly charges', cell: (info) => `€${info.getValue<number>().toFixed(2)}` },
  { accessorKey: 'contract', header: 'Contract' },
  {
    accessorKey: 'supportTickets',
    header: 'Support tickets',
    cell: (info) => info.getValue<number | null>() ?? <span className="missing-value">missing</span>,
  },
  { accessorKey: 'signupDate', header: 'Signup date' },
  { accessorKey: 'churn', header: 'Churn', cell: (info) => <span className={`binary-value ${info.getValue<string>().toLowerCase()}`}>{info.getValue<string>()}</span> },
]

export function DataPage({
  selectedColumn,
  filter,
  onSearchChange,
  onSelectColumn,
}: {
  selectedColumn: string
  filter: string
  onSearchChange: (value: string) => void
  onSelectColumn: (value: string) => void
}) {
  const { workspace } = useWorkspace()
  const [visibleColumns, setVisibleColumns] = useState<Record<string, boolean>>({})
  const normalizedFilter = filter.trim().toLowerCase()
  const rows = useMemo(
    () => workspace.rows.filter((row) => !normalizedFilter || Object.values(row).some((value) => String(value ?? '').toLowerCase().includes(normalizedFilter))),
    [workspace.rows, normalizedFilter],
  )
  const table = useTable({ features, columns, data: rows })
  const selected = workspace.variables.find((variable) => variable.name === selectedColumn) ?? workspace.variables[0]

  return (
    <div className="page-stack data-page">
      <header className="page-header">
        <div>
          <span className="eyebrow">Dataset workspace</span>
          <h1>Data</h1>
          <p>Inspect stored values, semantic roles, missingness and representative rows without loading the full production dataset into browser memory.</p>
        </div>
        <div className="header-stat-group">
          <HeaderStat value="7,043" label="rows" />
          <HeaderStat value="21" label="source columns" />
          <HeaderStat value="6.8%" label="max missing" />
        </div>
      </header>

      <section className="data-inspector-grid">
        <aside className="variable-rail" aria-label="Variables">
          <div className="variable-rail-header">
            <div><span className="eyebrow">Schema</span><h2>Variables</h2></div>
            <span className="count-chip">{workspace.variables.length}</span>
          </div>
          <div className="variable-list">
            {workspace.variables.map((variable) => (
              <button
                type="button"
                className={`variable-item ${variable.name === selected.name ? 'selected' : ''}`}
                key={variable.name}
                onClick={() => onSelectColumn(variable.name)}
              >
                <span className={`semantic-dot ${variable.semanticType}`} />
                <span><strong>{variable.name}</strong><small>{variable.semanticType} · {variable.storedType}</small></span>
                <span className="missing-mini">{variable.missingPercent ? `${variable.missingPercent}%` : '0%'}</span>
              </button>
            ))}
          </div>
        </aside>

        <div className="data-main-stack">
          <section className="variable-detail panel">
            <div className="variable-detail-title">
              <span className={`semantic-icon ${selected.semanticType}`}><Database size={17} /></span>
              <div><span className="eyebrow">Selected variable</span><h2>{selected.name}</h2></div>
            </div>
            <div className="variable-detail-stats">
              <DetailStat label="Semantic type" value={selected.semanticType} />
              <DetailStat label="Stored dtype" value={selected.storedType} />
              <DetailStat label="Missing" value={`${selected.missingPercent}%`} />
              <DetailStat label="Unique" value={selected.unique.toLocaleString()} />
              <DetailStat label="Preview" value={selected.preview} mono />
            </div>
          </section>

          <section className="panel data-table-panel">
            <div className="table-toolbar">
              <label className="table-search">
                <Search size={15} />
                <span className="sr-only">Filter preview rows</span>
                <input value={filter} onChange={(event) => onSearchChange(event.target.value)} placeholder="Filter preview rows" />
              </label>
              <div className="toolbar-actions">
                <button className="button tertiary" type="button"><Filter size={14} /> Filters</button>
                <button className="button tertiary" type="button" onClick={() => setVisibleColumns((current) => ({ ...current, supportTickets: current.supportTickets === false }))}>
                  <Columns3 size={14} /> Columns
                </button>
                <button className="icon-button" type="button" aria-label="Table settings"><SlidersHorizontal size={15} /></button>
              </div>
            </div>

            <div className="table-scroll" role="region" aria-label="Representative dataset rows" tabIndex={0}>
              <table className="data-table">
                <thead>
                  {table.getHeaderGroups().map((headerGroup) => (
                    <tr key={headerGroup.id}>
                      {headerGroup.headers.map((header) => {
                        if (visibleColumns[header.column.id] === false) return null
                        const sorted = header.column.getIsSorted()
                        return (
                          <th key={header.id}>
                            <button type="button" className="table-header-button" onClick={header.column.getToggleSortingHandler()}>
                              {header.isPlaceholder ? null : <table.FlexRender header={header} />}
                              {sorted === 'asc' && <ArrowUp size={12} />}
                              {sorted === 'desc' && <ArrowDown size={12} />}
                            </button>
                          </th>
                        )
                      })}
                    </tr>
                  ))}
                </thead>
                <tbody>
                  {table.getRowModel().rows.map((row) => (
                    <tr key={row.id}>
                      {row.getAllCells().map((cell) => visibleColumns[cell.column.id] === false ? null : (
                        <td key={cell.id}><table.FlexRender cell={cell} /></td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="table-footer-note">Showing {rows.length} representative rows. Production data access will remain backend-paginated or streamed.</div>
          </section>
        </div>
      </section>
    </div>
  )
}

function HeaderStat({ value, label }: { value: string; label: string }) {
  return <div className="header-stat"><strong>{value}</strong><span>{label}</span></div>
}

function DetailStat({ label, value, mono = false }: { label: string; value: string; mono?: boolean }) {
  return <div className="detail-stat"><span>{label}</span><strong className={mono ? 'mono' : ''}>{value}</strong></div>
}
