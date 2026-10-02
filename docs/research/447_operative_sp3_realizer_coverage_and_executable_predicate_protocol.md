# Research 447: OPERATIVE SP-3 realizer-coverage and executable-predicate micro-probe protocol

**Date:** 2026-10-02
**Status:** SP-3 PROTOCOL FROZEN / DEVELOPMENT IMPLEMENTATION NEXT
**Parent:** Research 446 / Research 442 / Research 438
**Fixed evidence base:** b51ca73b3029f0a9cc71b66ea4589ff2217cf5d9
**Scope:** Prospectively freeze a small development probe of J2 realizer-declared coverage and J3 executable operational predicates against the surviving OPERATIVE V0.2 candidate before implementation or result observation.
**Authority:** Development-probe protocol only. This record does not select OPERATIVE for production, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, authorize production implementation, or switch authority.

## 1. Questions

SP-3 asks two coupled questions.

### J2 / coverage

Can realization be represented as exact natural-owner declarations over accepted clause identities, including many-to-many coverage, without reconstructing canonical implementation grouping at governing birth?

### J3 / operational truth

Given bounded source-owned facts, can the Project system derive the operational predicates it needs through executable rules with exact reproducibility and no semantic adjudication inside the evaluator?

## 2. Development-only evidence

SP-3 uses no hidden R2 item-level semantic material.

The four requirement fixtures below are derived from owner-ACCEPTED SP-2 representations and are therefore development-burned.

The experiment implementation is a research prototype only.

Nothing created by SP-3 becomes production authority or a production schema merely because the probe passes.

## 3. Frozen requirement fixtures

Use exactly four realization-requiring development requirements.

### SP3-R1

Origin:

    SP2-C3 / C3-CL01

Meaning:

    a governing acceptance binds the human carrier,
    operative component and exact referenced domain-contract revisions
    as one accepted meaning boundary.

### SP3-R2

Origin:

    SP2-C2 / C2-CL03

Meaning:

    deterministic consequential Project-system predicates/decisions
    have executable normative definitions and regression qualification.

### SP3-R3

Origin:

    SP2-C3 / C3-CL03

Meaning:

    deterministic machine-critical semantics use bounded typed references,
    not future reinterpretation of free-text conditions/effects.

### SP3-R4

Origin:

    SP2-C3 / C3-CL04

Meaning:

    when one domain already owns detailed accepted machine semantics,
    cross-domain OPERATIVE semantics reference that exact domain contract
    rather than creating a second independently authoritative copy.

No new requirement may be added after implementation begins without a new prospective protocol.

## 4. Realizer declaration model under test

SP-3 does not create a central hand-maintained obligation-to-artifact database.

Each development realizer record declares its own coverage:

    realizer_id
    artifact_ref
    artifact_sha256
    realizer_owner
    scope_ref
    realizes[]:
        clause_ref
        coverage_mode

Allowed coverage modes:

    FULL
    PARTIAL

A PARTIAL edge does not satisfy clause coverage by itself unless the frozen clause fixture explicitly defines a bounded composition rule.

For this probe:

    all satisfying edges are FULL

The validator accepts a coverage edge only when:

    clause_ref exists
    clause is active
    artifact exists
    artifact SHA matches
    realizer owner is the declared natural owner for this development artifact
    scope is compatible
    coverage_mode is allowed

The evaluator never infers coverage from artifact prose or filenames.

## 5. Frozen many-to-many topology

Implement exactly three development realizers:

    SP3-A  acceptance-bundle prototype
        covers R1, R3, R4

    SP3-B  executable-predicate engine prototype
        covers R2, R3

    SP3-C  domain-reference validator prototype
        covers R3, R4

This intentionally tests:

    one realizer -> multiple clauses
    one clause -> multiple realizers

No canonical partition or MUST_JOIN/MUST_SPLIT structure is permitted in the probe.

## 6. Frozen source-fact schema

Each predicate fixture supplies only bounded facts:

    clause_active
    coverage_edges_present
    coverage_edges_valid
    deferral_present
    deferral_authorized
    deferral_scope_valid
    deferral_temporally_valid
    evidence_required
    evidence_present
    evidence_exact_subject
    evidence_fresh
    qualification_required
    qualification_passed
    activation_required
    activation_effective
    conflict_present

No fixture contains a free-text semantic field consumed by either evaluator.

## 7. Frozen derived predicates

Both independent implementations must compute exactly:

    coverage_present
    coverage_valid
    deferral_effective
    evidence_valid
    qualification_complete
    activation_effective
    conflict_present
    realization_satisfied
    review_required

Definitions:

    coverage_present
        = coverage_edges_present

    coverage_valid
        = coverage_present AND coverage_edges_valid

    deferral_effective
        = deferral_present
          AND deferral_authorized
          AND deferral_scope_valid
          AND deferral_temporally_valid

    evidence_valid
        = NOT evidence_required
          OR (
              evidence_present
              AND evidence_exact_subject
              AND evidence_fresh
          )

    qualification_complete
        = NOT qualification_required
          OR qualification_passed

    activation_effective
        = NOT activation_required
          OR activation_effective_source_fact

    conflict_present
        = conflict_present_source_fact

    realization_satisfied
        = clause_active
          AND NOT conflict_present
          AND (
              deferral_effective
              OR (
                  coverage_valid
                  AND evidence_valid
                  AND qualification_complete
                  AND activation_effective
              )
          )

    review_required
        = clause_active
          AND (
              conflict_present
              OR (
                  coverage_present
                  AND NOT coverage_valid
              )
              OR (
                  deferral_present
                  AND NOT deferral_effective
              )
          )

