# Research 156: Real CURRENT_STATE Decomposition and Source-Ownership Audit

**Date:** 2026-09-14
**Status:** COMPLETE BLOCK-LEVEL AUDIT / REAL DRIFT REPRODUCED / SOURCE-VAULT WORKSTREAM MIGRATION NEED IDENTIFIED / CURRENT AUTHORITY NOT SWITCHED
**Candidate:** `PKA-CANDIDATE-01`
**Exact audit base:** `a1f813c0a12d5682c34b7d0000476893756589c3`
**Scope:** Decompose the real `docs/CURRENT_STATE.md` by future semantic role, bind every audited block to exact source bytes, reproduce current-state drift against stronger repository authority, and identify which material current facts need a new canonical owner before Candidate 01 may treat the global surface as derived.
**Authority:** Architecture/migration evidence only. The current `CURRENT_STATE.md` remains operational authority until an explicit qualified transition.
**Declared references:** `research:124`, `research:144`, `research:153`, `research:155`, `checkpoint:500`, `path:docs/CURRENT_STATE.md`, `path:docs/current_routing.json`, `path:docs/CONTINUITY.md`, `path:docs/KNOWLEDGE_MAP.md`

## 1. Exact source boundary

The audit is bound to the exact Git blob at the Checkpoint 500 public boundary:

```text
path        docs/CURRENT_STATE.md
lines       1,159
bytes       282,796
SHA-256     c59e5102c42435a8049101fa59977f6a951f2ed92e7d443233643c984bd0df5a
base        a1f813c0a12d5682c34b7d0000476893756589c3
```

Machine audit:

```text
docs/research/project_knowledge_candidate_01_current_state_decomposition_v01/
    CURRENT_STATE_DECOMPOSITION_V01.json
```

The ledger covers every source line exactly once across 16 non-overlapping blocks. It also hash-binds 14 supporting repository sources used for ownership/drift comparison.

## 2. Classification model

The audit asks a migration question, not whether a paragraph is useful today.

```text
A_CANONICAL_SOURCE_REQUIRED
    material current truth does not yet have one adequate natural successor owner

B_*
    small deterministic current/core/task projection that can be regenerated

C_OPTIONAL_ORIENTATION
    useful non-authoritative orientation/provenance narrative

D_*
    history, copied subject-owned rules, navigation, or stale material that should not
    remain unique truth on the mandatory current-state surface

E_UNRESOLVED
    future role cannot yet be assigned safely without finer source tracing
```

This is intentionally a **block-level** audit. A D block is not authorized for deletion until must-preserve/source-trace parity is demonstrated. Zero block-level E bytes does not imply that no proposition inside a large block will require finer treatment during migration.

## 3. Quantitative result

At the coarse block level:

```text
D categories       277,925 bytes   98.28%
A category           1,738 bytes    0.61%
B categories         1,616 bytes    0.57%
C category           1,517 bytes    0.54%
------------------------------------------------
non-D total          4,871 bytes    1.72%
```

The dominant contributors are structural accumulation rather than irreducible current truth:

```text
lines 27-420   accumulated Research/checkpoint chronology       ~76.09% of file
lines 650-950  path-heavy current/canonical route inventory      ~8.87%
lines 971-1159 fixed minimum-reading packet                       ~5.29%
line 632       enormous historical runtime checkpoint chronology  ~4.58% block region
```

The exact percentage is not a proposed production file-size target. It is evidence that the current representation's growth is overwhelmingly caused by **historical copying and navigation accumulation**, not by the small amount of live project state that must be globally visible.

## 4. Block-level disposition

### B/C: small current projection and optional orientation

The header and latest orientation summary occupy a very small part of the artifact. Research 155 already proves that the routing subset of the header can be regenerated from natural semantic owners without global live-state input.

The interaction/session block is useful provenance but is not durable project truth. The latest free-form stage paragraph is useful human/model orientation but must not be the unique home of accepted facts.

### D: accumulated checkpoint/research history

Lines 27-485 are primarily a chronological replay of numbered checkpoints, research and validation evidence already preserved in their durable source artifacts. This material remains valuable for drill-down, but keeping it copied into the mandatory current-state surface creates active-context growth proportional to project age.

Candidate 01's future role is therefore historical/latent access through checkpoints, research, indexes and task-shaped retrieval, not duplicated current-state authority.

### D: subject-specific operational contracts

The accepted Git boundary and operational lessons in lines 486-567 have more natural existing owners, including:

```text
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
```

The current-state copies are useful compatibility prose today, but they should not become independent successor truth.

### A: Source Vault resumable state

Lines 568-625 are the main coarse block for which the audit does **not** accept simple derivation/removal yet.

They contain material paused-workstream facts such as:

```text
permanent Source Registry migrated / verified
Alembic head 0003_source_universe
first permanent corpus compare 20 / 20 MATCH
source ingestion NOT STARTED
working-store audit PENDING
backup / restore proof PENDING
Course 2 BLOCKED
preserved next action = reviewed ingestion of the frozen first corpus
subsequent audit -> backup -> retrieval -> restore sequence
```

Evidence for these facts exists across the Source Vault runbook, historical checkpoints and research, but there is no single Candidate-01-style canonical source that owns the complete **current resumable workstream state**.

Therefore this is a real migration requirement:

> Create one durable Source Vault bootstrap workstream source that owns current state, pause reason, return condition, dependencies, resume target and current anchor while retaining links to the runbook/checkpoint evidence.

Only after that source exists and parity is proven may the corresponding global current-state copy become derived/latent.

### B/D: integrity, collaboration and navigation

The small live integrity/method pointers can be generated from dedicated method/specification state. Collaboration state is naturally derived from per-thread `STATE.json` plus the review inbox. The large route and minimum-reading inventories are navigation/reconstruction products and should ultimately come from generated indexes/planning rather than copied truth.

## 5. Four real drift defects reproduced

The audit found four high-confidence examples where copied global state has already drifted relative to stronger/current repository authority.

### CS-DRIFT-001: stale current checkpoint claim

`CURRENT_STATE.md` line 632 says:

```text
Canonical numbered Checkpoint 353 is now the current meaningful project boundary.
```

At the exact same repository base:

```text
current_routing.current_checkpoint = 500
Checkpoint 500 is the current Research 124 boundary
```

Disposition: `STALE_HISTORICAL_COPY`.

### CS-DRIFT-002: stale MC-0010 lifecycle state

`CURRENT_STATE.md` says:

```text
MC-0010 is now OPEN / PARALLEL UPSTREAM RESEARCH
```

The authoritative thread state says:

```text
lifecycle_state = DEFERRED
phase = DEFERRED_BY_OWNER_ROUTING_RESEARCH124_PRIORITY
```

The Review Inbox also records MC-0010 as deferred.

Disposition: `DUPLICATED_LIVE_STATUS_DRIFT`.

### CS-DRIFT-003: stale conversation/current-stage prose

The conversation-rotation section still calls `chatgpt-19` the current interaction and says Research 122 governs the active stage. The file's own current header and active-stage section say `chatgpt-24` and Research 124.

Disposition: `STALE_ROTATION_HISTORY`.

### CS-DRIFT-004: stale fixed minimum-reading packet

The 189-line fixed minimum-reading list contains none of the following active artifacts:

```text
docs/research/124_scalable_repository_knowledge_architecture_and_reconstruction_redesign.md
docs/research/155_candidate01_zero_seed_routing_v01_result.md
docs/checkpoints/500_candidate01_zero_seed_routing_passed_current_state_decomposition_next.md
```

Disposition: `STALE_DERIVED_RECONSTRUCTION_PACKET`.

## 6. Architectural conclusion

This is stronger evidence than the earlier synthetic scaling probes because the failure is visible in the actual operational authority surface.

The present `CURRENT_STATE.md` is doing at least five jobs simultaneously:

```text
live control projection
orientation narrative
historical checkpoint/research archive
subject-specific operational copy
navigation/reconstruction packet
```

Those responsibilities have different update frequencies and different natural owners. Combining them in one hand-maintained file causes both linear active-surface growth and stale-current-language defects.

Candidate 01's proposed split is therefore strengthened:

```text
canonical semantic sources
    own durable current facts and resumable workstream state

CURRENT_STATE_CORE
    deterministic generated projection of genuinely live facts

orientation narrative
    optional non-authoritative synthesis with provenance/freshness

history/navigation
    latent/generated drill-down surfaces
```

This does **not** mean the existing file may now be deleted. Current authority remains unchanged until successor sources, generated parity, rollback and explicit transition are qualified.

## 7. Immediate operational correction versus future migration

Because `CURRENT_STATE.md` is still operational authority today, demonstrably false current-language should be repaired now. That repair is separate from Candidate 01 migration.

The minimal correction boundary is:

```text
Checkpoint 353 claim
    mark as historical runtime summary, not current project boundary

MC-0010
    correct OPEN -> DEFERRED from authoritative thread state

conversation-rotation section
    mark historical and remove its claim to current session/stage authority

fixed minimum-reading packet
    mark historical/non-current and route current reconstruction back through CONTINUITY + current routing
```

No authority-role switch is required to make those accuracy corrections.

## 8. Next qualification slice

The next Candidate 01 shadow slice should address the A-category gap and then exercise a generated current-state core:

```text
1. create a shadow Source Vault bootstrap workstream source
2. bind its state to the strongest current runbook/checkpoint evidence
3. combine it with the already-qualified active workstream + Project Integration Boundary
4. generate a compact CURRENT_STATE_CORE
5. use a must-preserve manifest against the real current-state audit
6. prove no unique accepted truth disappears
7. measure current-core size and mandatory reconstruction read cost
8. keep current CURRENT_STATE.md authoritative throughout the experiment
```

Only after that should the project consider changing the authority role or physical form of `CURRENT_STATE.md`.

```text
RESEARCH156=CURRENT_STATE_DECOMPOSITION_COMPLETE_AT_BLOCK_LEVEL
SOURCE_LINES_COVERED=1159_OF_1159
D_CATEGORY_BYTE_SHARE=98.28_PERCENT
REAL_DRIFT_FINDINGS=4
SOURCE_VAULT_CANONICAL_WORKSTREAM_MIGRATION=REQUIRED
CURRENT_STATE_AUTHORITY_SWITCH=NOT_AUTHORIZED
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=REPAIR_STALE_CURRENT_LANGUAGE_THEN_SOURCE_VAULT_WORKSTREAM_AND_CURRENT_STATE_CORE_SHADOW
```
