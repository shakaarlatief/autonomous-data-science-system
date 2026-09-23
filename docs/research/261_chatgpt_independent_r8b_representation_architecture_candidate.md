# Research 261: ChatGPT Independent R8-B Representation Architecture Candidate

**Date:** 2026-09-23
**Status:** CHATGPT INDEPENDENT CANDIDATE FROZEN / MC-0026 CLAUDE CANDIDATE PENDING / NO COMPARATIVE EXPOSURE YET / NO PHYSICAL MIGRATION
**Parent:** Research 260
**Frozen independent-design base:** 1fe4bbe4b2658532359411825d3b1d819a6c4c68
**Candidate name:** GCHR-DQI — Git-Canonical Hybrid Representation with Derived Query Index
**Independence:** This candidate was derived before reading any Claude MC-0026 Message 001. Claude has not yet produced or exposed its candidate to ChatGPT.
**Scope:** Select a complete candidate representation/content architecture for the future Project knowledge and Project Development System from the frozen Research 260 requirements. This is a candidate for later comparative reconciliation, not an owner-accepted target.
**Authority:** Architecture recommendation only. Specification 028 remains unchanged. No physical migration, AO-10 implementation, authority switch or PSMF extraction is authorized.

## 1. Design conclusion

The recommended architecture is a deliberately heterogeneous representation stack.

Different Project information classes have materially different authoring, authority, write-frequency, concurrency, query and recovery requirements. Forcing them into one universal representation would optimize one class by harming another.

The selected candidate is:

    CANONICAL DURABLE LAYER
        human-first durable knowledge
            Markdown
            optional bounded TOML governed envelope when machine semantics
            are actually required

        human-authored Project-system policy
            TOML

        machine-maintained durable Project-control facts
            small sharded JSON records

        independent structured semantic facts
            bounded TOML records in their natural responsibility owner
            only when no carrier endpoint naturally owns the fact

        retained consequential receipts
            immutable individual JSON records

        evidence/reproduction bytes
            native format
            plus bounded manifest when provenance/integrity requires it

    DERIVED ACCESS LAYER
        generated human orientation
            Markdown

        generated machine orientation
            JSON

        relational/semantic/query index
            rebuildable SQLite
            relational tables + edge projection + FTS

        optional graph exports
            derived

        optional semantic/vector retrieval
            derived cache behind adapter

    EPHEMERAL RUNTIME LAYER
        scratch execution state
        parser caches
        transport/session acceleration
        detailed low-consequence telemetry
            local/disposable
            never required for recovery

The candidate explicitly rejects:

    one universal file format
    one universal metadata schema
    a canonical Project knowledge SQL database
    a canonical graph database
    a universal semantic object registry
    broad event sourcing
    metadata on every file
    prose-parsing for machine-critical state

## 2. Why hybrid representation is the primary design decision

RC1 and RC5 have opposite optimization pressures.

Durable human knowledge wants:

    readable prose
    expressive argument
    citations
    diagrams
    careful review
    durable diff history
    low-friction editing

Durable machine control wants:

    deterministic state
    exact schema
    atomic guarded writes
    stale-write detection
    bounded records
    no natural-language interpretation

A single representation cannot optimize both without either turning human knowledge into awkward structured records or forcing machine control to infer state from prose.

The architecture therefore shares semantic contracts and identity rules while allowing representation to vary by responsibility.

## 3. Canonical authority model

Git remains the durable versioned container for accepted Project source artifacts.

Git does not itself decide semantic authority.

Canonical meaning is owned by:

    human knowledge carrier
    structured instance-policy record
    structured control-state record
    independent semantic-fact record
    retained evidence/receipt record

according to its accepted responsibility and contract.

Derived components may accelerate reconstruction but never become authority merely because they are easier to query.

The authority stack is:

    canonical Git-tracked sources
        ->
    validated normalized semantic model
        ->
    derived query/index layer
        ->
    generated views/search/graph/vector projections

A lower layer may be regenerated from the layer above.

The reverse is not required for recovery.

## 4. RC1 durable human knowledge

### 4.1 Selected carrier

Primary carrier:

    Markdown

Markdown is selected for long-form Project knowledge because the workload is predominantly explanatory, argumentative, procedural and evidentiary prose.

The selection is not based on inheritance.

