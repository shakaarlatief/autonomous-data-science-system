# Specification 001: V1 SQLite-Centered Technical Architecture

**Date:** 2026-08-20  
**Status:** Candidate technical specification v0.1; frozen for narrow architecture falsification before broad V1 implementation  
**Scope:** V1 methodological-knowledge, project-state, retrieval, rule-evaluation, context-assembly, provenance, and operational persistence architecture  
**Authority:** Technical contract for the next architecture spike. It is subordinate to current canonical decisions and Foundations 017-020. It is not yet a broad implementation authorization.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Purpose

D-028 selected a SQLite-centered local-first architecture for V1 after technology-neutral requirements, architecture comparison, external capability research, and a synthetic viability spike.

The next risk is different:

> selecting SQLite correctly at the architecture-family level but implementing it in a way that creates avoidable lock-in, weak history, brittle schema semantics, or an unnecessarily expensive future migration.

This specification therefore optimizes for two goals simultaneously:

```text
V1 simplicity and speed of development
        +
professional long-term architectural seams
```

The design should be good enough that a future move from SQLite to PostgreSQL, exact search to ANN search, or relational traversal to a specialized graph projection can be a bounded infrastructure evolution rather than a rewrite of methodological meaning, project semantics, rule logic, or application behavior.

The project should not deliberately under-build V1. It should also not pre-pay the complexity of infrastructure whose requirements have not appeared.

---

## 2. Governing design principles

The specification is governed by these already-promoted conclusions:

```text
what the system persists
    !=
what the LLM receives on every reasoning call

methodological knowledge
    !=
project-specific state

methodological meaning
    !=
execution implementation

retrieval
    !=
applicability
    !=
relevance

static semantic relation
    !=
conditional methodological rule

current state
    !=
event history

human-facing workflow
    !=
canonical internal representation
```

The following implementation-specific principles are candidate consequences of those foundations and must be tested by the architecture spike:

1. authoritative semantic state should use explicit relational structure where query/integrity value is high;
2. flexible narrative material may remain text or validated semi-structured JSON;
3. accepted knowledge revisions should be immutable in content;
4. derived indexes must be rebuildable;
5. large artifacts remain outside the operational metadata database;
6. transactions must remain short and must not span LLM/network/embedding calls;
7. SQL/storage-dialect details must remain behind application persistence ports;
8. durable domain identities must not depend on SQLite rowids or database-local sequences;
9. V1 must preserve a credible PostgreSQL migration path by construction rather than by future cleanup.

---

## 3. Scope and non-goals

### 3.1 In scope

```text
reusable methodological knowledge
knowledge revisions/components/relations/rules
knowledge provenance and governance
knowledge collections/navigation metadata
project epistemic and decision state needed by the methodological brain
exact knowledge-revision references from project state
criterion Findings
project event/audit provenance
execution-capability metadata
artifact metadata/references
lexical retrieval
semantic retrieval cache/interface
methodological-horizon construction
conditional-rule evaluation
selective LLM context-pack assembly
schema migration/integrity/backup/export boundaries
```

### 3.2 Explicitly not specified yet

```text
frontend framework
public HTTP/API framework
authentication/authorization system
multi-tenant architecture
cloud deployment
job queue
full execution scheduler
model serving
large-artifact storage service
embedding model
LLM provider
reranking model
ORM / SQL toolkit
schema migration library
final UI design
```

The architecture must leave room for these without pretending they are already requirements.

---

# 4. High-level runtime architecture

```text
                         HUMAN / UI / DEVELOPER TOOLS
                                   |
                                   v
+-------------------------------------------------------------------+
|                    ADS APPLICATION / SERVICE                      |
|                                                                   |
|  Domain + application logic                                      |
|      |                                                            |
|      +--> KnowledgeRepository / ProjectStateRepository ports      |
|      +--> RelationQuery port                                      |
|      +--> RuleEvaluation service                                  |
|      +--> Retrieval / HorizonBuilder                              |
|      +--> ContextAssembler                                        |
|      +--> ExecutionCapability registry                            |
|      +--> Backup / Export services                                |
|                                                                   |
|  SQLite adapter                                                   |
|      authoritative operational relational state                  |
|      FTS5 derived lexical index                                   |
|      rebuildable embedding cache                                  |
|                                                                   |
+--------------------------+----------------------------------------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
    filesystem / Git                future external
    project code                    services only when
    large artifacts                 requirements justify them
    reports/models
```

