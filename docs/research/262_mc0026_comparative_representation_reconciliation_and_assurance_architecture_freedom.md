# Research 262: MC-0026 Comparative Representation Reconciliation and Assurance-Architecture Freedom

**Date:** 2026-09-23
**Status:** INDEPENDENT CANDIDATES COMPARED / CONVERGED REPRESENTATION CANDIDATE RECOMMENDED FOR CRITIQUE AND PROBE / ASSURANCE MECHANISMS NOT GRANDFATHERED / NO OWNER REPRESENTATION DECISION / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Shared requirements:** Research 260
**ChatGPT independent candidate:** Research 261 / GCHR-DQI
**Claude independent candidate:** MC-0026 Message 001 / WMR
**Claude candidate commit:** 5ad0f213361d492bf426d34acd8f25b69f309458
**Scope:** Compare the two independently derived R8-B representation candidates, reconcile convergent and disputed mechanisms, record the owner's assurance/CI-CD anti-anchoring clarification, and define the empirical and collaboration steps required before any representation decision.
**Authority:** Comparative recommendation only. Specification 028 remains unchanged. No physical migration, AO-10 implementation, authority switch or PSMF extraction is authorized.

## 1. Independence result

The independent-design protocol succeeded.

ChatGPT froze GCHR-DQI in Research 261 before reading Claude Message 001.

Claude produced WMR from frozen base 1fe4bbe4b2658532359411825d3b1d819a6c4c68. Claude disclosed that the coordination inbox exposed only the name GCHR-DQI, not its design, and did not read Research 261.

The strong mechanism-level convergence therefore remains meaningful.

## 2. Strong independent convergence

Both candidates independently select:

    durable human knowledge
        Markdown

    selective human-authored machine semantics
        TOML attached to the human carrier

    human-authored Project-system policy
        TOML

    machine-maintained durable Project-control state
        sharded pretty JSON

    structural contracts
        JSON Schema Draft 2020-12 over normalized data models

    generated human views
        Markdown

    generated machine projections
        JSON when a file projection is justified

    query/search acceleration
        derived SQLite / FTS

    graph semantics
        typed relations in canonical sources plus derived projection

    vector retrieval
        optional derived acceleration only

    canonical Project SQL database
        NO

    canonical graph database
        NO

    broad event sourcing
        NO

    control receipts
        SELECTIVE / consequence-proportional

    break-glass recovery
        canonical files only; no generated/database/network dependency

    metadata
        selective, not universal

    PSMF mechanism
        separate from ADS instance policy/state

    current file formats
        no preservation right

## 3. Claude's strongest empirical finding is accepted

Claude inspected docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md and found current operational facts duplicated across:

    status header
    prose table
    hidden embedded machine declaration

Current repository inspection confirms that PAUSED, NOT_STARTED, BLOCKED and the resume target are duplicated.

The important inference is not merely to remove duplicate wording.

Descriptive meaning and operational state have different writers, write frequencies, concurrency needs and lifecycle semantics.

The comparative design therefore adopts:

    REPRESENTATION_FOLLOWS_WRITER

combined with the already accepted rule:

    OWNERSHIP_FOLLOWS_BEHAVIOR_AND_AUTHORITY

Representation follows the actor/process that legitimately authors or mutates the information.

Ownership follows the entity whose behavior/authority contract the information belongs to.

## 4. Converged candidate: WMR-H

Working name:

    WMR-H
    Writer-Matched Hybrid Representation

This remains a candidate.

### 4.1 Durable human knowledge

    CommonMark / Git-friendly Markdown

The Project system does not rewrite human prose carriers during ordinary control-state transitions.

### 4.2 Governed metadata on human carriers

Selectively:

    visible TOML project metadata

The comparative candidate prefers Claude's visible fenced TOML direction over Research 261's +++ TOML envelope.

The reasons are:

    visible in rendered Git-host views
    standard fenced Markdown
    removes the current hidden-comment problem
    moves atomically with the carrier
    selectively applied only to governed carriers

Exact tag, placement and fields remain probe material.

### 4.3 Metadata remains descriptive

Human-carrier metadata may describe:

    semantic identity
    semantic kind
    authority role
    lifecycle of the carrier's meaning
    controlled subject memberships
    typed semantic relations
    material provenance not already supplied by Git

It does not become the home of frequently machine-mutated operational state.

Example:

    workstream objective / procedure / semantic identity
        -> human carrier + descriptive metadata

    current workstream state / milestone realization
        -> Project-system control record

    joined reader view
        -> generated orientation

### 4.4 Project-system instance policy

    TOML

