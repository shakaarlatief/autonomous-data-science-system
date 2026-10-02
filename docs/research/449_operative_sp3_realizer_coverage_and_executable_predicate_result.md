# Research 449: OPERATIVE SP-3 realizer-coverage and executable-predicate result

**Date:** 2026-10-02
**Status:** SP-3 COMPLETE / SP3_MECHANISM_PLAUSIBLE / V0.2 CONTINUES / SP-4 FREEZE NEXT
**Protocol:** Research 447
**Implementation freeze:** Research 448
**Implementation commit:** 186e2c1d08296836fc4b9a356b4eef26aa95c0c1
**Implementation manifest SHA-256:** 336bf4629ffeb590aab05197971975b469357b9001f8956c2dae7b05626c8b48
**Result artifact:** experiments/ao10_operative_sp3_v01/SP3_RESULT_V01.json
**Result SHA-256:** 8572432082c2e350ec686841948a3e4351d2850c96c5b6f9cf880a2a0c27f4ea
**Result bytes:** 12697
**Scope:** Record the single authorized SP-3 execution and reconcile J2 realizer-declared coverage plus J3 executable-predicate mechanics against OPERATIVE V0.2.
**Authority:** Development evidence only. This result does not select OPERATIVE for production, amend Specification 028, authorize production implementation, expose hidden R2 material, resume dependent DRPs, migrate repository state, authorize SP-5, or switch authority.

## 1. Execution integrity

Research 447 froze the protocol before implementation.

Research 448 then froze the exact eleven-file pre-result implementation and pushed it before execution.

Immediately before the run, all implementation-manifest hashes were revalidated.

The runner was executed exactly once:

    python experiments/ao10_operative_sp3_v01/run_sp3.py

Observed exit code:

    0

No frozen implementation file was changed before execution.

Hidden R2 item-level semantic material was not used.

## 2. Coverage result

Frozen positive realizer declarations:

    SP3-A = VALID
    SP3-B = VALID
    SP3-C = VALID

Observed:

    positive realizers             3 / 3 valid
    realization coverage edges     7
    many-to-many topology          represented
    canonical grouping structure   absent

The topology includes:

    one realizer -> multiple clauses
    one clause -> multiple realizers

Coverage was validated only from explicit bounded declarations over:

    exact clause reference
    exact artifact reference
    artifact SHA-256
    declared realizer owner
    compatible scope
    allowed coverage mode

The validator never inferred coverage from prose or filenames.

## 3. Coverage negative controls

Frozen negative controls:

    N01 unknown clause reference
    N02 stale artifact SHA
    N03 wrong owner
    N04 incompatible scope

Observed:

    N01 = INVALID
    N02 = INVALID
    N03 = INVALID
    N04 = INVALID

Therefore:

    coverage negative controls = 4 / 4 PASS

## 4. Predicate result

Frozen predicate fixtures:

    12

Frozen derived predicates per fixture:

    coverage_present
    coverage_valid
    deferral_effective
    evidence_valid
    qualification_complete
    activation_effective
    conflict_present
    realization_satisfied
    review_required

Observed:

    Implementation A matches frozen expected outputs = true
    Implementation B matches frozen expected outputs = true
    A and B outputs exactly identical                = true

Therefore:

    A = 12 / 12 exact
    B = 12 / 12 exact
    cross-implementation agreement = 12 / 12 exact

Neither evaluator consumes free-text semantic fields.

No fixture required owner or LLM semantic adjudication during evaluation.

## 5. Frozen success-class evaluation

Research 447 defines SP3_MECHANISM_PLAUSIBLE only when all are true:

    12/12 A exact
    12/12 B exact
    A == B
    all positive realizers valid
    all four negative controls fail
    many-to-many coverage represented without grouping
    no evaluator consumes free text
    no result requires semantic adjudication

Every condition is satisfied.

Therefore:

    SP3 = SP3_MECHANISM_PLAUSIBLE

## 6. What SP-3 supports

The probe gives development support to two central OPERATIVE claims.

### J2

Realization-time coverage can be represented as explicit natural-owner-style relations over stable clause/artifact identities without requiring a canonical birth-time implementation partition.

At the mechanism level tested here, many-to-many coverage is straightforward.

### J3

Once source facts are bounded, operational truth can be derived through executable predicates without an authored global realization-state enum.

