# Research 135: Common Fixture V0.1 Machine Freeze Before Hypothesis Implementation

**Date:** 2026-09-13
**Status:** REPRESENTATION-NEUTRAL MACHINE FIXTURE FROZEN / H1-H2 IMPLEMENTATION NOT YET STARTED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Freeze the exact machine-readable Common Fixture V0.1 derived from Research 134 before either H1 or H2 receives candidate-specific implementation logic, so the first mechanism comparison cannot change its hard cases after observing a candidate implementation.
**Authority:** Experiment/probe input under Research 124 and Research 134. Requirements V0.2 remain the candidate-acceptance authority. The fixture is synthetic evidence input and does not alter project-development truth.
**Declared references:** `research:124`, `research:134`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:477`

## 1. Frozen artifact

```text
docs/research/project_knowledge_architecture_probe_v01/COMMON_FIXTURE_V01.json
fixture_id: PKA-CF-V01
bytes: 10,595
SHA-256: c8ed1873014b7a69016eb6fb259791d1c34b9cd14219547f1ebc0e755b836fe8
```

The file is frozen before H1/H2 implementation. It must not be edited inside this comparison run. If a semantic defect is later discovered, create a new fixture version and rerun every compared hypothesis rather than repairing V0.1 in place.

## 2. Representation-neutral content

The machine fixture instantiates the seven Research 134 hard-case slices without assigning any fact to an H1 document declaration or H2 spine location:

```text
F1 identity continuity
   carrier move
   identity merge
   mistaken-merge reversal
   identity split

F2 authority closure
   superseded procedure
   current base
   later-effective mandatory supplement
   non-authoritative conflicting candidate
   fail-visible missing precedence

F3 workstream continuation
   parent objective
   two dependencies
   completed sibling
   blocked child
   paused nested child
   explicit return condition and targets

F4 capture / consolidation / promotion
   low-structure conversation-born candidate
   supporting sources
   accepted promoted conclusion
   rejected historical alternative
   candidate deletion after promotion

F5 scale
   five fixed active items
   historical/evidence count 20 -> 100 -> 200
   no increase in active semantic complexity

F6 derived-state destruction
   active route
   authority closure
   identity resolution
   search projection
   all deletable/rebuildable

F7 action-contract fidelity
   base contract + later supplement
   six combined ordered constraints
   explicit precondition
   explicit prohibition
   missing-constraint and contradiction challenges
```

A synthetic private-only placeholder is included only to exercise non-leakage/degraded-mode declarations. It contains no real private project data.

## 3. Important fixture choices

### 3.1 Directional relations are not pre-judged as spine-owned

The fixture expresses semantic relations such as `P2 supplements P1` and `P1 supersedes P0` but does not state where those relations must be authored. H1 is free to represent them source-locally; H2 is free to assign qualifying cross-object relations to its bounded spine.

### 3.2 Split resolution is intentionally one-to-many

Historical subject `S-B` ends in a split into `S-B1` and `S-B2`. A correct implementation may not pretend there is one canonical successor when the fixture declares two. This tests representation-independent identity without forcing redirect semantics to remain one-to-one.

### 3.3 Missing-contract detection has an observable oracle

F7 sources declare `required_constraint_ids`. The missing-constraint challenge removes the body of required prohibition `C04` while the authoritative contract still requires that ID. Both hypotheses therefore have enough explicit source information to fail visibly; the test does not ask a system to infer an unknowable missing sentence.

### 3.4 Historical scale does not smuggle in new active complexity

F5 holds active items constant and multiplies only historical/evidence entries. This is necessary to test whether mandatory surfaces or H2's spine grow with history rather than with genuinely changed current semantics.

## 4. Implementation fairness rules

```text
same fixture bytes for H1 and H2
same expected semantic queries and challenge mutations
no candidate-specific fixture patch
no hidden manual correction during query execution
candidate-specific derived schemas/logic allowed
instrument every authoritative write/touch used by the probe
candidate may fail visibly rather than fabricate an answer
```

H1 must not introduce a separately authoritative cross-object relation/control substrate under another name. H2 must justify every spine-owned fact by cross-object or independent-lifecycle semantics rather than convenience.

## 5. Freeze disposition

```text
COMMON_FIXTURE_V01=MACHINE_FROZEN
COMMON_FIXTURE_SHA256=c8ed1873014b7a69016eb6fb259791d1c34b9cd14219547f1ebc0e755b836fe8
H1_IMPLEMENTATION=NOT_STARTED_AT_FREEZE
H2_IMPLEMENTATION=NOT_STARTED_AT_FREEZE
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_SMALLEST_HONEST_H1_AND_H2_AGAINST_EXACT_FIXTURE
```
