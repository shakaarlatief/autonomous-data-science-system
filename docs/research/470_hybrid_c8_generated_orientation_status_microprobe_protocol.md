# Research 470: thin-centred hybrid C8 generated orientation/status micro-probe protocol

**Date:** 2026-10-03
**Status:** PROTOCOL FROZEN / IMPLEMENTATION NEXT
**Parent:** Research 469
**Fixed evidence base:** 98a2304d36013d75aab2a88298e964670e6f6029
**Scope:** Prospectively freeze a bounded development probe for the smallest useful shared generated realization-orientation semantics before implementation or result observation.
**Authority:** Development-probe protocol only. This record does not select production architecture, amend Specification 028, expose hidden R2 item material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Question

Research 463 admitted a shared orientation need.

Research 469 now supplies stable current requirement identities and lineage.

C8 asks:

> What is the smallest shared, deterministic, non-authoritative realization-orientation projection that preserves the action-relevant distinctions needed by collaborators without restoring a separately authored global realization-state truth?

The probe does not rerun the full DRP-06 fresh-session comparison.

It qualifies only the realization-status projection that a later bounded orientation fixture may consume.

## 2. Source-fact boundary

C8 receives only current active requirement facts after governing-lifecycle and C7 lineage resolution.

The evaluator may consume:

    requirement_active
    source_facts_valid
    conflict_present

    deferral_present
    deferral_valid

    coverage_present
    coverage_complete

    evidence_required
    evidence_valid

    qualification_required
    qualification_complete

    activation_required
    activation_effective

    requirement_satisfied

No human-authored or realizer-authored realization-state label is authoritative input.

A fixture may include:

    reported_state

only as a negative control.

The evaluator must ignore it.

## 3. Candidate projection

Freeze one versioned derived projection:

    orientation_projection_version = HYBRID_C8_V01

Top-level state vocabulary:

    REVIEW_REQUIRED
    DEFERRED
    OPEN
    SATISFIED

Orthogonal next-gap vocabulary:

    REVIEW
    COVERAGE
    EVIDENCE
    QUALIFICATION
    ACTIVATION
    NONE

The purpose is to avoid turning every evidence/qualification milestone into a separately governed lifecycle truth.

## 4. Derivation order

For each active current requirement:

### 4.1 REVIEW_REQUIRED

If:

    source_facts_valid=false
        OR
    conflict_present=true
        OR
    deferral_present=true AND deferral_valid=false

then:

    state=REVIEW_REQUIRED
    next_gap=REVIEW

No later rule may override REVIEW_REQUIRED.

### 4.2 DEFERRED

Else if:

    deferral_present=true
    AND deferral_valid=true

then:

    state=DEFERRED
    next_gap=NONE

The projection does not infer deferral from a generic program hold.

It consumes only a validated governed deferral fact.

### 4.3 SATISFIED

Else if:

    requirement_satisfied=true

then:

    state=SATISFIED
    next_gap=NONE

### 4.4 OPEN

Otherwise:

    state=OPEN

and next_gap is the first unsatisfied required closure dimension in this order:

    if coverage_complete=false:
        COVERAGE

    else if evidence_required=true AND evidence_valid=false:
        EVIDENCE

    else if qualification_required=true AND qualification_complete=false:
        QUALIFICATION

    else if activation_required=true AND activation_effective=false:
        ACTIVATION

    else:
        REVIEW

The final REVIEW fallback prevents the orientation layer from silently calling an unexplained unsatisfied state complete.

## 5. Why this is smaller than V0.5's old state enum

The old V0.5 candidate used:

    UNLINKED
    LINKED
    EVIDENCED
    QUALIFIED
    OPERATIONAL
    DEFERRED
    REVIEW_REQUIRED

C8 tests whether the same action-relevant distinctions can be represented as:

    OPEN + COVERAGE
    OPEN + EVIDENCE
    OPEN + QUALIFICATION
    OPEN + ACTIVATION
    SATISFIED
    DEFERRED
    REVIEW_REQUIRED