The tested predicate vector is sufficient to distinguish:

    satisfied realization
    ordinary missing coverage
    valid governed deferral
    invalid coverage declaration
    invalid deferral
    stale/wrong-subject evidence
    incomplete qualification
    ineffective activation
    explicit conflict
    inactive clause

This supports predicate-oriented generated views rather than treating one enum as authoritative state.

## 7. Important limitations

This result is intentionally narrow.

First:

    the realizer topology is a development prototype,
    not evidence from independent production engineering teams.

Therefore SP-3 establishes representational/mechanical plausibility, not the full behavioral burden or social naturalness of realizer declaration in production.

Second:

    both executable implementations were separately encoded
    but authored within the same ChatGPT development interaction.

Their exact agreement is evidence that the frozen rule specification can be implemented in distinct code paths.

It is not cross-model or cross-human reproducibility evidence.

Third:

    source facts were deliberately bounded before evaluation.

SP-3 therefore does not establish that every future natural owner can produce those facts cheaply, completely, or without its own semantic ambiguity.

That remains a whole-system realization/observability concern.

Fourth:

    the four requirement fixtures are development-burned
    and cannot later serve as untouched confirmation for a descendant tuned from this work.

## 8. Falsifier reconciliation

Research 442 F5:

    realizer coverage harder/more ambiguous than grouping

Result:

    NOT TRIGGERED at tested mechanism level.

No grouping was needed and every frozen positive/negative edge was mechanically decidable.

This does not close production burden.

Research 442 F6:

    executable predicates still require semantic adjudication of source facts

Result:

    NOT TRIGGERED inside the evaluator.

The evaluator used bounded source facts only.

This does not prove that upstream fact production is always semantically trivial.

## 9. Descriptive burden observations

    clauses                          4
    development realizers           3
    coverage edges                  7
    declaration top-level fields    6 per realizer
    predicate fixtures             12
    coverage negative controls      4
    coverage validator             55 nonblank code lines
    predicate engine A             56 nonblank code lines
    predicate engine B             40 nonblank code lines
    comparison runner              29 nonblank code lines

These are descriptive micro-probe measurements only.

No adoption-economics conclusion is permitted.

## 10. Dependency consequences

SP-3 now permits successor-dependency remapping work, but does not resume dependent DRPs.

Candidate remaps are:

    DRP-04
        detector assumptions should target
        accepted clause/control-observation boundaries
        rather than inferred ObligationUnit semantics

    DRP-06
        orientation should be reconsidered as generated predicate views
        rather than one authoritative global realization-state enum

    DRP-07
        lineage should be reconsidered around
        accepted clause identities + realizer/evidence relations

    DRP-08
        actual realizer-declaration burden remains part of
        adoption economics and must retain null baseline N

No dependent DRP executes from this record.

## 11. Progressive-route consequence

Research 438 required SP-0 through SP-3 to justify any larger end-to-end pilot.

Observed development sequence:

    SP-0 = MIXED_EXISTING_IDIOM
    SP-1 = OPERATIVE_GRAMMAR_PLAUSIBLE
    SP-2 = V02_MICRO_SURVIVES
    SP-3 = SP3_MECHANISM_PLAUSIBLE

This is sufficient to continue the small-probe program.

It is not sufficient to skip SP-4 through SP-6 or to freeze a confirmatory protocol.

The next planned probe is:

    SP-4 recital-leak detector

Its purpose is to test whether important machine consequences accidentally left in human prose can be detected without making the detector authoritative.

## 12. Current disposition

    SP3=COMPLETE
    SP3_RESULT=SP3_MECHANISM_PLAUSIBLE

    POSITIVE_REALIZERS=3/3_VALID
    COVERAGE_NEGATIVE_CONTROLS=4/4_PASS
    PREDICATE_A=12/12_EXACT
    PREDICATE_B=12/12_EXACT
    IMPLEMENTATIONS_IDENTICAL=true

    BIRTH_TIME_GROUPING_REQUIRED=false
    FREE_TEXT_EVALUATION_REQUIRED=false
    AUTHORITATIVE_GLOBAL_STATE_ENUM_REQUIRED=false

    F5_TESTED_MECHANISM=NOT_TRIGGERED
    F6_EVALUATOR=NOT_TRIGGERED

    OPERATIVE_V02=CONTINUE_DEVELOPMENT
    OPERATIVE_V02_TARGET_STATUS=NOT_SELECTED

    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED_NOW=false

    NEXT=FREEZE_SP4_RECITAL_LEAK_DETECTOR_PROTOCOL
