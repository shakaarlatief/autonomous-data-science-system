# Research 504: ChatGPT independent R0 physical-realization candidate A

**Date:** 2026-10-04
**Status:** CHATGPT INDEPENDENT PHYSICAL CANDIDATE FROZEN / CLAUDE BLIND INDEPENDENT DESIGN NEXT
**Parent:** Research 503
**Selected logical target:** THIN_CENTRED_HYBRID_V03
**Candidate ID:** R0-CANDIDATE-A
**Candidate name:** Repository-Native Control Record Graph
**Independent base:** c459e9c8ac4435b80d4ac9d2bdb215aa72c13adc
**Collaboration thread:** MC-0030
**Scope:** Freeze ChatGPT's independently derived physical/software realization architecture before Claude sees it.
**Authority:** Physical-architecture candidate only. No implementation, migration, Specification 028 amendment, production activation, or authority switch is authorized.

## 1. Candidate summary

R0-CANDIDATE-A realizes V03 as a small repository-native control kernel built from immutable accepted control records, natural-owner source facts, pure versioned predicates, deterministic J3 evaluation, and disposable operational indexes.

The core shape is:

    human/domain governing source
        + proposal package
        + authenticated owner decision
        -> immutable Acceptance Record

    Acceptance Records
        -> accepted effect graph
        -> lineage/currentness
        -> deterministic control compilation

    natural-owner sources
        -> typed J2 fact adapters / evidence receipts

    accepted effects + J2 facts
        -> shared predicate runtime
        -> J3 truth

    J3 truth
        -> generated orientation
        -> review routing
        -> action/gate views

    all immutable/durable sources
        -> disposable SQLite operational index
        -> CLI/API/query surfaces.

The repository remains the durable system of record for cross-domain control semantics.

The SQLite index is explicitly derived and rebuildable.

No persistent service is required for correctness.

## 2. Why this family

R0-CANDIDATE-A deliberately avoids four failure-prone extremes:

    embedding all machine semantics inside prose documents;
    making one mutable database the sole semantic authority;
    building a universal ontology for all Project knowledge;
    adopting pure event sourcing for every Project mutation.

Instead it uses a bounded append-only record graph only for cross-domain governing/control semantics.

Natural domain meaning remains where it naturally belongs.

## 3. Candidate repository topology

The proposed target topology is:

    project_system/
        authority/
            acceptances/
                YYYY/
                    <acceptance_id>.json
        predicates/
            registry.json
        migrations/
            plans/
            receipts/
        compatibility/
            manifests/
        schemas/
            acceptance.schema.json
            predicate.schema.json
            receipt.schema.json
            migration.schema.json
        generated/
            README.md

    packages/
        project_system/
            pyproject.toml
            src/project_system/
                model/
                authority/
                canonical/
                facts/
                predicates/
                j3/
                lineage/
                compiler/
                orientation/
                assurance/
                adapters/
                index/
                migration/
                recovery/
                cli/
            tests/

    docs/
        project_system/
            architecture/
                overview.md
                authority-and-acceptance.md
                realization-and-j3.md
                lineage-and-migration.md
                recovery-and-cutover.md

    .cache/
        project_system/
            control-index.sqlite
            materialized/

The exact names are candidate choices, not logical invariants.

The architectural boundary is the important part:

    authoritative records
    implementation package
    human architecture documentation
    generated/disposable operational state

are physically distinct.

## 4. Canonical J1 Acceptance Record

One owner acceptance boundary becomes one immutable canonical JSON record.

A record contains:

    schema_version
    acceptance_id
    accepted_at
    effective_boundary
    governing_actor
    source_bindings[]
    proposal_digest
    decision_receipt
    accepted_effects[]
    provenance.

Each source binding uses an exact immutable reference, for example:

    repo path
    Git commit
    Git blob SHA
    optional semantic ID / fragment.

Each accepted effect contains:

    effect_id
    type
    accepted_effect_statement
    accounting disposition
    exact governing refs
    semantic digest
    type-specific payload.

Type-specific payload may include:

    completion contract
    standing enforcement
    authorization scope
    deferral contract
    lifecycle relation
    sequencing constraint.

The record is immutable after acceptance.

Semantic change creates a new acceptance and, where applicable, explicit lineage.

## 5. Identity

Use opaque durable UUIDv7-style identifiers for:

    acceptance_id
    effect_id
    receipt_id
    migration_id.

Do not derive semantic identity from:

    file path
    title
    prose text
    content hash.

The canonical content digest proves exact accepted bytes.

The stable ID provides continuity.

If accepted meaning changes materially:

    new effect_id