The application layer owns semantics. SQLite is an adapter implementing the accepted V1 persistence contract.

No business-domain code should depend directly on FTS5 syntax, SQLite PRAGMAs, rowids, or other SQLite-only behavior.

---

# 5. One operational database with explicit logical modules

V1 should use one logical SQLite operational database per ADS installation/workspace, with projects keyed by stable project identity.

This preserves one atomic integrity boundary for global methodological knowledge and project metadata/state while avoiding cross-database foreign-key and synchronization problems.

Table families should use explicit logical prefixes so later PostgreSQL migration can map them cleanly into schemas if useful:

```text
sys_    schema/version/maintenance metadata
kg_     global reusable methodological knowledge
prj_    project-specific state and epistemic objects
exec_   execution-capability metadata
idx_    rebuildable lexical/semantic indexes and cache metadata
```

The prefixes are organizational, not separate persistence authorities.

Large datasets, trained models, generated arrays, notebooks, source repositories, and other large artifacts remain outside SQLite. SQLite stores metadata, content hashes where useful, provenance, and stable locators.

---

# 6. Persistence ports are a mandatory migration seam

The application must depend on domain-oriented interfaces rather than raw database calls scattered throughout the codebase.

Minimum conceptual ports include:

```text
KnowledgeRepository
ProjectStateRepository
RelationQuery
RuleStore / RuleTraceRepository
LexicalIndex
SemanticIndex
HorizonRepository or HorizonTraceStore
ContextPackTraceStore
ExecutionCapabilityRepository
ArtifactMetadataRepository
UnitOfWork
BackupService
ExportService
```

The exact programming language/interface syntax is not selected here.

The portability requirement is behavioral:

```text
application/domain services
        -> stable ports
        -> SQLite adapter now
        -> PostgreSQL / specialized index adapter later if required
```

A future database migration must not require rewriting rule semantics, methodological assets, project-object meaning, horizon logic, or UI workflows merely because SQL dialect/storage changes.

---

# 7. Durable identity and time representation

## 7.1 Domain identities

All durable externally referenceable entities should use application-generated RFC 9562 UUID identities.

Preferred generation strategy:

```text
UUIDv7
```

because it is standardized, globally unique, time-ordered, independent of database sequences, and maps naturally to PostgreSQL's native UUID type.

The schema and application must treat IDs as opaque. Ordering by UUID must never substitute for explicit semantic time/order fields.

SQLite representation:

```text
canonical lowercase UUID text
```

Future PostgreSQL representation:

```text
UUID
```

SQLite `INTEGER PRIMARY KEY`, `AUTOINCREMENT`, or rowid values may be used only for internal/derived implementation details where identity is not part of the domain contract, such as an FTS helper row.

## 7.2 Timestamps

Application/domain timestamps must be timezone-aware UTC.

Canonical SQLite representation should be fixed-format RFC3339/ISO-8601 UTC text, for example:

```text
2026-08-20T08:30:00.123456Z
```

Future PostgreSQL adapters may map the same domain value to `timestamptz`.

Business semantics must not depend on SQLite-specific date/time coercion.

---

# 8. Core SQLite schema discipline

## 8.1 STRICT authoritative tables

Authoritative core tables should use SQLite `STRICT` mode where practical.

This reduces SQLite's dynamic-typing ambiguity and makes the operational schema behave more like a conventional relational database.

Portable storage primitives should remain deliberately small:

```text
TEXT
INTEGER
REAL
BLOB
NULL
```

Booleans should use constrained integers when persisted in SQLite:

```text
INTEGER CHECK(value IN (0, 1))
```

Dates/times use canonical UTC TEXT as described above.

## 8.2 JSON is a bounded escape hatch, not the primary data model

JSON may be used for:

```text
role-specific optional payloads
small rule arguments/consequences
retrieval-profile details
non-core metadata
provider-specific capability metadata
```