This keeps milestone facts in their natural source domains while standardizing one shared orientation rendering.

## 6. Governing lifecycle remains separate

C8 does not encode:

    superseded
    retired
    historical
    candidate
    blocked workstream
    paused branch
    migration phase

inside realization status.

Those remain governed by their own lifecycle/control domains.

Only current active requirements enter this projection.

## 7. Frozen fixtures

Freeze eleven fixtures.

### O1 NO_COVERAGE

Expected:

    OPEN / COVERAGE

### O2 PARTIAL_COVERAGE

coverage_present=true
coverage_complete=false

Expected:

    OPEN / COVERAGE

### O3 COVERAGE_COMPLETE_EVIDENCE_MISSING

Expected:

    OPEN / EVIDENCE

### O4 EVIDENCE_VALID_QUALIFICATION_MISSING

Expected:

    OPEN / QUALIFICATION

### O5 QUALIFIED_ACTIVATION_MISSING

Expected:

    OPEN / ACTIVATION

### O6 SATISFIED

Expected:

    SATISFIED / NONE

### O7 VALID_DEFERRAL

Expected:

    DEFERRED / NONE

### O8 INVALID_DEFERRAL

Expected:

    REVIEW_REQUIRED / REVIEW

### O9 CONFLICT

Expected:

    REVIEW_REQUIRED / REVIEW

### O10 INVALID_SOURCE_FACTS

Expected:

    REVIEW_REQUIRED / REVIEW

### O11 BOGUS_REPORTED_OPERATIONAL

The source facts show incomplete coverage but reported_state=OPERATIONAL.

Expected:

    OPEN / COVERAGE

This is the negative control proving that an authored/reported state cannot override source facts.

## 8. Aggregate orientation output

In addition to per-requirement projection, the harness must deterministically compute:

    state_counts
    open_gap_counts
    attention_required_ids

where:

    attention_required_ids
        = sorted requirement IDs in REVIEW_REQUIRED

The aggregate is generated and non-authoritative.

## 9. Two evaluator requirement

Implement two evaluators after protocol commit.

Evaluator A:

    ordered procedural decision tree.

Evaluator B:

    normalized predicate table / priority selection.

They may share fixture parsing only.

They may not call one another's business-rule functions.

## 10. Outcome classes

### C8_ORIENTATION_MECHANISM_PLAUSIBLE

Only if:

    all eleven fixtures match frozen expectations in both evaluators;
    evaluators agree exactly;
    aggregate counts match;
    reported_state never affects output;
    REVIEW_REQUIRED precedence is preserved;
    DEFERRED uses only validated deferral;
    OPEN next-gap remains deterministic;
    no free-text semantic field is consumed.

### C8_AMEND

Use if the compact projection is useful but a bounded vocabulary/precedence rule needs local amendment.

### C8_REDESIGN_REQUIRED

Use if action-relevant orientation cannot be represented without authoring a separate state truth, duplicating natural-domain facts, or losing material distinction.

### HARNESS_INVALID

Use if fixtures/expectations or implementation change after result observation.

## 11. Limits

A pass will not establish the full historical DRP-06 PASS.

It will not test:

    fresh-session orientation correctness;
    <=64 KiB whole-orientation payload;
    repository read reduction;
    current stage / branch / authority / collaboration questions;
    complete user-facing wording.

Those belong to a later revised DRP-06 confirmation after the successor semantic architecture is stable enough.

A C8 pass establishes only that the realization-status subprojection is deterministic, bounded and compact.

## 12. Current boundary

    PROBE=HYBRID_C8_ORIENTATION_V01
    FIXTURES=11
    TOP_LEVEL_STATES=4
    NEXT_GAPS=6
    IMPLEMENTATIONS_REQUIRED=2

    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=IMPLEMENT_AND_FREEZE_HYBRID_C8_ORIENTATION_V01