unless the qualified CARRY_FORWARD rule proves exact semantic continuity.

## 6. Canonical serialization

Canonical machine records use strict JSON with deterministic canonicalization.

The digest basis is:

    canonical JSON bytes

not worktree bytes.

Git blob identity is also recorded for repository-carried records.

This separates:

    semantic payload digest
    repository object digest.

Line-ending normalization therefore cannot create false semantic drift.

Human-readable rendering is generated from the record and source carrier.

The generated rendering is never authority.

## 7. Acceptance authenticity

Acceptance is a two-step protocol.

### Proposal

A tool generates:

    exact source bindings
    owner-visible structured consequence view
    canonical proposal bytes
    proposal digest.

The proposal is non-authoritative.

### Decision

An Acceptance Authority Adapter captures an explicit owner decision bound to that exact digest.

The core interface is provider-neutral:

    actor_identity
    decision
    proposal_digest
    base_revision
    decision_time
    receipt_type
    receipt_reference
    receipt_digest.

Possible adapters include:

    repository-host review/approval
    locally signed owner approval
    trusted orchestration/control-plane approval
    future provider-specific approval adapters.

The kernel does not hard-code GitHub or ChatGPT as semantic authority.

The acceptance record becomes authoritative only after the adapter proof is verified and the immutable record is committed through the governed repository mutation path.

## 8. J1 atomicity

One Acceptance Record may contain multiple accepted effects.

That preserves one governing meaning boundary without requiring one file per effect.

Effects remain individually identifiable.

The Git commit that introduces the accepted record binds the whole acceptance atomically at repository level.

Cross-file authority transactions are avoided wherever practical.

## 9. J2 natural-owner facts

R0-CANDIDATE-A does not create a central manually maintained J2 database.

J2 is an adapter contract over natural-owner sources.

Examples:

    Git facts
        commit/tree/blob/path identity

    workstream facts
        exact accepted workstream source + revision

    implementation facts
        artifact/revision/component identity

    CI/qualification facts
        exact run/attestation/artifact digest

    private facts
        private-companion receipt / opaque public proof

    human procedural facts
        governed execution receipt.

Adapters return normalized immutable fact snapshots to the evaluator.

A fact snapshot includes:

    fact_type
    natural_owner
    subject
    exact source revision
    observed value
    observation boundary
    provenance.

Facts that cannot be deterministically re-read later receive durable Evidence Receipts.

Reproducible repository facts do not need duplicate canonical copies.

## 10. Completion contracts

Completion contracts live:

    inside the governing Acceptance Record

or:

    in an exact separately accepted domain contract revision referenced by it.

They never live only in implementation code.

A completion contract contains:

    criterion IDs
    required component IDs
    composition rule
    evidence requirements
    qualification requirements
    activation requirements
    authority reference
    authority revision/digest.

R0-CANDIDATE-A initially supports the qualified:

    ALL_REQUIRED

composition rule.

Additional rules require explicit qualification before adoption.

## 11. Predicate registry

Shared executable predicates are implemented as pure functions in:

    packages/project_system/src/project_system/predicates/

and registered in:

    project_system/predicates/registry.json.

Each registry entry binds:

    predicate_id
    definition_revision
    implementation reference
    implementation digest
    input contract
    output contract
    consumers.

J3 and WARRANT-F consume the same predicate identity and implementation revision where semantics are shared.

Duplicate predicate IDs with different digests fail validation.

## 12. Dependency graph

The evaluator constructs an explicit same-revision dependency DAG.

Node families include:

    accepted J1
    lineage/currentness
    J2 facts
    shared predicates
    base assurance decisions
    J3
    orientation
    meta-assurance
    compiled control
    delivery/action receipts.

The DAG is validated before evaluation.

Forbidden same-revision back-edges fail closed.

Feedback from action/review becomes a new source snapshot at a later revision.

## 13. J3 engine

The J3 engine is a deterministic library.

Input:

    exact acceptance-set snapshot
    exact lineage/currentness snapshot
    exact J2 fact snapshot
    exact predicate-registry revision
    required assurance inputs.

Output:

    requirement truth
    consequence truth
    enforcement truth
    regression flags
    provenance/explanation trace.

A J3 result is identified by:

    input snapshot digest
    evaluator version
    predicate-registry digest.

No J3 result is accepted as authority merely because it was cached.

## 14. Lineage

Lineage is not stored in a separate hand-maintained graph.

It is derived from accepted LIFECYCLE effects in immutable Acceptance Records.

This avoids duplicate authority.

The lineage engine derives:

    current identities
    predecessor/successor graph
    semantic-portion closure
    retirements
    unaffected portions
    effective boundaries
    realization initialization.