Strongly queryable relationships, identities, statuses, revision links, provenance links, and project-to-knowledge references should remain relational.

JSON payloads must:

```text
have an explicit payload/schema version where evolution matters
be validated in application code
use json_valid() CHECK constraints where practical in SQLite
use deterministic canonical serialization for content hashing
```

Future PostgreSQL adapters may map these payloads to JSONB without exposing JSONB-specific behavior to the domain layer.

## 8.3 Avoid SQLite-only domain semantics

Do not use the following as durable domain assumptions:

```text
rowid identity
AUTOINCREMENT domain IDs
SQLite REPLACE semantics
SQLite-specific date arithmetic
business logic hidden in triggers
FTS rank values as persistent truth
binary SQLite JSON formats
arbitrary SQL stored in methodological rules
```

SQLite-specific functionality is acceptable inside the SQLite adapter when it implements a portable domain contract.

---

# 9. Global methodological-knowledge table families

The exact DDL remains subject to the architecture spike, but V1 should preserve the following families and integrity semantics.

## 9.1 Stable knowledge-node identity

A lightweight identity registry should provide one referential target for independently addressable assets and components:

```text
kg_node
    node_id
    node_type = ASSET | COMPONENT
    created_at
```

This is a technical supertype only. It does not collapse the semantic distinction between `KnowledgeAsset` and `KnowledgeComponent`.

Its purpose is to let relations reference either type with real foreign keys instead of polymorphic string IDs without database integrity.

## 9.2 Knowledge assets

```text
kg_asset
    asset_id -> kg_node
    stable slug / canonical key
    current_accepted_revision_id
    created_at
```

`current_accepted_revision_id` is a convenience/current-state pointer, not the history itself.

## 9.3 Immutable content revisions

A revision envelope should separate stable identity from immutable content revision:

```text
kg_content_revision
    revision_id
    node_id
    revision_no
    created_at
    semantic_content_hash
```

For an accepted/published revision, semantic content is immutable. A correction creates another revision.

Governance state should not require rewriting the immutable content row. Governance transitions should therefore live in a separate current-governance record plus append-only governance history/events.

Conceptually:

```text
kg_revision_governance
    revision_id
    current_status
    reviewed/accepted metadata

kg_governance_event
    event_id
    revision_id
    transition
    actor/provenance
    occurred_at
```

This permits a revision to move from candidate -> reviewed -> accepted -> superseded without changing the content that historical project reasoning referenced.

## 9.4 Asset revision content

```text
kg_asset_revision
    revision_id -> kg_content_revision
    asset_id
    intrinsic_kind
    title
    purpose
    scope
    known limitations / counterexamples
    reasoning-function metadata
    retrieval profile
    applicability specification
    context requirements
    semantic-check description/metadata
```

Strongly queried fields should be explicit columns or child tables. Rich explanatory content may remain narrative text.

## 9.5 Components

```text
kg_component
    component_id -> kg_node
    parent_asset_id
    stable component_key
    component_kind
    created_at

kg_component_revision
    revision_id -> kg_content_revision
    component_id
    parent_asset_revision_id
    typed payload / narrative body
    ordering metadata where useful
```

Component revision rows must be demonstrably tied to an asset revision of the same parent asset. The spike must test whether this invariant is best enforced entirely through composite foreign keys or through a database constraint plus application validation.

## 9.6 Narrative facets

Non-addressable explanatory material should not be forced into the stable-node registry.

```text
kg_narrative_facet
    owning asset revision
    facet kind
    position/key
    body
```

The row may have an internal surrogate key, but that key is not a stable methodological identity exposed to project reasoning.

---

# 10. Static semantic relations

Relations are stable methodological objects with independent revision/provenance when material.

Conceptually:

```text
kg_relation
    relation_id
    source_node_id -> kg_node
    target_node_id -> kg_node
    relation_type
    current_accepted_revision_id

kg_relation_revision
    relation_revision_id
    relation_id
    revision_no
    scope/conditions
    rationale
    created_at

kg_relation_revision_governance / provenance
```

Important requirements:

