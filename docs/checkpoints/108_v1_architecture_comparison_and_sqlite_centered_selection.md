# Checkpoint 108: V1 Architecture Comparison and SQLite-Centered Selection

**Date:** 2026-08-20  
**Status:** Historical architecture-selection checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 methodological-navigation architecture; V1 implementation architecture selection  
**Scope:** Compares plausible technology families against Checkpoint 107 requirements, records targeted external research and a synthetic SQLite viability spike, and selects the smallest currently justified V1 persistence/retrieval architecture.  
**Authority:** Historical provenance and rationale for the V1 architecture decision. `docs/DECISIONS.md` records the accepted decision; future technical specifications govern exact physical schema and implementation details.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## Why this checkpoint exists

Checkpoint 107 derived 59 technology-neutral requirements before allowing architecture selection.

The purpose of this checkpoint is not to rank fashionable databases. It is to answer:

> **What is the smallest technical architecture that can satisfy the V1 methodological-brain requirements cleanly, remain inspectable and local-first, and retain credible migration paths when stronger requirements actually appear?**

The comparison therefore uses three forms of evidence:

```text
1. promoted project requirements from Foundations 018-020 and Checkpoint 107;
2. current official capability documentation for candidate technologies;
3. a targeted synthetic viability spike for the leading embedded-database candidate.
```

The architecture is selected for **V1**, not declared the permanent final architecture of the complete future product.

---

# 1. Requirements that dominate the decision

The architecture comparison is driven especially by these V1 facts:

```text
expected scale:
    thousands to low tens of thousands of knowledge assets/revisions
    tens of thousands to low hundreds of thousands of components,
    rules, relations, provenance records, and project objects

concurrency:
    one active writer is acceptable initially
    multiple safe readers are desirable

availability:
    distributed high availability is not required

operation:
    local/offline development should remain practical
    installation and maintenance burden should remain low

relations:
    typed incoming/outgoing lookup and bounded local traversal are required
    arbitrary graph analytics are not required

semantic retrieval:
    required for methodological-horizon construction
    but no evidence yet requires approximate-nearest-neighbor infrastructure

project integration:
    methodological knowledge must combine frequently with current
    Definitions, Questions, Findings, Variables, Constraints, Decisions,
    Evidence, and other Foundation 018 objects

history:
    stable identity, immutable/recoverable revisions, provenance,
    supersession, and historical reconstruction are first-class

LLM context:
    selective bounded context assembly is mandatory
    full persistent state must not be serialized on every call
```

These requirements strongly favor a simple transactional relational core unless a specialized store earns its additional complexity.

---

# 2. Current external capability research

Research was performed on 2026-08-20 using current official documentation where possible.

## SQLite

Current SQLite documentation establishes that:

```text
FTS5 provides built-in/full extension-based full-text search;
recursive CTEs support hierarchical and graph-style queries;
JSON functions are built in by default in modern SQLite;
foreign-key constraints are supported but must be enabled explicitly
for each connection unless future defaults change;
WAL mode allows readers and a writer to proceed concurrently,
while still permitting only one writer at a time.
```

Relevant sources:

```text
https://www.sqlite.org/fts5.html
https://www.sqlite.org/lang_with.html
https://www.sqlite.org/json1.html
https://www.sqlite.org/foreignkeys.html
https://www.sqlite.org/wal.html
```

These capabilities map directly onto V1 requirements for text search, bounded relation traversal, semi-structured role-specific payloads, referential integrity, and the accepted initial concurrency envelope.

A critical implementation detail is that `PRAGMA foreign_keys = ON` must be set deliberately for every SQLite connection.

## PostgreSQL

PostgreSQL 18 provides, among many other capabilities:

```text
full-text search;
recursive CTEs;
JSONB with GIN indexing;
MVCC and multiple transaction-isolation levels;
strong concurrent multi-user transactional behavior.
```

Relevant sources:

```text
https://www.postgresql.org/docs/current/textsearch.html
https://www.postgresql.org/docs/current/queries-with.html
https://www.postgresql.org/docs/current/datatype-json.html
https://www.postgresql.org/docs/current/transaction-iso.html
```

The pgvector extension additionally supports exact vector search and ANN indexes including HNSW and IVFFlat:

```text
https://github.com/pgvector/pgvector
```

PostgreSQL + pgvector is therefore a technically strong candidate and an especially credible migration target if V1's single-writer/local assumptions cease to hold.

Its weakness for the current stage is not capability. It is that the server process, deployment/configuration, backup/upgrade surface, extension management, and broader concurrency machinery solve problems V1 has not yet demonstrated.

## Neo4j

Current Neo4j supports:

```text
property-graph storage and Cypher traversal;
full-text indexes;
vector indexes and vector-valued properties in recent versions;
local/self-managed deployment and Docker deployment.
```

Relevant sources:

```text
https://neo4j.com/docs/cypher-manual/current/indexes/
https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
https://neo4j.com/docs/operations-manual/current/installation/
```

Neo4j therefore can satisfy many requirements technically.

However, the promoted requirements call for **bounded local relation traversal**, not graph analytics as the central workload. Revision history, project-object state, rule traces, criterion Findings, and transactional relational integrity do not become simpler merely because relationships are first-class graph edges. A dedicated graph DBMS would also introduce an additional server/runtime and operational surface.

## Dedicated vector infrastructure

Qdrant and similar systems provide capable vector retrieval, filtering, APIs, and server deployment. Qdrant's normal local quickstart runs a separate service through Docker, while its Python ecosystem also offers a local mode for smaller use cases.

Relevant source:

```text
https://qdrant.tech/documentation/quick-start/
```

No current requirement demonstrates that this additional service boundary is necessary for V1.

The SQLite vector extension `sqlite-vec` is promising and highly portable, but its own current project documentation explicitly describes it as pre-v1 and warns that breaking changes should be expected:

```text
https://github.com/asg017/sqlite-vec
```

It should therefore not become a foundational V1 dependency merely to avoid implementing exact similarity over a modest embedding matrix.

---

# 3. Candidate architecture families

## Candidate A: Pure files/Git plus application scanning

Conceptually:

```text
structured files / Markdown / Git
        +
application-level scans and indexes
```

### Strengths

```text
excellent human inspectability
excellent source-level version history
minimal database infrastructure
strong alignment with the current development repository
```

### Failure against V1 needs

Dynamic project state, referential integrity, current-versus-historical queries, rule traces, criterion Findings, relation lookup, and atomic multi-object updates would require rebuilding substantial database behavior in application code.

### Result

```text
ELIMINATED AS THE PRIMARY RUNTIME ARCHITECTURE
```

Files/Git remain useful for source code, reviewable exports, and durable project-development documentation, but not as the sole application-state engine.

---

## Candidate B: Git/file-canonical methodological knowledge + SQLite runtime projection + SQLite project state

Conceptually:

```text
Git-tracked structured methodological knowledge
        -> compiled/rebuilt SQLite knowledge index

project state
        -> SQLite
```

### Strengths

```text
excellent human diff/review
natural Git history for reusable knowledge
SQLite provides fast runtime lookup
runtime knowledge indexes can be rebuilt
```

### Concerns

This creates two different persistence authorities and a compilation/synchronization boundary before V1 has shown that such separation is necessary. Cross-domain project-state/knowledge queries become application-level or attached-database operations, and exact referential integrity across the two authorities becomes more complicated.

### Result

```text
PLAUSIBLE, BUT DOMINATED FOR V1 BY A SINGLE SQLITE OPERATIONAL STORE
```

This design remains a useful fallback if future knowledge-authoring workflows prove that Git-native canonical authoring is substantially more valuable than transactional in-app editing.

---

## Candidate C: SQLite-centered local-first application store

Conceptually:

```text
                         +----------------------+
                         | large code/artifacts |
                         | filesystem / Git /   |
                         | artifact storage     |
                         +----------+-----------+
                                    |
                                    v
+---------------------------------------------------------------+
| ADS application/service                                       |
|                                                               |
|  SQLite authoritative operational store                       |
|    reusable knowledge identities/revisions/components          |
|    relations/rules/provenance/governance                      |
|    project metadata/state                                     |
|    execution-capability metadata                              |
|                                                               |
|  FTS5 derived lexical index                                   |
|  in-process exact semantic retrieval over rebuildable vectors |
|  application-layer minimal rule evaluator                     |
|  selective LLM context assembler                              |
+---------------------------------------------------------------+
                                    |
                                    v
                         deterministic human-readable
                         knowledge export / backup
```

### Strengths

```text
one transactional integrity boundary for knowledge + project metadata
very low local operational burden
natural relational representation for identities/revisions/references
bounded graph-like traversal through indexed relation tables + recursive CTEs
FTS5 for lexical retrieval
single file backup/portability characteristics
fits the accepted one-writer V1 envelope
straightforward testing and temporary databases
credible migration path to PostgreSQL
```

### Important constraints

```text
foreign_keys must be explicitly enabled
WAL still permits only one writer at a time
large binary artifacts remain outside SQLite
semantic vector search should remain derived/rebuildable
```

### Result

```text
SELECTED FOR V1
```

---

## Candidate D: PostgreSQL + pgvector integrated relational architecture

Conceptually:

```text
PostgreSQL
    relational project + knowledge state
    full-text search
    JSONB
    recursive relation queries
    pgvector semantic retrieval
```

### Strengths

```text
excellent transactional semantics
multi-writer concurrency
mature server database
strong integrated text/relational/vector capabilities
very strong future multi-user/cloud path
```

### Why it does not win V1

None of the capabilities that differentiate PostgreSQL operationally from SQLite are currently V1 requirements.

The project would pay additional installation, server lifecycle, configuration, backup, extension, and deployment complexity immediately in exchange for concurrency and scale headroom that is currently speculative.

### Result

```text
STRONG FUTURE MIGRATION TARGET, NOT CURRENT V1 DEFAULT
```

---

## Candidate E: Neo4j graph-first architecture

### Strengths

```text
excellent graph pattern/traversal ergonomics
native graph relationship model
current full-text and vector indexing
```

### Why it does not win

The project does not currently require:

```text
arbitrary graph algorithms
deep/high-frequency traversals across very large graphs
graph-native analytical workloads as the dominant access pattern
```

The actual workload includes substantial ordinary transactional state and revision semantics. Relational tables already answer required local graph queries cleanly at the expected scale.

### Result

```text
NOT JUSTIFIED FOR V1
```

Reconsider only if real workloads show graph traversal/analytics becoming a bottleneck or dominant product capability.

---

## Candidate F: Multi-store architecture

Examples:

```text
PostgreSQL + Qdrant
PostgreSQL + Neo4j + vector service
SQLite + graph server + vector server
```

### Result

```text
ELIMINATED FOR V1
```

It introduces consistency boundaries, backup/recovery coordination, deployment complexity, failure modes, and integration code without evidence that any V1 workload requires them.

---

# 4. Comparative decision matrix

The matrix intentionally uses qualitative judgments rather than fake decimal precision.

