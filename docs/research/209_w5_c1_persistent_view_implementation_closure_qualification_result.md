# Research 209: W5 C1 Persistent-View Implementation-Closure Qualification Result

**Date:** 2026-09-20
**Status:** C1 ACCEPTED / T1 NEXT
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**Prior accepted project milestone:** Checkpoint 554 / W4 ACCEPTED AND FINALIZED
**Implementation commit:** `66feafff44db26b7840c360b6fef01d372897fae`
**Manifest refresh commit:** `c52c379c27233c3e45221372a6d6c5cdfc354876`
**Scope:** Close Research 208 C1 by replacing the single maximal persistent-view implementation closure with explicit per-view Git-byte implementation closures while preserving exact committed execution semantics, deterministic rebuilds, full/selected equivalence, global source validation, W0-W4 behavior and generated view bytes.
**Authority:** This result accepts C1 only. It does not freeze T1/T3/T4, begin broad W5 semantic migration, overwrite live compatibility surfaces, switch operational authority, or reopen W0-W4 acceptance.

## 1. C1 requirement

Research 208 identified that all eight persistent views shared one maximal `implementation_files` closure, so any listed implementation/schema byte change invalidated every manifest. C1 required each view to bind the smallest explicit implementation closure that actually determines that view while preserving exact `GIT_BLOB_BYTES_AT_COMMIT` hashing, complete-input semantics, global canonical-source integrity, deterministic rebuild, full/selected equivalence and circularity protection.

## 2. Implementation result

The old monolithic `tools/project_knowledge/pure_units.py` carrier was split without changing the 31 restricted pure functions. An independent AST comparison against pre-C1 commit `a4fdffd8` proved 31/31 names preserved and 0 AST mismatches.

The new physical separation is:

```text
tools/project_knowledge/views.py
    shared builder / manifest / freshness / complete-input infrastructure only

tools/project_knowledge/pure_*.py
    restricted pure projection bodies split by actual dependency family

tools/project_knowledge/view_definitions/
    common.py
        shared exact implementation closure
    one module per view
        specification + view-private PURE_UNITS declarations
    units_*.py
        data-only unit declarations shared by actual consumers
    __init__.py
        host-side catalog only; not in any persistent view closure
```

The isolated worker does not import view-definition modules. It parses committed `PURE_UNITS` literals only from the selected view's bound Git blobs.

## 3. Original `views.py` coupling is closed

The first partial C1 attempt split pure bodies but still left every view specification and unit registry inside shared `views.py`. That would still stale all eight manifests when only one view specification changed.

The accepted implementation now enforces:

```text
views.py
    no *_specification functions
    no production_view_specifications
    no PURE_UNIT_REGISTRY
    no pure_* view-specific bindings
    no view_definitions imports

view-specific specification bytes
    live in that view's own bound definition module
    invalidate only the relevant view

shared helper declaration/source bytes
    invalidate exactly their real consumers

genuinely shared builder/admission bytes
    continue to invalidate all eight
```

## 4. Qualification evidence

Independent ChatGPT focused rerun:

```text
test_project_knowledge_persistent_views.py
test_project_knowledge_view_execution.py
test_project_knowledge_substrate_architecture.py

113 / 113 PASS
duration: 291.03 s
```

Independent AST preservation check:

```text
old pure functions     31
new pure functions     31
name set               exact match
AST mismatches         0
```

After committing implementation and before manifest refresh, W1/W2 qualification produced 7 PASS and 1 expected failure. The only failure was exact W2 manifest-byte comparison because generator bindings had changed while checked-in manifests still represented the prior closure. After exact manifest rebuild, W1/W2 produced 8/8 PASS.

The structural rebuild showed no semantic view-byte changes across all eight persistent views. Only their manifests changed to bind the new implementation closures.

Independent broad modern project-knowledge qualification:

```text
23 test files
882 / 882 PASS
duration: 1201.78 s
```

The run covered architecture, authority, capture, CLI, current-state core, identity, persistent views, privacy, refresh, substrate declaration/schema/snapshot/architecture, view execution, view semantics, W1, W2, W3, W4 and workstreams.

## 5. Architectural interpretation

C1 does not weaken complete repository admission. Global source/canonical integrity remains complete and shared. Only per-view implementation invalidation is narrowed to the implementation bytes that actually determine that view.

The host-side `view_definitions/__init__.py` catalog remains outside individual closures by design: changing the production view catalog does not retroactively alter the generation semantics of unrelated existing views.

Historical evidence such as Research 184 and MC-0018 Message 003 remains untouched because it correctly records the implementation that existed when authored. Current architecture documentation should describe the split implementation.

## 6. Acceptance

```text
C1_IMPLEMENTATION_GRANULARITY=ACCEPTED
PURE_FUNCTION_SEMANTICS=UNCHANGED
VIEW_SEMANTIC_BYTES=UNCHANGED_8_OF_8
PERSISTENT_MANIFESTS=REFRESHED_8_OF_8
FOCUSED_C1_REGRESSION=113_OF_113_PASS
W1_W2_POST_REFRESH=8_OF_8_PASS
MODERN_PROJECT_KNOWLEDGE_REGRESSION=882_OF_882_PASS
BROAD_W5_MIGRATION=PAUSED
NEXT=T1_CONTROLLED_SUBJECT_VOCABULARY_CORPUS
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