Important:

    review_required=false does not imply realization_satisfied=true.

A clean uncovered active requirement is:

    realization_satisfied=false
    review_required=false

and is surfaced as an ordinary coverage gap rather than an ambiguous/conflicting fact state.

## 8. Frozen predicate fixtures

Implement exactly twelve fixtures.

    F01 complete/no optional gates
        active + valid coverage
        no evidence/qualification/activation required
        -> satisfied

    F02 complete/all required
        active + valid coverage
        valid evidence + qualification PASS + activation effective
        -> satisfied

    F03 missing coverage
        active + no coverage + no deferral
        -> not satisfied / no review

    F04 invalid coverage declaration
        active + coverage present but invalid
        -> not satisfied / review

    F05 valid deferral
        active + no coverage + valid governed deferral
        -> satisfied through deferral

    F06 invalid deferral
        active + no coverage + invalid governed deferral
        -> not satisfied / review

    F07 stale evidence
        active + valid coverage + evidence required/present/exact but stale
        -> not satisfied / no review

    F08 failed qualification
        active + valid coverage + qualification required but not passed
        -> not satisfied / no review

    F09 inactive activation
        active + valid coverage + activation required but ineffective
        -> not satisfied / no review

    F10 conflict
        active + otherwise complete + conflict present
        -> not satisfied / review

    F11 inactive clause
        inactive even with valid coverage
        -> not satisfied / no review

    F12 exact-subject evidence failure
        active + valid coverage + evidence required/present/fresh
        but evidence not exact-subject-bound
        -> not satisfied / no review

The result artifact must record every source fact and every expected predicate for all twelve fixtures.

## 9. Independent executable implementations

Create two implementations from this frozen protocol.

### Implementation A

Imperative Python.

Requirements:

    explicit named intermediate predicates
    straightforward boolean evaluation
    no import from Implementation B
    no shared rule helper

### Implementation B

Independent table/expression-oriented Python.

Requirements:

    separately encoded expressions
    no import from Implementation A
    no shared rule helper
    same JSON fixture input/output contract

Both may share only:

    Python standard library
    frozen fixture JSON
    result-comparison runner

The comparison runner may not implement the business rules itself.

## 10. Coverage validator

A separate coverage validator checks the three development realizer declarations.

It must include negative controls constructed only after this protocol is frozen:

    unknown clause reference
    stale artifact SHA
    wrong owner
    incompatible scope

All four negative controls must fail.

All frozen positive realizer declarations must pass.

## 11. Success conditions

SP-3 returns:

### SP3_MECHANISM_PLAUSIBLE

only if all are true:

    12/12 fixtures match frozen expected predicates in Implementation A
    12/12 fixtures match frozen expected predicates in Implementation B
    A and B outputs are exactly identical
    all positive realizer declarations validate
    all four coverage negative controls fail
    many-to-many coverage is represented without grouping
    no evaluator consumes free-text semantics
    no result requires owner/LLM semantic adjudication

### SP3_AMEND

when:

    deterministic execution succeeds
    but the probe exposes a local missing predicate,
    edge attribute or bounded source fact needed for the tested questions

### SP3_REDESIGN_REQUIRED

when any of these occur:

    coverage cannot be represented without inferred grouping/semantic interpretation
    realizer-owned declarations cannot identify coverage precisely
    the two independent implementations disagree on the frozen rules
    source facts are insufficient without semantic adjudication
    the model creates duplicate authority between coverage declarations and governing meaning

## 12. Burden observations

Record descriptively:

    realizer count
    coverage edge count
    clause count
    declaration fields per realizer
    validator logic size
    evaluator logic size
    fixture count

No adoption-economics conclusion is permitted.

SP-6 remains required for comparison with the detective-only null baseline.

## 13. Dependency interpretation

A plausible SP-3 result may justify:

    remapping DRP-04 detector assumptions to accepted clauses/control observations
    remapping DRP-06 orientation from one global state enum to predicate views
    reconsidering DRP-07 lineage around clause + realizer relations

It does not automatically resume those DRPs.

Any dependency-route change must be separately reconciled after the SP-3 result.

## 14. Execution sequence

    freeze this protocol
    validate / commit / push

    create research-only fixture bundle
    create three realizer declarations
    create coverage validator
    create Implementation A
    create Implementation B
    create comparison runner

    execute once against the frozen fixture bundle
    freeze immutable result
    reconcile before SP-4

No owner participation is required for SP-3 execution.

## 15. Current boundary

    SP3_PROTOCOL=FROZEN
    FIXED_EVIDENCE_BASE=b51ca73b3029f0a9cc71b66ea4589ff2217cf5d9
    REQUIREMENT_FIXTURES=4
    DEVELOPMENT_REALIZERS=3
    PREDICATE_FIXTURES=12
    INDEPENDENT_IMPLEMENTATIONS=2
    COVERAGE_NEGATIVE_CONTROLS=4
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false
    SP3_EXECUTED=false
    NEXT=IMPLEMENT_AND_EXECUTE_SP3
