# Research 184: W0 Derived-View Framework G009 Result

**Date:** 2026-09-17
**Status:** PKA-G009 ACCEPTED / DETERMINISTIC DERIVED-VIEW FRAMEWORK VERIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179
**Prior accepted boundary:** Checkpoint 530 / Research 183 / `48e2cc060dee99d3237196b67829b8d443dfc024`
**Scope:** Record the production G009 derived-view framework, the adversarial defects exposed before acceptance, the final execution-contract provenance repair, and complete verification evidence for deterministic manifests and stale binding detection.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts PKA-G009 only. It does not accept PKA-G010+, publish persistent successor views, begin W1 migration, overwrite compatibility surfaces, or switch operational authority.

## 1. Accepted G009 boundary

G009 introduces the production deterministic derived-view framework under the existing layered `tools/project_knowledge/` architecture.

The accepted implementation adds or extends:

```text
tools/project_knowledge/views.py
    pure complete-input view building
    canonical serialization
    generator implementation digesting
    deterministic manifest construction
    manifest freshness comparison
    explicit source-inventory view specification

tools/project_knowledge/pure_units.py
    restricted data-only production compute units

tools/project_knowledge/adapters/pure.py
    restricted pure-unit source validation and execution

tools/project_knowledge/adapters/execution.py
    exact-Git isolated worker boundary and finite repository TCB

tools/project_knowledge/services/generation.py
    durable COMMIT_SNAPSHOT orchestration
    one selected-view-at-a-time isolated worker execution
    complete-current-input rebuild semantics

tools/project_knowledge/adapters/schema.py
    explicit persistent schema closure support

tools/project_knowledge/model.py
    immutable view specification/build/freshness value types

tests/unit/test_project_knowledge_views.py
tests/unit/test_project_knowledge_view_execution.py
    deterministic, stale-binding and adversarial execution qualification
```

No G010 current-state-core behavior is implemented or accepted by this boundary.

## 2. One full/incremental build architecture

The implementation follows Research 179's central simplification: full and selected/incremental operation use the same builder.

A selected view is never semantically patched from old persisted state. Selection narrows only which view is rebuilt. Every selected view receives its complete current canonical input set and executes the same selection, compute, serialization and manifest path used by full rebuild.

The lower-level builder accepts no persisted view state. Generated outputs and manifests are excluded from the canonical input corpus, preventing circular generated-view authority.

If input membership, content, identity, authority-relevant declaration material or generator binding changes, the rebuilt manifest changes and freshness fails visibly.

## 3. Deterministic serialization and manifest binding

Generated JSON uses the frozen deterministic representation required by Specification 028:

```text
UTF-8
LF
final newline
2-space indentation
stable object-key ordering
view-owned semantic array ordering
no wall-clock freshness timestamps
```

The implementation digest follows Research 179 exactly:

```text
sha256(
    for each implementation path in declared order:
        UTF8(path) || NUL || exact Git blob bytes || NUL
)
```

Persistent generator evidence includes:

```text
generator_id
generator_version
implementation_basis = GIT_BLOB_BYTES_AT_COMMIT
ordered implementation_files[]
implementation_digest
```

The deterministic `created_or_refreshed_boundary` is content-derived and does not require the final output commit SHA, preserving Specification 028's same-commit non-self-referential binding requirement.

## 4. Durable execution model

Early G009 designs established that exact implementation-file hashes are insufficient if the runtime can still execute unbound ambient Python behavior.

The accepted design therefore uses data-only durable view specifications. A durable specification names a qualified compute-unit identity and serializer identity rather than passing arbitrary live callbacks.

Pure compute/serializer units are loaded from exact committed source bytes under a restricted AST-validated language. The containing module body is never executed. The restricted language permits local plain-data control flow and direct calls only to explicitly declared helper units or deterministic capabilities. It rejects imports, arbitrary global access, attribute/reflection access, mutation, nested functions, generators, object identity, defaults/keyword defaults, decorators and annotations.

Inputs are copied/frozen as plain data before execution and outputs are validated back into plain deterministic data. Runtime object representations cannot enter persistent generated data.

## 5. Exact execution closure and isolated worker

Every durable view declares its complete execution closure. The production source-inventory specification binds:

```text
fixed repository TCB
all nine project-knowledge schemas
its restricted pure-unit source
```

The finite repository TCB contains 15 explicitly audited files. The worker validates their module initialization grammar and runs each selected view in a fresh isolated interpreter using exact committed blobs. Repository packages outside the declared closure cannot become implicit execution authority through normal imports, namespace packages or editable installs.

Each selected view receives its own worker and explicit implementation set, preventing one selected view from supplying undeclared helper code to another.

`WORKTREE_SNAPSHOT` remains structurally non-durable and cannot produce persistent G009 freshness evidence.

## 6. Adversarial defects exposed before acceptance

G009 was not accepted on its first implementation. Independent review and attack testing exposed a sequence of provenance/execution weaknesses.

### 6.1 Worktree execution under a Git manifest

An early implementation computed manifest digests from committed Git blobs but allowed callbacks/schema behavior from current worktree/runtime imports. This could falsely attest committed execution while running different bytes.

Repair: durable generation now verifies executing infrastructure/schema/pure-source material against exact Git blobs before evidence can escape.

### 6.2 Cross-view implementation leakage

A multi-view worker initially combined implementation files across selected views. One view could therefore satisfy another view's undeclared dependency.

