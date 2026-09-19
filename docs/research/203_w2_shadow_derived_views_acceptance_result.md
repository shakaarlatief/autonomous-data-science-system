# Research 203: W2 Shadow Derived Views Acceptance Result

**Date:** 2026-09-19
**Status:** W2 ACCEPTANCE RECORDED / POST-BOUNDARY MATERIALIZATION AND FINAL QUALIFICATION PENDING
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted boundary:** Checkpoint 551 / Research 202 / W1 ACCEPTED
**Qualified pre-acceptance materialization:** `1e615aec0e67b782ec7e599704e7c18a84ec932c`
**Scope:** Accept W2 after all eight V1 structural views are generated from the real successor semantic owners, persistently materialized with manifests, and compared with qualified shadow expectations plus current compatibility state.
**Authority:** This record does not start W3, overwrite a live compatibility path, resume Source Vault/Cockpit execution, or switch operational authority. Final publication remains blocked until the Checkpoint 552 semantic anchor is rematerialized and requalified.

## 1. W2 requirement

Specification 028 defines W2 as:

```text
Generate all V1 structural views from successor semantic owners.
Compare with qualified shadow expectations and current compatibility state.
```

The production W2 view set is:

```text
source_catalog.json
identity_index.json
authority_index.json
workstream_graph.json
subject_index.json
risk_obligation_index.json
current_state_core.json
CURRENT_STATE_CORE.md
```

Each view has one `derived_view_manifest.v1` representation under `docs/project_knowledge/generated/manifests/`.

## 2. Production materialization

W2 is the first real persistent materialization wave for the complete eight-view registry.

The generated area is now intentionally version-controlled through a narrow `.gitignore` exception:

```text
docs/project_knowledge/generated/**
```

The materialized footprint at qualification is:

```text
8 views
8 manifests
50,777 view bytes
43,331 manifest bytes
94,108 total bytes
```

Research 179 left a W2 watch item on whether every structural view should remain persistently committed. The live slice provides no evidence for removing a view: the total footprint is small, each view carries a distinct structural access role, all are deterministic/rebuildable, and none contains unique accepted truth. W2 therefore retains the complete eight-view persistent set.

## 3. W2-discovered materialization defect and repair

The first explicit W2 write failed closed with:

```text
MATERIALIZATION_SOURCE_DRIFT
```

The repository itself was Git-clean. The apparent drift came from comparing raw Windows checkout bytes against canonical Git blob bytes for two CRLF-materialized Markdown carriers.

This violated the already-frozen distinction between canonical Git blob identity and checkout materialization.

Repair commit:

```text
c6fdd1a1477a981a17d06068c71baf26bff06994
Fix W2 materialization alignment on clean checkouts
```

The guard now preserves the same influential-source set comparison while asking Git whether those carriers differ from the selected commit. This respects repository clean/text normalization rules, accepts a genuinely clean CRLF checkout, and still fails closed for real tracked source drift.

Materialization regression evidence:

```text
targeted clean-line-ending regression          1 / 1 PASS
CLI + snapshot regression                     77 / 77 PASS
```

## 4. Structural shadow comparison

Dedicated W2 qualification is version-controlled in:

```text
tests/unit/test_project_knowledge_w2_shadow_views.py
```

Qualification commit:

```text
6c8c3540ad58d2b54a9c4e4bbac4b3da7cc2e5fd
Qualify W2 shadow derived views
```

The test proves:

```text
all 8 materialized views + manifests equal an exact committed rebuild
all manifests bind successor semantic owners rather than live compatibility surfaces
generated outputs never become generated inputs
all manifests bind the same 10-source live semantic slice
current-state core matches current routing plus stable qualified shadow facts
Project Integration Boundary remains exact
current Specification 028 and Experiment 192/INCOMPLETE remain exact
Source Vault and Cockpit paused/resume semantics match qualified shadow expectations
workstream route remains WS-PKA-CURRENT with the paused branches preserved
source/identity/authority indexes cover exactly the 10 live successor identities
subject memberships cover the live slice
risk/obligation view preserves the six Source Vault constraints and both return conditions
```

Focused W2 result:

```text
5 / 5 PASS
```

Broader structural-view regression:

```text
411 / 411 PASS
```

## 5. Persistent-view qualification

Persistent materialization commit:

```text
1e615aec0e67b782ec7e599704e7c18a84ec932c
Materialize W2 persistent shadow views
```

Qualification on that exact commit:

```text
8 / 8 view freshness                      FRESH
W2 focused qualification                    5 / 5 PASS
COMMIT validation                         PASS
candidate count                           1,471
governed declarations                    10
generated noncanonical manifests           8
diagnostics                                0
PUBLIC_REPOSITORY_INTEGRITY               PASS
git show --check                          PASS
git diff --check                          PASS
```

## 6. Authority and compatibility boundary

W2 changes no operational authority.

The generated artifacts remain:

```text
derived
rebuildable
non-authoritative
not unique accepted truth
```

The following live compatibility surfaces remain untouched by generation:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/CONTINUITY.md
```

They are also absent from the persistent view input bindings.

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 7. Acceptance-finalization boundary

The semantic program anchor advances to:

```text
checkpoint       552
stage            SPECIFICATION:028 / W2_ACCEPTED
boundary         project-knowledge-wave-two-accepted-compatibility-shadow-next
```

Because this changes a canonical generated-view input, the eight persistent views must be rematerialized from the exact post-boundary commit before this result is finalized and published.

Until that post-boundary rematerialization and qualification pass:

```text
W2_PUBLICATION=BLOCKED
W3=NOT_STARTED
```
