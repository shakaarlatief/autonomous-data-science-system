# Research 164: Q9 Migration / Authority-Switch / Rollback Fixture Freeze

**Date:** 2026-09-14
**Status:** Q9 REAL-BASE SHADOW MIGRATION + ROLLBACK FIXTURE/ORACLE FROZEN BEFORE IMPLEMENTATION / CURRENT AUTHORITY UNCHANGED / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q9 migration / authority switch / self-hosting evolution
**Exact real base:** `fe40740e62dabc41e538b2b604e84f5e9167e92d`
**Scope:** Freeze a shadow-only real-base migration experiment that tests semantic parity, semantic identity/provenance preservation, reverse-reference safety, legacy-compatible rollback export, explicit single-authority switch blocking and the candidate's ability to preserve its own migration state.
**Authority:** Experimental protocol only. The existing continuity architecture remains operational authority. No authority switch, production migration or rollback mutation is authorized.
**Declared references:** `research:163`, `research:159`, `research:146`, `research:144`, `research:145`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:508`

## 1. Why Q9 is now the right falsification target

Candidate 01 now has substantial real subsystem evidence for routing/current-state decomposition, Q3 identity/temporal semantics and Q7 public/private degraded behavior. The central remaining transition risk is no longer whether individual source profiles can work. It is whether those profiles can replace pieces of the current architecture **without creating dual authority, losing semantic meaning or making rollback fictitious**.

Q9 therefore tests the migration boundary while preserving the strongest transition invariant:

```text
CURRENT CONTINUITY ARCHITECTURE
    remains operational authority

CANDIDATE 01
    remains shadow/candidate only

MIGRATION EXPERIMENT
    may transform and export in temporary shadow space
    may not overwrite current authority

AUTHORITY SWITCH
    forbidden in this experiment
```

## 2. Frozen artifacts

```text
Q9_MIGRATION_FIXTURE_V01.json
    SHA-256  5f6fec6c812692f8b085dde8f15ddc8c1f80a2695bf75933a80d736eeb83dfcc

Q9_MIGRATION_ORACLE_V01.json
    SHA-256  8994b9be935480aec58f9b1e25ba386a8ad979ac8f45c06665ac7d596d1c3015

SHADOW_ACTIVE_WORKSTREAM.md
    SHA-256  f68897636d7d8728b263d61a191a66ea1775a242e27014eb15f3fcd01ec43568

SHADOW_PROJECT_INTEGRATION_BOUNDARY.md
    SHA-256  dd03a8eea4696445b7def2424ffe05440e55790534aa98375000fce84a2bd893

SHADOW_MIGRATION_WORKSTREAM.md
    SHA-256  74e6cb5bc4971f07ddb60e707da886659d4f9b6c35cf10a9ae10eabccec95a2c
```

The fixture and oracle are separate. Prototype implementation is forbidden from reading the oracle.

## 3. Real authority slice

The exact base binds ten real repository sources, including:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/CONTINUITY.md
Research 144 Candidate 01 design
Research 163 Q7 result
Candidate 01 qualification matrix
Specification 027
Checkpoint 192 experiment outcome
Checkpoint 508
legacy current-routing validator
```

This is not a synthetic migration of invented project state. The migration targets the exact Checkpoint 508 authority boundary.

## 4. Shadow successor sources

Three source-local successor semantic units are frozen.

### Active Research 124 workstream

`WS-PKA-CURRENT` owns the active branch/PR/checkpoint/current-boundary anchor, Research 124 objective and explicit `TARGET_ARCHITECTURE_NOT_SELECTED` state. Its semantic identity is independent from the legacy `CURRENT_STATE.md` carrier.

### Project Integration Boundary

`PROJECT-INTEGRATION-BOUNDARY` keeps promoted branch + commit adjacent as one semantic fact.

### Candidate 01 migration workstream

`PKA-C01-MIGRATION` self-hosts the migration itself. It records:

```text
phase                     M6_SHADOW_RECONCILIATION
parent                    WS-PKA-CURRENT
current authority         CURRENT_CONTINUITY_ARCHITECTURE
successor authority       SHADOW_ONLY
final qualified passes    0 / 67
authority switch request  false
rollback mode             EXPORTER_BASED
```

It also records the Candidate 01 switch preconditions inherited from Research 144/146.

## 5. Frozen migration-parity units

Ten migration units are mapped without storing expected values in the fixture:

```text
MU01 current checkpoint
MU02 active development branch
MU03 active PR
MU04 current semantic boundary
MU05 promoted integration branch
MU06 promoted integration commit
MU07 latest specification
MU08 latest experiment outcome
MU09 target architecture remains unselected
MU10 final qualified pass count
```

Each unit declares the legacy source/query and the successor source/query or deterministic computed control. Implementation must establish parity rather than reading a pass label.

## 6. Reverse-reference challenge

The migration experiment does not assume that changing semantic ownership permits breaking old paths. Exact-base references are measured for:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/CONTINUITY.md
```

The successor design intentionally retains the first two as legacy-compatible generated paths and leaves `CONTINUITY.md` in place. This tests the Candidate 01 rule that representation can change while existing inbound references remain safely resolvable during migration.

## 7. Rollback exporter challenge

The implementation must generate **temporary** legacy-compatible surfaces from successor state:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
```

The export may not overwrite live files. The generated temporary tree must be consumable by the existing `check_current_routing.py` contract against Checkpoint 508. The routing manifest must also be semantically identical to the frozen real-base routing authority.

This is stronger than saying Git can revert a commit. It asks whether successor semantics can still generate a representation the old continuity system understands.

## 8. Authority-switch gate challenge

The candidate must not infer permission to switch merely because the exporter works. The frozen base still has:

```text
final qualified passes   0
target selection allowed false
authority switch request false
```

The experiment therefore expects the switch gate to remain closed. The implementation must report blockers rather than silently upgrading shadow evidence into authority.

## 9. Self-hosting challenge

The migration workstream itself is represented using Candidate 01 semantics. A fresh reconstruction from the shadow sources must be able to recover:

```text
current migration phase
current operational authority
successor authority state
parent workstream identity
next migration action
authority-switch-request state
```

This is a bounded real test of KA-R45: the architecture must be able to preserve its own redesign/migration state without depending on the conversation that created it.

## 10. Freeze preflight

The model-free freeze preflight passes:

```text
Q9_MIGRATION_V01_FREEZE_PREFLIGHT=PASS

real source hashes          10 / 10 match exact base
shadow source hashes         3 / 3 match
structured declarations      3 / 3 parse as shadow-only
policy markers                4 / 4 grounded in frozen sources
migration units              10
reverse-reference baselines  exact-base counts frozen in oracle
authority switch             forbidden during implementation
```

```text
RESEARCH164=Q9_MIGRATION_FIXTURE_FROZEN
REAL_BASE=fe40740e62dabc41e538b2b604e84f5e9167e92d
FIXTURE_SHA256=5f6fec6c812692f8b085dde8f15ddc8c1f80a2695bf75933a80d736eeb83dfcc
ORACLE_SHA256=8994b9be935480aec58f9b1e25ba386a8ad979ac8f45c06665ac7d596d1c3015
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_Q9_MIGRATION_V01
```
