# Research 464: thin-centred hybrid C4-C6 closure micro-probe protocol

**Date:** 2026-10-03
**Status:** PROTOCOL FROZEN / IMPLEMENTATION NEXT
**Parent:** Research 463
**Fixed evidence base:** 3c857f0f1a65b785566292eec22d85b0734a805f
**Scope:** Prospectively freeze a small development probe for J1 requirement granularity, governing completion-criterion authority, and deterministic multi-artifact PARTIAL composition before implementation or result observation.
**Authority:** Development-probe protocol only. This record does not select production architecture, amend Specification 028, expose hidden R2 item material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Why C4-C6 are tested together

Research 463 leaves three coupled questions open:

    C4  what constitutes one stable J1 requirement identity?
    C5  who is authorized to define what counts as completion?
    C6  how can several partial realizers jointly satisfy one requirement?

They cannot be tested independently without freezing assumptions about the others.

A coverage-composition rule needs a requirement identity.

A requirement identity needs a completion boundary.

A completion boundary must not be defined by the realizer whose work is being judged.

## 2. Candidate rule under test

The probe tests a deliberately small rule set.

### 2.1 J1 effect identity

At governing acceptance, every machine-tracked realization-requiring consequence receives one stable:

    accepted_effect_id

A REQUIRE identity binds exactly one independently acceptable governing effect.

An independently acceptable effect is one whose satisfaction or failure can be judged separately by the governing side without another sibling effect also being true.

Therefore:

    one independently acceptable effect
        -> one REQUIRE identity

A source sentence, paragraph or acceptance event may create multiple REQUIRE identities.

A single implementation artifact may later realize several REQUIRE identities.

Several artifacts may later contribute to one REQUIRE identity.

No J1 grouping is based on anticipated implementation artifact boundaries.

### 2.2 Completion contract

Every realization-requiring REQUIRE used for consequential completion must bind exactly one effective:

    completion_contract_ref

The completion contract is authoritative only when owned by:

    GOVERNING_ACCEPTANCE
        OR
    ACCEPTED_DOMAIN_CONTRACT

A realizer may not create or revise the completion contract merely by declaring coverage.

The completion contract contains:

    criterion_id
    requirement_ref
    authority_class
    authority_ref
    revision
    required_components[]
    composition_rule
    evidence_required
    qualification_required
    activation_required

For this first probe:

    composition_rule = ALL_REQUIRED

only.

The rule is intentionally narrow.

### 2.3 Realizer coverage

A natural-owner realizer may declare:

    realizer_id
    artifact_ref
    artifact_sha256
    realizer_owner
    requirement_ref
    covers_components[]

The realizer does not declare authoritative FULL completion.

A realizer may optionally report a self-assessment label for observability, but the evaluator must ignore it when computing completion.

### 2.4 Deterministic coverage closure

For one requirement:

    valid_component_coverage
        = union of components from valid realizer declarations
          intersected with the accepted completion contract's required_components

    coverage_complete
        = every required component is present in valid_component_coverage

Duplicate component claims add no coverage.

Unknown component claims are invalid and cause REVIEW_REQUIRED for the affected requirement.

A realizer-supplied or stale completion criterion is invalid.

### 2.5 Satisfaction

For this probe:

    requirement_satisfied
        = requirement_active
          AND completion_contract_valid
          AND coverage_complete
          AND evidence_valid
          AND qualification_complete
          AND activation_effective
          AND NOT conflict_present

where evidence, qualification and activation are evaluated from bounded source facts under the accepted completion contract.

A realizer's self-assessment is never an input to this predicate.

## 3. Granularity fixtures

Freeze four structured fixtures.

### G1 SINGLE_EFFECT

Accepted effect set:

    E1

Expected REQUIRE identities:

    R-E1

Expected result:

    VALID

### G2 TWO_INDEPENDENT_EFFECTS_SAME_SOURCE

Accepted effect set:

    E1
    E2

The two effects can be satisfied or fail independently.

Expected REQUIRE identities:

    R-E1
    R-E2

A single REQUIRE containing both effects is a negative control.

Expected result:

    SPLIT_REQUIRED

### G3 ONE_EFFECT_WITH_EVIDENCE_CONDITIONS

Accepted effect set:

    E1

The acceptance also requires evidence and independent qualification for completion.

Expected REQUIRE identities:

    R-E1

Evidence and qualification are completion-contract conditions, not additional realization-effect identities.

Expected result:

    VALID

### G4 EFFECT_PLUS_SEQUENCING_CONSEQUENCE

Accepted effect set:

    E1

A separate accepted sequencing consequence requires Q1 before E1 may become effective.

Expected:

    REQUIRE R-E1
    SEQUENCE S-Q1-E1

The sequencing consequence must not be folded into R-E1 as a second effect.

Expected result:

    VALID_WITH_SEPARATE_SEQUENCE

## 4. Completion and PARTIAL fixtures

