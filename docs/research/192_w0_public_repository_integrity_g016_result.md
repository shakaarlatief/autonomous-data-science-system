# Research 192: W0 Public Repository Integrity G016 Result

**Date:** 2026-09-19
**Status:** PKA-G016 ACCEPTED / PUBLIC REPOSITORY-INTEGRITY AGGREGATE QUALIFIED / W0 REMAINS IN PROGRESS
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179, with Research 185 retaining its G010 field-level refinement
**Prior accepted gate:** Checkpoint 540 / Research 191
**Implementation commit:** `e1f030d0b4c037226557778917dc3dc7ab9c7431`
**Scope:** Accept PKA-G016 by integrating production project-knowledge validation into the existing fail-closed public repository-integrity aggregate while preserving the inherited validators and aggregate PASS contract.
**Authority:** This record accepts PKA-G016 only. It does not accept PKA-G017, close W0, start W1, overwrite a live compatibility surface, or switch operational authority.

## 1. Gate interpretation

Specification 028 requires both:

```text
PKA-G016
    existing public repository-integrity aggregate remains PASS

Section 34
    production project-knowledge validation becomes a component
    of the existing aggregate public repository-integrity gate
    before any successor-generated compatibility surface can become authoritative
```

A bare rerun of the pre-G016 aggregate would therefore have been insufficient evidence for the intended integration boundary. Before this change, `scripts/check_repository_integrity.py` still executed the existing family-aware and focused validators but did not invoke the production `tools.project_knowledge validate` surface.

## 2. Accepted integration

The aggregate now invokes:

```text
python -B -m tools.project_knowledge validate
    --root <repository-root>
    --snapshot-mode WORKTREE_SNAPSHOT
```

as an explicit public-integrity component.

The component:

```text
uses the production project-knowledge CLI rather than a duplicate validator
runs in the same repository root as the aggregate gate
uses WORKTREE_SNAPSHOT because the aggregate validates the checked-out repository state
contributes failure to the aggregate failure set
prints Project-knowledge validation: PASS only on zero exit
preserves PUBLIC_REPOSITORY_INTEGRITY=PASS only when every required component passes
does not replace or weaken any inherited focused validator
```

The inherited aggregate components remain:

```text
family-aware repository contracts
checkpoint metadata
Knowledge Map
model collaboration state
current routing
```

## 3. CI path integration

The repository-integrity GitHub Actions workflow now observes both:

```text
schemas/project_knowledge/**
tools/project_knowledge/**
```

for push and pull-request path filtering.

This prevents production project-knowledge implementation or schema changes from silently bypassing the aggregate remote integrity workflow merely because no legacy documentation/integrity path changed.

## 4. Fail-closed regression coverage

`tests/unit/test_repository_integrity_aggregate.py` now verifies:

```text
the exact project-knowledge aggregate command
WORKTREE_SNAPSHOT binding
non-zero project-knowledge validation is retained as component failure
the aggregate emits PUBLIC_REPOSITORY_INTEGRITY=FAIL when that component fails
the GitHub Actions workflow tracks both project-knowledge implementation and schema roots
the inherited focused-validator command contracts remain unchanged
```

Focused aggregate regression result:

```text
11 / 11 PASS
```

The inherited repository-integrity regression set also remains green:

```text
test_repository_integrity.py
test_repository_integrity_aggregate.py
test_current_routing_integrity.py
test_continuity_preflight.py

39 / 39 PASS
```

## 5. Exact implementation qualification

Implementation commit:

```text
e1f030d0b4c037226557778917dc3dc7ab9c7431
Integrate project knowledge into repository integrity
```

Qualification:

```text
aggregate focused tests                       11 / 11 PASS
repository-integrity regression set          39 / 39 PASS
implementation COMMIT validation             PASS / 1,428 candidates / zero diagnostics / COMMITTED
production project-knowledge aggregate        PASS
inherited focused validators                  PASS
PUBLIC_REPOSITORY_INTEGRITY                   PASS
git show --check                              PASS
git diff --check                              PASS
```

The aggregate output now includes:

```text
Family-aware repository contracts: PASS
Project-knowledge validation: PASS
Focused validator checkpoint metadata: PASS
Focused validator Knowledge Map: PASS
Focused validator model collaboration state: PASS
Focused validator current routing: PASS
PUBLIC_REPOSITORY_INTEGRITY=PASS
```

## 6. Architectural disposition

G016 closes the W0 repository-integrity integration seam without switching authority.

In particular:

```text
production project-knowledge validation is now inside the aggregate gate
legacy focused validators remain active
no successor-generated compatibility surface is authoritative
no current compatibility file was overwritten
W1 has not started
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

## 7. Gate disposition

```text
PKA-G001..PKA-G016   PASS
PKA-G017             PENDING
W0                    IN PROGRESS
W1                    NOT STARTED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
SPECIFICATION_028=UNCHANGED
```

## 8. Next bounded gate

The final W0 executable gate is PKA-G017:

```text
inherited complete unit suite remains PASS
```

This result does not execute or accept G017.

```text
RESEARCH192=PKA_G016_ACCEPTED
PKA_G001_G016=PASS
PKA_G017=PENDING
NEXT=PKA_G017_INHERITED_COMPLETE_UNIT_SUITE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