| Requirement area | Pure files | File + SQLite projection | SQLite-centered | PostgreSQL + pgvector | Neo4j-first |
|---|---|---|---|---|---|
| Stable identity/revisions | Strong | Strong | Strong | Strong | Strong |
| Referential integrity | Weak | Moderate | Strong | Strong | Moderate-Strong |
| Project-state integration | Weak | Moderate | Strong | Strong | Moderate |
| Typed local relations | Moderate | Strong | Strong | Strong | Excellent |
| Bounded traversal | Weak-Moderate | Strong | Strong | Strong | Excellent |
| Conditional rule storage | Moderate | Strong | Strong | Strong | Strong |
| Lexical search | Moderate | Strong | Strong | Strong | Strong |
| Semantic retrieval V1 | Requires custom index | Strong | Strong | Excellent | Strong |
| Historical reconstruction | Strong | Strong | Strong | Strong | Strong |
| Human-readable review | Excellent | Excellent | Strong via export | Strong via export | Strong via export |
| Atomic multi-object writes | Weak | Moderate | Strong | Strong | Strong |
| Local/offline simplicity | Excellent | Excellent | Excellent | Moderate | Weak-Moderate |
| Multi-writer future scale | Weak | Weak-Moderate | Moderate | Excellent | Strong |
| Operational burden | Very low | Low | Very low | Moderate | Moderate-High |
| Migration/reversibility | Moderate | Strong | Strong | Strong | Moderate |
| V1 fit without speculative machinery | Weak | Strong | **Excellent** | Strong but oversized | Weak |

The decision is therefore not that PostgreSQL or Neo4j are incapable. They are more capable in several dimensions. The decision is that those extra dimensions are not currently worth their operational cost.

---

# 5. Targeted SQLite viability spike

A synthetic local spike was performed specifically to challenge whether the selected embedded architecture was merely conceptually attractive but practically too weak.

A reproducible version is preserved at:

```text
experiments/architecture_spikes/sqlite_v1_viability.py
```

The spike is deliberately not a production benchmark. It uses synthetic data, warm process state, one machine, and simple query forms. Its purpose is to detect an obvious order-of-magnitude mismatch.

## Workload 1

```text
10,000 knowledge assets
10,000 revisions
30,000 components
100,000 typed relations
FTS5 corpus over methodological text
```

Observed in the design runtime:

```text
SQLite file size: ~26.3 MiB

stable identity lookup median:          ~0.003 ms
outgoing typed relation median:         ~0.004 ms
incoming typed relation median:         ~0.006 ms
FTS top-20 median:                      ~1.16 ms
bounded relation traversal depth 3:    ~0.9-1.0 ms
```

## Workload 2

A larger synthetic pass used:

```text
50,000 assets
500,000 relations
```

Observed:

```text
SQLite file size: ~70.3 MiB

stable identity lookup median:       ~0.003 ms
typed relation lookup median:        ~0.005 ms
FTS top-20 median:                   ~48 ms
bounded traversal depth 3:           ~2.1 ms
bounded traversal depth 4:           ~24.7 ms
```

The FTS query intentionally used terms appearing in a very large share of the synthetic corpus, making it less selective than a typical knowledge-catalog query.

## Exact semantic retrieval

Normalized dense vectors were searched with exact NumPy matrix-vector similarity rather than an ANN index.

Observed synthetic warm-memory timings:

```text
20,000 x 768 float32 vectors
    memory: ~58.6 MiB
    median exact top-20 search: ~1.1 ms

100,000 x 768 float32 vectors
    memory: ~293 MiB
    median exact top-20 search: ~7.5 ms
```

These numbers must not be treated as production guarantees.

They do establish an important architectural point:

> **At the expected V1 methodological-knowledge scale, there is no current performance evidence requiring a dedicated vector database or ANN index at all.**

Embedding generation and retrieval quality are likely to be more important V1 questions than nearest-neighbor search speed.

---

# 6. Selected V1 architecture

The selected architecture is a **SQLite-centered local-first modular application architecture**.

## 6.1 Authoritative operational state

One SQLite operational database should initially own the structured application state needed for:

```text
reusable methodological knowledge identities and revisions
knowledge components
relations
conditional rules
provenance/governance
project metadata and epistemic objects
project-to-knowledge revision references
criterion Findings
execution-capability metadata
re-evaluation obligations / traces where persisted
```

This is a logical scope. Exact table design is the next technical-specification task.

## 6.2 Relational core plus flexible payloads