Human-authored, machine-read, comments allowed, strictly validated.

### 4.5 Durable Project-control state

    sharded pretty JSON
    one record per independently written lifecycle/entity boundary

Writer:

    Project Development System

Mutation:

    expected revision/blob precondition
    stale-write rejection
    atomic Git commit for coherent multi-record transitions

A canonical SQLite control store is not selected at current evidence level.

### 4.6 Independent semantic facts

Default:

    relation/fact remains on the natural semantic owner

Standalone fact:

    TOML structured record

only when no endpoint naturally owns it or the relation has independent lifecycle/provenance.

The comparative candidate does not adopt one universal project/system/instance/relations home.

Placement follows semantic responsibility:

    governing independent fact
        -> appropriate Project knowledge governance owner

    machine/control fact
        -> Project-system instance owner

    evidence fact
        -> evidence owner where independently justified

The Project system owns parsing/resolution machinery, not automatically the semantic authority of every relation.

### 4.7 Captures/candidates

Writer-matched hybrid:

    human-rich capture
        -> Markdown + selective visible TOML metadata

    machine-first capture
        -> structured JSON

Both are non-authoritative.

Promotion creates/updates the natural canonical owner and records disposition/provenance. It never flips the capture into authority in place.

### 4.8 Contracts

Primary structural contract:

    JSON Schema Draft 2020-12

applied to normalized JSON-compatible data parsed from TOML or JSON.

Semantic validators separately enforce:

    identity uniqueness
    authority
    relation closure
    controlled vocabularies
    lifecycle
    cross-record constraints
    public/private safety
    reference integrity

### 4.9 Generated views

Derived only.

Bounded committed cold-start accelerators remain candidates:

    project/system/generated/orientation/current.md
    project/system/generated/orientation/current.json

They remain non-authoritative, freshness-bound, rebuildable and unnecessary for break-glass recovery.

Other machine indexes/views are committed only if a real consumer requires repository-resident output.

### 4.10 Query/search layer

Standard optional/rebuildable local query substrate:

    SQLite
        relational projections
        typed edge table
        FTS

Normally disposable and source-revision bound.

Graph database is not selected.

Vector index remains optional and derived.

No retrieval rank may determine authority.

## 5. Material disagreement D1: receipt physical form

ChatGPT:

    one immutable JSON file per retained receipt

Claude:

    monthly/family JSONL append logs

Both agree on selective persistence, evidence-only authority, immutable logical receipts and bounded retention.

JSON-per-receipt strengths:

    independent writes
    minimal cross-branch collision
    independent identity
    localized corruption
    selective citation/retention

Costs:

    many files
    directory growth

JSONL strengths:

    compact population
    efficient sequential reading
    easy partitioning

Costs:

    multiple writers touch the same file
    Git branch append conflicts
    compaction rewrites evidence containers

Disposition:

    EMPIRICAL_PROBE_REQUIRED

Provisional preference:

    individual JSON

because receipt persistence is consequence-gated and concurrency is a first-order AO concern.

## 6. Material disagreement D2: captures

Claude chooses Markdown capture records.

ChatGPT chooses Markdown for human-rich captures and JSON for machine-first captures.

Comparative disposition:

    WRITER_MATCHED_HYBRID

This directly follows the WMR organizing rule.

## 7. Material disagreement D3: committed machine orientation

Claude normally leaves machine indexes uncommitted.

ChatGPT keeps current.md plus current.json as committed, non-authoritative cold-start accelerators.

Comparative disposition:

    retain both as bounded candidates

because R8-A explicitly selected a direct repository-read machine orientation accelerator.

All larger machine indexes remain rebuildable and normally uncommitted.

## 8. Material disagreement D4: evidence artifact metadata

Claude allows artifact hash/provenance on the citing carrier.

ChatGPT allows a bounded artifact manifest when provenance/integrity has independent lifecycle.

Comparative disposition:

    NATURAL-OWNER RULE

If artifact provenance has an independent lifecycle or multiple consumers, use a manifest.

If one carrier naturally owns the reference, keep it there.

No universal sidecar rule.

## 9. Current workstream carrier pattern is superseded in the candidate

The future representation should not combine:

    human description
    hidden machine declaration
    current operational state
    milestone realization
    evidence summary

into one mixed carrier merely because the current workstream profile does.

A future workstream can have:

    human governing/planning definition
        Markdown + visible descriptive TOML

    current machine control state
        JSON

    generated orientation
        joined projection

    qualification evidence
        separate evidence/receipt owner

