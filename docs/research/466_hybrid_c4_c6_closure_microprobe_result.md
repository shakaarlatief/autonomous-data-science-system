# Research 466: HYBRID C4-C6 closure micro-probe result

**Date:** 2026-10-03
**Status:** C4_C6_MECHANISM_PLAUSIBLE / C7 LINEAGE PROBE NEXT
**Protocol:** Research 464
**Implementation freeze:** Research 465
**Frozen implementation commit:** 3d19ade76d6e469b52b99de69b289ac62a460052
**Result artifact:** experiments/ao10_hybrid_c4_c6_v01/result.json
**Result SHA-256:** bcf04dd33e98649739b05874ab54d4f8a9d48534a545a9ff1eb5e6016c0efc6d
**Scope:** Record the single frozen execution of HYBRID_C4_C6_V01 and update the successor architecture hypothesis.
**Authority:** Development evidence only. This result does not select production architecture, amend Specification 028, expose hidden R2 item material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Frozen execution result

The single authorized execution returned:

    granularity_total              4
    granularity_all_match          true
    completion_total               10
    completion_all_match           true
    evaluators_agree_all           true
    negative_controls_visible      true
    self_certification_blocked     true
    outcome                        C4_C6_MECHANISM_PLAUSIBLE

Both separately encoded evaluators matched every frozen expected output.

No fixture, expected result or implementation file was changed after the execution.

## 2. C4: J1 granularity

The probe supports this bounded structural rule:

    one stable REQUIRE identity
        per independently acceptable governing effect

with sequencing represented separately rather than folded into the REQUIRE identity.

G2 correctly rejected one REQUIRE carrying two independently acceptable effects.

G4 correctly preserved one REQUIRE for the effect and a separate SEQUENCE relation.

The result supports a J1 effect boundary that is independent from future implementation artifact grouping.

It does not prove that humans or models can always identify independently acceptable effects reliably from arbitrary prose.

That authoring problem remains part of later burden/faithfulness qualification.

## 3. C5: governing completion authority

The probe supports a strict separation between:

    realizer coverage declaration

and:

    governing completion definition.

A completion contract was valid only when owned by:

    GOVERNING_ACCEPTANCE
        OR
    ACCEPTED_DOMAIN_CONTRACT

P5 correctly refused a realizer-supplied replacement criterion.

P7 correctly refused a stale criterion revision.

Therefore a realizer cannot make its own work complete by changing the standard against which it is evaluated.

## 4. C6: PARTIAL composition

For the bounded ALL_REQUIRED rule, the probe supports deterministic multi-artifact composition.

Coverage closure is computed from:

    union(valid component claims)
        against
    accepted required_components.

Observed controls:

    one partial edge did not satisfy A+B;
    A from one realizer plus B from another completed coverage;
    duplicate A+A did not complete A+B;
    unknown component C caused review;
    self-reported FULL did not override missing component B.

This establishes a concrete alternative to trusting author-supplied FULL/PARTIAL labels as completion authority.

The realizer reports bounded component coverage.

The system computes completion against the accepted criterion.

## 5. Satisfaction remains stronger than coverage

P2 and P10 confirm:

    coverage_complete=true

does not imply:

    requirement_satisfied=true.

Independent required qualification or activation can still keep the requirement unsatisfied.

The successor architecture should therefore preserve distinct predicates for:

    coverage closure
    evidence validity
    qualification completion
    activation effectiveness
    conflict
    final satisfaction.

## 6. Candidate successor amendment

The thin-centred hybrid successor can now be amended with the following mechanism-level contract:

### J1

    accepted_effect_id
        stable identity for one independently acceptable governing effect

    REQUIRE
        binds exactly one accepted_effect_id

    completion_contract_ref
        mandatory for consequential realization completion

    completion contract authority
        governing acceptance or exact accepted domain contract

### J2

    realizer declaration
        identifies requirement
        identifies artifact/natural owner
        declares covered completion components

    no authoritative self-declared FULL state

### J3

    coverage_complete
        deterministically derived from accepted criterion + valid component coverage

    requirement_satisfied
        derived from coverage + evidence + qualification + activation + conflict rules

This does not require:

    birth-time implementation grouping
    V0.5 ObligationUnit as universal core
    realizer-authored completion criteria
    authoritative global realization state.

## 7. Limits and next question

C4-C6 are mechanism-plausible only.

Still unresolved:

    C7  N:M requirement lineage across split / merge / carry-forward / replacement
    C8  minimal shared generated orientation/status semantics
    C9  owner burden for the surviving richer acceptance metadata

C7 is next because lineage determines whether the new stable J1 requirement identities remain safe when governing contracts evolve.

The next development probe should test:

    one-to-one carry-forward
    one-to-many split
    many-to-one merge
    replacement with partial carry-forward
    explicit retirement
    unmapped live predecessor detection
    cycle rejection
    exact authority/effective-boundary validity

against the DRP-01 shared semantic seam and DRP-07 lineage obligations.

No owner participation is required to freeze and run the first C7 mechanism probe.

## 8. Current disposition

    C4=MECHANISM_PLAUSIBLE
    C5=MECHANISM_PLAUSIBLE
    C6=MECHANISM_PLAUSIBLE

    FULL_THIN_V02_SUFFICIENT=false
    FULL_RICH_V05_REQUIRED=false
    LEADING_CANDIDATE=THIN_CENTRED_HYBRID

    PRODUCTION_TARGET_SELECTED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_HYBRID_C7_REQUIREMENT_LINEAGE_MICROPROBE
