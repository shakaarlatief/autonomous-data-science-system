# Research 452: OPERATIVE SP-5 owner-review efficacy seeded-error protocol freeze

**Date:** 2026-10-02
**Status:** SP-5 PROTOCOL FROZEN / EXPLICIT INFORMED OWNER AUTHORIZATION REQUIRED BEFORE SEEDING OR REVIEW
**Parent:** Research 451 / Research 446 / Research 443 / Research 442
**Fixed evidence base:** 3d628e09444c1b7e4d2efc438692fb0e7dabf8bb
**Scope:** Prospectively freeze the owner-review efficacy micro-probe design, error classes, source units, blindness model and scoring before any deliberately erroneous owner-facing packet is created.
**Authority:** Development-probe protocol only. This record does not authorize SP-5 execution, select OPERATIVE for production, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Purpose

SP-2 established that the owner can judge faithful OPERATIVE consequence views with LOW burden after the task is explained.

SP-5 asks the complementary question:

> When a compact consequence review contains material semantic mistakes, does the owner actually detect them rather than simply accepting a plausible-looking machine summary?

This is an owner-review efficacy test.

It is not a test of the owner's memory, expertise or attentiveness as a person.

Its purpose is to determine whether the proposed governance workflow can rely on owner review as one safety layer.

## 2. Explicit-consent boundary

SP-5 intentionally introduces false statements into owner-facing development material.

Therefore:

    protocol design may be frozen now

but:

    no seeded packet may be created
    no error placement may be instantiated
    no seeded item may be shown to the owner
    no SP-5 review may begin

until the owner gives explicit informed authorization after being told:

    the review will deliberately contain some material errors
    the errors are inserted only for this development experiment
    the owner will not be told which items are altered before review
    the results will be used only as development evidence
    accepting a seeded error has no governing consequence
    the packet does not change real project authority

A generic "proceed" issued before this consent request does not count.

## 3. Frozen source units

Use exactly six previously owner-accepted SP-2 consequence units as clean source material.

### U1

Origin:

    SP2-C1 / C1-CL02

Clean meaning:

    R2 may not be retried, relabeled, threshold-tuned,
    converted into a final key, or rescued by owner adjudication.

### U2

Origin:

    SP2-C1 / C1-CL03

Clean meaning:

    hidden R2 item-level semantics may be exposed only after a
    separate prospective owner route that records the exposure purpose,
    evidence-burn consequence and replacement-confirmation consequence.

### U3

Origin:

    SP2-C1 / C1-CL04

Clean meaning:

    Research 436 successor development does not itself authorize
    physical migration or operational authority switch.

### U4

Origin:

    SP2-C2 / C2-CL04

Clean meaning:

    SP-5 seeded-error owner-review execution requires explicit informed owner authorization.

### U5

Origin:

    SP2-C2 / C2-CL06

Clean meaning:

    unaccepted model/LLM semantic output may not become governing authority merely because it was generated.

### U6

Origin:

    SP2-C3 / C3-CL04

Clean meaning:

    when a domain-native accepted contract already owns detailed machine semantics,
    OPERATIVE references that contract rather than creating a second independent authority copy.

These six units are already development-burned by SP-2 and may be reused for development.

## 4. Frozen error classes

Exactly three of the six review items will be materially corrupted.

Exactly one seeded item uses each error class:

### E1 WRONG_OWNER

A consequence is reassigned to a semantically wrong authority/domain owner in a way that would change who controls the decision.

### E2 MISSING_GATE_CONDITION

One necessary prerequisite is removed from a gate, making an otherwise prohibited transition appear admissible under weaker conditions.

### E3 INVERTED_OR_BROKEN_PROHIBITION_SCOPE

A prohibition is narrowed, inverted, or supplied with an unauthorized exception such that action becomes permitted in a scope where the accepted meaning prohibits it.

The other three items remain clean.

No cosmetic/trivial error counts as a seed.

## 5. Prospective placement without pre-consent seeding

Seed placement is not chosen now.

After explicit owner authorization is durably recorded, compute one deterministic permutation from:

    SHA256(
        "OPERATIVE-SP5-V01|"
        + <authorization-record-commit-sha>
        + "|U1|U2|U3|U4|U5|U6"
    )

