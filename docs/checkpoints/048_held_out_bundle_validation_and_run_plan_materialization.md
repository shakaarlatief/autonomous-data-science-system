# Checkpoint 48: Held-Out Bundle Validation and Run-Plan Materialization

**Date:** 2026-08-10

## Purpose

Implement the next condition-neutral held-out control layer after B0/B1 resource parity was deterministically validated.

No paid H1/H2 treatment call has occurred.

## Implemented controls

A new module, `ads_v0.heldout_execution`, now performs no model inference and provides deterministic pre-execution controls:

```text
1. load the preregistered held-out protocol;
2. load the bundle identities frozen before P0 implementation;
3. verify local H1/H2 bundle case identity, surface variant, selected seed,
   self-test status, file count, and aggregate SHA-256 fingerprint;
4. materialize the exact registered 30-slot H1/H2 condition schedule;
5. verify that each replicate contains B0, B1, and P0 exactly once;
6. verify 10 slots per condition and 30 total slots;
7. generate stable attempt IDs inside each slot;
8. preserve at most two replacement attempts without changing slot order;
9. write a deterministic run-plan JSON linked to the verified bundle hashes;
10. refuse to overwrite an existing run plan unless explicitly forced.
```

The committed pre-P0 bundle identity record is:

```text
prototype_v0/configs/held_out_bundle_fingerprints_v0_1.json
```

Frozen identities remain:

```text
H1
seed: 811
files: 9
SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2
seed: 1601
files: 9
SHA-256: 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

## Stable slot semantics

A preregistered slot has a stable identifier such as:

```text
h1-r01-b0
```

Its initial and possible infrastructure-replacement attempts are represented as:

```text
h1-r01-b0-a01
h1-r01-b0-a02
h1-r01-b0-a03
```

The latter two are replacement attempts inside the same slot. They never create a new experimental slot or reorder later conditions.

Replacement eligibility itself remains unchanged from Foundation 012 and will be enforced by the paid execution layer:

```text
provider/infrastructure generation termination after retries -> replacement eligible
behavioral failure -> not replacement eligible
```

Behavioral failures include Python errors/timeouts, poor methodology, semantic failures, and treatment-caused resource exhaustion.

## New deterministic tests

Four tests were added for:

```text
exact 30-slot preregistered order and per-condition counts;
stable initial/replacement attempt identifiers;
exact bundle fingerprint acceptance and tamper rejection;
run-plan resource snapshot plus no-overwrite protection.
```

Expected complete suite after this checkpoint:

```text
62 passed
```

## Boundary

This checkpoint does not yet execute B0, B1, or P0 on H1/H2. It prepares and verifies the immutable inputs and schedule that the paid sequential executor will consume.

P0 remains behaviorally frozen.

## Next step

Run the complete local deterministic suite. If all 62 tests pass, validate/materialize the real local H1/H2 plan and then implement the safe sequential `run-next` execution layer with replacement-attempt handling.
