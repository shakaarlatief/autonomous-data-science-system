# Checkpoint 135: First Production Lexical Retrieval Baseline Cross-Platform Passed

**Date:** 2026-08-22  
**Status:** Historical implementation/verification checkpoint; lexical baseline validated and ready for bounded promotion/merge  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Records the first production accepted-current SQLite FTS5 reusable-knowledge retrieval implementation and the complete Specification 009 v0.1 RH-L/RH-S lexical gate.  
**Authority:** Historical verification provenance. Specification 009 governs the evaluation contract; `experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md` is the detailed result artifact. Current routing documents govern the next project step.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Milestone

The first production retrieval channel for governed reusable methodological knowledge is now executable and cross-platform validated.

Implementation boundary:

```text
ADS application
    KnowledgeRetrievalPort
    KnowledgeRetrievalHit
        |
        v
SQLite retrieval infrastructure
    SqliteFtsKnowledgeRetrieval
        |
        v
rebuildable FTS5 accepted-current projection
```

The derived retrieval layer is revision-transparent but is not methodological authority.

---

## 2. Frozen benchmark result

Specification 009 v0.1 was frozen before implementation.

Final observable workflow:

```text
V1 methodological horizon
run 32559177057
source head c462365bf64ebe9d676a0d9ce6402bba61e67279
```

Results on both Ubuntu and Windows:

```text
frozen lexical retrieval benchmark    PASS
existing V1 Python regression suite    PASS
```

Quality metrics:

```text
indexed accepted-current assets    10
RH-L Recall@3                      1.00
RH-L MRR                           1.00
RH-L critical omissions            0 / 10
RH-L required target rank 1       10 / 10
RH-S diagnostic Recall@3           0.75
```

The benchmark output was identical across operating systems.

---

## 3. What the lexical baseline proves

The production slice proves that ADS can:

```text
keep candidate benchmark knowledge non-retrievable before acceptance
explicitly accept test-only knowledge through normal governance
rebuild one current lexical document per accepted KnowledgeAsset
retrieve every frozen lexical-addressable target within top 3
return every frozen lexical target at rank 1
return exact accepted knowledge revision IDs
honor bounded top-k output
handle blank/punctuation queries safely
rebuild deterministically
preserve authoritative semantic state unchanged
remove superseded accepted revisions from the current retrieval projection
retain historical knowledge revisions in authoritative persistence
execute consistently on Ubuntu and Windows
```

This is the first production realization of the D-028 / Specification 001 FTS5 retrieval seam rather than only an architecture spike.

---

## 4. Measured semantic gap

The frozen RH-S semantic/paraphrase diagnostics intentionally did not gate the lexical baseline.

Result:

```text
RH-S01  class-imbalance                         MISS
RH-S02  prediction-time-feature-eligibility    HIT rank 1
RH-S03  temporal-validation                    HIT rank 1
RH-S04  ecdf                                   HIT rank 1
```

RH-S01 query:

```text
positive cases are scarce and overall correctness hides failures on them
```

produced no lexical hits despite targeting `class-imbalance`.

This is useful evidence because semantic retrieval now has a concrete frozen gap to beat. It does not yet justify any particular embedding model, vector store, or semantic architecture.

---

## 5. First workflow failure was not a product failure

Initial PR workflow run:

```text
32559023163
```

The frozen retrieval test passed on both Ubuntu and Windows, but the broad regression step failed during test collection because the new workflow used:

```text
pytest tests -q
```

instead of the repository-proven invocation:

```text
python -m pytest -q
```

The difference caused existing runtime-bakeoff tests to lose repository-root import visibility for `experiments.*`.

Only the workflow invocation was corrected. The implementation, benchmark cases, expected keys, projection fields, and BM25 weights were unchanged.

Corrected run `32559082914` passed cross-platform. Final observable run `32559177057` also passed cross-platform.

---

## 6. Promotion audit

### Strong enough to retain as current V1 implementation

The following now have executable evidence:

```text
storage-neutral KnowledgeRetrievalPort
revision-transparent KnowledgeRetrievalHit
SQLite FTS5 accepted-current derived projection
rebuildable deterministic lexical index
weighted BM25 baseline from Specification 009
query-safety and accepted-current invariants
```

These implement the already-accepted D-028 / Specification 001 architecture rather than introducing a new system-level architectural family.

### Do not promote yet

Do not infer selection of:

```text
embedding model/provider
semantic retrieval implementation
vector database
ANN index/service
lexical/semantic fusion
reranker
final MethodologicalHorizon ranking/budget
final applicability evaluator
final context assembler
```

No new Foundation or project-level Decision is required at this checkpoint.

---

## 7. Exact continuation

The validated lexical slice should now be merged independently into the promoted V1 integration branch.

Then begin a new bounded semantic-retrieval comparator from that merged boundary.

The semantic step must:

```text
reuse the exact frozen RH-S cases
preserve the lexical result as control
measure incremental useful recall
measure irrelevant candidate growth
prefer an exact/in-process comparator before ANN/vector infrastructure
avoid retroactive query changes
```

Only after retrieval-channel evidence is complete should the track advance into frozen RH-R relation expansion and RH-A applicability/context behavior for the first real MethodologicalHorizon.

Primary sources:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```