## 10. Owner clarification: tests, CI/CD, integrity and verification machinery are also redesignable

The owner explicitly clarified that the same from-scratch philosophy applies to:

    test architecture
    test runs
    unit/contract/integration/system/e2e organization
    integrity checks
    repository checks
    validators
    regression suites
    static analysis
    CI workflows
    CI provider/trigger/job topology
    CD/release/deployment machinery
    qualification gates
    build/release checks
    generated verification reports
    repository-health checks
    related scripts/tooling

Current implementations have no target-preservation right merely because they exist or because they previously produced accepted evidence.

This clarification is now a design principle.

## 11. What has already been done on assurance

Substantial work already exists, but mostly at behavioral/responsibility and historical-qualification levels.

W0:

    complete unit suite
    repository-integrity integration
    accepted semantic/system gates

W1:

    fail-closed public repository-integrity aggregate
    focused W1 semantic/routing qualification

W2-W4:

    focused successor-view, compatibility-shadow and capture/promotion tests
    repeated repository-integrity qualification
    Git diff/show checks
    regression maintenance

Those runs remain historical qualification evidence.

They do not imply that their harness topology is the ideal future architecture.

Research 249 J06 already derives Verification and Quality Engineering as a durable responsibility, including:

    unit/contract/integration/system tests
    acceptance gates
    regression suites
    static analysis
    compatibility checks
    repository integrity
    cross-workspace qualification
    product-behavior evaluation
    release-quality evidence

Research 249 J07 separately derives Repository, Workspace and Build Engineering, including:

    build/package/dependency tooling
    developer commands
    code generation
    cache/artifact policy
    CI execution architecture
    repository-wide engineering conventions

The same Research 249 deliberately did not decide:

    testing folder topology
    deployment technology
    cloud provider
    observability stack
    monorepo tool
    package-manager changes

Research 252 then explicitly rejected one universal future tests directory and split tests by Product, Product Interaction, JW1, cross-workspace qualification, repository governance and research ownership.

Research 258 AM-3 further freezes:

    JW1
        owns semantic validation

    project/engineering
        owns repository/cross-workspace validation and invocation

    engineering may invoke JW1
    JW1 must not depend on engineering

## 12. What has not yet been designed

The project has not yet performed a full from-scratch exact-target design of:

    future test topology
    exact test frameworks
    future repository-integrity architecture
    which current validators survive
    aggregate integrity command shape
    CI workflow decomposition
    CI trigger policy
    PR/branch/scheduled qualification
    caching strategy
    artifact/report publication
    release/CD architecture
    deployment promotion
    branch-protection/check requirements
    security/supply-chain implementation
    local-versus-CI parity
    CI/project-engineering observability

The current repository contains many GitHub Actions workflows and many check/integrity scripts.

Those are current mechanisms, not future requirements.

## 13. Assurance anti-anchoring rule

A current-era validator defect surfaced during this reconciliation: merely discussing the legacy structured-declaration marker token inside Claude Message 001 caused the present project-knowledge validator to classify the collaboration message as a malformed declaration carrier. Two literal marker spellings in Message 001 were therefore wording-sanitized without changing Claude's substantive design. This is negative evidence about the current marker-intent detection mechanism, not a reason to preserve or patch that mechanism into the future architecture.

Freeze:

> Verification requirements and accepted historical evidence may survive; verification mechanisms do not survive by inertia.

Therefore current pytest layout, tests/unit, repository_integrity.py, check scripts, workflow inventory, workflow names/triggers/jobs, GitHub Actions provider choice and PUBLIC_REPOSITORY_INTEGRITY aggregation shape are not grandfathered.

The behavioral assurance need behind a mechanism may survive.

For example:

    current routing must not silently contradict governing state

may remain a requirement even if the current check_current_routing.py implementation does not.

## 14. Relationship to accepted R8-A

R8-A accepted:

    project/engineering/
        checks/
        tests/
        tooling/

The owner clarification does not silently delete that accepted target.

It makes explicit that exact internal engineering topology is amendable through AO-4.

When assurance architecture is designed from scratch it may KEEP, CLARIFY, AMEND or SUPERSEDE those subareas.

The durable project/engineering owner and semantic-validation versus repository-validation boundary remain accepted unless later evidence reopens them.

## 15. Required future assurance stage

Before physical migration/cutover, R8 must include a distinct from-scratch:

    VERIFICATION / ASSURANCE / CI-CD / DELIVERY REALIZATION STAGE

