# Research 169: Q4 Real Workstream / Concurrency / Interruption Fixture Freeze

**Date:** 2026-09-14
**Status:** Q4 REAL-SOURCE WORKSTREAM STRESS FIXTURE + ORACLE FROZEN / IMPLEMENTATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q4 workstream continuation / concurrency
**Exact real base:** `eece72a16d9664387a67e38998ec715f8efe927e`
**Scope:** Freeze a real-source Candidate 01 stress test for multiple dependencies, interruption recovery and stale concurrent update rejection while preserving live workstream authority and testing the Research 168 explicit source-revision-basis amendment.
**Authority:** Experimental protocol only. Current continuity remains operational authority; all mutation stress is temporary/shadow-only.
**Declared references:** `research:168`, `research:166`, `research:165`, `research:144`, `checkpoint:513`, `path:docs/cockpit/README.md`, `path:docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`

## 1. Why Q4 is next

Research 168 leaves Q4 as the cleanest remaining real-behavior gap. Candidate 01 already has real support for durable workstream identity, pause/return semantics and current route reconstruction, but the following remain synthetic-only:

```text
multiple dependencies
interruption recovery after unrelated work
stale concurrent authoritative update rejection
```

This fixture targets exactly those three mechanisms without creating a real conflicting write.

## 2. Frozen artifacts

```text
Q4_REAL_FIXTURE_V01.json
    SHA-256  5046c5cfa6672e8467ba91c30c8dd0212267df6cd7cfb316f875d11299ccca40

Q4_REAL_ORACLE_V01.json
    SHA-256  1aa4225794ec5eaf0085bc6c961270e4a178dba55443d24550ca729696386e79

SHADOW_Q4_WORKSTREAM_DAG.json
    SHA-256  6f7e7bb4a387590320129da12bbde30d9e01ea1122489c48b2c13c1b226bfc35
```

The implementation may read the fixture and real/shadow sources but may not read the oracle.

## 3. Real-source grounding

The fixture binds exact blobs from the Checkpoint 513 base for:

```text
Research 168 integrated Q1/Q2/Q5 result
Research 166 evidence reconciliation V0.2
Research 165 Q9 migration result
Checkpoint 513
Candidate 01 qualification matrix
Cockpit paused-workstream source
Permanent Source Vault bootstrap runbook
previously qualified Source Vault shadow workstream source
Candidate 01 architecture record
```

The Q4 DAG is a **shadow coordination representation grounded in those real work units**. It is not asserted to be an already-existing canonical current dependency graph.

## 4. Multi-dependency challenge

Two nodes deliberately require more than a tree:

```text
WS-Q4-STRESS
    depends_on
        WS-Q125-INTEGRATED
        WS-Q9-MIGRATION

WS-Q10-FINAL
    depends_on
        WS-Q4-STRESS
        WS-Q1-PORTABILITY
        WS-Q2-HARD-CASES
```

The predecessor nodes correspond to current real qualification results/gaps rather than anonymous synthetic placeholders. The first pair is complete at the frozen base, so the Q4 stress node is runnable. Q10 remains blocked because Q4 and the Q1/Q2 residual gaps are unresolved.

This tests whether Candidate 01 can reconstruct a dependency DAG without collapsing workstreams into one linear route.

## 5. Interruption-recovery challenge

The frozen Q4 qualification transition has five steps:

```text
S1  confirm whole-architecture evidence V0.2
S2  confirm integrated Q1/Q2/Q5 result
S3  freeze Q4 real fixture
S4  execute Q4 real stress
S5  reconcile post-Q4 evidence
```

Durable receipts exist only for S1 and S2. An unrelated read-only Cockpit diagnostic interruption is inserted. Recovery must therefore reconstruct:

```text
completed  S1 S2
pending    S3 S4 S5
resume     S3
blind replay of S1/S2  forbidden
```

The Cockpit interruption is deliberately read-only and may not alter either workstream.

## 6. Real revision / stale-write challenge

The stale-write test is bound to the real paused Cockpit workstream source at the frozen base:

```text
source_commit   eece72a16d9664387a67e38998ec715f8efe927e
source_path     docs/cockpit/README.md
hash_algorithm  SHA-256
hash_basis      GIT_BLOB_BYTES_AT_COMMIT
content_digest  2e5fe6ab83b89f1bec267c64580c53844d82350f1454ebdc45a64454dc5952e0
```

This directly exercises the revision-binding amendment from Research 168 rather than using an ambiguous bare working-tree hash.

All writes occur only in a temporary copy:

```text
WRITER-B-FRESH
    uses the frozen base revision
    creates the next temporary revision

WRITER-A-STALE
    still expects the frozen base revision
    must fail with zero mutation after Writer B

WRITER-C-FRESH
    uses Writer B's new exact revision
    may apply
```

The live Cockpit file is hash-checked before and after the stress and must remain unchanged.

## 7. Existing real paused workstreams remain visible

The shadow DAG also carries two actual paused ADS workstreams:

```text
WS-SOURCE-VAULT-BOOTSTRAP
    resume target = reviewed ingestion of the frozen 20-entry first corpus
    return condition = explicit project routing

WS-COCKPIT-DESIGN
    resume target = v1-cockpit-design-exploration@04f2a907094b8023ac7377c399a6eef1a6e1da99
    return condition = owner explicitly returns to frontend work
```

Their presence tests that concurrency/dependency reasoning does not erase paused-workstream continuity.

## 8. Limitations and evidence discipline

This is stronger than Research 150 because workstream states, predecessor evidence, pause/resume anchors and revision bytes are bound to real ADS sources. The Q4/Q10 coordination edges themselves remain an experimental Candidate 01 shadow representation of the current qualification program, not current project authority.

A pass may therefore establish **real-source stress support** for the Q4 mechanisms, but final cluster qualification still requires later integrated program-level judgment.

## 9. Freeze preflight

```text
Q4_REAL_V01_FREEZE_PREFLIGHT=PASS
real source hashes                    9 / 9 exact-base match
shadow DAG hash                       exact
multi-dependency nodes                2
actual paused ADS workstreams         2
revision basis                        GIT_BLOB_BYTES_AT_COMMIT
live mutation                         FORBIDDEN
oracle separation                     PASS
```

```text
RESEARCH169=Q4_REAL_FIXTURE_FROZEN
REAL_BASE=eece72a16d9664387a67e38998ec715f8efe927e
FIXTURE_SHA256=5046c5cfa6672e8467ba91c30c8dd0212267df6cd7cfb316f875d11299ccca40
ORACLE_SHA256=1aa4225794ec5eaf0085bc6c961270e4a178dba55443d24550ca729696386e79
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_Q4_REAL_V01
```