```text
incoming lookup by target
outgoing lookup by source
filter by relation type
bounded recursive traversal
revision-aware historical inspection
```

Indexes must cover the actual access patterns, at minimum:

```text
(source_node_id, relation_type)
(target_node_id, relation_type)
```

V1 does not optimize for arbitrary graph analytics.

---

# 11. Conditional methodological rules

Rules must remain declarative methodological guidance, not executable code stored in the database.

A rule specification is owned by an exact asset/component content revision so history is naturally pinned.

Conceptually:

```text
kg_rule_spec
    rule_spec_id
    owner_content_revision_id
    stable rule_key within owner
    condition_json
    consequence_type
    consequence_payload_json
    force
    unknown_behavior
    rationale
```

## 11.1 Minimal condition AST

The stored condition language should be limited to the conceptual forms:

```text
Predicate(name, arguments)
ALL([...])
ANY([...])
NOT(condition)
```

Predicate evaluation returns:

```text
TRUE
FALSE
UNKNOWN
```

Unknown must propagate according to explicit tri-valued semantics rather than silently becoming false.

Stored rules must not contain:

```text
raw SQL
Python code
JavaScript
shell commands
arbitrary eval expressions
```

Predicates are application-registered semantic functions that access project state through `ProjectStateRepository`/query ports.

## 11.2 Consequences

Consequence categories remain small and inspectable, such as:

```text
activate concern
open/activate Question
require evidence
recommend option
raise/lower priority
apply validity constraint
constrain Claim
request clarification
require revalidation
```

A rule consequence may influence project work but must not silently perform an analytical action such as dropping a feature or selecting a model.

## 11.3 Rule trace

Consequential evaluations must be reconstructable:

```text
rule_spec_id
owner knowledge revision
project-state snapshot/version references used
predicate outcomes
TRUE/FALSE/UNKNOWN aggregate result
force
unknown behavior
consequence produced
evaluator version
occurred_at
```

The trace may be persisted selectively for consequential reasoning rather than for every cheap exploratory evaluation.

---

# 12. Provenance architecture

Provenance must be relationally attachable at the granularity required by Foundation 020 and Checkpoint 107.

Minimum source registry:

```text
kg_provenance_source
    source_id
    source_type
    title
    stable locator/reference
    author/organization where known
    source date where known
    metadata
```

Separate link tables should attach sources to important revision types rather than using an unconstrained polymorphic `target_type + target_id` table.

Examples:

```text
kg_content_revision_provenance
kg_relation_revision_provenance
kg_rule_spec_provenance
```

This intentionally accepts a few explicit junction tables in exchange for real foreign-key integrity.

---

# 13. Knowledge collections

Human navigation groupings should remain non-authoritative organizational structures:

```text
kg_collection
kg_collection_member
```

Members reference stable knowledge nodes.

A collection must not imply applicability, methodological dependence, or validity merely because two assets are grouped together.

---

# 14. Project-state persistence pattern

Foundation 018 deliberately contains project objects with different lifecycle semantics. V1 must not undo that work by forcing all project objects into one generic JSON table or one universal revision lifecycle.

## 14.1 Technical identity registry

A lightweight project identity registry may provide a common FK target for cross-object relations/events:

```text
prj_entity
    entity_id
    project_id
    entity_type
    created_at
```

As with `kg_node`, this is a technical identity supertype, not a claim that all project objects have identical semantics.

## 14.2 Typed lifecycle tables

Each important object family should retain type-appropriate state/history.

Examples:

```text
Definition
    stable identity + semantic revisions/supersession

Question
    stable identity + open/resolved/deferred lifecycle + evidence links

Evidence
    normally immutable record with provenance

Finding
    normally append-only/immutable assertion, with supersession/challenge links

Claim
    evidence/finding support and current validity/scope

Decision
    stable identity + decision revisions/supersession/rationale

Run
    immutable configuration snapshot + mutable execution status
    + append-only run events; not a semantic-revision chain per heartbeat
```

This means V1 should use common technical patterns where useful but should not impose one universal project-object revision table merely for implementation convenience.

## 14.3 Minimum typed state needed by the methodological brain

