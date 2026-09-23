# Research 272: WMR-H V0.3 Owner Acceptance, MC-0027 Closure, and Assurance-Architecture Entry

**Date:** 2026-09-23
**Status:** R8-B REPRESENTATION ARCHITECTURE ACCEPTED / MC-0027 RESOLVED / ASSURANCE ARCHITECTURE UNBLOCKED / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Representation requirements:** Research 260
**Comparative reconciliation:** Research 263
**Independent result audit:** MC-0027 Message 001
**Audit reconciliation and corrected probe contract:** Research 266
**Final corrected evidence:** Research 271
**Owner decision:** ACCEPT
**Repository base before acceptance:** aa0eda73685f6f91d107db99db2d1d7f7f560a1e
**Scope:** Record the project owner's explicit acceptance of WMR-H V0.3 as the target R8-B representation architecture direction, resolve MC-0027, preserve the exact meaning and limits of that acceptance, and unblock first-principles assurance / verification / CI-CD architecture design.

## 1. Owner decision

The project owner explicitly chose:

    I ACCEPT.

This accepts WMR-H V0.3 as the target R8-B representation architecture direction.

The acceptance is grounded in:

    Research 260
        from-scratch representation requirements

    Research 261 and Claude MC-0026 Message 001
        independent architecture candidates

    Research 262 / Research 263
        comparative reconciliation into WMR-H V0.2

    Claude MC-0027 Message 001
        adversarial audit that invalidated overclaimed probe evidence

    Research 266
        accepted audit amendments and corrected probe contract

    Research 267-270
        prospective harness freezes and repairs

    Research 271
        final corrected P-R8B-01-R2 attempt-3 PASS

The final empirical gate is:

    original blocking gates     18 / 18 PASS
    WMR-H V0.3 amendment gates   2 / 2 PASS
    threshold changes             none
    post-freeze candidate changes none

## 2. Accepted representation architecture

The accepted target direction is:

    durable human Project knowledge
        Markdown

    selective machine-readable descriptors on governed human carriers
        visible fenced TOML metadata
        only where machine semantics are required

    governed TOML value model
        JSON-compatible subset

    human-authored Project-system instance policy
        TOML

    machine-maintained durable Project control state
        sharded pretty JSON

    state concurrency
        exact stale-write/content precondition
        plus monotonic revision history enforced over committed history

    machine contracts
        versioned JSON Schema over normalized structured representations

    standalone independent semantic facts
        natural-owner structured records
        repository-wide direct-record review bound = 12

    human captures
        human-readable carriers

    machine captures
        JSON

    receipts
        selective immutable individual JSON records
        content-derived locator candidate

    generated orientation
        bounded committed current.md / current.json accelerators
        derived
        non-authoritative
        freshness-qualified
        not required for break-glass recovery

    query/search acceleration
        rebuildable SQLite / FTS

    graph semantics
        canonical typed relations
        derived graph projections
        no canonical graph database required

    vector retrieval
        optional derived cache only

    canonical Project SQL database
        not selected

    broad event-sourcing architecture
        not selected

    break-glass recovery
        stable anchor + canonical source
        derivative-independent

    PSMF seam
        framework mechanism and ADS instance meaning independently replaceable

    governance recognition
        intended governed carrier is GOVERNED or ERROR
        never silently downgraded to plain because of BOM,
        leading whitespace or supported title variation

    real-carrier migration
        rule-based and loss-accounted

## 3. Acceptance does not adopt the temporary probe as production architecture

The following are evidence/probe implementation only and are not accepted as production machinery merely because the probe used them:

    experiments/r8b_representation_probe_v01/
    experiments/r8b_representation_probe_v02/
    temporary parser implementations
    temporary transition validators
    temporary conversion functions
    temporary JSON Schemas
    temporary SQLite schema
    temporary Git fixture repositories
    temporary result/evidence directory layout

The acceptance is architectural.

Production realization remains to be designed and qualified.

## 4. Acceptance remains evolvable

This acceptance does not make WMR-H V0.3 immutable.

AO-4 remains the governing path for material evidence that later warrants:

    KEEP
    CLARIFY
    AMEND
    SUPERSEDE
    REOPEN

Therefore:

    ACCEPTED TARGET
        !=
    FOREVER FROZEN IMPLEMENTATION

and:

    EMPIRICALLY SUPPORTED DIRECTION
        !=
    COMPLETE PRODUCTION QUALIFICATION

## 5. Specification 028 remains unchanged for now

Specification 028 remains the current governing implementation/migration contract until explicitly amended.

The accepted R8-B architecture now creates a concrete later amendment obligation.

