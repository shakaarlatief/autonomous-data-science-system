# Research 183: W0 Workstream Engine G008 Result

**Date:** 2026-09-16
**Status:** PKA-G008 ACCEPTED / WORKSTREAM ENGINE VERIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179
**Prior accepted boundary:** Checkpoint 529 / Research 182 / `7cb32f2725fb43617c325b5c450ca68854cdac41`
**Scope:** Record the production workstream/DAG/interruption/concurrency implementation, independent defects exposed before acceptance, bounded repairs, deterministic-serialization correction, and final PKA-G008 verification.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts PKA-G008 only. It does not accept PKA-G009+, begin W1 migration, publish successor generated views, or switch operational authority.

## 1. Implemented boundary

G008 adds the production pure workstream domain layer under `tools/project_knowledge/workstreams.py`, immutable L0 workstream/recovery/version values in `tools/project_knowledge/model.py`, a bounded L3 optimistic mutation seam under `tools/project_knowledge/services/workstream_ops.py`, focused qualification coverage in `tests/unit/test_project_knowledge_workstreams.py`, and architecture-guard extensions in `tests/unit/test_project_knowledge_substrate_architecture.py`.

The L2 workstream engine performs no filesystem, Git, repository-discovery, clock, network or service I/O. Repository mutation is not implemented in L2. The L3 update seam delegates the actual compare-and-mutate primitive to the caller/store and validates its explicit attestation.

## 2. Graph and readiness semantics

The accepted engine projects explicit canonical `workstream.v1` sources into immutable workstream values and validates duplicate identities, dangling/self dependencies, dependency cycles, parent references/cycles, snapshot consistency and pause/resume contracts. Noncanonical candidate/historical/evidence/capture/derived material is excluded from current workstream admission and cannot become current work merely because it is supplied.

Dependency and parent semantics remain distinct:

```text
depends_on
    prerequisite completion relation
    controls readiness

parent
    structural/context relation
    controls context paths only
    does not imply prerequisite completion
```

Multiple dependencies and transitive dependency closure are supported with iterative graph algorithms. An ACTIVE workstream is ready only when every dependency in closure is COMPLETED. ACTIVE-but-incomplete work is `DEPENDENCY_BLOCKED`; explicit `BLOCKED`, `PAUSED`, `COMPLETED` and `SUPERSEDED` states remain distinct. Direct and transitive dependency blockers remain visible.

Paused work does not auto-resume from prose or completed dependencies. When expected to resume, pause reason, return condition and resume target must form a complete explicit contract. Return-condition text is carried as data and never interpreted as permission to resume.

## 3. Active-ready set and route semantics

The engine produces a deterministic `active_ready_set`. Stable lexical sorting is used only for representation and never as authority or route priority.

A primary branch is derived only where explicit parent/context structure yields one maximal ready branch. When multiple incomparable ready branches remain, the engine returns `NO_UNIQUE_PRIMARY_ROUTE` together with all ready branch anchors/context rather than selecting by fixture order, file order, input order, semantic-ID lexical order or anchor lexical order.

The qualified Q4 real-source DAG behavior is reproduced: `WS-Q4-STRESS` is runnable from completed predecessors; `WS-Q10-FINAL` remains blocked with its ACTIVE/BLOCKED prerequisites visible; Source Vault and Cockpit remain PAUSED with their explicit continuation metadata.

## 4. Interruption recovery

Recovery operates over an explicit ordered workflow definition plus durable step receipts. Only durable `COMPLETED` receipts bound to the exact workflow/workstream/definition revision establish completion. Receipt iteration order is nonsemantic. Unknown, duplicate, contradictory, non-completed, stale-definition, non-durable and skipped-prefix receipt sets fail visibly.

Completed receipts must form a contiguous prefix of the workflow, so omitted earlier consequential work cannot be inferred complete. Recovery returns completed and pending steps plus only the first pending `next_resume_step`; completed steps never re-enter the execution surface. An unrelated read-only interruption leaves graph/recovery state unchanged.

The qualified Q4 interruption case is reproduced exactly at the semantic level:

```text
completed              S1, S2
pending                S3, S4, S5
next resume            S3
blind replay required  false
```

## 5. Independent-review defect 1: stale-write TOCTOU gap

The initial implementation passed 73 focused G008 tests but used a read/check/write callback sequence. Independent ChatGPT review reproduced a time-of-check/time-of-use race: a concurrent writer could advance the authoritative store after the stale writer's read but before its write, after which the stale writer still returned `APPLIED` and overwrote the concurrent state.

