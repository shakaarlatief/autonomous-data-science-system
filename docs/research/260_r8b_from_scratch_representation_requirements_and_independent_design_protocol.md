# Research 260: R8-B From-Scratch Representation Requirements and Independent Design Protocol

**Date:** 2026-09-23
**Status:** REPRESENTATION REQUIREMENTS FROZEN / NO REPRESENTATION TARGET SELECTED / INDEPENDENT DESIGN NEXT / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Immediate parent:** Research 259
**Accepted architecture basis:** Research 248-259
**Repository base:** 181991476bb7091f30235674acf6bfb2b065df59
**Scope:** Derive the representation/content requirements for the future Project knowledge and Project Development System from first principles before choosing Markdown, structured files, databases, graph structures, metadata schemas, event logs, generated indexes or other implementation mechanisms.
**Authority:** Architecture research protocol. This record freezes the problem decomposition and comparison criteria only. It does not select a representation target, amend Specification 028, authorize AO-10 implementation, or authorize physical migration.

## 1. Why a separate representation stage is required

R8-A selected responsibility and workspace residency:

    project/system/
    project/engineering/
    project/research/
    project/reproductions/
    project/knowledge/

It deliberately did not decide how the information and control semantics inside those boundaries should be represented.

The project owner has now made the design freedom explicit:

    current files are evidence
    current metadata is evidence
    current schemas are evidence
    current document templates are evidence
    current serialization is evidence

None is a target requirement merely because it already exists.

Therefore the next problem is not:

> How should the current Markdown/JSON system be moved into the new folders?

It is:

> What future information/control objects exist, what behavior must they support, and what representation architecture best realizes those requirements?

## 2. Scope boundary

This stage designs representation for the Project plane, especially:

    project/knowledge/
        governance
        evidence
        operations
        history

    project/system/
        durable machine contracts
        instance policy
        control state
        capture/candidate state
        transition state
        continuity state
        activation/orchestration evidence
        generated views/indexes
        retrieval/search acceleration

It also covers the bounded root machine locator:

    project_anchor.json

It does not redesign ordinary Product source-code serialization, runtime business databases or analytical artifact formats unless a cross-plane contract requires a Project-side representation decision.

## 3. First-principles information/control classes

The accepted R7 classes are preserved as responsibility/authority inputs, but they are refined here by representation behavior rather than by current file family.

### RC1 Durable human knowledge

Includes durable governing, evidentiary, operational and historical understanding whose primary value is meaningful human review.

Examples of responsibilities:

    architecture rationale
    specifications
    owner/project decisions
    research synthesis
    qualification interpretation
    runbooks/procedures
    collaboration guidance
    historical milestone narrative

Representation needs:

    excellent long-form readability
    high-quality diffs
    stable deep references where justified
    rich links/citations
    easy manual editing
    durable Git history
    bounded machine-readable identity/authority metadata only where needed

### RC2 First-class semantic identity and authority descriptors

Some knowledge/control entities require machine-resolvable identity independent of path.

Examples:

    current governing sources
    specifications
    first-class decisions
    workstreams
    obligations
    procedures
    authority-scoped semantic owners
    transition identities

Representation needs:

    deterministic parsing
    stable identity
    explicit lifecycle and authority role
    explicit relation targets
    schema/version evolution
    no path-as-identity assumption
    source ownership without a universal registry unless independently justified

This class does not imply that every file receives metadata.

### RC3 Independent cross-object semantic facts

Some relations/facts have no natural single prose carrier or have an independent lifecycle.

Examples may include:

    a genuinely independent relation between two semantic owners
    alias/redirect identity transitions
    framework-materialization lineage
    cross-object transition records
    obligation-realization bindings where neither endpoint naturally owns the binding

Representation needs:

    independent identity where justified
    deterministic relation semantics
    lifecycle/provenance separate from either endpoint when required
    bounded admission so this does not become a universal semantic database

### RC4 Authored Project-system instance policy

Project-specific machine-readable policy/configuration belongs to the ADS instance, not generic PSMF mechanism.

Examples:

    enabled integrations
    local routing policy
    provider/tool selection
    project-specific boundaries
    bridge/control enablement policy
    project-specific overrides/extensions