Reasons:

    direct human readability without special software
    mature editing/tooling
    good Git textual diffs
    natural links/code/tables/diagrams
    low migration lock-in
    easy extraction by agents and search tooling
    native coexistence with repository source code

Alternative rich-document formats are not currently justified by requirements that Markdown fails.

### 4.2 Governed envelope

A durable human carrier gets structured metadata only when it participates in machine-governed semantics.

Selected mechanism:

    one optional TOML envelope at the beginning of the Markdown carrier

Illustrative example:

    +++
    contract = "project-knowledge-carrier/1"
    id = "architecture:project-system-representation"
    kind = "architecture-rationale"
    authority = "governing"
    lifecycle = "active"
    subjects = ["project-system", "representation"]

    [[relations]]
    type = "supersedes"
    target = "architecture:legacy-representation"
    +++

    # Human-readable title

The example is illustrative, not a frozen field schema.

### 4.3 Why TOML for the human-authored envelope

TOML is selected over strict embedded JSON for this human-authored boundary because:

    syntax is designed for human-authored structured configuration
    comments are possible
    duplicate key definitions are invalid
    parsing semantics are explicit
    Python 3.12+ has a standard-library TOML parser
    the envelope can remain small and readable

The governed envelope is constrained to a JSON-compatible semantic subset for schema validation.

In particular:

    semantic timestamps use explicit string formats where needed
    TOML date/time native values are not required
    highly nested document content does not belong in the envelope

The envelope is metadata/control, not a second prose document.

### 4.4 Selective, not universal

An envelope is required when a carrier needs one or more of:

    first-class semantic identity
    machine-resolved authority role
    machine-resolved lifecycle
    controlled subject membership
    typed semantic relations
    explicit non-Git provenance required by validation
    participation in promotion/authority closure

Plain Markdown is allowed when none of those capabilities is required.

Therefore:

    repository file != semantic object
    project/knowledge document != mandatory metadata object

### 4.5 No duplicated fields by default

The candidate deliberately avoids metadata merely because it is conventional.

Examples:

    title
        read from the first document heading when possible

    author
        use Git provenance unless semantic authorship differs materially

    created / modified timestamp
        use Git history unless an event time is semantically meaningful

    conversation title / interaction environment / primary collaborator
        record only when that provenance is substantively required

    summary
        keep in prose or generate unless a stable authored summary has
        independent value

This directly prevents the current metadata-heavy document style from becoming a future requirement.

## 5. Human knowledge content architecture

The candidate rejects one universal document template.

Instead, the substantive body follows a small number of role-specific content contracts.

These are authoring expectations, not mandatory headings unless a validator later demonstrates value.

### Governance / architecture rationale

Expected semantic content:

    problem/context
    selected or governing position
    rationale
    alternatives/trade-offs where material
    consequences
    supersession/evolution conditions
    references to evidence

### Normative specification

Expected semantic content:

    scope
    normative behavior/constraints
    invariants
    interfaces/contracts
    acceptance/qualification conditions
    amendment/version semantics

### Decision record

Expected semantic content:

    decision
    authority/owner
    relevant alternatives
    accepted evidence
    consequences
    reversal/supersession conditions

A decision should not duplicate a separate architecture specification unless the content has an independent lifecycle.

### Research/evidence

Expected semantic content:

    question/hypothesis
    method
    evidence
    findings
    limitations/uncertainty
    implications
    promoted governing impact, if any

Raw machine evidence stays in native/structured artifacts rather than being pasted into prose without need.

### Operational procedure

Expected semantic content:

    scope
    preconditions
    procedure
    verification
    failure/recovery
    escalation/decision boundary

### Historical record

Expected semantic content:

    event/milestone
    state/outcome
    significance for reconstruction
    durable references

No future global numbered Research / Checkpoint family is required by this candidate.

Stable semantic IDs are used only where first-class reference/identity requires them.

Human filenames should normally be semantic and readable.

Existing numbered IDs remain migration aliases/evidence until explicitly dispositioned.

## 6. RC2 first-class semantic identity and authority descriptors

Human carriers use the optional governed envelope.

The normalized semantic model should expose only fields justified by behavior.

Candidate core concepts:

    contract/profile identity
    optional stable semantic ID
    artifact/semantic kind
    authority role when applicable
    lifecycle when applicable
    controlled subject memberships when applicable
    typed outbound relations when applicable
    provenance extension when Git alone is insufficient

