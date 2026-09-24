# Research 301: P-D4 Successor Semantic Contract Freeze

**Date:** 2026-09-24
**Status:** P-D4 SUCCESSOR CLAIMS/WARRANTS FROZEN / IMPLEMENTATION NOT YET AUTHORED / NO P-D4 RESULT
**Parent protocol:** Research 277
**Corpus freeze:** Research 299
**Old-oracle replay:** Research 300 / PASS 11 OF 11
**Contract:** `experiments/r8c_assurance_probe_v01/p_d4_successor_contract.json`
**Contract SHA-256:** `c7b63213779a68b188e73f985460315da8ca3047f0b867c2cb2a0a5ced703db5`
**Scope:** Freeze the semantic successor claims, representation boundary, intentional mechanism differences and PASS discriminator before successor implementation.
**Authority:** Successor-contract freeze only. No implementation result or oracle retirement is authorized.

## 1. Design principle

P-D4 is explicitly not an implementation-cloning exercise.

The current-routing oracle has useful semantic invariants but its exact physical form is transitional:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
checkpoint filename scans
exact Markdown fragments
current checker stdout / return-code taxonomy
```

None of those mechanisms receive target preservation rights merely because the current oracle uses them.

The successor therefore consumes a structured `ROUTING_ASSURANCE_SUBJECT_V1` whose facts are independent of those carrier paths.

## 2. Frozen successor claims

Six semantic claims are frozen before code exists:

```text
PD4-SR1  translatable structured routing facts
PD4-SR2  routed checkpoint exists
PD4-SR3  active-line freshness is branch scoped
PD4-SR4  orientation projection has semantic parity
PD4-SR5  routing boundary is explicitly stable semantic identity
PD4-SR6  promoted integration revision has complete Git commit identity
```

Each claim names its historical/research warrant basis and one or more frozen corpus cases.

## 3. Representation change is deliberate

The successor subject separates:

```text
route
boundary
integration
knowledge
orientation_projection
```

It does not require the legacy nine-key JSON manifest shape.

It also does not make the old `current_boundary` regex the target semantic model. The compatibility adapter may use the old syntax to classify legacy data, but the successor receives an explicit semantic stability value:

```text
SEMANTIC
VOLATILE
```

Likewise, checkpoint existence/freshness is evaluated from explicit available checkpoint identities rather than by requiring target-time filesystem filename scanning.

## 4. Current human/machine synchronization is translated, not inherited

The current oracle requires `CURRENT_STATE.md` fragments to duplicate and agree with `current_routing.json`.

The preserved semantic invariant is narrower:

> If an independent orientation projection claims overlapping live facts, those facts must agree with canonical structured routing facts.

A future generated orientation may derive from the same canonical facts and therefore need no separately authored synchronization contract.

This allows the current duplicate-surface obligation to disappear once the representation no longer duplicates authority manually.

## 5. Frozen intentional mechanism differences

Before any successor execution, the contract explicitly rejects preservation requirements for:

```text
legacy current_routing JSON key layout
Markdown fragment matching
current_boundary regex as target semantic representation
old checker stdout wording
old distinction between return codes 1 and 2
checkpoint filename scanning as target input mechanism
```

These are mechanism differences, not accept/reject differences for the frozen corpus.

All 11 corpus cases must still retain the same GOOD/BAD disposition.

## 6. Translated-representation discriminator

The successor must accept the semantics of frozen good case PD4-C02 when materialized directly in the new structured subject without:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
checkpoint files
old checker execution
```

A paired negative control changes active checkpoint 269 to 268 while the active line remains checked and available checkpoints still include 269. It must fail the frozen branch-scoped freshness claim.

This directly tests semantic transfer across representation rather than source-format preservation.

## 7. Implementation independence controls

The future successor classifier:

```text
must not import or execute scripts/check_current_routing.py
must not read docs/current_routing.json
must not read docs/CURRENT_STATE.md
must return structured violated successor claim IDs
```

Legacy parsing/translation is permitted only in a separate compatibility adapter used to materialize corpus semantics.

## 8. Frozen PASS criteria

P-D4 may return PASS only if:

```text
old replay remains 11/11
successor accepts all frozen GOOD cases
successor rejects all frozen BAD cases
direct translated PD4-C02 passes without legacy carrier access
direct stale translated negative control fails PD4-SR3
no frozen invariant requires retention of legacy carrier/output shape
no thresholds or labels change after execution
```

## 9. Current state

```text
P_D4_CORPUS=FROZEN
P_D4_OLD_ORACLE_REPLAY=PASS_11_OF_11
P_D4_SUCCESSOR_CONTRACT=FROZEN
P_D4_SUCCESSOR_IMPLEMENTATION=NOT_AUTHORED
P_D4_RESULT=NOT_AVAILABLE

COMPLETED_VALID_SCOPED_PROBES=6_OF_8
OWNER_ASSURANCE_DECISION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=IMPLEMENT_AND_FREEZE_P_D4_SUCCESSOR_HARNESS
```
