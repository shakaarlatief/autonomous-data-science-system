# Research 194: W1 Selected Architecture Workstream G101 Result

**Date:** 2026-09-19
**Status:** PKA-G101 ACCEPTED / W1 LIVE-CONTROL SEMANTIC MIGRATION STARTED / CURRENT CONTINUITY STILL OPERATIONAL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted boundary:** Checkpoint 542 / Research 193 / W0 ACCEPTED
**Implementation commit:** `75bc3ab43b8f161596aec09e452df5f47f4fced0`
**Scope:** Accept the first W1 live semantic owner for the selected Candidate 01 implementation/migration workstream.
**Authority:** This record accepts PKA-G101 only. It does not accept PKA-G102..PKA-G109, overwrite a live compatibility surface, or switch operational authority.

## 1. W1 entry

W0 is accepted, so Specification 028 permits the bounded W1 live-control migration wave to begin.

The first W1 semantic owner is:

```text
docs/project_knowledge/selected_architecture_workstream.md
```

It is intentionally project-global because the selected architecture implementation/migration program is a project-wide resumable workstream with its own lifecycle.

## 2. Semantic ownership

The source carries one production `workstream.v1` declaration:

```text
semantic_id       WS-PKA-CURRENT
kind              PROJECT_KNOWLEDGE_ARCHITECTURE_WORKSTREAM
authority_class   canonical
state             ACTIVE
architecture      PKA-CANDIDATE-01
program           project-knowledge-architecture
```

The source owns only the workstream-level semantics needed at this gate:

```text
durable workstream identity
active lifecycle state
bounded scope
implementation/migration objective
provenance and navigation references
```

It deliberately does not duplicate the substantive Candidate 01 selection rationale. D-035 remains the natural owner of that decision.

It also does not yet claim later W1 responsibilities such as:

```text
Project Integration Boundary ownership
Source Vault paused/resume state
Cockpit paused/resume state
D-035 machine-resolved selection semantics
current-core execution anchor/stage projection
operational-authority switching
```

Those remain bounded by PKA-G102 onward.

## 3. Current-authority boundary

The live source explicitly preserves:

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

The new source is canonical within the successor semantic model, but current compatibility/continuity surfaces remain operational authority until the later qualified cutover program and explicit W8 decision.

## 4. Compatibility discoverability

Because current continuity remains live during W1, the existing `docs/KNOWLEDGE_MAP.md` now routes directly to the new workstream owner under development governance.

This is compatibility maintenance, not a successor-generated overwrite.

## 5. Qualification

Focused W1 G101 tests:

```text
2 / 2 PASS
```

The tests prove:

```text
exactly one live canonical WS-PKA-CURRENT owner exists
the owner is the intended repository carrier
profile/kind/state/authority/scope are exact
D-035 and Specification 028 remain provenance
current operational authority and no-switch boundary remain explicit
```

Exact implementation qualification:

```text
implementation COMMIT validation     PASS / 1,433 candidates / 1 governed declaration / zero diagnostics / COMMITTED
PUBLIC_REPOSITORY_INTEGRITY          PASS
git show --check                     PASS
git diff --check                     PASS
```

## 6. Gate disposition

```text
PKA-G101           PASS
PKA-G102..G109     PENDING
W0                 ACCEPTED
W1                 IN PROGRESS
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 7. Next bounded gate

The next gate is PKA-G102:

```text
Project Integration Boundary has one natural canonical semantic owner
```

```text
RESEARCH194=PKA_G101_ACCEPTED
PKA_G101=PASS
NEXT=PKA_G102_PROJECT_INTEGRATION_BOUNDARY
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
