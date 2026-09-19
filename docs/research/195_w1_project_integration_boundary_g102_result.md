# Research 195: W1 Project Integration Boundary G102 Result

**Date:** 2026-09-19
**Status:** PKA-G102 ACCEPTED / W1 LIVE-CONTROL SEMANTIC MIGRATION CONTINUES / CURRENT CONTINUITY STILL OPERATIONAL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior accepted gate:** Checkpoint 543 / Research 194
**Implementation commit:** `dae622f7baa42fe99551789156e12beefae7424b`
**Scope:** Accept one natural canonical successor owner for the Project Integration Boundary.
**Authority:** This record accepts PKA-G102 only. It does not accept PKA-G103..PKA-G109, overwrite a live compatibility surface, or switch operational authority.

## 1. Natural owner

The Project Integration Boundary now has one production semantic owner:

```text
docs/project_knowledge/project_integration_boundary.md
```

This is a natural project-global owner because promoted integration branch + exact promoted commit form one durable project-wide semantic unit with no more local workstream owner.

The source deliberately rejects becoming a broad project-control registry.

## 2. Machine contract

The source carries one `project_boundary.v1` declaration:

```text
semantic_id       PROJECT-INTEGRATION-BOUNDARY
kind              PROJECT_INTEGRATION_BOUNDARY
authority_class   canonical
state             ACTIVE
promoted_branch   v1-frontend-spike
promoted_commit   2480109fadeee1e480ef03b82e335aacdf9adf91
```

The exact promoted commit still matches the current repository's `origin/v1-frontend-spike` reference and the current compatibility projection in `docs/current_routing.json`.

The declaration therefore exercises the meaningful `project_boundary.v1` contract introduced by Research 185 rather than leaving the profile as a label-only abstraction.

## 3. Ownership boundary

The Project Integration Boundary owns only:

```text
promoted integration branch
exact promoted integration commit
```

It does not own:

```text
active development branch
active pull request
current checkpoint
current workstream boundary
latest specification
experiment outcome
unrelated project-control facts
```

This preserves the Candidate 01 decomposition from Research 153 and avoids a new central project-control registry.

## 4. Compatibility and authority

The current live `docs/current_routing.json` remains an operational compatibility/continuity surface during W1.

The G102 tests compare the successor owner against that live compatibility projection, but the successor owner is not generated from the compatibility target.

No compatibility path was overwritten.

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 5. Qualification

Focused W1 tests:

```text
4 / 4 PASS
```

Exact implementation qualification:

```text
implementation COMMIT validation     PASS / 1,436 candidates / 2 governed declarations / zero diagnostics / COMMITTED
PUBLIC_REPOSITORY_INTEGRITY          PASS
git show --check                     PASS
git diff --check                     PASS
```

## 6. Gate disposition

```text
PKA-G101..PKA-G102   PASS
PKA-G103..PKA-G109   PENDING
W0                    ACCEPTED
W1                    IN PROGRESS
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 7. Next bounded gate

The next gate is PKA-G103:

```text
Source Vault paused/resume semantics reproduce the qualified real state
```

```text
RESEARCH195=PKA_G102_ACCEPTED
PKA_G101_G102=PASS
NEXT=PKA_G103_SOURCE_VAULT_PAUSED_RESUME
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
