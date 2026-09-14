# Research 150: Candidate 01 Operational Shadow V0.2 Fixture Freeze

**Date:** 2026-09-14
**Status:** BROADER OPERATIONAL FIXTURE + ORACLE FROZEN BEFORE IMPLEMENTATION / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Freeze the second Candidate 01 shadow fixture before implementation, covering operational continuity behaviors deliberately omitted from V0.1: workstream DAG/pause/resume/interruption, capture-consolidate-promote fidelity, generated current views, public/private degraded behavior, authority uncertainty and stale update safety.
**Authority:** Experimental protocol only. Requirements V0.2 and the current continuity architecture remain authoritative.
**Declared references:** `research:149`, `research:145`, `research:144`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:494`

## 1. Freeze boundary

```text
fixture
    docs/research/project_knowledge_candidate_01_shadow_v02/SHADOW_OPERATIONAL_FIXTURE_V02.json
    bytes      15444
    SHA-256    6daefddd448ead145281d56da8325925cb82c71fc57418283ef21c65418ec486

oracle
    docs/research/project_knowledge_candidate_01_shadow_v02/SHADOW_OPERATIONAL_ORACLE_V02.json
    bytes      4606
    SHA-256    a1af441f356fbd0e7cac65ba1f6c45589f96941139e669d99de4276acf8440b6
```

The implementation may read the fixture but may not read the oracle. The fixture contains no expected-status/pass/fail/route/promotion/conflict-answer keys. Any change to fixture or oracle requires a new version.

## 2. Why V0.2 is broader than V0.1

V0.1 established narrow executable support for five architecture-sensitive foundations. It did not exercise ordinary long-lived project operation. V0.2 therefore targets the behaviors most likely to determine whether Candidate 01 actually improves ADS development rather than only passing isolated semantic tests.

The frozen behavior groups are:

```text
O1  workstream DAG, pause/return, route reconstruction, interruption recovery, stale update
O2  capture -> consolidation -> fidelity gate -> explicit promotion
O3  deterministic routing/current-state/navigation derived views and novel-narrative capture
O4  public/private delegation, non-leakage and required-private degraded mode
O5  resolved, missing-required, conflicting and optional-retrieval-down authority states
```

## 3. O1 workstream challenge

The fixture has eight workstreams spanning `ACTIVE`, `PAUSED`, `BLOCKED` and `COMPLETED`. It includes two multi-dependency nodes, so a strict tree implementation cannot satisfy the fixture. Every paused workstream carries pause reason, return condition and resume target.

Baseline expected semantics are not stored in the fixture. The oracle separately expects the mandatory active route to be rooted through `WS-PKA -> WS-C01 -> WS-OPS`, while paused work remains visible but does not occupy the mandatory route. A later signal makes `WS-PRIVATE` eligible to activate.

An interrupted four-step transition has durable receipts for only steps T1 and T2. Recovery must reconstruct completed versus pending steps without replaying completed operations.

Two workstream writes exercise optimistic concurrency:

```text
STALE-WS-OPS  expects revision 3 while actual is 4
FRESH-WS-OPS  expects revision 4
```

## 4. O2 capture / consolidation / promotion challenge

`CAP-1` contains conclusion, limitation, uncertainty, negative evidence, relation and provenance units. `CAP-2` is separate unpromoted candidate material.

Two consolidation candidates use the same declared view contract:

```text
SYN-BAD
    omits negative-evidence unit U4 from its must-preserve dispositions

SYN-GOOD
    preserves U4 as intentionally latent but recoverable from CAP-1:U4
```

Both have accepted promotion requests, so review status alone cannot cause promotion. Promotion must depend on fidelity. Unpromoted `CAP-2` must remain candidate and absent from accepted-current knowledge.

A generated narrative also contains one source-supported claim and one novel unsupported claim. The novel claim must become candidate capture material rather than silently entering current authority.

## 5. O3 generated-view challenge

Three persistent derived views are frozen:

```text
ROUTING_CURRENT
CURRENT_STATE_CORE
NAVIGATION_INDEX
```

They are explicitly `derived` and deterministic. The prototype must delete/rebuild them from source facts with stable output and may not rely on unique truth stored only in a generated view.

## 6. O4 public/private challenge

The fixture contains public records that expose only an abstract private dependency ID plus synthetic private-only records with forbidden public sentinels.

Four cases distinguish:

```text
public-only task with private unavailable
private-required task with private available
private-required task with private unavailable
previously RESOLVED_PRIVATE public conclusion while private verification is temporarily unavailable
```

Generated public outputs must never contain the private locator, private sentinel or private-only detail.

## 7. O5 authority uncertainty challenge

The fixture includes:

```text
complete base + supplement authority
missing required supplement
two incompatible current canonical sources with no precedence relation
low-risk exploratory work with optional retrieval unavailable
```

The candidate must distinguish `RESOLVED`, fail-visible missing required authority, unresolved conflict and calibrated low-risk degraded operation.

## 8. Anti-treatment-bias and limitations

This remains a synthetic shadow fixture. It is intentionally more integrated than V0.1 but does not claim realistic natural-language extraction, real private data handling or production storage semantics. Synthetic private values are non-sensitive sentinels used only to test leakage filtering.

The workstream/capture patterns are ADS-shaped and grounded in frozen requirements, but they are not imported as live authority from current repository files. This avoids allowing the prototype to mutate or reinterpret current project state.

## 9. Preflight

A model-free preflight verified:

```text
8 workstreams
ACTIVE / PAUSED / BLOCKED / COMPLETED states present
multiple dependency edges present
all paused work has reason + return condition + resume target
2 consolidation candidates
4 public/private scenarios
4 authority scenarios
fixture/oracle IDs match
forbidden expected-answer keys absent from fixture
SHADOW_OPERATIONAL_V02_FREEZE_PREFLIGHT=PASS
```

No V0.2 implementation exists at this freeze boundary.

```text
RESEARCH150=OPERATIONAL_SHADOW_V02_FROZEN
FIXTURE_SHA256=6daefddd448ead145281d56da8325925cb82c71fc57418283ef21c65418ec486
ORACLE_SHA256=a1af441f356fbd0e7cac65ba1f6c45589f96941139e669d99de4276acf8440b6
IMPLEMENTATION=NOT_YET_WRITTEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_EXACT_FROZEN_OPERATIONAL_FIXTURE
```
