# Research 199: W1 Generated View Determinism G106 Result

**Date:** 2026-09-19
**Status:** PKA-G106 ACCEPTED / LIVE W1 CANONICAL OWNERS DRIVE DETERMINISTIC WORKSTREAM + CURRENT-CORE VIEWS / CURRENT CONTINUITY STILL OPERATIONAL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted gate:** Checkpoint 547 / Research 198
**Accepted implementation commit:** `d572a5c4616f96efac2dbf86dd2d23a16ad6a155`
**Scope:** Prove that the persistent workstream graph and machine/human current-state-core views are generated deterministically from the live W1 canonical semantic owners rather than compatibility state.
**Authority:** This record accepts PKA-G106 only. It does not publish a compatibility overwrite, accept PKA-G107..PKA-G109, or switch operational authority.

## 1. Live canonical inputs completed for current-core generation

G106 required the production current-state-core generator to operate on real W1 owners rather than the synthetic G010 fixture.

The active project-knowledge workstream now owns the typed current execution anchor and stage:

```text
WS-PKA-CURRENT
execution checkpoint      547 at the implementation boundary
development branch        v1-source-vault-bootstrap-resume
pull request              null
current boundary          project-knowledge-decision-accepted-views-next
stage id                  SPECIFICATION:028
stage state               W1_IN_PROGRESS
```

Two additional current semantic roles required by the frozen G010 input contract now live at their natural owners:

```text
SPECIFICATION:028
    carrier  docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
    kind     SPECIFICATION

EXPERIMENT:192
    carrier  docs/checkpoints/192_specification_022_incomplete_result_preservation_promotion_candidate.md
    kind     EXPERIMENT_RESULT
    outcome  INCOMPLETE
```

These are small structured projections. They do not duplicate the substantive specification or experiment evidence.

## 2. Generated current-state core

At the accepted implementation commit the production generator resolves:

```text
active workstream       WS-PKA-CURRENT / ACTIVE
stage                   SPECIFICATION:028 / W1_IN_PROGRESS
integration boundary    PROJECT-INTEGRATION-BOUNDARY
current specification   SPECIFICATION:028
current experiment      EXPERIMENT:192 / INCOMPLETE
paused workstreams      WS-COCKPIT-DESIGN
                        WS-SOURCE-VAULT-BOOTSTRAP
```

Source Vault contributes its source-owned governing procedure and compact ingestion/Course-2 milestones. Cockpit contributes only its generic paused/resume semantics.

The current-core manifest input bindings include the W1 canonical owners and exclude:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/CONTINUITY.md
```

Those current compatibility surfaces are comparison/operational surfaces during W1, not generation authority for G106.

## 3. Generated workstream graph

The persistent workstream graph deterministically resolves:

```text
ready set            [WS-PKA-CURRENT]
route disposition    UNIQUE_PRIMARY_ROUTE
primary route        WS-PKA-CURRENT
WS-PKA-CURRENT       RUNNABLE
WS-COCKPIT-DESIGN    PAUSED
WS-SOURCE-VAULT-BOOTSTRAP PAUSED
```

### Live-evidence repair

The first live W1 probe exposed a semantic gap in the W0 persistent projection.

The domain workstream engine already normalizes:

```text
execution_anchor.current_boundary
    -> current route anchor
```

but the pure persistent `workstream_graph` unit still projected only the older loose `current_anchor` field. The generated W1 graph was deterministic but emitted `current_anchor = null` for the active workstream.

G106 therefore repaired the pure view to use:

```text
current_anchor when explicitly authored
else execution_anchor.current_boundary when the typed anchor is authored
else null
```

This mirrors the G008 domain semantics and does not create a second normative anchor. A persistent-view regression now cross-checks the derived anchor against the domain workstream result.

## 4. Determinism evidence

The live W1 G106 test generates all three relevant persistent views twice from the exact committed snapshot and requires both view bytes and manifest bytes to be identical:

```text
workstream_graph
current_state_core
current_state_core_markdown
```

Result:

```text
3 / 3 G106 tests PASS
1 / 1 domain workstream-anchor cross-check PASS
```

A separate command-level production rebuild was also run twice before the semantic repair and produced byte-identical deterministic JSON command output. After the repair, the exact accepted commit rebuild succeeds and the G106 two-build test provides the stronger exact-commit determinism proof for the affected views.

Accepted implementation-view digests at `d572a5c...`:

```text
current_state_core
    view      b0c3cd10391c1732cfbd98fe30277d8aa71c648a8bc8cda5f8dd8d749749a941
    manifest  ae44833018eff18bf9dc81420979e72e8db46092fb7477da2d6e4e516b3ab7a1

current_state_core_markdown
    view      422ab1ec8f8b88e898477008bc78ddc786b8c3270ad3af73cff384b12ce93d8d
    manifest  f46d6799d2580252386b849e6b98e0458cfb34bc3a16e4fcff1b425f9e9157d5

workstream_graph
    view      60f93728efed93e29ad2b2ab43933f18a004baad0e7b8b94f65198235eb9f0d0
    manifest  7231951ec6bb588d94712d95c7284342d642a55e310c6140329b30afbc4c02f0
```

The generated artifacts remain staged/computed outputs only. G106 does not materialize or overwrite a live compatibility path.

## 5. Exact implementation qualification

```text
G106 live-view tests                  3 / 3 PASS
domain anchor parity regression       1 / 1 PASS
COMMIT_SNAPSHOT validation            PASS / 1,447 candidates / 10 governed declarations / zero diagnostics
PUBLIC_REPOSITORY_INTEGRITY           PASS
git show --check                      PASS
git diff --check                      PASS
```

## 6. Gate disposition

```text
PKA-G101..PKA-G106   PASS
PKA-G107..PKA-G109   PENDING
W0                    ACCEPTED
W1                    IN PROGRESS
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 7. Next bounded gate

The next gate is PKA-G107:

```text
no existing live compatibility path is overwritten
```

```text
RESEARCH199=PKA_G106_ACCEPTED
PKA_G101_G106=PASS
NEXT=PKA_G107_COMPATIBILITY_NON_OVERWRITE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