That implementation was not accepted.

The bounded repair moves expected-version comparison into a store-owned conditional-mutation callback whose contract requires comparison and mutation to be indivisible relative to the store's other writers. The service no longer exposes an unguarded read-then-write pair. A stale conditional mutation returns `REJECTED_STALE_REVISION` and attests identical before/after state; an applied mutation must attest that the before version exactly equals the expected version and that the after materialization exactly equals the requested replacement. Silent no-ops, inconsistent attestations and store exceptions cannot become `APPLIED`.

## 6. Honest transient version semantics

The same repair removed fabricated future Git revisions from in-memory concurrency tests. `SourceRevision` remains the accepted exact durable repository descriptor bound to `GIT_BLOB_BYTES_AT_COMMIT`. Uncommitted changed copies instead use:

```text
TransientContentVersion
    base_revision    exact immutable Git seed SourceRevision
    content_digest   sha256 of exact transient bytes

TransientContent
    version
    exact bytes
```

This preserves the qualified Q4 distinction: the immutable Git seed remains truthful while changed in-memory copies receive separate exact-byte version identity without pretending a future commit exists. Q4-R03 reproduces B fresh -> APPLIED, A stale -> zero mutation, C fresh against the new transient version -> APPLIED, while the live repository target remains untouched.

## 7. Independent-review defect 2: unordered serialization leak

After the concurrency repair, 87 focused G008 tests passed, but independent ChatGPT review found that semantically unordered source metadata still leaked authored array order into deterministic serialization. Equivalent permutations of finite scope values, risk/reopen references and durable receipt evidence references produced different serialized bytes; raw provenance/reference/relation metadata had the same structural risk.

ChatGPT repaired this bounded defect directly. Workstream dependencies and risk/reopen reference sets are canonicalized at the typed workstream boundary; durable receipt evidence references are canonicalized at the receipt boundary; and the workstream serializer now uses field-aware canonicalization for finite scope values, relation sets and ordinary provenance/reference sets. Stable lexical ordering is representation only.

Genuinely ordered semantics remain ordered. Workflow step sequence, completed/pending workflow order and parent/context paths are not globally sorted. Regression tests prove that unordered permutations serialize byte-identically while changing `S1,S2,S3,...` to `S2,S1,S3,...` remains a semantically different recovery definition/result.

## 8. Independent verification

Independent post-repair verification results:

```text
G008 workstream suite                 89 / 89 PASS
authority suite                      103 / 103 PASS
identity suite                        63 / 63 PASS
substrate suite                      222 / 222 PASS
inherited unit inventory            309 / 309 PASS
complete unit inventory             786 / 786 PASS
compileall                           PASS
WORKTREE project-knowledge validate PASS / zero diagnostics / zero live declarations
COMMIT project-knowledge validate   PASS / zero diagnostics / zero live declarations
PUBLIC_REPOSITORY_INTEGRITY         PASS
git diff --check                    PASS
```

The 222-test substrate suite was run in bounded non-overlapping partitions, including the slower snapshot family. The 309-test inherited suite was likewise run in non-overlapping partitions under the Runtime Bridge execution ceiling. No test failure was hidden by timeout partitioning.

The accepted pre-G008 COMMIT validation remained bound to `7cb32f2725fb43617c325b5c450ca68854cdac41`.

## 9. Gate disposition

```text
PKA-G001 PASS
PKA-G002 PASS
PKA-G003 PASS
PKA-G004 PASS
PKA-G005 PASS
PKA-G006 PASS
PKA-G007 PASS
PKA-G008 PASS
PKA-G009..PKA-G017 PENDING
```

No G009 implementation, W1 migration, persistent successor view, compatibility-surface replacement or operational authority switch occurred.

## 10. Next W0 work

The next bounded task is PKA-G009, the deterministic derived-view framework required by Specification 028 and Research 179: explicit view specifications, deterministic serializers/manifests, exact generator implementation binding, freshness/stale-input detection and the shared full/incremental builder architecture without yet advancing into G010 current-state-core behavior.

```text
RESEARCH183=PKA_G008_ACCEPTED
PKA_G001_G008=PASS
PKA_G009_G017=PENDING
SPECIFICATION_028=UNCHANGED
NEXT=PKA_G009_DERIVED_VIEW_FRAMEWORK
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