The first narrow schema spike should cover at least:

```text
Project
Variable / Dataset identity as required by predicates
Definition
Question
Evidence
Finding
Constraint
Decision
```

and enough Proposal/Investigation/Run metadata to prove the knowledge-to-work boundary.

Other Foundation 018 object families may be added before broad product implementation as their concrete workflows are specified.

---

# 15. Exact project-to-knowledge revision references

When reusable knowledge materially generated, constrained, interpreted, or justified project reasoning, the project must reference the exact revision used.

The default durable link should be revision-specific:

```text
project object / object revision
        -> exact kg content revision
        + influence/reference type
        + optional rationale/context
```

A later accepted knowledge revision must not mutate historical project meaning.

Rule traces additionally reference the exact `kg_rule_spec` involved.

Criterion Findings must support:

```text
subject project entity
criterion knowledge revision
verdict
conditions
supporting Evidence
rationale
```

without introducing a universal `Assessment` object.

---

# 16. Project events and audit history are not event sourcing

The system should maintain append-only events for audit/provenance where valuable:

```text
QuestionOpened
DefinitionChanged
FindingCreated
DecisionChanged
RunCompleted
KnowledgeRevisionReferenced
HumanClarificationReceived
```

The event stream explains how the project evolved.

Current project state remains stored explicitly in the relevant current tables/pointers. V1 should not require replaying the entire event stream to reconstruct current state.

This preserves Foundation 018's `current state != event history` distinction and avoids introducing full event sourcing without evidence.

---

# 17. Execution capabilities and artifacts

`ExecutionCapability` remains separate from methodological meaning.

Conceptually:

```text
exec_capability
    capability_id
    methodological asset reference
    implementation/provider key
    implementation version/compatibility
    input contract metadata
    configuration mapping metadata
    output contract metadata
    limitations
```

Methodological relevance must never be inferred merely from execution availability.

Large artifact content remains outside the operational DB.

Artifact metadata should include enough to support provenance:

```text
artifact_id
project_id
artifact kind
stable locator/path/URI
content hash where practical
size/media type
producer Run or source reference
created_at
```

Credentials and API secrets must not be stored as plaintext methodological/project metadata. Secret-management architecture is a later subsystem.

---

# 18. Lexical search architecture

SQLite FTS5 is a derived index, not the authority for knowledge.

The application should generate a deterministic search document for each searchable current accepted asset revision from selected fields such as:

```text
title
purpose
scope
aliases/synonyms where available
selected component text
selected narrative facets
limitations
```

Conceptually:

```text
idx_search_document
    asset_id
    revision_id
    document_schema_version
    canonical_text
    content_hash

idx_knowledge_fts
    FTS5 derived projection
```

A full rebuild command must be able to regenerate the index from authoritative knowledge.

Incremental refresh after an accepted knowledge revision should occur through the application index service, preferably in the same short database transaction for cheap lexical state. V1 should avoid trigger-heavy FTS synchronization because it adds SQLite-specific hidden behavior with little value at the expected write rate.

Search results must rejoin authoritative tables and should ignore stale/superseded revisions by default.

---

# 19. Semantic retrieval architecture

V1 semantic retrieval uses a provider abstraction:

```text
EmbeddingProvider
SemanticIndex
```

The authoritative knowledge layer stores no semantic truth in vectors.

Embeddings are derived from a deterministic search-document representation and keyed by at least:

```text
knowledge revision
content hash
embedding model/provider key
model revision/version where available
vector dimension
embedding schema/preprocessing version
```

A practical V1 cache may store normalized float32 vectors as BLOBs in a derived `idx_embedding` table and load the current candidate matrix into process memory for exact similarity search.

The binary representation is an adapter detail and must not escape through the `SemanticIndex` interface.

Missing or stale embeddings must be detectable. The system must not silently interpret "embedding unavailable" as "knowledge irrelevant".

No ANN index or vector service is selected initially.

Migration path:

```text
exact in-process SemanticIndex
        -> pgvector / ANN / dedicated vector provider later
```

without changing the methodological horizon or knowledge model.

---

# 20. Methodological-horizon construction