Qualified forms:

    CARRY_FORWARD
    REPLACE
    SPLIT
    MERGE
    REPARTITION
    RETIRE
    REINSTATE.

The initialization result is always:

    ordered array of zero or more records

sorted by effect_id.

## 15. Realization succession

For semantic succession:

    default = OPEN_RESET.

Explicit carry is a J2 realization-carry fact bound to:

    exact predecessor realization snapshot
    exact successor component mapping
    authority
    effective boundary
    freshness
    qualification recheck.

Valid carry yields:

    CARRY_FACTS_FOR_REVALIDATION.

It never directly yields SATISFIED.

## 16. Orientation

Orientation is generated on demand from J3.

Canonical vocabulary:

    REVIEW_REQUIRED
    DEFERRED
    OPEN
    SATISFIED.

Next-gap vocabulary:

    REVIEW
    UNOWNED
    DEPENDENCY
    COVERAGE
    EVIDENCE
    QUALIFICATION
    ACTIVATION
    NONE.

Orientation records are not committed as governing state.

If persisted for performance, they are cached with exact input digests and can be deleted/rebuilt safely.

## 17. Derived operational index

For speed and query ergonomics, build a disposable SQLite index:

    .cache/project_system/control-index.sqlite.

It contains derived tables for:

    acceptance lookup
    effect lookup
    current identities
    lineage edges
    completion contracts
    J2 normalized facts
    J3 latest evaluated snapshot
    orientation
    review queue
    reverse references.

The database is:

    not committed
    not authoritative
    rebuildable from durable sources
    versioned by schema/index-builder version
    invalidated on source drift.

This gives relational query performance without database authority.

## 18. Control compiler

A pure compiler turns accepted current effects into executable control artifacts:

    ActionContract
    ControlObligationSet
    gate requirements
    transition requirements
    evidence requirements
    reconstruction requirements
    enforcement expectations.

Compiler outputs bind:

    exact source acceptance IDs/digests
    compiler version
    predicate-registry version.

They are disposable products.

An action executor refuses compiled artifacts whose source snapshot is stale.

## 19. CLI and library boundary

The default user/developer interface is one provider-neutral CLI plus importable library.

Candidate CLI:

    projectctl validate
    projectctl propose
    projectctl accept verify
    projectctl status
    projectctl explain <effect>
    projectctl review
    projectctl rebuild
    projectctl check
    projectctl doctor
    projectctl migrate plan
    projectctl migrate verify
    projectctl shadow compare
    projectctl recover.

The CLI is a shell over the same library used by CI and orchestration.

No semantic rule is reimplemented in CLI code.

## 20. No correctness-critical daemon

The base architecture requires no always-on service.

Correctness-critical state lives in:

    repository records
    natural-owner sources
    durable evidence receipts.

This improves:

    portability
    recovery
    local operation
    fresh-agent reconstruction
    operational simplicity.

A later read/query service may be added as a disposable accelerator if scale demonstrates need.

It may not become the only authority carrier.

## 21. Branch and review workflow

Target workflow is trunk-oriented with short-lived change branches and guarded merge.

Authoritative semantic mutations require:

    expected base revision
    exact acceptance proposal
    validation
    owner decision receipt where normative
    passing authority/integrity CI
    non-stale merge.

High-value branches are protected.

A merge queue or equivalent serialization is preferred for authoritative mutation paths.

Routine code changes that do not alter governing semantics use normal engineering review without owner semantic acceptance.

The workflow distinguishes:

    normative semantic change
    realization fact change
    implementation code change
    generated-view refresh
    migration action.

They do not all require the same reviewer.

## 22. Optimistic concurrency

Every normative proposal records:

    expected base commit
    expected governing source revisions.

Finalization revalidates them immediately before mutation.

If any bound source changed:

    STALE_PROPOSAL
    refuse.

J2 writes/receipts similarly bind exact subject revisions.

Git merge success alone is not sufficient concurrency proof for semantic mutations.

## 23. CI architecture

CI has layered gates.

### Fast PR gate

    formatting/canonical JSON
    schema
    references
    closed accounting
    predicate registry uniqueness
    DAG acyclicity
    lineage closure
    generated artifact non-authority checks
    unit tests.

### Semantic integration gate

    J1/J2/J3 fixtures
    completion/self-certification tests
    lineage/repartition property tests
    orientation
    public/private degraded behavior
    stale-write controls
    rebuild/incremental equivalence.

### Migration gate

    live-scope inventory closure
    compatibility
    reverse references
    parity
    rollback.