It should derive:

    assurance classes
    required local feedback loops
    Product test ownership
    Project-system test ownership
    cross-workspace qualification
    repository architecture/integrity checks
    migration/shadow qualification
    release gates
    security/supply-chain checks
    CI orchestration
    CD/deployment responsibilities
    artifact/provenance publication
    failure/retry/flaky-test policy
    cost/time budgets
    required-versus-advisory checks
    branch/PR enforcement
    local/CI parity
    observability and recovery

Only after that should it decide tools, providers, workflow counts, test directories, aggregate commands, caching and deployment automation.

## 16. Representation probe P-R8B-01

The convergence is strong enough that a bounded empirical probe is more useful than another abstract redesign.

Minimum fixtures:

    governing Markdown + visible TOML metadata
    human workstream definition
    machine workstream-state JSON
    human policy TOML
    machine-first capture JSON
    human capture Markdown + metadata
    independent governing relation TOML
    independent machine/control relation TOML
    individual receipt JSON
    JSONL receipt alternative
    native evidence artifact + optional manifest
    generated current.md
    generated current.json
    rebuildable SQLite/FTS index

Required checks:

    parse and schema validation
    metadata visibility/render sanity
    no operational-state restatement in human definition
    definition/state ID pairing
    move/rename without identity loss
    authority resolution
    subject navigation
    typed relation resolution
    natural-owner relation placement
    stale state-write rejection
    unrelated concurrent state writes
    multi-record transition under one commit
    JSON-per-receipt concurrent writes
    JSONL concurrent append/merge
    representative receipt volume
    human and machine capture promotion
    delete/rebuild SQLite
    FTS and graph-edge query
    delete derivatives then perform break-glass recovery
    generated orientation freshness
    PSMF framework refresh leaving ADS instance untouched
    Git diff/review quality

The probe harness is temporary qualification machinery and is not itself the future assurance architecture.

## 17. Comparative falsifiers

Amend/reopen WMR-H if:

    definition/state splitting creates more practical drift than it removes
    visible TOML causes material authoring/rendering friction
    TOML/JSON writer split causes repeated errors
    sharded Git JSON cannot safely support AO-10 concurrency
    JSONL materially outperforms individual JSON without unacceptable conflict cost
    individual receipt files create unacceptable repository growth
    committed current.json provides no cold-start value or excessive churn
    independent fact placement cannot be classified reliably
    SQLite derived indexing is too expensive
    framework/schema evolution cannot preserve ADS instance state

## 18. Next collaboration step

Request one bounded Claude comparative critique of:

    visible TOML metadata
    representation-follows-writer
    definition/state split
    natural-owner independent facts
    hybrid captures
    receipt form
    committed current.json
    assurance anti-anchoring
    P-R8B-01 sufficiency

Then:

    reconcile critique
    run P-R8B-01
    owner representation decision
    from-scratch assurance architecture
    Specification 028 amendment
    file-level migration manifest

## 19. Current state

    MC0026_MESSAGE001=READ_AND_COMPARED
    CHATGPT_CANDIDATE=GCHR-DQI
    CLAUDE_CANDIDATE=WMR
    INDEPENDENT_CONVERGENCE=STRONG

    COMPARATIVE_CANDIDATE=WMR-H
    REPRESENTATION_FOLLOWS_WRITER=PROVISIONALLY_SELECTED
    OWNERSHIP_FOLLOWS_BEHAVIOR_AUTHORITY=RETAINED

    HUMAN_KNOWLEDGE=MARKDOWN
    HUMAN_GOVERNED_METADATA=VISIBLE_SELECTIVE_TOML
    INSTANCE_POLICY=TOML
    DURABLE_MACHINE_CONTROL=SHARDED_JSON
    CAPTURES=WRITER_MATCHED_HYBRID
    CONTRACT_SCHEMA=JSON_SCHEMA_2020_12

    RECEIPT_PHYSICAL_FORM=EMPIRICAL_PROBE
    DERIVED_QUERY_LAYER=SQLITE_FTS
    CANONICAL_SQL_DATABASE=false
    CANONICAL_GRAPH_DATABASE=false

    CURRENT_TEST_CI_CD_INTEGRITY_MECHANISMS=EVIDENCE_NOT_TARGET_REQUIREMENTS
    FUTURE_ASSURANCE_ARCHITECTURE=REQUIRED_BEFORE_PHYSICAL_MIGRATION

    REPRESENTATION_OWNER_DECISION=NOT_YET_REQUESTED
    SPECIFICATION028=UNCHANGED
    FILE_LEVEL_MIGRATION=HELD
    AO10=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=CLAUDE_COMPARATIVE_CRITIQUE_THEN_P_R8B_01
