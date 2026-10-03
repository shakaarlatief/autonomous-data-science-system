# Research 469: HYBRID C7 requirement-lineage micro-probe result

**Date:** 2026-10-03
**Status:** C7_LINEAGE_MECHANISM_PLAUSIBLE / C8 ORIENTATION PROBE NEXT
**Protocol:** Research 467
**Implementation freeze:** Research 468
**Frozen implementation commit:** 4e80160f1b1cbfecd00db95070737f09c07cfaf0
**Result artifact:** experiments/ao10_hybrid_c7_lineage_v01/result.json
**Result SHA-256:** 59d01fff11cdc38e6c79810d8c75f787a55b641b26dc7742d5cbc255afa2cad4
**Scope:** Record the single frozen HYBRID_C7_LINEAGE_V01 execution and update the thin-centred hybrid successor hypothesis.
**Authority:** Development evidence only. This result does not select production architecture, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Frozen execution result

The single authorized execution returned:

    fixture_total                12
    all_match                    true
    evaluators_agree_all         true
    negative_controls_visible    true
    nm_targets_correct           true
    outcome                      C7_LINEAGE_MECHANISM_PLAUSIBLE

Both separately encoded evaluators matched every frozen expected output exactly.

No fixture, expected output or implementation rule was changed after execution.

## 2. N:M lineage result

The probe supports a bounded requirement-lineage domain contract with immutable accepted requirement identities and governed relations:

    CARRY_FORWARD
    REPLACE
    SPLIT
    MERGE
    RETIRE

One-to-many SPLIT and many-to-one MERGE both produced the frozen current-target sets correctly.

This means requirement evolution does not require:

    mutating accepted historical meaning;
    forcing successor semantics into carrier paths;
    or treating one physical realization boundary as the canonical semantic identity.

## 3. Carry-forward is continuity, not succession

L1 showed that unchanged accepted meaning can retain the same requirement identity across a new carrier/revision.

CARRY_FORWARD therefore acts as a continuity annotation.

L12 showed that changed semantic digest cannot pass as carry-forward.

This preserves the distinction:

    same accepted meaning
        -> same semantic identity

    changed accepted meaning
        -> governed successor relation

rather than silently replacing one with the other.

## 4. Closed predecessor accounting

L7 correctly failed when a live predecessor in the accepted transition scope was neither:

    mapped;
    retired;
    nor explicitly declared unaffected.

This supplies a machine-checkable omission boundary for requirement evolution.

It is structurally analogous to the acceptance-time completeness rule qualified in Research 463 and the realization-completeness rule in KA-R52.

## 5. No competing owner-by-accident

L8 correctly rejected two separate outgoing semantic-succession relations for the same predecessor at the same boundary.

If one predecessor intentionally becomes several successors:

    use one SPLIT relation.

If several predecessors intentionally become one successor:

    use one MERGE relation.

This keeps cardinality explicit and prevents later traversal order or path order from choosing meaning.

## 6. Acyclic semantic succession

L9 correctly rejected a lineage cycle.

This is compatible with:

    DRP-01 governed_relation_reference
    existing identity-transition acyclicity
    DRP-07's normative dependency acyclicity requirement.

A historical semantic requirement may have many descendants or ancestors, but its prospective succession graph cannot point back into itself.

## 7. Authority and effective-boundary validity

L10 and L11 correctly failed relations whose:

    governing authority was not valid for the exact source/target revisions;
    or effective boundary did not match the accepted decision.

Therefore relation shape alone cannot manufacture semantic succession.

The accepted transition remains authority-bound.

## 8. Partial replacement and retirement

L5 supports:

    one predecessor
        -> one successor
        + explicit accepted retirement of an unmapped semantic remainder.

L6 supports explicit no-successor retirement.

This is important for future Specification 028 lineage work because semantic migration cannot assume every predecessor has a perfect successor.

Loss must be explicit and governed rather than disappearing from the graph.

## 9. DRP-01 seam result

The mechanism fits the already-supported shared substrate without adding a universal shared taxonomy.

Shared concepts remain:

    semantic identity
    exact subject/revision binding
    provenance
    governing lifecycle reference
    obligation reference
    governed relation reference.

Requirement-lineage classes and validation rules remain inside the bounded semantic/lifecycle domain.

Therefore:

    DRP01_SEAM_COMPATIBLE_AT_MECHANISM_LEVEL=true

This is not a rerun of DRP-01 and does not alter its historical PASS.

## 10. DRP-07 implication

The old DRP-07 preregistration expected a lineage matrix over Specification 028.

C7 does not execute that full audit.

It establishes a stronger successor mechanism on which a revised DRP-07 can later rely:

    every live predecessor accounted;
    exact current successor set;
    explicit retirement/loss;
    no competing owners;
    acyclic lineage;
    exact authority/effective-boundary binding.

The full 46-section / 104-MUST Specification 028 lineage reconciliation still remains later work.

## 11. Current successor mechanism after C4-C7

The leading development candidate now has plausible mechanisms for:

    stable J1 effect identity;
    governing completion criteria;
    deterministic bounded multi-artifact composition;
    N:M requirement succession;
    explicit retirement;
    exact source/revision/authority binding.

Still unresolved before owner architecture decision or larger pilot:

    C8  minimal shared generated orientation/status semantics
    C9  owner burden for surviving richer acceptance metadata.

C8 is next.

It should test the smallest useful generated orientation vocabulary over source-owned facts, not restore a separately authored global realization-state truth.

## 12. Current disposition

    C4=MECHANISM_PLAUSIBLE
    C5=MECHANISM_PLAUSIBLE
    C6=MECHANISM_PLAUSIBLE
    C7=LINEAGE_MECHANISM_PLAUSIBLE

    LEADING_CANDIDATE=THIN_CENTRED_HYBRID
    PRODUCTION_TARGET_SELECTED=false

    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=FREEZE_HYBRID_C8_ORIENTATION_STATUS_MICROPROBE