Repair: one isolated worker per view, with only that view's explicit implementation closure.

### 6.3 Ambient repository package imports

Editable or otherwise importable repository packages could have become undeclared runtime authority.

Repair: repository package containment is explicit. Declared pure helpers may live in ordinary repository package paths, but they are compiled directly from declared Git bytes rather than imported as ambient modules.

### 6.4 Arbitrary callback/runtime state

A runtime callable/projector design remained vulnerable to ambient mutable function/default/module state. Deep attacks demonstrated that committed module initialization could mutate stdlib runtime behavior such as JSON string encoding or Enum value access while leaving the apparent manifest binding unchanged.

This invalidated the finite runtime-projector approach.

Repair: G009 was redesigned around data-only specifications plus restricted pure functions compiled from exact source declarations. General module-body execution is not part of the durable compute surface.

### 6.5 Runtime representation leakage

Naive text conversion could serialize nondeterministic runtime representations such as generator/object addresses.

Repair: deterministic text capabilities accept plain bounded data only.

### 6.6 Missing compute/serializer identity binding

After the restricted execution redesign, final independent review found one remaining provenance omission. A single exact committed implementation closure could contain two already-qualified compute units or serializers. Switching the selected identity could change view bytes while leaving the exact implementation file list and implementation digest unchanged.

This meant freshness could incorrectly treat a changed execution contract as equivalent if only file-level provenance were considered.

Repair: `ViewSpecification` now preserves explicit `compute_identity` and `serialize_identity`. The deterministic manifest boundary includes:

```text
execution_contract:
    compute_unit
    serializer
```

Freshness therefore becomes stale when the selected compute/serializer identity changes even when the exact implementation digest remains identical.

Focused regressions prove both cases independently. In each test, both variants are committed in one unchanged implementation closure, the implementation digest is equal, output bytes differ, manifest bytes differ, and freshness returns `STALE` with `STALE_VIEW_BOUNDARY`.

## 7. Freshness behavior

Manifest freshness distinguishes contract classes rather than collapsing all mismatches:

```text
input bindings changed       STALE_VIEW_INPUTS
generator binding changed    STALE_VIEW_GENERATOR
execution/selection boundary STALE_VIEW_BOUNDARY
artifact bytes changed       STALE_VIEW_CONTENT
incompatible metadata        INVALID
non-committed durable claim  UNSUPPORTED_SNAPSHOT
```

`FRESH` means the persistent binding equals a complete current rebuild. It does not mean the derived artifact is canonical authority.

## 8. Verification evidence

Independent post-repair verification completed the whole relevant inventory through bounded non-overlapping partitions under the Runtime Bridge execution ceiling:

```text
G009 view framework                    53 / 53 PASS
G009 execution/adversarial             76 / 76 PASS
authority suite                       103 / 103 PASS
identity suite                         63 / 63 PASS
workstream suite                       89 / 89 PASS
substrate incl. architecture guards   223 / 223 PASS
inherited unit inventory              309 / 309 PASS
-----------------------------------------------
complete unit inventory               916 / 916 PASS
```

Additional gates:

```text
compileall                             PASS
WORKTREE validation                   PASS / zero diagnostics
accepted-HEAD COMMIT validation       PASS / zero diagnostics
accepted HEAD                         48e2cc060dee99d3237196b67829b8d443dfc024
PUBLIC_REPOSITORY_INTEGRITY           PASS
git diff --check                      PASS
```

Final WORKTREE validation after acceptance/recovery documentation contained 1,402 candidates and zero diagnostics. Accepted-HEAD COMMIT validation contained 1,399 candidates and zero diagnostics.

Temporary `g009-*` verification directories were removed. The pre-existing access-restricted historical `.tmp/pytest-checkpoint-275/` and `.tmp/pytest-publication-276/` directories were intentionally left untouched.

## 9. Runtime incident during verification

G009 verification was interrupted by a local Codex Desktop/Codexless Windows sandbox startup failure unrelated to repository semantics.

The incident was independently recovered without repository permission widening or broad ACL repair. Its detailed evidence is preserved as Validation 209, and the evergreen recovery procedure is incorporated into `docs/local_execution/OPERATIONS.md`.

The incident did not weaken or bypass any G009 acceptance gate. After recovery, Runtime Bridge model-free execution resumed and the complete G009 verification above was run to completion.

## 10. Gate disposition

```text
PKA-G001 PASS
PKA-G002 PASS
PKA-G003 PASS
PKA-G004 PASS
PKA-G005 PASS
PKA-G006 PASS
PKA-G007 PASS
PKA-G008 PASS
PKA-G009 PASS
PKA-G010..PKA-G017 PENDING
```

No persistent successor view is published by this acceptance record. No current compatibility path changes authority. W1 remains blocked until all W0 gates pass.

## 11. Next W0 work

The next bounded gate is PKA-G010:

```text
current-state-core generator reproduces bounded qualified must-preserve fixture behavior
```

G010 should build on the accepted G009 builder and must not introduce a separate derived-view execution architecture. The qualified current-state-core shadow evidence from the Candidate 01 program remains the behavioral basis, while Specification 028 and Research 179 remain governing.

```text
RESEARCH184=PKA_G009_ACCEPTED
PKA_G001_G009=PASS
PKA_G010_G017=PENDING
SPECIFICATION_028=UNCHANGED
NEXT=PKA_G010_CURRENT_STATE_CORE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
