# Research 160: Q3 Real Identity / Relationship / Temporal Fixture Freeze

**Date:** 2026-09-14
**Status:** Q3 REAL-ADS FIXTURE + ORACLE FROZEN BEFORE IMPLEMENTATION / H3 REOPEN RULE ACTIVE / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q3 identity / relationship / temporal semantics
**Exact real base:** `d8690d215e9701fc25d378a7d104aa6dbab10b2d`
**Scope:** Freeze five real ADS semantic cases plus five shadow Candidate 01 source-local declarations, a separate oracle, and explicit H3/Object-Primary reopening triggers before any Q3 implementation is written.
**Authority:** Experimental protocol only. Current repository authority is unchanged. Requirements V0.2 remain frozen.
**Declared references:** `research:159`, `research:144`, `research:143`, `specification:027`, `path:docs/DECISIONS.md`, `path:docs/cockpit/README.md`, `path:docs/model_collaboration/threads/MC-0013/STATE.json`, `checkpoint:504`

## 1. Why this is the next experiment

Research 159 selected Q3 because it is the weakest real-evidence cluster and the most architecture-family-discriminating. Candidate 01 currently has synthetic support for relationship/identity mechanics but no real Candidate 01 implementation evidence for any Q3 item.

The purpose is therefore not to migrate another current file. It is to ask whether selective repository-native source profiles remain natural when confronted with real ADS identity, supersession, epistemic-role and temporal cases.

## 2. Exact frozen artifacts

```text
Q3_REAL_FIXTURE_V01.json
    SHA-256  d30a3968e901b6f273a25ddef8d1ebbe093e1040e74f3ab80ba68ce523760ab6

Q3_REAL_ORACLE_V01.json
    SHA-256  74c0684ec341311f0f91241f8f79bbe02c83d699784406b0d886bca34994f8a8

SHADOW_DECISION_D015.md
    SHA-256  1b9dd2ab66646278eb502a3b5584fc9149863b31c519d55f9fe46a956ea8fcb0

SHADOW_DECISION_D011.md
    SHA-256  1de955e619e51d38f3ce07a344dc58a95e1c1e924c9cd7b4782b4d0df199aa8e

SHADOW_HISTORICAL_INTERMEDIATE.md
    SHA-256  0adf6d94c1ec32f8550c1e1e484876b507fce9352038f72f034ae3ae3889559a

SHADOW_COCKPIT_WORKSTREAM.md
    SHA-256  7e7dab176f7a9f95824591e5a8e4de72efbf02271fb7c3ead29a5979cb77e10d

SHADOW_MC0013_REVIEW.md
    SHA-256  ef2f102a02d190a9d170d4a84ea3389838ef7c3415f9a102b52af2b890b8bd28
```

The fixture contains no expected semantic query answers. Expected outputs live only in the separate test oracle.

## 3. Frozen real cases

### Q3-R01: D-015 scoped supersession with retained outcome

Real source: `docs/DECISIONS.md`.

D-015 is superseded by D-033 only for the external-source architecture uncertainty while its durable public-Git source-binary exclusion outcome is retained. This tests partial supersession without forcing the whole predecessor identity to disappear.

### Q3-R02: D-011 multi-successor scoped supersession

One older decision remains applicable to still-unselected implementation subsystems while six later decisions replace it in six specific scopes. This is deliberately dense enough to expose whether Candidate 01 turns ordinary scoped relations into a relation-object registry.

The shadow declaration does **not** invent per-successor effective dates because the D-011 status line preserves three supersession dates without unambiguously mapping each date to each successor. This tests selective temporal semantics rather than metadata completion by guesswork.

### Q3-R03: historical-intermediate identity repair

The source-faithful reintegration milestone was originally created at:

```text
docs/checkpoints/252_source_faithful_reintegration_interaction_integrity_gate.md
```

and renamed at real Git commit:

```text
b79d6ae0187b61e73c3b08312e4c7ec9d8f7f61d
```

to the current historical-intermediate carrier. `Original recorded identity: Checkpoint 252` remains provenance only and must not collide with the canonical spatial-rail Checkpoint 252.