Use that digest to derive:

    three seeded unit IDs
    assignment of E1/E2/E3 to those three units

subject to compatibility rules below.

If a derived error class is incompatible with a unit's semantics, advance deterministically to the next compatible unit in cyclic source-unit order.

Compatibility:

    E1 WRONG_OWNER
        permitted on U2, U3, U4, U5, U6

    E2 MISSING_GATE_CONDITION
        permitted on U2, U3, U4

    E3 INVERTED_OR_BROKEN_PROHIBITION_SCOPE
        permitted on U1, U3, U4, U5

The exact deterministic algorithm must be implemented and frozen immediately after authorization before the packet is shown.

This prevents the experimenter from choosing "easy" or "hard" placements after consent.

## 6. Owner-facing format

The packet contains six compact natural-language consequence cards in shuffled order.

Each card shows only:

    review_item_id
    short context
    proposed consequence view

The owner is asked:

> Does this consequence view still correctly represent the accepted meaning?

For each item:

    ACCEPT
    AMEND
    REJECT
    CANNOT_JUDGE

Free-form correction is allowed.

The owner is **not** told:

    which three items are seeded
    which error class is attached to any item
    how the packet maps back to U1-U6

until review is committed.

The owner **is** told in advance that exactly three of six items contain deliberate material errors.

## 7. Scoring semantics

A seeded item is detected when the owner returns:

    AMEND
    or
    REJECT

and the stated correction identifies the material semantic problem sufficiently to distinguish it from an unrelated stylistic objection.

A seeded item is missed when the owner returns:

    ACCEPT

A CANNOT_JUDGE on a seeded item is:

    protective but not a semantic detection

and is recorded separately.

A clean item produces a false alarm when the owner returns:

    AMEND
    or
    REJECT

for a claimed semantic defect that is not present in the clean reference meaning.

CANNOT_JUDGE on a clean item is recorded as review friction, not a false semantic alarm.

## 8. Frozen outcome classes

### SP5_OWNER_REVIEW_EFFICACY_PLAUSIBLE

    all 3 seeded errors detected
    AND
    0 clean semantic false alarms

### SP5_OWNER_REVIEW_EFFICACY_AMEND

Any of:

    2 / 3 seeded errors detected
    AND <= 1 clean semantic false alarm

or:

    all 3 seeded errors detected
    AND 1 clean semantic false alarm

### SP5_OWNER_REVIEW_EFFICACY_WEAK

Any of:

    <= 1 / 3 seeded errors detected
    OR
    >= 2 clean semantic false alarms

CANNOT_JUDGE counts are reported separately and may trigger interface redesign even if semantic detection is otherwise plausible.

These are development-routing classes only.

They do not quantify a universal human-review error rate.

## 9. Non-consequence guarantee

SP-5 review responses have no governing semantic effect.

Specifically:

    accepting a seeded false statement does not amend the project
    rejecting a clean statement does not invalidate existing authority
    corrections do not automatically change OPERATIVE V0.2
    all six packet statements are experimental review material only

After scoring, the owner is shown:

    which items were seeded
    the exact clean meaning
    the seeded alteration
    the score

Any architectural amendment requires a separate reconciliation record.

## 10. Evidence limitations

This is a deliberately tiny micro-probe.

The owner has already seen the underlying clean meanings in SP-2.

The owner will know that three errors exist.

Therefore a successful result supports only:

    owner review can detect material corruption under an informed review condition

It does not establish:

    production false-negative rate
    detection under fatigue
    detection when error prevalence is unknown
    detection by another reviewer
    production adoption economics

Those questions remain outside this probe.

## 11. Current boundary

    SP5_PROTOCOL=FROZEN
    SOURCE_UNITS=6
    SEEDED_ITEMS=3
    CLEAN_ITEMS=3
    ERROR_CLASSES=WRONG_OWNER|MISSING_GATE_CONDITION|INVERTED_OR_BROKEN_PROHIBITION_SCOPE

    OWNER_EXPLICIT_INFORMED_AUTHORIZATION=false
    SEEDED_PACKET_CREATED=false
    SEEDED_PACKET_SHOWN=false

    HIDDEN_R2_DETAILS=SEALED

    NEXT=OWNER_DECIDE_SP5_SEEDED_ERROR_AUTHORIZATION
