# Research 157: Source Vault Workstream and Current-State Core Shadow Fixture Freeze

**Date:** 2026-09-14
**Status:** SUCCESSOR WORKSTREAM + CURRENT-STATE-CORE FIXTURE FROZEN BEFORE IMPLEMENTATION / CURRENT AUTHORITY UNCHANGED / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Exact real base:** `57df6561f506cba2c26222693d1403585fad23d2`
**Scope:** Freeze the first shadow successor source for the paused permanent Source Vault bootstrap together with the active-workstream/integration-boundary sources, a 23-item must-preserve manifest, and an exact current-state-core oracle before implementation.
**Authority:** Experimental protocol only. The three shadow sources are canonical only inside the Candidate 01 shadow model; `docs/CURRENT_STATE.md` and the current continuity architecture remain operational authority.
**Declared references:** `research:156`, `research:155`, `research:144`, `checkpoint:501`, `path:docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`

## 1. Frozen artifacts

```text
CURRENT_STATE_CORE_FIXTURE_V01.json
    SHA-256  4b7ac27801e7d89c0cd782c895d6d0db47693916e4aae7696eb3fc4d6081ad38

CURRENT_STATE_CORE_ORACLE_V01.json
    SHA-256  f7ceee34aa68d79dea8df4043bf5b1711f3a31078cf86d48bfc3b3f0b008af35

SHADOW_ACTIVE_WORKSTREAM.md
    SHA-256  ec7cb761360b7fedc3f66ab1bff66d055c97cb477785c71de725fe1a1e344f49

SHADOW_PROJECT_INTEGRATION_BOUNDARY.md
    SHA-256  256df6b025b4fe476b8d6409839c7af16dd3069e0f5fd2349a0b69f7aed86440

SHADOW_SOURCE_VAULT_WORKSTREAM.md
    SHA-256  2f4acb786f1c16df4b045d25ed2dffef0a1a82e4687c0fbc80c88789b19d7d71
```

No current-state-core implementation exists at this boundary.

## 2. Why this is an architecture test, not a file-refactor test

Research 156 showed that the current global state surface mixes responsibilities. The purpose of this experiment is therefore not to make `CURRENT_STATE.md` shorter. It is to test whether the successor architecture has enough natural semantic owners to reconstruct genuinely current project orientation without carrying history/navigation/copies as global truth.

The frozen successor sources represent three different semantic units:

```text
primary active project-knowledge workstream
Project Integration Boundary
paused Permanent Source Vault Bootstrap workstream
```

The physical Markdown-plus-adjacent-JSON representation is experimental. Only semantic ownership is under test.

## 3. Source Vault workstream ownership

The new shadow workstream owns current resumable Source Vault state that Research 156 identified as the main A-category gap:

```text
state = PAUSED
objective
pause reason
explicit-project-routing return condition
resume target
governing procedure
private dependency classification
bootstrap status
resume sequence
evidence references
```

It does not duplicate the operational procedure. `docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md` remains the procedure source. Validation 003/004 and Checkpoint 274 remain evidence.

The frozen Source Vault state includes:

```text
registry migrated / verified
Alembic 0003_source_universe
33 tables
20 / 20 prospective MATCH
ingestion NOT_STARTED
working audit PENDING
independent encrypted backup proof PENDING
clean restore + restored audit PENDING
Course 2 BLOCKED
resume target = reviewed ingestion of the frozen 20-entry first corpus
```

The old `CURRENT_STATE.md` sentence saying resume occurs when the current Research 113 route closes is intentionally **not** copied into the successor source. Research 113 is no longer the active project route. The successor workstream instead uses explicit project routing as its return condition. Because `CURRENT_STATE.md` remains operational authority during this research, that stale current-language sentence is also corrected in the live file at this checkpoint without changing its authority role.

## 4. Must-preserve manifest

The fixture freezes 23 semantic items. Fifteen are required directly in the compact current-state core; eight must remain recoverable from their natural source without being repeated in the core.

Core-required classes include:

```text
current checkpoint / branch / PR / boundary
active Research 124 stage
target-selection state
promoted integration branch + SHA
latest specification
latest governed experiment outcome
Source Vault paused state / resume target / procedure / ingestion state / Course 2 gate
```

Source-owned drill-down classes include the detailed registry/Alembic/compare/audit/backup/restore/private-dependency/resume-sequence facts.

This tests **preservation without universal duplication**.

## 5. Target isolation

Generation may read the three frozen shadow successor sources plus real non-target evidence. It may not read:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
```

until the generated core exists. These targets are comparison-only.

The fixture freezes:

```text
global_target_generation_fact_count = 0
manual_shadow_source_touch_count = 3
new Source Vault workstream sources = 1
```

## 6. Frozen success dimensions

The separate oracle asks whether:

```text
all source hashes remain exact
all three successor source kinds parse
Source Vault successor state aligns with real runbook/validation/checkpoint evidence
compact CURRENT_STATE_CORE matches the frozen live semantics
routing subset still has exact parity
selected live CURRENT_STATE markers match after generation
all 23 must-preserve semantic items remain recoverable
generation reads no forbidden targets
old Research-113 pause condition is detected as stale rather than propagated
```

## 7. Freeze preflight

A model-free preflight verified:

```text
fixture/oracle IDs match
forbidden answer-bearing keys absent
23 unique must-preserve items
15 core-required items
3 successor source hashes exact
all 3 structured declarations parse as shadow-only candidate-canonical sources
all 10 real source hashes match exact base
comparison targets are exactly current_routing + CURRENT_STATE
global target generation facts = 0
CURRENT_STATE_CORE_V01_FREEZE_PREFLIGHT=PASS
```

```text
RESEARCH157=CURRENT_STATE_CORE_FIXTURE_FROZEN
FIXTURE_SHA256=4b7ac27801e7d89c0cd782c895d6d0db47693916e4aae7696eb3fc4d6081ad38
ORACLE_SHA256=f7ceee34aa68d79dea8df4043bf5b1711f3a31078cf86d48bfc3b3f0b008af35
MUST_PRESERVE_ITEMS=23
CORE_REQUIRED_ITEMS=15
NEW_SOURCE_VAULT_WORKSTREAM_SOURCE=1
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_CURRENT_STATE_CORE_V01
```