Profile-specific fields extend the core.

There is no requirement that every profile expose every field.

Identity uniqueness is validated across all admitted semantic sources.

Paths remain locators.

Moves update location, not semantic identity.

## 7. RC3 independent cross-object semantic facts

Default rule:

    relation/fact lives with the natural semantic owner

Examples:

    A supersedes B
        normally declared by A if A owns the supersession assertion

    procedure governs workstream
        normally declared by the governing procedure or workstream
        according to the relation contract

A standalone structured fact is admitted only when:

    neither endpoint naturally owns it
    the fact has independent lifecycle/provenance
    the fact must survive endpoint representation changes independently
    putting it on one endpoint would create false ownership

Selected standalone representation:

    TOML record

The record lives under the natural Project responsibility area, not in one global registry merely because it is structured.

This preserves the strongest prior H1/H2 evidence:

    source-local by default
    bounded independent spine only for genuinely independent facts

## 8. RC4 authored Project-system instance policy

Selected representation:

    TOML files under the ADS instance side of project/system

Rationale:

    policy is primarily human-authored
    machines must parse it deterministically
    comments are useful
    Git review matters
    write frequency is low/moderate
    policy should not be hidden in Python source
    policy should not be encoded as prose

Generic PSMF code owns:

    policy schema
    parser
    validation
    defaults that are truly generic

ADS instance owns:

    provider/tool selection
    integration enabling
    local routing rules
    ADS-specific boundaries
    project-specific overrides
    bridge/transition enablement policy

A framework upgrade must not overwrite ADS instance policy.

## 9. RC5 durable Project-control facts

Selected representation:

    small sharded JSON records

These records are machine-maintained canonical Project state.

Examples:

    one workstream record per first-class active/paused workstream
    one obligation record per independently governed obligation
    bounded authority-regime state
    bounded transition state
    bounded continuity state

The architecture rejects one giant state.json.

### 9.1 Why JSON here

Control records are predominantly machine-written.

JSON provides:

    deterministic standard machine serialization
    broad schema/tool support
    easy atomic rewrite
    stable pretty textual Git diffs
    no writer dependency equivalent to TOML editing
    natural JSON Schema validation

Human break-glass inspection remains feasible.

Human explanations belong in Project knowledge, not comments inside machine state.

### 9.2 Sharding rule

Split state by independent lifecycle/write domain.

Do not create one file per trivial field.

Do not combine unrelated control domains merely to reduce file count.

Sharding criteria:

    independent write frequency
    concurrency/conflict boundary
    independent lifecycle
    independent identity
    different access/recovery requirements

### 9.3 Concurrency and stale writes

Every machine mutation uses guarded expected-state semantics.

At minimum, the mutation binds:

    target record
    expected Git blob hash or equivalent exact revision
    expected semantic state/version when applicable
    intended transition

Before commit:

    all preconditions are rechecked

For a multi-record transition:

    preconditions for all records are checked
    all writes are staged
    one Git commit publishes the coherent transition

If any record drifted:

    fail stale
    reconstruct/re-plan
    do not auto-merge consequential state

Separate records allow unrelated branches/agents to change unrelated state with ordinary Git merge behavior.


## 10. RC6 control-cycle receipts and observations

The candidate selects:

    SELECTIVE PERSISTENCE

It explicitly rejects broad event sourcing.

Persist a durable receipt when one or more applies:

    consequential mutation/action occurred
    authority closure must be auditable
    recovery may need the control decision
    bridge/transition qualification needs evidence
    activation miss / owner-reminder dependence occurred
    accepted obligation changed realization state
    high-consequence resolution failed visibly
    postflight discovered an architecture/control defect

Ordinary low-consequence fast-path interactions do not create durable repository receipts.

### 10.1 Retained receipt format

Selected representation:

    one immutable JSON record per retained receipt

Reason for individual records rather than one append-only JSONL file:

    parallel writers do not append to the same file
    Git merge conflicts are reduced
    each receipt has independent provenance/content hash
    selective retention/removal is easier
    corruption is localized

Receipts may be partitioned physically by time or category when scale warrants it.

The logical receipt identity is independent of its path.

### 10.2 Detailed telemetry

High-volume detailed execution telemetry may use:

    local SQLite
    local logs
    provider/runtime telemetry

as ephemeral runtime evidence.

