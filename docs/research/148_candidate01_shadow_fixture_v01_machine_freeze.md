# Research 148: Candidate 01 Shadow Fixture V0.1 Machine Freeze Before Implementation

**Date:** 2026-09-14
**Status:** FIXTURE + ORACLE FROZEN BEFORE IMPLEMENTATION / CANDIDATE 01 SHADOW PROTOTYPE NOT YET IMPLEMENTED / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Freeze the exact machine-readable falsification fixture and separate expected-result oracle for the first Candidate 01 shadow prototype before any prototype implementation is written.
**Authority:** Experimental protocol only. The fixture and oracle do not become project-development authority and do not select Candidate 01. Requirements V0.2 and the current continuity architecture remain authoritative.
**Declared references:** `research:147`, `research:144`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:492`

## 1. Anti-treatment-bias boundary

The first Candidate 01 shadow implementation must not be allowed to shape the evidence fixture after seeing which cases are easiest to pass. The machine fixture and the separate test oracle are therefore frozen and committed before implementation.

Exact files:

```text
docs/research/project_knowledge_candidate_01_shadow_v01/SHADOW_FIXTURE_V01.json
docs/research/project_knowledge_candidate_01_shadow_v01/SHADOW_ORACLE_V01.json
```

Exact identities:

```text
fixture id       PKA-C01-SHADOW-V01
fixture bytes    61778
fixture SHA-256  77ffecc278995ef03130d962f863d46ccebac41d446de7099cc666750e8b66f7

oracle id        PKA-C01-SHADOW-V01-ORACLE
oracle bytes     2968
oracle SHA-256   3ced74eb18f4d792c9a43eaf2b3d6956c497bc7b85c71bfc6b5e226f840fc38b
```

The implementation must hash-check the fixture. The implementation itself must not read the oracle. The oracle is test-only evidence.

## 2. Why the oracle is separate

Research 139/MC-0014 showed that a classifier becomes construct-invalid when the fixture contains answer-bearing labels that the implementation can directly read. The fixture therefore contains no `should_be_joint_authority`, `expected_joint_authority`, `is_joint_authority_case`, or equivalent expected-answer flag.

The fixture contains semantic facts, relations, evidence records, review receipts, mutation inputs and action attempts. The oracle separately states what the tests expect from those facts.

This preserves a crucial distinction:

```text
fixture
    describes the world / challenge inputs

oracle
    describes expected experimental behavior

implementation
    may read fixture
    may not read oracle
```

## 3. Frozen hard cases

### F1: single normative contract home and source-integrity drift

`P1` contains a structured exact-fidelity action contract with stable constraint IDs `C01..C05` and explanatory prose assertions aligned to those constraints.

Two mutations are frozen:

```text
P1-PROSE-ADD-UNSTRUCTURED-MANDATORY
    prose introduces C07 without a structured normative constraint

P1-PROSE-CONTRADICT-C03
    prose assertion for C03 changes semantic value while the structured contract remains unchanged
```

The prototype must surface drift without treating prose as a second normative authority.

### F2: natural-direction near-miss versus irreducible symmetric joint authority

The fixture contains three relevant authority patterns:

```text
P1 + P2
    P2 naturally SUPPLEMENTS P1

N1 + N2
    N2 naturally SPECIALIZES N1 for EU scope

X1 + X2 + X3
    peer procedures with identical semantic role, no directional source relation,
    non-redundant governing constraints, and reviewed evidence of an all-members-required
    set-level governing fact
```

Both the symmetric positive case and the ordinary directional near-miss have completed admission-review receipts. A mere review receipt is therefore not an answer label. J2/J3 must distinguish the cases from their semantics.

### F3: BL-001-style action-contract fidelity

`P1 + P2` resolve to six ordered material constraints:

```text
C01 C02 C03 C06 C04 C05
```

`BL1-GOOD` preserves them. `BL1-BAD` omits the prohibition `C04` and emits `C02` before precondition `C01`. The candidate must fail visibly on the bad attempt.

### F4: dependency-local incremental refresh versus full rebuild

The frozen derived-view manifests contain:

```text
AUTHORITY_CURRENT
CONTRACT_CURRENT
IDENTITY_CURRENT
```

`CHANGE-P2-CONTRACT` changes only P2. The prototype must determine affected views from declared dependencies rather than refresh every view. It must also support an independent clean full rebuild.

### F5: growing identity-transition history with bounded current lookup

Core identity history includes:

```text
MOVE S-A carrier
MERGE S-A + S-B -> S-M
REVERSE_MERGE S-M -> S-A + S-B
SPLIT S-B -> S-B1 + S-B2
```

The fixture additionally contains 200 passive MOVE events for `S-C`. Scale prefixes 20, 100 and 200 all end at the same active carrier, so active semantic state is held constant while transition history grows.

The test must distinguish full index rebuild event scanning from normal current-target lookup.

## 4. Frozen scale boundaries

The scale prefixes are:

```text
1x   20 passive move records
5x  100 passive move records
10x 200 passive move records
```

The fixture holds the active procedure set, governing semantics and final current identity state fixed at all three scales.

## 5. Representation boundary

This fixture deliberately tests the candidate's semantic rules without committing the production architecture to YAML front matter, a database, a graph store or another physical representation. The first prototype may use Python dictionaries/JSON internally because its purpose is mechanism falsification, not final storage selection.

Likewise, `prose_assertions` are frozen as a deterministic stand-in for semantic assertions extracted from prose. Passing F1 does **not** prove production-quality natural-language drift detection. It proves only that the architecture can maintain one normative home and route a detected semantic mismatch into review. Natural-language extraction quality remains later qualification work.

## 6. Freeze rules

```text
fixture bytes are immutable for V0.1
oracle bytes are immutable for V0.1
prototype code may not patch fixture facts
prototype code may not read the oracle
changing fixture/oracle requires a new version and rerun
raw first-run failures must be preserved before repair
no aggregate winner score
current architecture remains operational authority
```

## 7. Preflight

Before this freeze, a model-free check verified:

```text
7 governing procedures present
200 passive identity MOVE records present
scale boundaries 20/100/200 all return S-C to the same current carrier
fixture contains none of the forbidden answer-bearing joint-authority keys
fixture and oracle fixture IDs match
authority cases include natural SUPPLEMENT, natural SPECIALIZE and symmetric peer evidence
SHADOW_FIXTURE_FREEZE_PREFLIGHT=PASS
```

No Candidate 01 shadow implementation exists at this freeze boundary.

```text
RESEARCH148=SHADOW_FIXTURE_V01_FROZEN
FIXTURE_SHA256=77ffecc278995ef03130d962f863d46ccebac41d446de7099cc666750e8b66f7
ORACLE_SHA256=3ced74eb18f4d792c9a43eaf2b3d6956c497bc7b85c71bfc6b5e226f840fc38b
IMPLEMENTATION=NOT_YET_WRITTEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_EXACT_FROZEN_FIXTURE
```
