# Research 473: thin-centred hybrid C9 owner-burden protocol

**Date:** 2026-10-03
**Status:** PROTOCOL FROZEN / OWNER PACKAGE DRAFTING NEXT
**Parent:** Research 472
**Fixed evidence base:** bca984569a7df80fde253a50b47b0e319678b380
**Scope:** Prospectively freeze the owner-burden test for the surviving richer acceptance metadata in the thin-centred hybrid.
**Authority:** Development-probe protocol only. This record does not select production architecture, amend Specification 028, expose hidden R2 item material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Question

SP-2 established LOW semantic-review burden for the tested thin consequence view after the review task was explained clearly.

Research 461 correctly states that this result cannot simply be transferred to richer metadata.

C9 asks:

> Can the additional owner-reviewed information that survived C4-C8 be reviewed as part of the same governing acceptance without disproportionate burden or requiring the owner to understand internal schema mechanics?

## 2. What richer metadata actually survived

C9 tests only metadata that still plausibly belongs at J1 owner/governance acceptance time:

    stable accepted-effect identity
    explicit realization-tracking disposition
    governing completion criterion where consequential completion is claimed
    exact completion-criterion authority/reference
    explicit lineage mapping when an accepted governing effect is amended/replaced/split/merged/retired

C9 does not test owner review of:

    realizer declarations
    generated coverage closure
    generated orientation status
    evidence/qualification runtime facts
    compiled control projections

Those are J2/J3/generated concerns and must not be shifted onto the owner merely to make the architecture look complete.

## 3. Review cases

Freeze exactly three compact cards.

### C9-A: completion criterion for an executable requirement

Source semantic anchor:

    SP2-C2 / C2-CL03

Meaning already owner-accepted in SP-2:

    deterministic consequential Project-system predicates/decisions must be defined executably and regression-tested.

The richer card adds only:

    accepted effect identity
    realization-tracked = yes
    completion criterion:
        executable normative definition exists
        required regression qualification passes
    completion authority:
        governing acceptance / accepted verification contract

### C9-B: closed accounting for an acceptance-boundary requirement

Source semantic anchor:

    SP2-C3 / C3-CL01

Meaning already owner-accepted in SP-2:

    a governing acceptance binds the human carrier, operative component and exact referenced domain-contract revisions as one accepted meaning boundary.

The richer card adds only:

    accepted effect identity
    realization-tracked = yes
    completion criterion:
        all required bound components/revisions are present and exact
        acceptance validation passes
    explicit no-untracked-third-state accounting

### C9-C: lifecycle/lineage review

Source semantic anchor:

    SP2-C2 / C2-CL01

Meaning already owner-accepted in SP-2:

    Research 438 prospectively amends Research 437 for the reconciled successor-design scope.

The richer card adds only an owner-visible lifecycle summary:

    predecessor
    successor
    relation
    affected scope
    whether anything is explicitly retired or left unaffected

The card must not expose graph/schema internals.

## 4. Owner interface

The package must be presented in natural language.

For each card the owner answers one of:

    ACCEPTABLE
        this is a reasonable amount/type of extra information to review when making the governing decision

    NEEDS_SIMPLIFICATION
        the underlying idea is fine but this asks the owner to review too much or presents it badly

    CANNOT_JUDGE
        the review still requires architecture/schema knowledge that should not be necessary

Optional free-form correction is allowed.

After all three cards the owner supplies exactly one overall burden rating:

    LOW
    MODERATE
    HIGH

Definitions shown to the owner:

    LOW
        the extra review feels small and straightforward

    MODERATE
        noticeable additional review, but still practical for consequential governing decisions

    HIGH
        burdensome enough that this should not be a normal acceptance requirement

No timing measurement is required.

## 5. Interpretation

C9_BURDEN_PLAUSIBLE only if:

    no card is CANNOT_JUDGE
    no card identifies a conceptual need to remove the metadata
    overall burden is LOW or MODERATE

C9_INTERFACE_AMEND if:

    one or more cards are NEEDS_SIMPLIFICATION
    but the owner does not reject the underlying information need
    and overall burden is not HIGH

C9_BURDEN_FAILURE if:

    overall burden is HIGH
    OR
    the owner cannot judge because the architecture requires schema/internal mechanics
    OR
    the owner says the metadata itself should not normally be part of governing review

The Project must not infer the owner verdict or burden rating.

## 6. Baseline interpretation

The historical SP-2 LOW rating is retained as context only.

C9 does not ask the owner to repeat C1/C2/C3 semantic-faithfulness review.

It asks whether the incremental richer acceptance information is practical.

## 7. UX constraint

The package must obey the SP-2 lesson:

    state the task directly
    show meaning in ordinary language
    do not require probe nomenclature
    do not require internal JSON
    do not require clause-schema knowledge
    do not require architecture-research bookkeeping

Machine details may remain available as drill-down but are not part of the default owner task.

## 8. Current boundary

    PROBE=HYBRID_C9_OWNER_BURDEN_V01
    CARDS=3
    PRIOR_THIN_BURDEN=LOW
    HIDDEN_R2_DETAILS=SEALED

    OWNER_PARTICIPATION_REQUIRED=true
    NEXT=FREEZE_C9_OWNER_REVIEW_PACKAGE