It is not Project authority.

A material observation is promoted into a retained receipt/capture/evidence carrier.

## 11. RC7 capture/candidate information

No single capture format is required.

Two primary forms:

    human-rich candidate
        Markdown + candidate envelope

    machine-first candidate
        JSON record

Both must encode:

    explicitly non-authoritative status
    origin/provenance
    review/disposition state
    intended natural owner when known

Promotion does not flip a candidate to governing in place.

Instead:

    update/create natural canonical owner
    bind provenance to candidate/evidence
    record review disposition
    close/archive/delete candidate according to retention policy

This retains capture != promotion while removing the assumption that every capture is one specific JSON profile.

## 12. RC8 machine contracts and schemas

Selected primary structural schema technology:

    JSON Schema Draft 2020-12

This is a new selection based on requirements, not inheritance.

Why:

    language-neutral data-model validation
    mature ecosystem
    expressive profile composition
    explicit version/dialect declaration
    suitable for JSON records
    can validate normalized JSON-compatible objects parsed from TOML
    envelopes/policy

The candidate rejects:

    one universal schema for every artifact
    schema as a substitute for cross-record semantic validation
    Python classes as the sole normative contract

Validation stack:

    syntax parser
        Markdown envelope / TOML / JSON / native manifest

    structural schema
        JSON Schema profiles

    normalized internal model
        implementation types

    semantic validators
        uniqueness
        relation closure
        authority
        lifecycle
        workstream/obligation rules
        public/private restrictions
        reference integrity

    derived-index build
        fails closed on admitted-source defects

JSON Schema authority lives with project/system/contracts.

Implementation models must remain test-equivalent to schemas.

### 12.1 Schema evolution

Every structured contract has:

    stable contract identity
    explicit version
    compatibility policy
    migration/read-old strategy

Derived SQLite schema does not require in-place migration for correctness.

When the derived schema changes:

    delete and rebuild from canonical sources

is always a valid recovery path.

## 13. RC9 generated views and indexes

Generated artifacts are use-case projections, not one mandatory family of JSON files.

Selected durable generated outputs:

    project/system/generated/orientation/current.md
        human fast orientation

    project/system/generated/orientation/current.json
        machine fast orientation

These may be committed for immediate cold-start acceleration, provided freshness validation binds them to their source revision.

They are not required for break-glass recovery.

Other generated projections are persisted only when an actual consumer requires a durable file.

Examples:

    compatibility export
    diagram
    release/qualification report
    machine handoff bundle

The candidate does not preserve the current rule that every identity/authority/subject/workstream view must exist as a separate committed JSON file.

## 14. RC10 derived query/search/index substrate

Selected standard acceleration substrate:

    rebuildable SQLite index

It is derived, not canonical.

It should be safe to delete completely.

Rebuild inputs:

    governed Markdown envelopes
    standalone semantic records
    Project-system policy/control records
    retained receipts admitted for indexing
    relevant plain Markdown text
    artifact manifests
    Git revision metadata where required

Candidate relational model includes conceptual tables such as:

    sources
    identities
    authority_roles
    subjects
    relations
    references
    workstreams
    obligations
    receipts
    artifact_manifests
    FTS document index

Exact SQL schema is not frozen here.

### 14.1 Why SQLite

The workload is repository-local, relational/graph-shaped and full-text-heavy but does not currently justify a network database service.

SQLite offers:

    relational querying
    transactions for index construction
    FTS5 full-text search
    JSON functions where useful
    one portable local file
    mature Python/runtime support

Because the database is derived, its binary Git characteristics do not matter:

    it should normally be gitignored or otherwise treated as cache
    it may be rebuilt at a known source revision

### 14.2 Freshness membrane

The SQLite index records:

    source repository revision
    index schema version
    generator version
    admitted source digests where necessary

A query may use the index for discovery/acceleration.

A consequential authority decision may use indexed data only when freshness/contract checks prove the index matches the required canonical boundary.

If absent/stale:

    rebuild
    or direct-scan canonical sources
    or fail visibly if safe closure is impossible

The index may never outrank canonical sources.

## 15. Graph role

The Project semantics are graph-shaped.

That does not imply graph-database storage.

Selected role:

    canonical typed relations in source-owned envelopes/records
        ->
    derived relational edge table
        ->
    generated graph projections when useful

