# Research 421: Owner Acceptance of DRP-03 R2 Component-Scoped Continuation

**Date:** 2026-10-01
**Status:** ACCEPTED / PROSPECTIVE IMPLEMENTATION AUTHORIZED / KEY B STILL HELD
**Parent:** Research 420
**Scope:** Record the owner's explicit acceptance of the component-scoped continuation amendment and define the implementation boundary that follows.
**Authority:** Owner decision for the Research 420 protocol amendment. This authorizes prospective implementation and qualification of component-scoped Key A packaging/commitment and the clean Key B control plane. It does not authorize semantic retry of Key A LEGACY, P6C, Key B semantic execution before qualification, reviewer scoring, migration, oracle retirement, or authority switching.

## 1. Owner decision

The project owner explicitly chose:

    ACCEPT

for Research 420.

The accepted amendment is therefore part of the active DRP-03 R2 protocol from this point forward.

## 2. Frozen historical Key A LEGACY disposition

The observed Key A LEGACY result is preserved exactly:

    P6B sources accepted = 17 / 17
    material-gap witness floor = PASS
    already-realized false-gap control floor = PASS
    negative-control source check = FAIL
    P6B finalization = EVIDENCE_INSUFFICIENT

Historical Key A LEGACY is now terminal:

    KEY_A_LEGACY_KEY_CONSTRUCTION = INCONCLUSIVE
    reason = FROZEN_NEGATIVE_CONTROL_CHECK_FAILURE
    P6C = NOT_RUN

No same-corpus semantic repair, retry, relabeling, regrouping, source replacement, threshold relaxation, evidence-horizon widening, or control-plane bypass is authorized.

## 3. Accepted component-scoped continuation

The qualifying Key A bundle may contain only:

    STATE
    BIRTH classification
    BIRTH grouping

LEGACY is explicitly excluded from that qualifying bundle.

Any Key A component-scoped commitment must bind both:

    exact included component set
    exact excluded-component disposition

with:

    LEGACY = INCONCLUSIVE / NEGATIVE_CONTROL_CHECK_FAILURE

The commitment is an immutability/provenance commitment, not a qualification claim for LEGACY.

## 4. Consequence preservation

The accepted amendment does not weaken the historical LEGACY consequence.

The following remain blocked:

    qualified obligation-unit lineage
    legacy migration/reconciliation authority
    oracle-retirement uses that require qualified LEGACY units

Historical LEGACY construct validity remains:

    NOT_ESTABLISHED

## 5. Key Author B boundary

A fresh blind Key Author B may later author:

    STATE
    BIRTH

only after the component-scoped packaging/commitment machinery and clean Key B environment are implemented and mechanically qualified.

Key B must remain blind to Key A private outputs and storage.

Key B does not author historical LEGACY in this attempt.

## 6. Authorized implementation work

The following prospective work is now authorized:

    component-scoped canonical Key A serialization
    component-scoped Key A commitment generation
    included/excluded component verification
    explicit preservation of failed LEGACY disposition
    private artifact immutability verification
    clean isolated Key B root/control-plane preparation
    tests proving excluded LEGACY cannot be interpreted as PASS
    tests proving excluded LEGACY cannot alter included component bytes
    tests proving Key B cannot read Key A private storage
    bounded Runtime Bridge publication/activation of the qualified controls

Key B semantic execution remains held until these controls qualify.

## 7. Attempt accounting

This acceptance does not create a second historical semantic attempt.

The existing Key A semantic work remains Attempt 1.

Any future LEGACY qualification effort requires a new prospective experiment/protocol version under independently frozen conditions unless a genuinely independent HARNESS_INVALID finding is established.

No such HARNESS_INVALID finding exists now.

## 8. Current boundary

    RESEARCH420_OWNER_DECISION = ACCEPT
    COMPONENT_SCOPED_CONTINUATION = ACTIVE_PROTOCOL
    KEY_A_LEGACY = INCONCLUSIVE / FROZEN
    KEY_A_P6C = NOT_RUN

    COMPONENT_SCOPED_IMPLEMENTATION = AUTHORIZED
    COMPONENT_SCOPED_COMMITMENT = NOT_YET_QUALIFIED
    KEY_AUTHOR_B_CONTROL_PLANE = AUTHORIZED_TO_PREPARE
    KEY_AUTHOR_B_SEMANTIC_EXECUTION = NOT_YET_AUTHORIZED
    CONSTRUCT_COMPARISON = NOT_YET_AUTHORIZED

    NEXT = IMPLEMENT_AND_QUALIFY_COMPONENT_SCOPED_KEY_CONTINUATION
