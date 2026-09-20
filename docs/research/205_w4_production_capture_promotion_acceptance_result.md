# Research 205: W4 Production Capture and Promotion Acceptance Result

**Date:** 2026-09-20
**Status:** W4 ACCEPTED / POST-BOUNDARY FINALIZATION PENDING
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted boundary:** Checkpoint 553 / Research 204 / W3 ACCEPTED AND FINALIZED
**Qualified pre-acceptance state:** `055cd7284af4834d4a1b21607e0aaac962ac6cde`
**Scope:** Accept W4 after one bounded real capture was reviewed, revision-bound, promoted into its natural canonical owner, archived out of the open-capture state, and proven to preserve accepted meaning and provenance after archival.
**Authority:** This record accepts W4 only. It does not begin W5 semantic migration, overwrite live compatibility paths, resume Source Vault/Cockpit execution, or switch operational authority. Checkpoint 554 is the W4 semantic anchor.

## 1. W4 requirement

Specification 028 defines W4 as:

```text
Run one bounded real capture through review and canonical promotion.
Verify accepted meaning/provenance remains after capture archival/removal
according to the preservation contract.
```

The W0 capture/promotion substrate remains intentionally split between:

```text
capture.v1 record
    -> explicit review
    -> exact canonical target revision binding
    -> PromotionPlan
    -> explicit canonical edit / promotion
    -> capture archival
```

Captures remain structurally non-authoritative throughout.

## 2. Real capture selected for W4

The bounded real capture is:

```text
semantic ID
    CAPTURE:W4-BRANCH-BOUNDARY-SCOPE

open carrier
    docs/project_knowledge/captures/open/w4_branch_boundary_scope.json

canonical target
    PROJECT-INTEGRATION-BOUNDARY
    docs/project_knowledge/project_integration_boundary.md

promoted semantic unit
    UNIT:PROJECT-INTEGRATION-BOUNDARY-BRANCH-LIFECYCLE-NONOWNERSHIP
```

The captured observation came from the live branch-lifecycle discussion and AB-032. Its accepted meaning is narrow:

```text
PROJECT-INTEGRATION-BOUNDARY owns:
    promoted integration branch
    exact promoted integration commit

PROJECT-INTEGRATION-BOUNDARY does not own or imply:
    when development branches are created
    when they are continued or rotated
    when they are merged
    when they are archived or retired
```

The broader branch-lifecycle policy remains a separate deferred architecture question under AB-032.

## 3. Review and revision-bound promotion

The open capture was committed at:

```text
43a7e9308b2a869fc00edef8647be35144370d9b
```

Promotion planning then resolved the natural target by semantic identity and bound the exact committed target revision:

```text
target semantic ID
    PROJECT-INTEGRATION-BOUNDARY

target carrier
    docs/project_knowledge/project_integration_boundary.md

target source commit
    43a7e9308b2a869fc00edef8647be35144370d9b

target content digest
    sha256:0e05f2294891a4ffb9bca5f281ac6b00850b41de29331d321b0bfe55550627b

review disposition
    ACCEPTED_FOR_PROMOTION

semantic-unit disposition
    MATERIALIZED_IN_CANONICAL_SOURCE
```

The accepted understanding was then materialized into the existing natural canonical owner. No new competing authority source was created.

## 4. Archival and provenance preservation

Promotion commit:

```text
aeecf47e0fbe43a82309dd17fb78ffc27d0d1ffd
```

The canonical owner now explicitly states the branch-lifecycle non-ownership boundary and records provenance to:

```text
docs/project_knowledge/captures/historical/w4_branch_boundary_scope.json
docs/OPEN_ARCHITECTURE_BACKLOG.md#AB-032
```

The original open-capture location is retained only as an inert archival pointer without a `profile`, so it is not a second `capture.v1` record. The historical capture is `COMPLETED`, remains non-authoritative, and cannot re-enter promotion planning.

Dedicated production qualification proves:

```text
open capture replaced by inert archival pointer
exactly one real CAPTURE:W4-BRANCH-BOUNDARY-SCOPE record remains
historical capture state = COMPLETED
accepted non-ownership meaning exists in canonical owner
capture provenance survives archival
canonical owner references historical capture provenance
archived capture promotion re-entry -> CAPTURE_NOT_OPEN
```

## 5. Implementation chronology

The bounded W4 implementation sequence is:

```text
43a7e9308b2a869fc00edef8647be35144370d9b  Open W4 real capture
aeecf47e0fbe43a82309dd17fb78ffc27d0d1ffd  Promote W4 branch-boundary capture
6b64f5c6fa5f6e3591ad2942203e7c134ed0c7d7  Qualify W4 capture promotion
10478b2c932619dcb97063d99b2fb54675e5380a  Refresh structural views after W4 promotion
457cb6191ea57dddfd9c19233e790b8a3332b4fa  Refresh compatibility shadow after W4 promotion
25ef1525cad07731202dd874461bf50a7d9b7de0  Generalize migration-stage regressions
055cd7284af4834d4a1b21607e0aaac962ac6cde  Extend branch lifecycle durability question
```

The branch-lifecycle backlog extension also records that local commit durability and authorized remote publication are distinct concerns, so long sequences of already-qualified commits should not remain unpublished merely by collaborator habit.

## 6. Pre-acceptance qualification

Exact qualification on `055cd72...`:

```text
W4 + capture + W3/W2/W1/architecture focused regression    77 / 77 PASS
persistent structural views                                8 / 8 FRESH
compatibility-shadow artifacts                              5 / 5 exact generated-byte match
compatibility blocking                                     false
MIGRATION_GAP                                              0
UNRESOLVED                                                 0
COMMIT project-knowledge validation                        PASS
candidate count                                            1,482
governed declarations                                      10
noncanonical declarations                                  9
capture-area carriers                                      2
diagnostics                                                 0
PUBLIC_REPOSITORY_INTEGRITY                                PASS
git show --check                                           PASS
```

The compatibility shadow remains non-blocking after the W4 promotion. Its content-derived source boundary is:

```text
sha256:d94e2275d3b7889d7a7b93efdd4c4deeae63e7cbd2ef59cbc74440ad4df9732c
```

## 7. Authority boundary

W4 changes no operational authority.

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

The promoted semantic unit is now canonical project knowledge, but the legacy continuity architecture remains the live operational authority until the separately qualified W8 decision.

## 8. Acceptance-finalization boundary

The semantic program anchor advances to:

```text
checkpoint       554
stage            SPECIFICATION:028 / W4_ACCEPTED
boundary         project-knowledge-capture-accepted-semantic-migration-next
```

Because this changes the canonical workstream execution anchor and adds W4 acceptance artifacts to the committed documentation tree, the structural views and compatibility shadow must be rematerialized from the exact Checkpoint 554 state before final publication.

```text
W4=ACCEPTED
POST_BOUNDARY_FINALIZATION=PENDING
W5=NOT_STARTED
NEXT=W5_BROADER_CURRENT_SEMANTIC_MIGRATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