SQLite recursive queries or in-memory graph construction are sufficient at current/projected scale unless evidence proves otherwise.

A graph database remains an optional future derived adapter.

It is not canonical.

Falsifier:

    repeated graph workloads become materially difficult or too slow in
    the relational/derived model at actual project scale

Even then, the first response is a derived graph projection, not an authority move.

## 16. Vector/semantic retrieval role

Optional only.

Embeddings/vector indexes may improve discovery across long-form evidence/history.

They must remain:

    derived
    rebuildable
    source-revision bound
    non-authoritative
    subordinate to deterministic authority resolution

No safe Project operation may require an embedding service.

## 17. RC11 durable evidence attachments and reproduction artifacts

Do not convert binary/native evidence into Markdown/JSON merely for uniformity.

Selected model:

    native evidence bytes
        +
    bounded provenance/integrity manifest when required

Manifest representation:

    TOML for human-reviewed artifact/reproduction manifests

The manifest may record:

    logical artifact identity when needed
    media/type
    cryptographic digest
    provenance/source
    generation/reproduction command or environment reference
    retention role
    relation to human interpretation

A binary file may use an adjacent manifest because inline metadata is impossible or unsafe.

This is a justified sidecar exception.

Large artifact storage is not preselected here.

If Git suitability fails due to size/change pattern, a later evidence-storage policy may select Git LFS or an external immutable/object store with repository-tracked digest/retrieval contract.

Private storage locations remain non-public.

## 18. RC12 ephemeral runtime/cache state

Ephemeral state is explicitly outside Project authority.

Possible mechanisms:

    local SQLite
    temp files
    in-memory state
    tool/runtime logs
    local cache directory

Properties:

    gitignored
    disposable
    reconstructable
    no unique accepted truth
    no cold-start dependency

If ephemeral state produces durable meaning:

    capture / retained receipt / evidence promotion

is required.


## 19. Cold-start and recovery architecture

The accepted R8-A break-glass rule is preserved.

Machine path:

    project_anchor.json
        ->
    authored canonical locator/control source
        ->
    governing Project knowledge / Project-system state

Generated orientation is optional acceleration:

    project_anchor.json
        ->
    current.json

only when fresh and available.

The anchor itself contains locators and contract versioning, not unique substantive truth.

Human path:

    root README
        ->
    Project overview / knowledge entry / recovery procedure

and optionally:

    generated current.md

Recovery must still work if:

    generated directory is deleted
    SQLite index is deleted
    vector cache is unavailable
    activation/orchestration process is down

## 20. PSMF framework versus ADS instance seam

Reusable PSMF mechanism owns:

    envelope parser
    TOML/JSON adapters
    schema engine
    normalized semantic model
    identity/relation validation
    generated-view framework
    SQLite index builder
    authority/reconstruction algorithms
    guarded write primitives
    receipt/capture mechanism
    transition mechanism
    generic provider/tool adapters when project-agnostic

ADS instance owns:

    actual knowledge carriers
    actual semantic IDs/subjects
    actual Project policy TOML
    actual control-state JSON
    actual workstream/obligation state
    actual provider/tool selection
    actual integration bindings/configuration
    actual captures/receipts
    actual authority regime
    project-specific schema/profile extensions when justified

Framework updates may evolve generic schemas/mechanisms through explicit compatibility rules.

They must not overwrite ADS instance state or policy.

## 21. Content examples: what current families become conceptually

These are representation examples, not file-level migration decisions.

### Current Research files

Future pattern:

    durable research synthesis
        Markdown evidence carrier

    raw result
        native/JSON evidence artifact

    machine qualification result
        structured evidence/receipt

No requirement for global Research NNN numbering.

### Current Checkpoint files

Future pattern:

    material human milestone
        history/evidence Markdown carrier when independent value exists

    ordinary control transition
        structured control record / retained receipt / Git history

    current orientation
        generated view

Therefore one Markdown checkpoint per project transition is not a future requirement.

### Current model-collaboration thread bundle

Future responsibilities may split into:

    active collaboration/control state
        project/system structured state

    reviewer request
        human-readable governed carrier or structured request,
        depending complexity

    returned substantive review
        evidence Markdown carrier when durable

    routing/index
        generated/system state

    resolution
        governing decision/evidence relation, not necessarily an additional
        duplicated file