`HorizonBuilder` is an application service, not a database query pretending to be the whole reasoning process.

Candidate flow:

```text
current project signals / task intent
        |
        v
high-recall candidate union
    structured activation
    lexical retrieval
    semantic retrieval
    explicit related knowledge
        |
        v
deduplicate / preserve retrieval provenance
        |
        v
cheap applicability prerequisites/exclusions
        |
        +--> missing required context -> Question / UNKNOWN
        |
        v
semantic applicability checks / flexible reasoning
        |
        v
relevance / recommendation / requiredness reasoning
        |
        v
bounded methodological horizon
```

The architecture must retain why each candidate entered or left the horizon.

A methodological horizon is derived by default. For consequential LLM reasoning, experiments, or debugging, a compact horizon snapshot/manifest should be persistable.

The persistence schema should be designed after the spike establishes which trace fields are genuinely useful rather than logging every intermediate score automatically.

---

# 21. LLM context-pack architecture

`ContextAssembler` consumes project state and a bounded methodological horizon and produces a task-specific context pack.

It must enforce an explicit size/token budget and support mixed content:

```text
compact structured project facts
selected evidence/findings/constraints
knowledge asset/revision references
selected rule outcomes
selected methodological narrative
```

The persistent database must not be shaped around one model's prompt serialization.

For consequential reasoning calls, persist a manifest sufficient to identify:

```text
context assembly version
budget
project objects/revisions supplied
knowledge revisions supplied
rule traces supplied
ordering/priority
rendered context hash
token estimate
LLM/provider/model configuration reference where appropriate
```

The full rendered prompt may be persisted only when justified by evaluation/debugging/privacy requirements. The manifest is the minimum architectural requirement.

---

# 22. Transaction ownership and concurrency rules

## 22.1 One application-owned write path

V1 should have one application/service layer responsible for authoritative database writes.

Background workers and execution processes should return results through controlled interfaces rather than each independently treating the SQLite file as a shared free-for-all write target.

Multiple read consumers are allowed.

## 22.2 SQLite connection contract

Every operational SQLite connection must enable:

```text
PRAGMA foreign_keys = ON
```

Database initialization should establish:

```text
journal_mode = WAL
```

The default V1 durability profile should use:

```text
synchronous = FULL
```

unless a measured performance result later justifies a documented weaker durability profile.

A bounded busy timeout/retry policy should handle short lock contention rather than hanging indefinitely.

`PRAGMA optimize` should be incorporated into schema-change/maintenance workflows rather than hand-maintaining planner statistics.

## 22.3 Short transactions only

Never hold an authoritative write transaction open while waiting for:

```text
LLM responses
embedding APIs
human input
network calls
long analytical execution
large file operations
```

Typical write transactions should be semantic units such as:

```text
publish one knowledge revision and update its current pointer
record one project Finding + knowledge references + event
accept one Decision + rationale + provenance
record one completed Run metadata snapshot
```

SQLite-specific adapters may use `BEGIN IMMEDIATE` for planned write units so lock acquisition fails early/predictably. This is not a domain-level transaction primitive.

## 22.4 Index work and transactions

Cheap FTS updates may be part of a publish transaction.

Expensive embedding generation must happen outside the transaction. After generation, a short transaction may insert/update the derived embedding cache if the source content hash is still current.

---

# 23. Schema migrations

All authoritative schema changes must occur through ordered migrations.

Minimum migration metadata:

```text
sys_schema_migration
    version
    name
    checksum
    applied_at
    application/build version where useful
```

Rules:

```text
no ad-hoc production DDL
startup refuses a database schema newer than the application understands
migrations are forward-tested against representative fixtures
potentially destructive migrations require a verified backup first
migration scripts remain reviewable in source control
```

Downgrade migrations are not required by default. Recovery from a bad migration may use a pre-migration backup plus a corrected forward migration.

The migration framework/library remains unselected until the schema spike clarifies whether a dedicated library is valuable.

---

# 24. Backup, recovery, integrity, and export

The professional V1 backup path should use SQLite's supported online backup mechanism through the chosen language binding, or `VACUUM INTO` where a compact snapshot is specifically useful.