Representation needs:

    human inspectability
    deterministic machine parsing
    strict validation
    low-to-moderate write frequency
    safe Git review
    explicit separation from reusable framework code

### RC5 Durable Project-control facts

State that materially affects future Project behavior and must survive interaction/process loss.

Examples:

    active/paused workstream state
    current Project-system mode
    accepted open obligations
    authority regime locator
    transition/cutover state
    consequence-bearing continuity state
    branch/workstream purpose state when it cannot be reconstructed safely elsewhere

Representation needs:

    durable across machines/sessions
    directly recoverable without generated views
    deterministic writes
    expected-revision/stale-write protection
    bounded concurrency semantics
    human inspectability sufficient for break-glass recovery
    clear separation from derived cache/state

### RC6 Control-cycle receipts and observations

Potential logical records include:

    EventInterpretation
    ControlClosure
    AuthorityReceipt
    ActionContract
    BridgeReceipt
    activation-miss observation
    obligation-realization observation
    postflight result

Not every control cycle warrants durable persistence.

Representation needs:

    consequence-proportional persistence
    immutable/auditable form when retained
    exact source/revision binding where relevant
    efficient append/write behavior
    bounded retention
    promotion path when an observation becomes durable Project knowledge
    no authority laundering

### RC7 Capture/candidate information

Unreviewed understanding and migration candidates.

Representation needs:

    explicitly non-authoritative
    easy creation
    provenance to source interaction/evidence
    review/disposition state
    promotion into natural owner rather than authority flip in place
    bounded cleanup/retention

### RC8 Machine contracts and schemas

Defines how the Project Development System validates structured representations.

Representation needs:

    versioned contract identity
    deterministic validation
    language/tool portability where valuable
    migration/evolution rules
    framework versus ADS-instance separation
    human inspectability
    no requirement that one schema language validate every artifact family

### RC9 Generated views and indexes

Examples:

    current orientation
    subject navigation
    identity/authority indexes
    workstream projections
    obligation/risk views
    source catalogs
    dependency/reference graphs

Representation needs:

    no unique accepted truth
    complete rebuildability
    source-revision manifest
    deterministic semantic content
    deletable/recreatable
    machine and/or human projections chosen by use case
    explicit stale detection

### RC10 Retrieval/search/query acceleration

Examples:

    full-text index
    relational query index
    semantic/vector index
    graph traversal projection

Representation needs:

    derived only unless a later explicit architecture decision says otherwise
    disposable/rebuildable
    cannot resolve governing authority by ranking alone
    clear source revision/freshness
    local/offline fallback for required Project recovery
    adapter boundary so optional engines do not become semantic owners

### RC11 Durable evidence attachments and reproduction artifacts

Examples:

    structured experiment outputs
    machine logs retained as qualification evidence
    diagrams
    bounded data fixtures
    exact reproduction packages
    externally sourced immutable evidence where licensing permits

Representation needs:

    content integrity/hash binding
    explicit provenance
    retention policy
    not forced into prose formats
    separation between evidence bytes and human interpretation
    Git suitability assessment by size/change pattern

### RC12 Ephemeral runtime/cache state

Examples:

    temporary parser caches
    local execution scratch state
    disposable session acceleration
    uncommitted search cache
    transient transport state

Representation needs:

    never required for semantic recovery
    safe deletion
    no unique authority
    explicit promotion/retention path if material meaning emerges

## 4. Representation properties that must be derived per class

For every RC class, the selected design must explicitly answer:

    authority role
    canonical versus derived
    identity model
    lifecycle
    ownership
    update locality
    expected write frequency
    expected volume/growth
    mutability versus append-only behavior
    human readability requirement
    machine determinism requirement
    query/traversal requirement
    diff/merge requirement
    concurrency requirement
    provenance requirement
    retention requirement
    privacy/public-safety requirement
    offline/recovery requirement
    framework/instance ownership
    schema/version-evolution requirement
    migration/export requirement

No representation family may be selected without mapping these properties.

## 5. Cross-cutting hard requirements

### RR-01 Single accepted meaning

The architecture MUST avoid accidental duplicate authority.

A richer query/index layer may project accepted sources but MUST NOT silently become a second source of truth.

