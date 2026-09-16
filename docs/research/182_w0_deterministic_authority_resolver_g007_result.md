# Research 182: W0 Deterministic Authority Resolver G007 Result

**Date:** 2026-09-16
**Status:** PKA-G007 ACCEPTED / AUTHORITY RESOLVER VERIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179
**Prior accepted boundary:** Checkpoint 528 / Research 181 / `99cca3484f4dcb37128c38c2436a6dbcd6d00a0f`
**Scope:** Record the production deterministic authority resolver, the finite-scope defect exposed during independent review, the bounded repair, and independent acceptance of PKA-G007.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts PKA-G007 only. It does not accept PKA-G008+, begin W1 migration, publish successor views, or switch operational authority.

## 1. Implemented boundary

G007 adds the production authority domain layer under `tools/project_knowledge/authority.py`, extends immutable L0 authority values in `tools/project_knowledge/model.py`, and adds qualification coverage in `tests/unit/test_project_knowledge_authority.py`. The resolver remains pure L2 domain logic: no filesystem, Git, repository discovery, network, persistence, implicit wall-clock time, or retrieval ranking participates in authority decisions.

## 2. Accepted authority semantics

The accepted resolver operates over explicit candidate canonical sources and supports the frozen authority query dimensions: action, target, scope, consequence, optional time, optional workstream/actor, explicit required authorities, revision/freshness evidence, and required delegated private-state evidence.

Per-candidate scope matching remains exactly three-valued: `NO_MATCH`, `UNDERSPECIFIED`, `MATCH`. Scope is a finite conjunction of named exact-match facets with no wildcard, regex, executable predicate, or lexical-priority semantics. Consequence never resolves an otherwise undetermined authority query.

The resolver applies `REPLACE`, `CORRECT`, `SPECIALIZE`, and `SUPPLEMENT` using authored natural direction. Replacement/correction/specialization closure removes predecessors only for the applicable scope, supplement closure retains required bases and ordering, and cycles fail visibly rather than being broken by path or lexical order. `SPECIALIZE` uses a genuine subset/partial-order check rather than facet count.

Retrieval nominations are deliberately non-authoritative and may be ignored even when adversarially ranked. Qualified joint authority is admitted only through the bounded J1-J6 contract and cannot resurrect sources removed by scope, temporal, lifecycle, or relation closure.

## 3. Receipt and failure contract

The resolver implements the Specification 028 statuses: `RESOLVED`, `UNRESOLVED_SCOPE_REQUIRED`, `UNRESOLVED_AUTHORITY_CONFLICT`, `MISSING_REQUIRED_AUTHORITY`, `STALE_REQUIRED_AUTHORITY`, and `REQUIRED_PRIVATE_STATE_UNAVAILABLE`.

A resolved receipt contains governing semantic IDs/carriers, exact revisions where applicable, applicability reason, relation/combination semantics, per-source scope dispositions, removed sources with explicit reasons, snapshot mode, freshness/availability evidence, activated governing-procedure constraints, and explicit constraint precedence. Sorting is serialization only and never semantic precedence.

Public `RESOLVED_PRIVATE` facts remain public-resolved without private reinspection unless the current query explicitly requires delegated private state. When private state is required and unavailable/stale/unverified, resolution fails visibly.

## 4. Independent-review defect and repair

The initial G007 implementation passed 89 authority tests but independent ChatGPT review found one missing finite-query invariant. For a query such as `region=(eu, us)`, with authority only for `eu`, the resolver enumerated both cells but silently skipped the uncovered `us` cell and incorrectly returned `RESOLVED`.

The bounded repair separates explicitly requested finite cells from hypothetical completions of omitted facets. Every explicitly requested Cartesian cell now requires candidate coverage. An uncovered requested cell returns `MISSING_REQUIRED_AUTHORITY` with diagnostic `NO_APPLICABLE_AUTHORITY`; it can no longer disappear from the outcome. If explicit cells resolve to different governing sets, the result remains fail-visible as `UNRESOLVED_SCOPE_REQUIRED` / `DISCRIMINATING_SCOPE_REQUIRED`. If all explicit cells resolve to the same governing set, resolution succeeds.

The adjacent review also corrected finite-set receipt scope assessments: a source that matches every explicitly requested finite cell is `MATCH`, while partial/mixed coverage is not mislabeled as a complete match. Literal values such as `OTHER` remain ordinary literals and are not confused with the internal hypothetical omitted-facet completion cell.

Regression coverage now includes same-outcome finite sets, different-outcome finite sets, uncovered cells, uncovered Cartesian combinations across multiple facets, omitted-facet completions, literal `OTHER`, failures isolated to one requested cell, and permutation-stable deterministic serialization.

## 5. Independent verification

ChatGPT inspected the production implementation and independently reproduced the repaired finite-scope behavior:

```text
uncovered eu/us cell set      MISSING_REQUIRED_AUTHORITY / NO_APPLICABLE_AUTHORITY
same governing set            RESOLVED
different governing sets      UNRESOLVED_SCOPE_REQUIRED / DISCRIMINATING_SCOPE_REQUIRED
```

Independent post-repair verification results:

```text
authority suite                        103 / 103 PASS
identity suite                          63 / 63 PASS
substrate suite                        222 / 222 PASS
inherited unit inventory              309 / 309 PASS
complete unit inventory               697 / 697 PASS
compileall                            PASS
WORKTREE project-knowledge validate   PASS / zero diagnostics / zero live declarations
COMMIT project-knowledge validate     PASS / zero diagnostics / zero live declarations
PUBLIC_REPOSITORY_INTEGRITY           PASS
git diff --check                      PASS
```

One oversized inherited partition exceeded the Runtime Bridge 30-second command ceiling during independent verification. It was rerun as two non-overlapping partitions, 52/52 and 40/40, both passing. This was an execution-ceiling event, not a product/test failure.

The accepted pre-G007 COMMIT validation remained bound to `99cca3484f4dcb37128c38c2436a6dbcd6d00a0f`.

## 6. Gate disposition

```text
PKA-G001 PASS
PKA-G002 PASS
PKA-G003 PASS
PKA-G004 PASS
PKA-G005 PASS
PKA-G006 PASS
PKA-G007 PASS
PKA-G008..PKA-G017 PENDING
```

No G008 implementation, W1 migration, persistent successor view, live compatibility replacement, or operational authority switch occurred.

## 7. Next W0 work

The next bounded implementation task is PKA-G008, the deterministic workstream engine required by Specification 028 and Research 179: DAG/dependency semantics, pause/return/resume behavior, interruption recovery from durable receipts, and stale expected-revision rejection without replaying completed consequential work.

```text
RESEARCH182=PKA_G007_ACCEPTED
PKA_G001_G007=PASS
PKA_G008_G017=PENDING
SPECIFICATION_028=UNCHANGED
NEXT=PKA_G008_WORKSTREAM_ENGINE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