Freeze ten cases.

### P1 SINGLE_PARTIAL

Required components:

    A
    B

Valid realizer coverage:

    R1 -> A

Expected:

    coverage_complete=false
    requirement_satisfied=false
    review_required=false

### P2 TWO_PARTIALS_COMPLETE_BUT_UNQUALIFIED

Required:

    A
    B

Coverage:

    R1 -> A
    R2 -> B

Qualification required and not passed.

Expected:

    coverage_complete=true
    requirement_satisfied=false
    review_required=false

### P3 TWO_PARTIALS_COMPLETE_AND_QUALIFIED

Required:

    A
    B

Coverage:

    R1 -> A
    R2 -> B

All required evidence, qualification and activation facts are valid.

Expected:

    coverage_complete=true
    requirement_satisfied=true
    review_required=false

### P4 SELF_CERTIFIED_FULL_MISSING_COMPONENT

Required:

    A
    B

Coverage:

    R1 -> A

R1 self-reports FULL.

Expected:

    coverage_complete=false
    requirement_satisfied=false
    review_required=false

The self-report must have no governing effect.

### P5 REALIZER_SUPPLIED_CRITERION

The accepted completion contract requires:

    A
    B

The realizer supplies a different local criterion requiring only:

    A

Expected:

    completion_contract_valid=false
    requirement_satisfied=false
    review_required=true

### P6 ACCEPTED_DOMAIN_CRITERION

The completion contract is owned by an exact accepted domain contract rather than the governing acceptance object.

Coverage and all required source facts satisfy it.

Expected:

    completion_contract_valid=true
    requirement_satisfied=true
    review_required=false

### P7 STALE_CRITERION_REVISION

The requirement binds completion-contract revision 3.

The evaluated criterion fact is revision 2.

Expected:

    completion_contract_valid=false
    requirement_satisfied=false
    review_required=true

### P8 DUPLICATE_PARTIALS

Required:

    A
    B

Coverage:

    R1 -> A
    R2 -> A

Expected:

    coverage_complete=false
    requirement_satisfied=false
    review_required=false

### P9 UNKNOWN_COMPONENT

Required:

    A
    B

Coverage:

    R1 -> A
    R2 -> C

Expected:

    coverage_complete=false
    requirement_satisfied=false
    review_required=true

### P10 COMPLETE_COVERAGE_ACTIVATION_MISSING

Required:

    A
    B

Coverage:

    R1 -> A
    R2 -> B

Activation is required but not effective.

Expected:

    coverage_complete=true
    requirement_satisfied=false
    review_required=false

## 5. Negative-control requirements

Implementation must reject or visibly fail:

    one REQUIRE carrying two independently acceptable effect IDs;
    a missing completion contract for consequential completion;
    a completion contract whose authority class is REALIZER;
    a stale criterion revision;
    an unknown component claim;
    self-reported FULL being treated as authoritative completion.

## 6. Implementation independence

Implement two evaluators after this protocol is committed.

Evaluator A:

    straightforward procedural validation and set coverage.

Evaluator B:

    separately encoded normalized-relation evaluation.

They may share fixture parsing but must not call one another's business-rule functions.

Both implementations must return exactly the frozen expected outputs.

This is implementation independence within one ChatGPT development interaction, not independent-author confirmation.

## 7. Outcome classes

### C4_C6_MECHANISM_PLAUSIBLE

Only if:

    all four granularity fixtures match expected outcomes;
    all ten completion/PARTIAL fixtures match expected outputs in both evaluators;
    both evaluators agree exactly on every derived field;
    every negative control fails visibly as frozen;
    no evaluator consumes free-text semantics;
    self-reported FULL never changes computed completion.

### C4_C6_AMEND

Use if the core rule is viable but one or more bounded schema/evaluator assumptions need local amendment.

### C4_C6_REDESIGN_REQUIRED

Use if:

    independently acceptable effect identity cannot avoid implementation grouping;
    completion authority cannot be separated from realizer self-certification;
    deterministic PARTIAL composition cannot be expressed without semantic prose adjudication;
    or the candidate needs the discarded full V0.5 grouping core to work.

### HARNESS_INVALID

Use if implementation deviates from this frozen protocol or expected fixtures are changed after result observation.

## 8. Limits

A pass will show only mechanism plausibility.

It will not establish:

    that humans/models can always identify independent effects reliably from arbitrary prose;
    that ALL_REQUIRED is the only needed composition rule;
    that component authoring burden is acceptable;
    that the final production schema is selected;
    that C7 lineage, C8 orientation or C9 owner burden is solved.

Those remain later questions.

## 9. Current boundary

    PROBE=HYBRID_C4_C6_V01
    GRANULARITY_FIXTURES=4
    COMPLETION_FIXTURES=10
    IMPLEMENTATIONS_REQUIRED=2

    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=IMPLEMENT_AND_FREEZE_HYBRID_C4_C6_V01
