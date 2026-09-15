# Research 181: W0 Identity Transition and Current-Index G006 Result

**Date:** 2026-09-15
**Status:** PKA-G006 ACCEPTED / IDENTITY ENGINE VERIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179
**Scope:** Record the production identity-transition/current-index implementation, the identity-contract defects exposed before acceptance, the bounded repair, and independent verification of PKA-G006.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts PKA-G006 only. It does not accept PKA-G007+, begin W1 migration, persist a live identity view, or switch operational authority.

## 1. Implemented boundary

PKA-G006 adds the production identity domain layer under:

```text
tools/project_knowledge/identity.py
```

with supporting immutable typed values in:

```text
tools/project_knowledge/model.py
```

and qualification coverage in:

```text
tests/unit/test_project_knowledge_identity.py
tests/unit/test_project_knowledge_substrate_architecture.py
```

The implementation remains pure L2 domain logic. It performs no repository discovery, Git-history scan, filesystem I/O, persistence, authority resolution, or migration.

## 2. Accepted identity semantics

The implementation supports all seven Specification 028 transition classes:

```text
MOVE_OR_RENAME
REPRESENTATION_REPLACEMENT
MERGE
SPLIT
SUPERSEDE
RETIRE
REDIRECT
```

The accepted rules are:

```text
semantic identity remains independent of carrier path, title and Git blob identity
MOVE_OR_RENAME preserves one identical predecessor/successor semantic ID
REPRESENTATION_REPLACEMENT preserves one identical predecessor/successor semantic ID
MERGE requires multiple predecessors and one successor
SPLIT requires one predecessor and multiple successors
SUPERSEDE and REDIRECT carry explicit predecessor -> successor identity change
RETIRE has predecessor identity/identities and no successor
historical identities remain resolvable
normal current lookup is flattened and bounded
transition order is never inferred from path or lexical sort order
candidate/evidence/capture/derived transition records cannot govern current identity
```

Explicit temporal applicability uses half-open windows and requires an explicit timezone-aware `at_time`; the implementation never substitutes implicit wall-clock `now`.

## 3. Transition-source identity is separate from transition endpoints

An `identity_transition.v1` source may itself carry an explicitly authored `semantic_id` when the transition semantic unit needs durable identity.

That source identity:

```text
participates in current/historical ownership
participates in collision detection
participates in carrier/history lookup
may itself be the explicit endpoint of another transition
is serialized deterministically
remains logically separate from predecessor/successor endpoint identities
is never minted automatically from path, title, hash, filename or position
```

An unidentified transition source remains a transition record only and does not acquire an identity implicitly.

## 4. Pre-acceptance defects and repair

The first G006 implementation was not accepted immediately. Independent inspection found two identity-contract holes.

### 4.1 Continuity classes could change durable identity

The initial implementation allowed `MOVE_OR_RENAME` or `REPRESENTATION_REPLACEMENT` to connect different predecessor/successor IDs. That contradicted the selected architecture's rule that a move or representation replacement preserves semantic identity while changing its carrier or representation.

The repair now requires exactly one identical predecessor and successor ID for both continuity classes. A different ID fails visibly with:

```text
CONTINUITY_IDENTITY_CHANGED
```

Different-ID transitions remain represented by the explicit non-continuity classes such as `REDIRECT` and `SUPERSEDE`.

### 4.2 Transition-source semantic identity was dropped

The initial implementation treated a transition source's authored `semantic_id` as metadata rather than as the durable identity of the transition semantic unit itself.

The repair registers explicitly identified canonical/historical transition sources in the identity corpus while preserving complete separation from their relation endpoints. Ownership, lifecycle/time applicability, collisions, history and later explicit transitions over that transition identity now behave consistently with ordinary selectively identified semantic units.

These repairs did not require a Specification 028 amendment, Research 179 change, Candidate 01 reopen or H3/Object-Primary reopen.

## 5. Failure and ambiguity behavior

The accepted engine fails visibly rather than inventing precedence when identity state is ambiguous or malformed. Covered failures include:

```text
duplicate simultaneously current identity ownership
conflicting simultaneous outgoing identity transitions
dangling predecessor/successor identity references
invalid transition cardinality
continuity-class identity change
active transition cycles
historical target with no current successor or explicit retirement
snapshot-mode mixing
invalid or missing explicit temporal evaluation context
scoped transition presented to the global identity index without a scoped identity contract
```

A same-ID continuity transition does not itself choose between two simultaneously current carriers. Deterministic carrier handoff requires explicit lifecycle or temporal controls.

## 6. Deterministic rebuild and bounded lookup

The index is rebuilt from the supplied governed identity corpus plus accepted transition records.

Construction validates the active transition graph, computes lineage iteratively, and flattens each historical/current semantic ID to its current target set or retirement state. Split outcomes remain sets of successors without an invented primary successor.

Normal lookup is one precomputed mapping access:

```text
resolve_identity(index, semantic_id)
historical_lookup(index, semantic_id)
```

A deep 1,050-node transition-chain regression proves construction does not depend on Python recursion and lookup does not traverse history.

Deterministic serialization is stable across source order, transition order and endpoint order where those orders have no semantic meaning. Output uses UTF-8/LF and a final newline.

## 7. Evidence preservation

The G006 tests reuse qualified Candidate 01 evidence without importing research orchestration into production behavior.

Coverage includes:

```text
real Q3-R03 carrier continuity / retired historical label behavior
real Q3-R04 paused durable workstream identity
qualified synthetic Shadow V0.1 move / merge / time-bounded reversal / split behavior
```

The synthetic `REVERSE_MERGE` fixture is translated into the frozen production transition vocabulary as an ended MERGE applicability window plus an explicit SPLIT. No eighth transition class is introduced.

## 8. Independent verification

Codex reported the repaired implementation passing the requested verification boundary. ChatGPT then independently reran and inspected the relevant evidence before acceptance.

Independent results:

```text
identity suite                         63 / 63 PASS
substrate suite                       222 / 222 PASS
inherited unit inventory              309 / 309 PASS
complete unit inventory               594 / 594 PASS
compileall                            PASS
WORKTREE project-knowledge validate   PASS / zero diagnostics / zero live declarations
COMMIT project-knowledge validate     PASS / zero diagnostics / zero live declarations
PUBLIC_REPOSITORY_INTEGRITY           PASS
git diff --check                      PASS
```

The COMMIT validation was bound to pre-acceptance `HEAD`:

```text
256c5bfa253a9ad178e1fa578c028071cb26f6d2
```

One first substrate verification attempt encountered the known local temporary-directory permission boundary, and one oversized test partition exceeded the Runtime Bridge 30-second command ceiling. Neither represented a product/test failure. ChatGPT reran the same checks using workspace-local temporary directories and smaller non-overlapping partitions; the complete requested inventory passed.

## 9. Gate disposition

The accepted W0 gate state is now:

```text
PKA-G001 PASS
PKA-G002 PASS
PKA-G003 PASS
PKA-G004 PASS
PKA-G005 PASS
PKA-G006 PASS
PKA-G007..PKA-G017 PENDING
```

G006 acceptance does not imply that `identity_index.json` is now a persisted production view. Persistent derived-view publication/manifests remain later W0 work under their own gates.

## 10. Authority and migration boundary

```text
W0_OVERALL_ACCEPTED=false
W1_MIGRATION_STARTED=false
G007_IMPLEMENTED=false
LIVE_IDENTITY_VIEW_PERSISTED=false
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

No current canonical source adopted Candidate 01 semantics as part of G006.

## 11. Next W0 work

The next bounded implementation task is PKA-G007: the deterministic authority resolver required by Specification 028 and concretized in Research 179.

It must preserve the already accepted identity/substrate boundary and prove `REPLACE`, `SUPPLEMENT`, `SPECIALIZE`, `CORRECT`, scope discrimination, ambiguity/conflict handling, retrieval non-authority, source freshness/revision binding, private-availability behavior where applicable, and deterministic authority receipts without beginning G008 or W1 migration.

```text
RESEARCH181=PKA_G006_ACCEPTED
PKA_G001_G006=PASS
PKA_G007_G017=PENDING
SPECIFICATION_028=UNCHANGED
NEXT=PKA_G007_AUTHORITY_RESOLVER
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