Representation-sensitive clauses to reconcile include at least:

    embedded strict JSON declarations in Markdown
    current native-JSON carrier rules
    current one-declaration-per-carrier realization
    current schema/profile assumptions
    current generated-view paths and shapes
    current project-knowledge directory assumptions
    current authority/index/catalog representation
    current graph/index representation
    current parser assumptions
    current migration rules

No clause is silently changed by this acceptance.

## 6. Assurance anti-anchoring is now a hard downstream input

The project owner previously clarified that:

    tests
    validators
    integrity checks
    CI workflows
    CD/deployment machinery
    repository checks
    current pytest organization
    current GitHub Actions topology
    current aggregate PASS shape

are all redesignable from scratch.

That clarification remains binding.

The accepted transition obligations are:

    CURRENT_ASSURANCE_TARGET_PRESERVATION_RIGHT=false

    CURRENT_ASSURANCE_MIGRATION_ORACLE_OBLIGATION=true

    ASSURANCE_INVARIANT_EXTRACTION_BEFORE_REPLACEMENT=true

The corrected probe strengthened this principle by showing that a check can carry the right label and still fail to exercise the intended invariant.

The next stage must therefore design assurance from required behaviors and failure modes, not from current test files or CI workflows.

## 7. MC-0027 closure

MC-0027 is resolved.

Claude's audit did not fail or get overridden.

Its AMEND finding was accepted and materially changed the evidence program.

The final sequence was:

    original probe
        18 / 18 reported PASS

    Claude audit
        7 VALID
        4 WEAK_BUT_DIRECTIONAL
        7 INVALID

    corrected protocol
        frozen without weakening original thresholds

    attempt 1
        HARNESS_INVALID

    attempt 2
        HARNESS_INVALID because G04 false-positive

    attempt 3
        18 / 18 blocking PASS
        2 / 2 amendment PASS

    owner
        ACCEPT

This history is retained because it is itself assurance-design evidence.

## 8. Next stage: first-principles assurance architecture

The next stage must derive, from scratch:

    what must be assured
    at which lifecycle boundary
    by which evidence class
    with what failure semantics
    under what trust assumptions
    at what execution location
    with what ownership
    and with what migration/cutover role

It must not begin with:

    "How should we reorganize the current tests?"

or:

    "Which GitHub Actions workflows should survive?"

The correct order is:

    system/repository invariants
        ->
    threat and failure model
        ->
    assurance claims
        ->
    evidence required per claim
        ->
    execution boundaries
        ->
    local/CI/release/cutover responsibilities
        ->
    mechanisms and tools
        ->
    migration mapping from current checks
        ->
    implementation

## 9. Relationship to activation/orchestration and migration

The assurance stage is upstream of physical migration because migration must be qualified by a trustworthy successor evidence system.

The activation/orchestration architecture remains semantically retained where already accepted, but its exact realization must later be reconciled against:

    accepted R8-A repository/workspace architecture
    accepted R8-B representation architecture
    accepted assurance architecture
    Specification 028 amendments

AO-10 remains held until those dependencies are sufficiently resolved.

Therefore the downstream order remains:

    accepted repository / information / representation architecture
        ->
    assurance architecture
        ->
    Specification 028 reconciliation
        ->
    exact migration/disposition planning
        ->
    AO-10 exact realization and qualification
        ->
    migration readiness gates
        ->
    owner migration authorization
        ->
    physical migration

If assurance or Specification-028 reconciliation reveals material architecture invalidation, AO-4 reopens the affected decision rather than patching around it.

## 10. Still held

    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false
    W5_F0=PAUSED
    AO10=HELD
    PSMF_EXTRACTION=NOT_AUTHORIZED
    SPECIFICATION028=UNCHANGED
    FILE_LEVEL_MIGRATION=HELD

## 11. Current state

    R8A=ACCEPTED_AS_AMENDED
    R8B=WMR_H_V0_3_ACCEPTED
    MC0027=RESOLVED

    P_R8B_01_R2_ATTEMPT_3=PASS
    BLOCKING_GATES=18_OF_18_PASS
    AMENDMENT_GATES=2_OF_2_PASS

    ASSURANCE_ARCHITECTURE=UNBLOCKED
    CURRENT_ASSURANCE_MECHANISMS=EVIDENCE_NOT_TARGET
    CURRENT_ASSURANCE_MIGRATION_ORACLE_OBLIGATION=true
    ASSURANCE_INVARIANT_EXTRACTION_BEFORE_REPLACEMENT=true

    SPECIFICATION028=UNCHANGED_PENDING_RECONCILIATION
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=FROM_SCRATCH_ASSURANCE_ARCHITECTURE