Do not make a naive filesystem copy of a live WAL database the primary backup strategy.

A verified backup should be accompanied by enough metadata to identify:

```text
schema version
application version
creation time
source database identity
artifact/reference manifest where relevant
```

Recovery verification must include:

```text
PRAGMA integrity_check or quick_check according to maintenance level
PRAGMA foreign_key_check
schema migration/version verification
selected semantic invariant checks
```

Derived FTS/embedding indexes must be rebuildable after restore.

The system must also support deterministic human-readable export of accepted reusable knowledge, including stable IDs/revisions/provenance sufficiently for review, diffing, debugging, and migration verification.

The export is not a second runtime authority.

---

# 25. Portability contract: design now so PostgreSQL is a migration, not a rewrite

PostgreSQL + pgvector is the preferred first migration family if SQLite's envelope is exceeded.

The V1 design must therefore obey these portability rules:

```text
1. application-generated UUID domain identities;
2. no domain dependence on SQLite rowid or AUTOINCREMENT;
3. timezone-aware domain timestamps with explicit adapters;
4. standard relational FKs/UNIQUE/CHECK semantics for core integrity;
5. SQLite STRICT as an adapter-level strengthening, not domain logic;
6. JSON only behind typed application models and versioned payload schemas;
7. no arbitrary business logic in SQLite triggers;
8. FTS5 isolated behind LexicalIndex;
9. vector BLOB/exact NumPy search isolated behind SemanticIndex;
10. PRAGMA/connection behavior isolated in SQLite adapter;
11. SQL statements live in persistence modules, not domain/application services;
12. canonical exports use storage-neutral domain forms;
13. rule AST contains semantic predicates, never SQL fragments;
14. relation traversal uses RelationQuery semantics, not raw recursive-SQL assumptions;
15. transaction boundaries are application UnitOfWork concepts.
```

Expected PostgreSQL evolution:

```text
UUID TEXT                -> native UUID
UTC TEXT timestamps      -> timestamptz
validated JSON TEXT      -> JSONB where useful
FTS5 adapter             -> PostgreSQL text-search adapter
exact SemanticIndex      -> pgvector / exact or ANN adapter
SQLite write coordinator -> normal server-DB transaction manager
same domain/application interfaces remain
```

A migration may require DDL/data-conversion work. It should not require rethinking the methodological knowledge representation or project reasoning architecture.

---

# 26. Security and trust boundary

The operational database is an application-owned trusted data file, not an arbitrary user-uploaded SQLite database.

User datasets must be treated as artifacts/data inputs rather than blindly attached as operational schemas.

All SQL must be parameterized. Stored rules cannot contain executable code or raw SQL.

Secrets/tokens/API keys must not be stored as ordinary plaintext metadata.

Broader authentication, authorization, encryption-at-rest, and multi-user security architecture are outside this V1 subsystem specification and must be designed before any deployment context that requires them.

---

# 27. Observability

Persistence and retrieval operations should emit structured observability information without making observability part of correctness semantics.

Useful measurements include:

```text
query latency by operation class
write-transaction duration
lock/busy retry count
FTS candidate latency
semantic retrieval latency
horizon candidate counts by stage
context-pack size/token estimate
index freshness/staleness
backup duration/status
integrity-check status
```

The observability layer must remain downstream/read-only in accordance with P-022.

---

# 28. Architecture falsification gate before broad implementation

Broad V1 implementation is blocked until a narrow vertical architecture spike demonstrates the following.

## FT-01: Identity/revision historical integrity

Create a knowledge asset revision R1, create project reasoning that pins R1, publish R2, and verify that:

```text
new reasoning resolves current R2
historical project reasoning still reconstructs R1 exactly
R1 content remains unchanged
```

## FT-02: Component and relation integrity

Represent assets/components/relations from at least Histogram, Random Forest, and Missing Data. Verify foreign-key integrity, incoming/outgoing typed lookups, and bounded traversal without loading the whole knowledge network.

## FT-03: Missing Data rule reconstruction

Encode a small but real branch of the `Missing_Data.md` structure and prove:

```text
TRUE/FALSE/UNKNOWN behavior
missing context generates/activates the correct Question
hard safeguard is distinguishable from strategy recommendation
no rule silently executes a project action
rule trace identifies exact knowledge revision + project facts
```

## FT-04: Criterion-Finding chain

Represent Prediction-Time Feature Eligibility as:

```text
Question -> Evidence -> criterion Finding -> Decision
```

and verify the Finding pins the exact criterion knowledge revision.

## FT-05: Retrieval/horizon coverage fixture

Create a curated methodological catalog fixture including the six stress-test topics plus distractors. Use representative project/task queries and verify that hybrid candidate retrieval can recover expected relevant knowledge at high recall without passing the full catalog onward.

This test evaluates retrieval coverage/ranking behavior, not just nearest-neighbor speed.

## FT-06: Missing/stale embedding behavior

Remove or stale selected embeddings and verify that:

```text
index health reports the gap
knowledge is not silently classified irrelevant
lexical/structured fallback remains available
embedding regeneration can repair the cache
```

## FT-07: Context-budget enforcement

Construct a synthetic large project state and catalog. Verify that `ContextAssembler` stays within its configured budget while retaining required/blocking information and records a reproducible context manifest.

## FT-08: Transaction atomicity and crash boundary

Inject failures during representative semantic write units and verify there is no partially published knowledge revision, orphaned current pointer, half-written criterion Finding, or broken project-to-knowledge reference.

No test may depend on a network call occurring inside the transaction.

## FT-09: Reader/writer behavior

Under WAL, run multiple readers while one controlled writer performs short transactions. Verify correctness, bounded lock handling, and absence of long write transactions.

## FT-10: Backup/restore

Create a live backup, restore it into a separate location, and pass:

```text
integrity_check
foreign_key_check
schema-version check
historical revision reconstruction
knowledge export equivalence checks
```

## FT-11: Derived-index rebuild

Delete/recreate the FTS and embedding-derived state and verify authoritative knowledge/project state is unchanged and retrieval indexes can be reconstructed.

## FT-12: PostgreSQL-portability review/spike

Before broad schema growth, validate that the core domain schema and repository interfaces can map to PostgreSQL without semantic redesign.

At minimum this must review/test:

```text
UUID mapping
UTC timestamp mapping
foreign keys and uniqueness
JSON payload mapping
revision/current-pointer model
project-to-knowledge references
relation queries
rule storage
transaction boundaries
```

The exact PostgreSQL test mechanism may use a temporary CI/service container once implementation tooling is chosen.

---

# 29. Architecture acceptance criteria

The candidate technical specification may be promoted from v0.1 to the accepted V1 implementation specification only if the spike shows:

```text
all correctness-critical FT tests pass
no semantic invariant requires bypassing the persistence ports
no major object family is forced into an obviously wrong lifecycle model
no unacceptable SQLite locking/contention appears under the V1 write model
retrieval/context behavior is testable without full-state serialization
backup/recovery is reliable
PostgreSQL migration remains a bounded adapter/schema evolution
```

If a test fails, the response should be the smallest correction supported by evidence.

Failure of one part, such as exact semantic search, does not automatically justify replacing the authoritative operational database.

---

# 30. What remains intentionally unselected after this specification

```text
exact full DDL
ORM / SQL toolkit
migration library
embedding model/provider
lexical/semantic fusion algorithm
reranker
LLM provider
HTTP/API framework
frontend framework
job queue
artifact-storage backend
PostgreSQL migration date/trigger threshold
```

These choices should be made at the layer where their requirements become concrete.

---

# 31. Exact next step

Implement a **narrow architecture falsification spike**, not the broad product.

The spike should include only enough code/schema to test FT-01 through FT-12, using real representative knowledge from the current stress-test set.

After the gate:

```text
PASS
    -> promote this specification with corrections to accepted V1 technical contract
    -> choose implementation libraries/tooling
    -> begin bounded V1 subsystem implementation

FAIL
    -> diagnose which architectural assumption failed
    -> revise only the affected layer
    -> rerun the gate before broad implementation
```

This is the project's main protection against discovering late that the implementation architecture was structurally wrong.