Strongly queryable semantics should use explicit relational columns/tables.

Role-specific or narrative material can use text and carefully bounded JSON/semi-structured payloads where normalization would create low-value schema explosion.

The technical schema should therefore follow Foundation 020's hybrid structured/semantic boundary rather than attempting either complete normalization or one giant JSON document.

## 6.3 Lexical retrieval

Use SQLite FTS5 as a **derived/rebuildable** lexical index over the relevant knowledge text.

FTS is not the authority for knowledge content.

## 6.4 Semantic retrieval

V1 should begin with:

```text
rebuildable embeddings
        +
in-process exact similarity search
        +
structured/lexical candidate filtering where useful
        +
optional LLM reranking/reasoning
```

No dedicated vector DB is selected.

No ANN index is selected initially.

`sqlite-vec` may be tested later, but its current pre-v1 status means it should not be a core architectural dependency now.

## 6.5 Rule evaluation

Conditional methodological rules remain stored as structured data but evaluated by a small application-layer evaluator implementing Foundation 020 / Checkpoint 107 semantics:

```text
predicate reference
ALL
ANY
NOT
TRUE / FALSE / UNKNOWN
force
unknown behavior
consequence category
trace
```

A generic external rules engine is not selected.

## 6.6 Writer/read model

V1 should prefer:

```text
one application-owned write path
multiple read/query consumers where needed
SQLite WAL mode
short transactions
explicit foreign-key enforcement
```

The architecture should not rely on many independent subprocesses writing directly and competitively to the same database.

Execution workers can communicate results through the application/service boundary or controlled persistence interfaces.

## 6.7 Large artifacts remain outside

Do not store large datasets, trained models, array dumps, notebooks, or arbitrary binary outputs in SQLite merely because metadata lives there.

SQLite stores metadata/provenance/pointers.

The project filesystem, Git repository, and later artifact storage remain separate responsibilities under Foundation 018.

## 6.8 Human-readable knowledge export

Accepted reusable knowledge must remain reviewable outside opaque database tools.

The V1 design should provide deterministic, lossless-enough human-readable export of methodological knowledge/revisions for:

```text
review
diffing
debugging
backup/migration testing
Git preservation where useful
```

The runtime SQLite database remains the V1 operational authority. Export/index files are not allowed to silently become conflicting second runtime authorities.

---

# 7. Why PostgreSQL remains the primary migration target

Selecting SQLite should not make migration accidentally difficult.

The relational logical model should remain portable enough that a future move to PostgreSQL is credible.

PostgreSQL should be reconsidered when measured requirements show one or more of:

```text
routine concurrent writers
multiple users editing project/knowledge state concurrently
remote shared database access becomes a product requirement
SQLite write serialization becomes a measured bottleneck
server-side operations/backup/availability become preferable to local files
catalog/project scale materially exceeds the tested envelope
```

If semantic retrieval also grows, pgvector provides a path to keep vector search in the same relational system rather than automatically adding another service.

---

# 8. When specialized stores would become justified

## Dedicated vector infrastructure

Reconsider when evidence shows that exact in-process retrieval no longer meets memory/latency/throughput requirements or when vector-specific filtering/serving becomes operationally dominant.

Do not use raw asset count as the only trigger. Measure:

```text
embedding memory footprint
p95 retrieval latency
retrieval throughput
index update cost
retrieval quality requirements
filtering complexity
```

## Graph database

Reconsider if the product develops frequent deep or complex graph workloads that are materially awkward or slow in relational form, for example:

```text
large multi-hop dependency analysis
complex path matching as a central interactive workload
graph algorithms / communities / centrality become product features
```

Current bounded traversal requirements do not justify this.

## PostgreSQL

Reconsider primarily for concurrency, shared-server operation, operational maturity at multi-user scale, or later integrated vector search.

---

# 9. Architecture risks and mitigations

## Risk: SQLite single-writer ceiling

Mitigation:

```text
single application-owned write path
short transactions
WAL
measurement of write contention
clear PostgreSQL migration boundary
```

This is acceptable because one active writer is already part of the V1 requirements envelope.

## Risk: relational schema becomes too rigid for heterogeneous knowledge

Mitigation:

```text
normalize stable identities/references/rules/provenance
use bounded JSON/text payloads for heterogeneous facets
keep Foundation 020 knowledge-kind/reasoning-function separation
avoid one table per methodological subtype unless justified
```

## Risk: embeddings become hidden authority

Mitigation:

```text
embeddings/indexes are derived and rebuildable
canonical knowledge revision remains authoritative
record embedding model/version for reproducibility
```

## Risk: SQLite choice becomes permanent through accidental coupling

Mitigation:

```text
repository/service interfaces around persistence
portable logical identifiers
migration tests / deterministic exports
avoid SQLite-specific semantics in domain objects where unnecessary
```

## Risk: human knowledge review degrades compared with Git files

Mitigation:

```text
deterministic human-readable exports
provenance/revision UI
optional Git preservation of accepted exports
```

---

# 10. Explicit non-decisions

This architecture decision does **not** yet select:

```text
Python ORM / SQL toolkit
migration framework
exact physical schema
exact JSON payload structure
embedding model
embedding dimension
reranker
LLM provider
frontend stack
API framework
job queue
artifact store
cloud deployment
PostgreSQL migration date
exact backup strategy
final knowledge governance UI
```

It also does not claim SQLite is the final long-term database of the complete product.

---

# 11. Decision summary

The comparison supports the following V1 decision:

> **Use a SQLite-centered local-first operational architecture for reusable methodological knowledge and project metadata/state. Use FTS5 for rebuildable lexical indexing, in-process exact semantic retrieval over rebuildable embeddings initially, and a minimal application-level conditional-rule evaluator. Keep large artifacts outside the database. Do not introduce a dedicated graph database, vector database, external rules engine, or PostgreSQL server until a measured requirement justifies it. Preserve a credible relational migration path to PostgreSQL, with pgvector as a future integrated semantic-search option.**

This is a simplification decision, not a rejection of richer future infrastructure.

It follows Prototype V0's broader lesson:

```text
explicit machinery must earn its complexity
```

---

## Promotion audit

### Canonical decision

Warranted.

`D-011` was intentionally a temporary prohibition on premature architecture selection. Foundations 017-020 and Checkpoint 107 have now supplied the product model, knowledge model, relevance architecture, and implementation requirements that D-011 said were missing.

A new V1 architecture decision should therefore supersede D-011 for this scope while leaving still-unselected subsystems open.

### New foundation

Not warranted yet.

Foundation 020 remains the conceptual knowledge architecture. The selected V1 technology should now be made concrete through a technical specification rather than promoted as another broad conceptual foundation.

### Knowledge-map update

Warranted because future sessions now need a route from Foundation 020 / Checkpoint 107 to the selected V1 architecture.

### Major-change entry

Warranted because the project has crossed the long-standing D-011 boundary and selected its first V1 persistence/retrieval architecture family.

### Current-state update

Warranted.

---

## Exact continuation point

The next task is to write the **V1 technical architecture specification** for this selected SQLite-centered design.

That specification should make concrete, without yet building the full product:

```text
1. logical persistence boundaries and authoritative/derived state;
2. initial relational entity/table families;
3. knowledge identity + revision strategy;
4. component/relation/rule physical representation;
5. project-object integration and knowledge-revision references;
6. FTS5 indexing strategy;
7. embedding generation/storage/cache and exact-search interface;
8. rule-evaluation interface and trace format;
9. context-pack assembly boundary;
10. transaction/write ownership;
11. backup/export/migration strategy;
12. minimal architecture tests that would falsify the design before broad V1 implementation.
```

The specification should preserve a migration path to PostgreSQL and should not add specialized services unless this concrete design exposes a requirement the comparison missed.
