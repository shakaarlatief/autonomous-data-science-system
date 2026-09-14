# Research 152: Candidate 01 Real-Repository Shadow V0.1 Fixture Freeze

**Date:** 2026-09-14
**Status:** REAL-REPOSITORY SHADOW FIXTURE + ORACLE FROZEN BEFORE IMPLEMENTATION / CURRENT AUTHORITY UNCHANGED / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Freeze a bounded real-repository shadow fixture against exact public commit `e10fd108330f2cf8d260a621ea59053aebd28291` before implementation. The experiment tests whether Candidate 01 can reconstruct a useful live project slice from real repository-native sources, quantify the migration-seeding burden still owned by today's global live-state surfaces, derive current routing/navigation, and preserve an exact governing bootstrap contract without using the existing global comparison targets as generation authority.
**Authority:** Experimental protocol only. The current continuity architecture remains operational authority. Requirements V0.2 remain the frozen candidate-acceptance boundary.
**Declared references:** `research:149`, `research:151`, `research:144`, `research:145`, `checkpoint:496`, `path:docs/CONTINUITY.md`, `path:docs/DEVELOPMENT_METHOD.md`, `path:docs/current_routing.json`, `path:docs/CURRENT_STATE.md`, `path:docs/KNOWLEDGE_MAP.md`

## 1. Exact freeze boundary

```text
base branch      v1-source-vault-bootstrap-resume
base commit      e10fd108330f2cf8d260a621ea59053aebd28291

fixture
    docs/research/project_knowledge_candidate_01_real_shadow_v01/REAL_SHADOW_FIXTURE_V01.json
    bytes        8299
    SHA-256      9e8cd2ce0be7ced69eabc246414bd9aa0f21b305e03efeffd81db86c222d42bc

oracle
    docs/research/project_knowledge_candidate_01_real_shadow_v01/REAL_SHADOW_ORACLE_V01.json
    bytes        2170
    SHA-256      7e42889a65ac181feb9bcdc9fdacdab2d6d7e295aa2ed1a71583bd5beb4cf32b
```

The implementation may read the fixture and exact real source blobs at the frozen base commit. It may not read the oracle.

## 2. Strong comparison-target isolation

Three real files are intentionally withheld from the **generation** path and exist only as comparison targets:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

This prevents a trivial parity result in which the candidate simply reads the artifact it is supposed to regenerate.

The fixture identifies those targets explicitly. Generation code must reject any attempt to use them as ordinary source inputs. The only exception is the separately declared **migration seed** described below, which exists precisely to measure truth that Candidate 01 cannot yet regenerate from naturally owned real sources.

## 3. Real source manifest

The fixture hash-binds every source used at `e10fd108330f2cf8d260a621ea59053aebd28291`. Important source classes include:

```text
existing semantic sources
    Research 124
    Research 144 / Candidate 01
    Research 151 operational result
    Checkpoint 496 current prototype boundary

governing procedure
    docs/CONTINUITY.md

method / integrity context
    docs/DEVELOPMENT_METHOD.md

computed current-control evidence
    Specification 027
    Checkpoint 192 / Specification 022 incomplete outcome

comparison targets only
    current_routing.json
    CURRENT_STATE.md
    KNOWLEDGE_MAP.md
```

All manifest bytes and SHA-256 hashes were independently checked against `git show e10fd108330f2cf8d260a621ea59053aebd28291:<path>` before freeze.

## 4. Real workstream shadow declarations

The frozen shadow identifies four semantic workstream units from real sources:

```text
WS-R124
    source      Research 124
    state       ACTIVE
    source mode EXISTING_SOURCE

WS-C01
    source      Research 144
    state       ACTIVE
    parent      WS-R124
    source mode EXISTING_SOURCE

WS-OPS-V02
    source      Research 151
    state       COMPLETED
    parent      WS-C01
    source mode EXISTING_SOURCE

WS-REAL-SHADOW
    source      Checkpoint 496
    state       ACTIVE
    parent      WS-C01
    depends on  WS-OPS-V02
    source mode MIGRATION_SEED_REQUIRED
```

The last classification is intentionally important. Checkpoint 496 records the current next boundary, but the existing repository does not yet have a dedicated Candidate-01-style canonical workstream source for this live semantic unit. The fixture therefore records one **workstream migration seed** rather than pretending the successor representation already exists.

This is evidence about migration burden, not a defect to conceal.

## 5. Project-control migration seed

Three current project-control facts remain owned today by the existing global live-state architecture and do not yet have naturally separate Candidate 01 homes in the selected real slice:

```text
active_pr
promoted_integration_branch
promoted_integration_sha
```

The fixture therefore contains one explicitly tagged migration source:

```text
source mode  MIGRATION_FROM_EXISTING_GLOBAL_AUTHORITY
source       CURRENT_STATE comparison/migration surface
fact count   3
```

This exception is not allowed to masquerade as source-local success. Its purpose is to answer a concrete migration-design question: **where should these project-wide control facts live if `current_routing.json` becomes derived?**

Possible later dispositions include a small project-control canonical source/profile or natural ownership by another already-justified semantic unit. This experiment does not decide that before evidence.

## 6. Computed control facts

Two live routing values are intentionally reconstructed from real non-target authority:

```text
latest_specification
    parse Specification 027 title/identity

latest_experiment_outcome
    parse Checkpoint 192 preserved status
    INCOMPLETE / EXECUTION INTEGRITY FAILED -> routing value INCOMPLETE
```

The active development branch is frozen from experiment/base context rather than read from the routing target. Current checkpoint and current boundary are taken from the real current boundary source, Checkpoint 496.

## 7. Real governing-procedure contract

The fixture creates a shadow structured action contract over the real `docs/CONTINUITY.md` section `Required new-session reconstruction`.

The ten ordered constraints are exact source tokens B01..B10 corresponding to the real mandatory reconstruction sequence:

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
governing canonical documents/specifications routed by current state
current checkpoint/research boundary
specialized ledgers/manifests for active topic
relevant private companion state only when indicated and accessible
```

The implementation must independently verify that these tokens appear in the real governed section in the same order.

Two action attempts are frozen:

```text
BOOTSTRAP-GOOD
    B01..B10 in order

BOOTSTRAP-BAD
    omits B03 and emits B05 before B04
```

This connects Candidate 01's action-contract mechanism to an actual current ADS governing procedure rather than a synthetic procedure.

## 8. Shadow-derived surfaces

The candidate must generate, without reading the targets:

```text
routing projection
    using workstream declarations + base branch + migration seeds + computed controls

current-state semantic core
    enough to compare checkpoint, active branch, Research 124 stage, next real-shadow boundary
    and target-unselected status

navigation projection
    generated from the frozen real-source subject declarations
```

Only after generation may the comparison phase read the exact target blobs and score parity.

## 9. Real capture seed

One current reasoning increment is frozen as candidate capture:

> Real-repository shadow qualification may reveal migration-seeding facts currently owned only by global live-state surfaces.

Its authority class is explicitly `candidate`. Merely participating in this experiment must not promote it into canonical truth.

## 10. Frozen oracle dimensions

The separate test oracle expects:

```text
all real source hashes match exact base
workstream route reconstructs WS-R124 -> WS-C01 -> WS-REAL-SHADOW
one workstream semantic unit requires migration seeding
three project-control facts require migration from current global live-state authority
routing projection exactly matches current_routing.json
current-state semantic markers match CURRENT_STATE.md
selected real source artifacts are discoverable in KNOWLEDGE_MAP.md
real CONTINUITY contract aligns with B01..B10
good bootstrap plan passes
bad bootstrap plan fails visibly for missing/reordered constraints
navigation projection is deterministic
real capture remains candidate
generation does not read comparison targets
```

## 11. Preflight result

Before this freeze, a model-free check verified:

```text
fixture/oracle IDs match
forbidden answer-bearing keys absent
11 source-manifest entries match exact base bytes/hashes
3 comparison targets are exactly declared
ordinary workstream/computed/navigation sources do not use comparison targets
project-control seed is the one explicit migration exception
4 workstream declarations present
10 continuity constraints present
real capture authority = candidate
REAL_SHADOW_V01_FREEZE_PREFLIGHT=PASS
```

No real-shadow implementation exists at this freeze boundary.

```text
RESEARCH152=REAL_REPOSITORY_SHADOW_V01_FROZEN
BASE_COMMIT=e10fd108330f2cf8d260a621ea59053aebd28291
FIXTURE_SHA256=9e8cd2ce0be7ced69eabc246414bd9aa0f21b305e03efeffd81db86c222d42bc
ORACLE_SHA256=7e42889a65ac181feb9bcdc9fdacdab2d6d7e295aa2ed1a71583bd5beb4cf32b
MIGRATION_SEED_WORKSTREAMS=1
MIGRATION_SEED_PROJECT_CONTROL_FACTS=3
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_EXACT_FROZEN_REAL_REPOSITORY_SHADOW
```