### RR-02 Recovery does not depend on derivatives

Break-glass reconstruction MUST remain possible from authored/canonical state without requiring generated views, optional databases, embeddings or external services.

### RR-03 Path is not semantic identity

When first-class identity is justified, moves/renames MUST NOT destroy semantic continuity.

### RR-04 Selective structure, not universal metadata

The architecture MUST NOT require structured metadata on every repository file merely for uniformity.

Structure exists when machine behavior, authority, identity, provenance, lifecycle or retrieval requirements justify it.

### RR-05 Rich human knowledge remains first-class

Long-form rationale, research, procedures and explanations MUST remain pleasant to author/review and must not be forced into database rows or fragmented atomic records solely for machine convenience.

### RR-06 Machine-critical state is not prose-parsed

State required for deterministic control MUST have an explicit machine contract and MUST NOT depend on natural-language extraction for basic correctness.

### RR-07 Generated views are disposable

Any generated index/view/cache MUST be reproducible from its declared source boundary and generation logic.

### RR-08 Consequence-proportional persistence

The system MUST NOT persist every low-consequence control-cycle detail merely because it can.

Persistence burden must be justified by:

    recovery value
    audit value
    qualification value
    future control value
    governance/evidence value

### RR-09 Provenance is explicit where material

Durable evidence and promoted knowledge MUST retain enough provenance to explain origin, review/promotion and source revision where those affect trust.

### RR-10 Safe evolution

Every structured representation MUST define how its schema/version evolves and how older material remains interpretable or migratable.

### RR-11 Git compatibility is evaluated, not assumed

Git remains current durable Project-development authority, but every proposed canonical artifact must still be assessed for:

    meaningful diffs
    merges
    binary behavior
    repository growth
    reviewability
    reconstruction

A database file is not rejected merely because it is a database, and a text file is not accepted merely because Git can diff it.

### RR-12 PSMF upgradeability

Generic Project Development System mechanism must remain separable from ADS-specific instance policy and state.

Representation choices MUST NOT make framework upgrades overwrite project-specific meaning.

### RR-13 Product/Project separation

The Product runtime MUST NOT require Project-system storage or Project knowledge representation for runtime correctness.

### RR-14 Public/private boundary

Public canonical representation MUST remain public-safe.

Private complements may be referenced abstractly without leaking private locations or contents.

### RR-15 Reference integrity

A representation or migration design MUST account for inbound references, semantic references, generated projections, external triggers and historical citations.

### RR-16 Concurrency and stale-write behavior

Canonical machine-controlled state MUST define stale-write/precondition behavior.

Human-authored Git content may rely on normal Git merge/review where appropriate; machine state that can be concurrently changed requires stronger explicit guards.

### RR-17 No technology by prestige

Graph, vector, database, event-sourcing, knowledge-graph or agent-memory technologies are selected only when the workload requires them.

### RR-18 No inheritance by familiarity

Markdown, JSON, JSON Schema, one-declaration-per-carrier, numbered documents and current metadata fields receive no preference merely because the repository already uses them.

## 6. Accepted contracts that enter as hypotheses, not untouchable implementation constraints

The next design must explicitly test the continued value of:

    path != identity
    path != authority
    selective first-class identity
    source-owned semantic subject membership
    controlled semantic subjects
    generated views contain no unique accepted truth
    capture != promotion
    one declaration per ordinary carrier
    carrier-resident declaration instances
    no mass historical retrofit

The first six have strong conceptual/empirical support.

The latter representation-sensitive rules, especially declaration shape/count/residency, are deliberately open to amendment if a better representation preserves the underlying semantics more cleanly.

## 7. Representation families that must be compared

The design must compare at least:

    F1 plain/rich Git-native documents with minimal structured metadata
    F2 structured document envelopes/front matter
    F3 separate metadata sidecars
    F4 bounded canonical structured registries
    F5 Git-authoritative sources plus rebuildable relational/query database
    F6 database-backed canonical Project control state
    F7 graph-first canonical or derived semantic representation
    F8 append/event-log representation for retained control evidence
    F9 hybrid combinations by RC class

The comparison must distinguish:

    canonical storage
    authored machine contract
    generated projection
    query index
    optional acceleration cache