This is a real representation-independent identity case rather than a synthetic MOVE event.

### Q3-R04: durable paused Cockpit workstream

The Cockpit workstream remains the same semantic workstream while paused, while project routing has moved elsewhere, and while an exact future branch/head/workflow/job resume anchor is preserved.

This tests durable identity plus single-source authority without central workstream-object storage.

### Q3-R05: MC-0013 epistemic-role transition

Message 001 remains the preserved independent architecture counter-design bound to substantive base `233eb932...`; the current thread is `COMPARATIVE_ONLY`, and Message 003 onward is comparative after exposure to Research 133 and ChatGPT Message 002.

This tests epistemic roles and phase transitions without universal event sourcing.

## 4. Candidate 01 representation under test

The five frozen shadow sources use only the smallest profile-specific structured semantics required by their cases:

```text
decision D-015
    one scoped REPLACE relation + retained outcome + two material dates

decision D-011
    six scoped REPLACE relations + residual applicability

historical milestone
    durable semantic ID + current carrier + retired original identity provenance + Git rename provenance

Cockpit workstream
    durable workstream ID + PAUSED state + exact resume anchor

MC-0013 review
    current comparative state + preserved independent phase + comparative exposure transition
```

No universal object schema is imposed. No relation object or transition object is frozen merely to make the fixture pass.

## 5. Prospective H3/Object-Primary reopening triggers

The experiment freezes the reopening logic **before implementation**. H3 review must reopen if implementation demonstrates any of the following:

```text
a general authoritative object registry is required

2 or more of the five real cases require standalone canonical relation/transition sources
    because natural source ownership cannot express the semantics honestly

any authoritative relation must be duplicated across canonical sources

all participants must be universally objectized merely to answer the real queries

any frozen real semantic query cannot be resolved from source-local declarations + Git/source evidence
```

These are reopening triggers, not an aggregate winner score. A trigger means the object-primary family deserves renewed comparative design work; it does not automatically select H3.

## 6. Complexity measurements

The implementation must report at least:

```text
shadow source count
source-local relation count
selective temporal field count
standalone relation-source count
standalone identity-transition-source count
joint-authority-source count
general authoritative registry count
duplicated authoritative relation count
universally objectized participant count
real semantic query failure count
```

This makes architecture complexity observable rather than hiding it behind successful query outputs.

## 7. What a pass would and would not mean

A pass would add real ADS evidence that Candidate 01 can handle partial/multi-scope supersession, real carrier/identity repair, durable paused identity and epistemic-role transitions without collapsing into a central object substrate.

A pass would **not** fully qualify Q3. In particular, real semantic merge/split/tombstone cases may still be absent from the repository sample; synthetic evidence for those transitions remains useful but weaker. A later Q3 disposition must say exactly which transition types have real versus synthetic support.

## 8. Freeze preflight

Before this record was written, a model-free preflight verified:

```text
fixture/oracle IDs match
forbidden expected-answer keys absent from fixture
8 real source blobs match exact base bytes/hashes
5 shadow source blobs match frozen bytes/hashes
all 5 structured declarations parse
D-015 / D-011 source tokens exist
historical-intermediate original identity/disposition exists
canonical numeric Checkpoint 252 exists separately
actual Git rename provenance contains b79d6ae... and the original carrier
Cockpit PAUSED state + exact branch/head exist
MC-0013 current COMPARATIVE_ONLY state and independent base exist
H3 standalone-relation/transition threshold = 2
Q3_REAL_V01_FREEZE_PREFLIGHT=PASS
```

```text
RESEARCH160=Q3_REAL_FIXTURE_FROZEN
FIXTURE_SHA256=d30a3968e901b6f273a25ddef8d1ebbe093e1040e74f3ab80ba68ce523760ab6
ORACLE_SHA256=74c0684ec341311f0f91241f8f79bbe02c83d699784406b0d886bca34994f8a8
REAL_CASES=5
SHADOW_SOURCES=5
H3_REOPEN_RULE=ACTIVE
IMPLEMENTATION=NOT_YET_WRITTEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_Q3_REAL_V01
```