The current BRIEF / THREAD / STATE / RESOLUTION / messages layout is evidence, not a target.

### Current semantic declarations

Future human carriers use the bounded TOML envelope when needed.

Machine-first Project state uses native JSON records.

No embedded strict JSON code block inside Markdown is required by the candidate.

## 22. Current retained-contract dispositions

### KEEP

    path != identity
    path != authority
    selective first-class identity
    source-owned semantic subject membership
    controlled semantic subjects
    generated views contain no unique accepted truth
    capture != promotion
    no mass historical retrofit
    authority resolution independent of retrieval ranking

### AMEND

Current:

    one declaration per ordinary carrier

Candidate:

    at most one governed envelope per human carrier
    one primary first-class carrier identity when justified
    multiple bounded relations/subjects may live in that envelope
    independent semantic facts get independent records only when lifecycle/
    ownership justifies them

Current:

    declaration instances are carrier-resident

Candidate:

    human-carrier semantic metadata is carrier-resident
    machine-first state/policy is natively structured
    genuinely independent semantic facts may be standalone canonical records

### SUPERSEDE

    embedded strict JSON declaration block as universal Markdown mechanism
    separate committed JSON file for every generated index family
    capture representation fixed to one JSON profile
    current metadata-heavy Research/Checkpoint/Message header conventions

## 23. Representation-family comparison

### F1 plain Git-native documents only

Strength:

    simplicity
    readability

Failure:

    deterministic machine-critical state and typed relations become weak or
    require prose parsing

Disposition:

    reject as universal solution

### F2 structured document envelopes/front matter

Strength:

    atomic human content + semantic metadata
    diffable
    source-local

Weakness:

    not appropriate for machine-heavy state

Disposition:

    select for governed human carriers

### F3 sidecars

Strength:

    clean prose
    works for binary artifacts

Weakness:

    pairing drift
    duplicate move/update burden
    more file count

Disposition:

    reject for ordinary Markdown
    select selectively for binary/native artifacts

### F4 bounded canonical structured registry

Strength:

    central query
    explicit structure

Weakness:

    authority bottleneck
    update locality loss
    relation/source ownership ambiguity

Disposition:

    reject universal registry
    allow bounded standalone facts when independently owned

### F5 Git sources + rebuildable relational/query database

Strength:

    strong query/search
    canonical source remains inspectable
    derived DB can be dropped/rebuilt

Disposition:

    select

### F6 canonical database-backed Project control state

Strength:

    transactions
    concurrent mutation
    queries

Weakness at current scale:

    weak Git diff/review
    binary recovery dependency
    extra operational authority substrate
    harder repository-only reconstruction

Disposition:

    reject for canonical Project authority now
    retain as falsifier-driven future option

### F7 graph-first canonical representation

Strength:

    relation traversal

Weakness:

    human knowledge mismatch
    operational complexity
    second authority risk

Disposition:

    reject canonical graph store
    allow derived graph projection

### F8 broad append/event-log representation

Strength:

    audit/history
    replay

Weakness:

    volume
    cognitive/operational overhead
    current-state derivation complexity
    persistence of low-value events

Disposition:

    reject broad event sourcing
    select consequence-proportional immutable receipts

### F9 hybrid

Disposition:

    selected

## 24. RR-01 through RR-18 conformance

### RR-01 Single accepted meaning

PASS.

Canonical sources are explicit; SQLite/graph/vector/generated views are derived.

### RR-02 Recovery does not depend on derivatives

PASS by design.

Anchor reaches authored canonical state without generation/index.

### RR-03 Path is not semantic identity

PASS.

Stable IDs are optional/selective and independent of path.

### RR-04 Selective structure, not universal metadata

PASS.

Only machine-governed human carriers receive envelopes.

### RR-05 Rich human knowledge remains first-class

PASS.

Markdown is the primary long-form carrier.

### RR-06 Machine-critical state is not prose-parsed

PASS.

Machine-maintained canonical control state is structured JSON.

### RR-07 Generated views are disposable

PASS.

Generated views and SQLite are rebuildable.

Tracked orientation views still have complete source/freshness manifests.

### RR-08 Consequence-proportional persistence

PASS.

Selective retained receipts; broad telemetry remains ephemeral.

### RR-09 Provenance explicit where material

PASS.

Git supplies default provenance; envelopes/manifests/receipts extend only when needed.