so a useful technology is not rejected merely because it should be derived rather than authoritative.

## 8. Technology-neutral evaluation matrix

Each candidate must be evaluated against:

    authority clarity
    human authoring quality
    deterministic validation
    diff/review quality
    merge/concurrency behavior
    path-move robustness
    identity/relationship expressiveness
    provenance
    update locality
    cold-start/recovery
    rebuildability
    schema evolution
    query/search capability
    performance at projected scale
    tooling/runtime dependency
    PSMF extraction/upgrade compatibility
    migration complexity
    operational complexity
    failure blast radius
    public/private safety

No single scalar score is required. Material trade-offs must remain visible.

## 9. Current external mechanism evidence to carry into design

This stage does not select technologies, but current mechanism facts have been checked so the next comparison is not based on folklore.

### TOML

TOML 1.0 is UTF-8, maps unambiguously to hash-table-like data, permits comments and rejects duplicate key definitions.

Python 3.11+ includes tomllib for TOML 1.0 parsing, though the standard library parser does not write TOML.

Implication:

    TOML is a credible human-authored structured representation,
    but write/edit tooling must be evaluated separately.

### JSON Schema

The current published JSON Schema dialect is Draft 2020-12.

Implication:

    JSON Schema remains a credible language-neutral validation candidate,
    but current use does not grandfather it.

### SQLite

SQLite provides mature relational storage, JSON functions and FTS5 full-text search.

Implication:

    SQLite is a credible generated query/search substrate and a possible
    control-state candidate, but canonical-database use must be evaluated
    against Git/recovery/concurrency semantics rather than assumed.

## 10. Independent-design protocol

Representation architecture has enough downstream commitment that a second-model design should be genuinely independent rather than merely adversarial after ChatGPT has already selected a target.

Protocol:

    1. freeze this requirements record at an immutable Git commit
    2. open MC-0026 against that exact commit
    3. Claude independently derives a representation architecture
       without reading any later ChatGPT representation candidate
    4. ChatGPT independently derives its representation architecture
       from the same frozen requirements
    5. only after both are durable do the models receive the other's design
    6. perform comparative reconciliation
    7. owner decides any material architecture selection/amendment

Claude may read upstream accepted architecture needed to understand the requirements.

Claude must not read later commits containing ChatGPT's representation candidate before writing its independent proposal.

ChatGPT must not read Claude's proposal before freezing its own candidate.

This is not a blind study of the problem history; it is independent target synthesis from a shared accepted requirements boundary.

## 11. Required independent-design outputs

Each model should produce:

    representation class mapping RC1-RC12
    canonical-versus-derived authority model
    proposed authored carrier formats
    proposed structured metadata/semantic model
    Project-control state representation
    receipt/event persistence model
    schema/contract strategy
    generated-view strategy
    query/search/index strategy
    graph role
    database role
    cold-start/recovery behavior
    Git/diff/merge/concurrency behavior
    PSMF framework/instance seam
    migration implications
    Specification 028 implications
    rejected alternatives and falsifiers

The proposal must include enough physical examples to test the architecture without treating example syntax as sacred.

## 12. No premature file-level migration

The next representation design may inspect current files for evidence.

It MUST NOT begin by classifying every current file.

The order remains:

    representation architecture
        ->
    explicit owner acceptance/amendment
        ->
    Specification 028 delta
        ->
    file-level disposition manifest
        ->
    compatibility/migration graph
        ->
    qualification
        ->
    physical migration only after later authorization

## 13. Current state

    R8B_REQUIREMENTS=FROZEN
    REPRESENTATION_TARGET=UNSELECTED
    CURRENT_FILE_INTERNALS=EVIDENCE_ONLY
    CURRENT_METADATA=EVIDENCE_ONLY
    RC_CLASSES=12
    RR_REQUIREMENTS=18
    REPRESENTATION_FAMILIES_TO_COMPARE=9

    INDEPENDENT_DESIGN_REQUIRED=true
    CHATGPT_CANDIDATE=NOT_YET_FROZEN
    CLAUDE_CANDIDATE=NOT_YET_PRODUCED
    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=FREEZE_BASE_AND_OPEN_MC0026_INDEPENDENT_REPRESENTATION_DESIGN