### Release/cutover qualification

    fresh environment rebuild
    untouched evaluator runs
    interruption/recovery
    concurrency
    cold continuation
    authority resolution
    rollback rehearsal.

The same core validators run locally and in CI.

## 24. Test architecture

Use distinct test layers:

    unit
        pure models/predicates/compiler

    property
        lineage, repartition, currentness, idempotence

    contract
        adapters and receipt schemas

    fixture/golden
        V03 qualified cases

    integration
        acceptance -> J2 -> J3 -> orientation

    mutation/adversarial
        self-certification, stale refs, duplicate authority, cycles

    migration
        wave parity and rollback

    recovery
        cache loss, partial run, interrupted write

    fresh confirmation
        untouched environment/model/provider where decision-relevant.

Tests live beside the production package, while durable architecture-level fixtures may remain in a dedicated testdata area.

## 25. Public/private architecture

Public authority records must never contain private detail.

When J3 needs private evidence:

    private companion owns the sensitive fact/evidence;
    public J2 adapter receives only an opaque evidence identity plus allowed qualification/freshness result;
    public provenance records the private authority boundary without revealing payload.

If private evidence is unavailable:

    do not infer success;
    emit the appropriate evidence/review gap.

Private unavailability therefore degrades safely.

## 26. Project-system / ADS-product separation

The physical package is a Project-system package.

It is not imported into ADS Product runtime by default.

The interface is:

    Project system governs development/qualification/activation of ADS
    ADS Product consumes only explicitly published product artifacts/contracts.

Project history, owner decisions and migration bookkeeping do not become ADS runtime dependencies.

## 27. Documentation

Maintain hand-authored rationale and generated factual reference separately.

Hand-authored:

    architecture overview
    authority model
    realization/J3 model
    migration/cutover model
    operator/developer workflow.

Generated from code/schemas:

    record field reference
    predicate registry
    CLI reference
    current compatibility matrix.

Preferred diagrams are text-source version-controlled diagrams, initially Mermaid where adequate.

Documentation generation is never semantic authority.

## 28. Observability

Every failed evaluation returns:

    exact subject/effect
    failed predicate/gate
    source revision
    expected authority
    review owner
    remediation class.

Avoid generic:

    invalid
    failed
    unknown

without actionable provenance.

Operational metrics include:

    unresolved accepted effects
    stale evidence
    unowned reviews
    detector findings
    legacy-unreconciled count
    migration parity gaps
    rebuild divergence
    stale-proposal rejects.

Metrics are observations, not authority.

## 29. Recovery

Because authoritative semantic records are repository-native and immutable:

    delete cache
    checkout exact revision
    rebuild index
    re-read natural-owner facts
    re-evaluate J3.

Interrupted acceptance finalization cannot leave a half-authoritative local DB transaction.

Repository mutation is the durable commit boundary.

Migration tooling uses explicit plan/receipt records and idempotent steps.

Recovery instructions are generated from exact durable state.

## 30. Migration architecture

Migration begins with a semantic inventory, not file conversion.

Each live legacy item is classified:

    already represented by V03 accepted meaning
    needs accepted successor effect
    compatibility-only surface
    historical/latent
    private delegated
    unresolved.

A migration wave binds:

    scope
    source revisions
    target identities
    lineage
    compatibility requirements
    parity tests
    rollback plan.

Shadow evaluation runs both current authority and V03-derived views.

Only the current system may issue authoritative decisions until cutover.

No dual semantic authority.

## 31. Specification 028 transition

Specification 028 remains operational authority during R0/R1.

R0-CANDIDATE-A does not mechanically preserve its physical contracts.

R1 reconciliation must disposition every live Specification 028 mechanism into:

    PRESERVE_AS_COMPATIBLE
    REFINE_AND_PROMOTE
    REIMPLEMENT
    COMPATIBILITY_ONLY
    SUPERSEDE_PROSPECTIVELY
    RETIRE_AFTER_CUTOVER.

Only after an accepted prospective successor/amendment may implementation begin against changed operational contracts.

## 32. Current-mechanism disposition hypothesis

Before comparative review, ChatGPT's provisional dispositions are:

    tools/project_knowledge research mechanisms
        KEEP_AS_TEST_OR_REFERENCE_ONLY by default
        selectively REFINE_AND_PROMOTE when implementation quality merits

    strict JSON declaration concepts
        preserve the deterministic structured-record principle
        do not preserve Markdown-embedded declaration markers by default

    current routing/current-state files
        KEEP_AS_COMPATIBILITY_ONLY during migration
        replace with derived views after qualified cutover if V03 equivalents prove superior

    current repository validators
        reuse/refine individual invariants
        consolidate semantic logic behind the new library

    current Codexless Runtime Bridge
        keep as a ChatGPT execution/control adapter
        do not make it semantic authority or universal provider requirement

    current GitHub collaboration-message pattern
        keep as migration-compatible collaboration evidence
        reconsider long-term workflow in the broader provider-neutral action/receipt architecture.

