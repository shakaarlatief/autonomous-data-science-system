# Research 204: W3 Compatibility Shadow Acceptance Result

**Date:** 2026-09-19
**Status:** W3 ACCEPTED / POST-BOUNDARY FINALIZATION PENDING
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted boundary:** Checkpoint 552 / Research 203 / W2 ACCEPTED
**Qualified pre-acceptance materialization:** `4e26f7fb317953d8d82ff6b933efe9f34d97e62d`
**Qualified pre-acceptance source boundary:** `sha256:e10d564f726cfd2a17c4054b83406a7236fb2ee8a1c9698dc982fa19136b518f`
**Scope:** Accept W3 after successor-owned compatibility candidates for routing, current-state and Knowledge Map roles are generated independently from the still-live compatibility content, materialized only under the compatibility-shadow area, and compared against the live surfaces with every observed difference explicitly classified.
**Authority:** This record accepts W3 only. It does not overwrite a live compatibility path, start W4 capture execution, resume Source Vault/Cockpit execution, or switch operational authority. Checkpoint 553 is the W3 semantic anchor.

## 1. W3 requirement

Specification 028 defines W3 as:

```text
Produce shadow candidates for routing/current-state/Knowledge-Map roles
without overwriting live paths.

Classify every difference as exactly one of:
EXPECTED_SEMANTIC_IMPROVEMENT
EQUIVALENT_REPRESENTATION
MIGRATION_GAP
LEGACY_DRIFT
UNRESOLVED

MIGRATION_GAP or UNRESOLVED blocks advancement.
```

The production W3 implementation lives in:

```text
tools/project_knowledge/services/compatibility.py
tests/unit/test_project_knowledge_w3_compatibility_shadow.py
```

The materialized shadow set is:

```text
docs/project_knowledge/generated/compatibility_shadow/current_routing.json
docs/project_knowledge/generated/compatibility_shadow/CURRENT_STATE.md
docs/project_knowledge/generated/compatibility_shadow/KNOWLEDGE_MAP.md
docs/project_knowledge/generated/compatibility_shadow/artifact_inventory.json
docs/project_knowledge/generated/compatibility_shadow/comparison_report.json
```

## 2. Candidate-generation boundary

Candidate generation requires one exact committed repository snapshot, validates the successor semantic owners first, and constructs the compatibility model from canonical non-superseded successor sources.

The candidate builder does not use the live compatibility file contents as generation inputs. The still-live:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

are read only by the separate comparison phase.

The successor model resolves the active project-knowledge workstream, Project Integration Boundary, current specification, current experiment result and paused expected-to-resume workstreams. The Knowledge Map candidate combines governed multi-axis semantic memberships with a deterministic complete non-generated documentation inventory as its high-recall fallback.

## 3. W3 implementation chronology

The bounded implementation sequence is:

```text
009d55bb0eac9c69c77ce1b70dacba605c0ef473  Implement W3 compatibility shadow generation
ce6ef69                                           Refresh structural views for W3 inputs
8b617f95a626760a34fae1d333ab19a002d2ccef  Bind W3 shadow to content boundary
4e26f7fb317953d8d82ff6b933efe9f34d97e62d  Materialize W3 compatibility shadow
```

The first full W3 boundary run correctly exposed stale source-digest bindings after canonical input wording changed. The structural views were refreshed, and the final implementation binds compatibility output to a content-derived source boundary rather than an incidental commit SHA.

## 4. Pre-acceptance materialization

At `4e26f7f...`, the shadow contains five derived/non-authoritative artifacts.

```text
routing candidate           436 bytes
current-state candidate   2,671 bytes
Knowledge Map candidate   5,331 bytes
artifact inventory      223,802 bytes
comparison report         3,093 bytes
```

The artifact inventory covers 1,346 committed non-generated documentation artifacts across 13 top-level documentation groups.

The materialized bytes were independently compared against a fresh build from the same exact committed source state and all five matched their generated SHA-256 values exactly.

## 5. Difference classification

The pre-acceptance comparison contains six explicit differences:

```text
EQUIVALENT_REPRESENTATION        3
EXPECTED_SEMANTIC_IMPROVEMENT   2
LEGACY_DRIFT                     1
MIGRATION_GAP                    0
UNRESOLVED                       0
blocking                         false
```

The exact dispositions are:

```text
routing.semantic-parity
    EQUIVALENT_REPRESENTATION

current-state.control-parity
    EQUIVALENT_REPRESENTATION

current-state.history-compaction
    EXPECTED_SEMANTIC_IMPROVEMENT

current-state.legacy-source-vault-route
    LEGACY_DRIFT

knowledge-map.artifact-reachability
    EQUIVALENT_REPRESENTATION

knowledge-map.organization
    EXPECTED_SEMANTIC_IMPROVEMENT
```

The routing candidate reproduces the live routing schema and values exactly. The current-state candidate preserves the high-consequence controls while replacing accumulated historical replay with compact canonical-owner orientation. All 652 unique legacy Knowledge Map path/directory references checked by the compatibility comparison remain reachable through the successor inventory.

The one legacy-drift result is non-blocking because the still-live current-state surface retains an older Research 124 Source Vault routing sentence while the migrated Source Vault workstream now carries durable explicit return semantics.

## 6. Qualification

Exact pre-acceptance materialization qualification on `4e26f7f...`:

```text
W3 focused qualification                    7 / 7 PASS
W1 compatibility/live-semantic regression  27 / 27 PASS
W2 focused regression                        5 / 5 PASS
persistent structural-view freshness         8 / 8 FRESH
COMMIT project-knowledge validation         PASS
candidate count                            1,478
governed declarations                         10
diagnostics                                    0
PUBLIC_REPOSITORY_INTEGRITY                 PASS
git show --check                            PASS
```

The W3 suite proves generation independence from live compatibility content, exact routing parity, compact owner-oriented current state, Knowledge Map reachability, frozen difference classes with zero blockers, blocking behavior for a synthetic routing mismatch, byte determinism and shadow-only materialization.

## 7. Authority and compatibility boundary

W3 changes no operational authority.

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

The live compatibility surfaces remain authored under the current continuity architecture. The W3 candidates are derived, rebuildable and non-authoritative. No live compatibility path is overwritten by materialization.

## 8. Acceptance-finalization boundary

The semantic program anchor advances to:

```text
checkpoint       553
stage            SPECIFICATION:028 / W3_ACCEPTED
boundary         project-knowledge-wave-three-accepted-capture-promotion-next
```

Because that changes a canonical generated-view input and adds the W3 acceptance artifacts to the committed documentation tree, the structural views and compatibility-shadow artifacts must be rematerialized from the exact Checkpoint 553 state before final publication.

Post-boundary finalization is therefore still required after the Checkpoint 553 boundary commit. No later checkpoint is required merely for that generated-output refresh if the semantic anchor itself does not change.

```text
W3=ACCEPTED
POST_BOUNDARY_FINALIZATION=PENDING
W4=NOT_STARTED
NEXT=W4_PRODUCTION_CAPTURE_PROMOTION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
