# Research 454: OPERATIVE SP-5 deterministic seed algorithm and corruption library freeze

**Date:** 2026-10-03
**Status:** SEED ALGORITHM + COMPLETE COMPATIBLE CORRUPTION LIBRARY FROZEN / PLACEMENT NOT YET COMPUTED
**Protocol:** Research 452
**Owner authorization:** Research 453 / commit b3f06a414697b8ac99fd57fcae04159ab01eb35c
**Seed-freeze manifest:** experiments/ao10_operative_sp5_v01/seed_freeze_manifest.json
**Seed-freeze manifest SHA-256:** 338a95a8c63f339bc5caf0c0d4eb53fcd2abf5b6bbeaa62585631de64d308d09
**Scope:** Freeze the exact deterministic placement mechanism and every compatible seeded alteration before computing which units receive errors.
**Authority:** Development implementation freeze only. No placement/result is observed in this record and no owner-facing seeded packet exists yet.

## 1. Prospective anti-selection rule

The authorization commit is fixed:

    b3f06a414697b8ac99fd57fcae04159ab01eb35c

The placement implementation is frozen before it is executed.

The experimenter therefore does not select the three seeded units after seeing the algorithm output.

## 2. Seed material

The exact base digest input is:

    OPERATIVE-SP5-V01|b3f06a414697b8ac99fd57fcae04159ab01eb35c|U1|U2|U3|U4|U5|U6

The algorithm computes SHA-256 of that string once.

All subsequent deterministic ranks are SHA-256 values over:

    seed_digest | tag | value

## 3. Placement algorithm

The algorithm:

1. deterministically orders U1-U6 using tag SEED-UNIT-ORDER;
2. processes error classes in the fixed Research 452 order E1, E2, E3;
3. for each error, scans cyclically from the current cursor until it finds the first compatible unused unit;
4. selects that unit and advances the cursor;
5. separately orders all six owner cards using tag OWNER-PACKET-ORDER.

No random library, wall-clock time, environment value, model choice, or manual seed decision is used.

## 4. Complete corruption library

Before placement execution, all compatible error/unit pairs are frozen.

Counts:

    E1 WRONG_OWNER compatible templates                    5
    E2 MISSING_GATE_CONDITION compatible templates         3
    E3 BROKEN_PROHIBITION_SCOPE compatible templates       4
    total frozen corruption templates                     12

Each template includes:

    exact seeded consequence view
    exact detection criterion used after owner review

The library prevents post-placement tailoring of wording to make the chosen items easier or harder.

## 5. Frozen implementation files

    experiments/ao10_operative_sp5_v01/clean_units.json
    experiments/ao10_operative_sp5_v01/corruption_templates.json
    experiments/ao10_operative_sp5_v01/seed_algorithm.py
    experiments/ao10_operative_sp5_v01/seed_freeze_manifest.json

Only syntax parsing and static JSON/compatibility validation were performed.

The placement function was not executed before this freeze.

## 6. Packet-generation behavior

After this freeze is pushed, exactly one placement/build execution will create:

    owner_review_packet.json
    evaluator_key.json

The owner-facing packet exposes only:

    review item ID
    short context
    proposed consequence view
    the reminder that exactly three of six cards are deliberately erroneous

The evaluator key remains blinded from the owner until the review response is frozen and scored.

## 7. Current boundary

    OWNER_EXPLICIT_INFORMED_AUTHORIZATION=true
    SEED_ALGORITHM_FROZEN=true
    CORRUPTION_TEMPLATE_LIBRARY_FROZEN=true
    COMPATIBLE_TEMPLATE_COUNT=12

    SEED_PLACEMENT_COMPUTED=false
    SEEDED_PACKET_CREATED=false
    SEEDED_PACKET_SHOWN=false

    NEXT=EXECUTE_SP5_SEED_PLACEMENT_ONCE