These are candidate hypotheses, not accepted dispositions.

## 33. Alternatives considered

### Alternative B: Markdown-embedded declarations as primary physical authority

Strengths:

    high locality
    direct human context
    minimal new artifact family.

Weaknesses:

    marker/parser fragility
    mixed prose/machine lifecycle
    difficult atomic structured evolution
    repeated hash/line-ending hazards
    higher risk that physical document shape contaminates semantic identity.

Disposition:

    not preferred as the default V03 physical authority.

### Alternative C: authoritative SQLite/PostgreSQL semantic database

Strengths:

    strong relational integrity
    excellent query performance
    transactional updates
    convenient graph/current-state queries.

Weaknesses:

    hidden mutation surface
    weaker Git-native inspectability
    backup/export becomes authority-critical
    larger operational dependency
    harder fresh-agent reconstruction
    public/private and branch review become more complex.

Disposition:

    use SQLite only as a derived index unless scale later falsifies that choice.

### Alternative D: pure append-only event-sourced Project state

Strengths:

    complete temporal history
    explicit event causality
    natural reconstruction.

Weaknesses:

    event schema becomes a very broad Project ontology
    replay/versioning complexity
    harder owner inspection
    unnecessary ceremony for domain-native facts that already have authoritative sources.

Disposition:

    preserve append-only accepted control records, not universal event sourcing.

## 34. Why Candidate A currently leads

It combines:

    repository auditability
    immutable governing records
    natural-owner fact separation
    deterministic rebuild
    relational query speed through disposable SQLite
    no correctness-critical service
    provider-neutral acceptance adapters
    conventional Python/JSON/Git engineering
    explicit migration compatibility
    low authority duplication.

It also avoids re-centralizing all Project meaning into the control kernel.

## 35. Material risks

### Risk A: acceptance record sprawl

Mitigation:

    one record per governing acceptance boundary, not one file per sentence/effect.

### Risk B: owner-authenticity adapter complexity

This is a real open issue.

A small probe must show that owner acceptance can be captured securely with low burden across the actual ChatGPT/GitHub/local workflow.

### Risk C: J2 adapter inconsistency

The typed fact contract must prevent each adapter from redefining shared semantics.

Contract tests and natural-owner responsibility boundaries are required.

### Risk D: derived SQLite becomes de facto authority

The CLI and APIs must be able to delete/rebuild it at any time.

CI should periodically run from cache absence.

### Risk E: too much JSON for humans

Owner workflows render source + consequences.

Humans should not manually author canonical JSON unless explicitly appropriate.

### Risk F: repository scale

If accepted-control records or fact snapshots become large enough to make full rebuild/query too slow, the architecture may need a more aggressive materialization strategy without changing authority.

## 36. Falsifiers and required probes

Before physical target selection, test at least:

    P-AUTH
        real owner-acceptance flow with exact digest binding and low burden

    P-REBUILD
        full rebuild versus incremental index refresh equivalence

    P-SCALE
        representative record/fact volumes and query/rebuild latency

    P-CONCURRENCY
        simultaneous stale proposals and realization updates

    P-PRIVATE
        private evidence available/unavailable behavior with no leakage

    P-RECOVERY
        delete cache + interrupted migration + fresh reconstruction

    P-MIGRATION
        one real legacy obligation slice through mapping, shadow parity and rollback

    P-WORKFLOW
        branch/PR/CI path for normative versus ordinary implementation changes

    P-FRESH
        fresh collaborator reconstructs current authority/action without hand-held chat context.

Candidate A should be amended or rejected if those probes show unacceptable burden, hidden authority, non-rebuildability, or workflow fragility.

## 37. Current disposition

    CHATGPT_R0_CANDIDATE=R0-CANDIDATE-A
    CANDIDATE_NAME=Repository-Native_Control_Record_Graph
    STATUS=FROZEN_INDEPENDENT_POSITION

    PHYSICAL_ARCHITECTURE_SELECTED=false
    IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED

    CLAUDE_EXPOSURE_TO_RESEARCH504=FORBIDDEN_UNTIL_MESSAGE001_FROZEN
    NEXT=CLAUDE_INDEPENDENT_R0_PHYSICAL_ARCHITECTURE