### RR-10 Safe evolution

PASS at architecture level.

Versioned envelopes/JSON schemas plus old-read/migration rules required.

Needs implementation qualification.

### RR-11 Git compatibility evaluated

PASS.

Text canonical sources are Git-friendly.

Derived SQLite is not committed as authority.

Native/binary artifacts require suitability/manifest policy.

### RR-12 PSMF upgradeability

PASS at architecture level.

Framework parsers/schemas/mechanisms separate from ADS instance data.

Needs an upgrade probe.

### RR-13 Product/Project separation

PASS.

No Product runtime dependency on Project representation.

### RR-14 Public/private boundary

PASS conceptually.

Private complements referenced abstractly; requires schema non-leakage tests.

### RR-15 Reference integrity

PASS conceptually.

Stable IDs plus migration/reference graph; exact migration remains later.

### RR-16 Concurrency/stale writes

PASS conceptually.

Sharded records + expected blob/revision guards + atomic Git commit.

Needs empirical multi-writer probe.

### RR-17 No technology by prestige

PASS.

Graph/vector/network DB rejected without workload evidence.

SQLite selected only as disposable local query substrate.

### RR-18 No inheritance by familiarity

PASS.

Current strict JSON-in-Markdown, metadata headers and generated file inventory are explicitly superseded/amended where better mechanisms exist.

## 25. Specification 028 likely disposition

This is not yet the final amendment set.

Likely RETAIN at semantic level:

    Git durable authority
    identity separate from path
    authority resolver semantics
    capture non-authority / promotion semantics
    deterministic validation
    derived-view rebuildability/freshness
    full/incremental equivalence principle
    public/private fail-visible behavior
    compatibility/shadow/cutover discipline
    no automatic authority switch

Likely GENERALIZE:

    governed semantic source discovery
    native structured carrier support
    schema profile/version model
    generated-view framework
    rebuild/refresh CLI
    migration-unit contracts
    no mass historical conversion

Likely AMEND:

    Markdown structured-declaration contract
        strict embedded JSON block
        ->
        optional TOML governed envelope for human carriers

    one declaration per carrier
        ->
        one optional governed envelope / primary carrier identity rule

    fixed capture JSON profile
        ->
        human-rich or machine-first capture representations

    generated JSON view inventory
        ->
        use-case-generated outputs plus derived SQLite query substrate

    parser assumptions
        ->
        top-of-document TOML envelope parser + native JSON/TOML records

    path-sensitive Project-knowledge locations
        ->
        accepted project/system and project/knowledge target

Likely SUPERSEDE:

    current docs/project_knowledge/generated physical contract
    current eight-view committed JSON requirement as universal production shape
    current embedded JSON declaration delimiter/profile mechanism

New Specification 028 successor/amendment must define:

    TOML envelope contract
    machine state JSON records
    instance-policy TOML
    independent semantic-record admission
    selective receipt persistence
    SQLite derived-index freshness/rebuild
    generate-independent recovery
    framework/instance representation seam

## 26. Strongest alternative

Strongest materially different alternative:

    canonical SQLite Project semantic/control store
    with Markdown as human-rendered/linked knowledge views

Why it is attractive:

    transactional updates
    strong queries
    natural relations
    indexing
    one consistency boundary
    easier concurrent machine state

Why it loses under current ADS requirements:

    makes a database file an authority substrate that is poor for normal
    Git review/diff
    increases break-glass dependency
    moves rich human knowledge away from its natural representation
    raises PSMF/instance lifecycle coupling
    requires more operational machinery
    solves concurrency/scale pressure not yet evidenced for durable Project
    facts

This alternative should be reopened if actual concurrent control-write volume or relational-state complexity makes guarded Git records materially unreliable.


## 27. Candidate falsifiers

