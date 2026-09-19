# Research 198: W1 D-035 Selection Semantics G105 Result

**Date:** 2026-09-19
**Status:** PKA-G105 ACCEPTED / W1 LIVE-CONTROL SEMANTIC MIGRATION CONTINUES / CURRENT CONTINUITY STILL OPERATIONAL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted gate:** Checkpoint 546 / Research 197
**Implementation commit:** `440959aa4d771a0c37ebe40bc3b33c977ed7fb31`
**Scope:** Make the D-035 architecture-selection fact machine-resolvable at its natural owner without copying D-035's substantive decision text into another source.
**Authority:** This record accepts PKA-G105 only. It does not accept PKA-G106..PKA-G109, overwrite a live compatibility path, or switch operational authority.

## 1. Natural decision owner retained

The selection decision already has a natural canonical owner:

```text
docs/DECISIONS.md#D-035
```

G105 therefore does not create a second selected-architecture decision file or a central selection registry.

D-035 now carries one small `semantic_source.v1` declaration:

```text
semantic_id       D-035
kind              ARCHITECTURE_SELECTION_DECISION
authority_class   canonical
state             ACTIVE
decision_domain   project-development-knowledge-architecture
selected_target   PKA-CANDIDATE-01
```

The declaration is adjacent to the rich decision text and is machine-resolvable through the production project-knowledge parser/validator.

## 2. No substantive-decision duplication

The structured projection deliberately does not copy:

```text
the Repository-Native Semantic Sources architecture description
the 67/67 qualification evidence
the selected architecture commitments
the authority-switch conditions
the rationale for selection
the implementation/migration authorization narrative
```

Those remain solely in D-035's authored prose.

The selected architecture workstream may name `PKA-CANDIDATE-01` as its scope because that describes what the workstream operates on; the selection fact itself resolves back to D-035.

## 3. Cross-owner consistency

The G105 regression proves:

```text
WS-PKA-CURRENT.scope.architecture
    ==
D-035.scope.selected_target
    ==
PKA-CANDIDATE-01
```

This gives the successor workstream a deterministic connection to the selected target while preserving D-035 as the canonical semantic owner of the selection decision.

## 4. Qualification

Focused W1 live-semantics tests:

```text
14 / 14 PASS
```

Relevant declaration/schema/authority/current-core regression set:

```text
349 / 349 PASS
```

Exact implementation qualification:

```text
implementation COMMIT validation     PASS / 1,445 candidates / 8 governed declarations / zero diagnostics / COMMITTED
PUBLIC_REPOSITORY_INTEGRITY          PASS
git show --check                     PASS
git diff --check                     PASS
```

## 5. Gate disposition

```text
PKA-G101..PKA-G105   PASS
PKA-G106..PKA-G109   PENDING
W0                    ACCEPTED
W1                    IN PROGRESS
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 6. Next bounded gate

The next gate is PKA-G106:

```text
generated workstream/current-core views are deterministic from W1 canonical owners
```

```text
RESEARCH198=PKA_G105_ACCEPTED
PKA_G101_G105=PASS
NEXT=PKA_G106_W1_DERIVED_VIEW_DETERMINISM
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