Amend/reject GCHR-DQI if evidence shows:

    FALSIFIER-1
        canonical control writes conflict frequently enough that sharded
        Git records + stale guards are operationally inadequate

    FALSIFIER-2
        TOML envelopes create repeated authoring/parser/editor friction or
        cannot express required metadata cleanly without becoming large

    FALSIFIER-3
        semantic metadata routinely changes independently of prose such that
        carrier-resident envelopes cause harmful co-change

    FALSIFIER-4
        derived SQLite rebuild/incremental maintenance becomes too expensive
        for projected corpus scale

    FALSIFIER-5
        graph workloads require graph-native persistence for practical
        traversal, even while authority stays elsewhere

    FALSIFIER-6
        retained receipt volume causes unacceptable repository growth

    FALSIFIER-7
        framework upgrades cannot preserve the proposed schema/instance seam

    FALSIFIER-8
        generate-independent recovery cannot be demonstrated with the
        canonical record set alone

    FALSIFIER-9
        JSON Schema proves materially too complex/weak for contract evolution
        and another schema language produces clearer portable contracts

    FALSIFIER-10
        binary evidence volume makes Git-centered artifact retention
        operationally unsustainable

## 28. Empirical qualification recommended before final representation freeze

After independent-model reconciliation, but before irreversible migration design, run a bounded representation probe over synthetic/representative carriers.

Minimum fixture:

    architecture rationale Markdown + TOML envelope
    first-class decision Markdown + TOML envelope
    plain Markdown without metadata
    Project policy TOML
    workstream/control JSON
    independent semantic relation TOML
    retained receipt JSON
    binary/native evidence + manifest

Tests:

    parse/validate
    path move without identity loss
    typed relation closure
    subject navigation
    authority resolution
    stale JSON state write rejection
    two unrelated concurrent record changes
    multi-record atomic transition
    delete/rebuild SQLite index
    FTS query
    graph-edge query
    generated current.md/current.json rebuild
    break-glass recovery with generated/index layers deleted
    schema-version migration fixture
    PSMF framework refresh leaving ADS instance state untouched
    Git diff/review quality inspection

If the probe exposes a representation defect, amend before Specification 028 is rewritten around it.

## 29. External mechanism evidence used

TOML 1.0 specification:

    TOML is UTF-8, designed to map unambiguously to hash-table-like data,
    supports comments and rejects duplicate key definitions.

Python standard library:

    tomllib is available in Python 3.11+ for TOML 1.0 parsing.
    It does not provide a writer.

Current ADS Python requirement:

    Python >=3.12

JSON Schema:

    current published dialect is Draft 2020-12.

SQLite:

    FTS5 provides full-text search.
    SQLite JSON functions provide JSON handling.
    These capabilities support the selected derived query/index role.

None of these mechanism facts determines semantic authority.

## 30. Independent-candidate status

This candidate is frozen without Claude comparative exposure.

Claude's independent candidate must remain hidden from ChatGPT until this record is committed.

After both candidates exist:

    compare architecture principles
    classify agreements/disagreements
    identify genuinely better mechanisms
    run bounded empirical probe where disagreement cannot be resolved by
    first-principles evidence
    produce owner decision candidate

## 31. Current state

    CHATGPT_R8B_CANDIDATE=GCHR-DQI
    CHATGPT_CANDIDATE_FROZEN=true
    CLAUDE_CANDIDATE=PENDING
    COMPARATIVE_EXPOSURE_ALLOWED=false

    HUMAN_KNOWLEDGE=MARKDOWN
    HUMAN_GOVERNED_METADATA=OPTIONAL_TOML_ENVELOPE
    HUMAN_METADATA_UNIVERSAL=false

    INSTANCE_POLICY=TOML
    DURABLE_MACHINE_CONTROL=SHARDED_JSON
    INDEPENDENT_SEMANTIC_FACTS=BOUNDED_TOML_WHEN_JUSTIFIED
    RETAINED_RECEIPTS=SELECTIVE_IMMUTABLE_JSON
    CAPTURES=HYBRID_BY_CONTENT
    CONTRACT_SCHEMA=JSON_SCHEMA_2020_12

    GENERATED_ORIENTATION=MARKDOWN_PLUS_JSON
    DERIVED_QUERY_INDEX=SQLITE
    CANONICAL_PROJECT_SQL_DATABASE=false
    CANONICAL_GRAPH_DATABASE=false
    VECTOR_INDEX=OPTIONAL_DERIVED
    BROAD_EVENT_SOURCING=false

    BREAK_GLASS_REQUIRES_GENERATION=false
    SPECIFICATION028_REPRESENTATION_AMENDMENT_EXPECTED=true
    EMPIRICAL_REPRESENTATION_PROBE_RECOMMENDED=true

    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=CLAUDE_INDEPENDENT_MC0026_MESSAGE001_THEN_COMPARATIVE_RECONCILIATION
