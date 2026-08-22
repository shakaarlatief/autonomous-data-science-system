# Checkpoint 134: Retrieval and MethodologicalHorizon Benchmark Contract Frozen

**Date:** 2026-08-22  
**Status:** Historical experiment-design checkpoint; Specification 009 v0.1 frozen before production lexical implementation  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the production retrieval reconnaissance and freezes the first Q-044/Q-045 lexical retrieval / MethodologicalHorizon evaluation contract before implementation.  
**Authority:** Historical provenance for the preregistered boundary. Specification 009 v0.1 governs the first lexical implementation/evaluation until explicitly revised after its evidence is preserved.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Boundary reached

The runtime bakeoff is merged into the promoted V1 integration branch and D-032 is accepted. The next bounded branch is:

```text
v1-methodological-horizon
```

Repository reconnaissance confirms that production V1 currently contains governed reusable-knowledge persistence/interchange but no application retrieval port, production FTS5 index, MethodologicalHorizon builder, or context assembler.

This makes Q-044/Q-045 the next legitimate implementation track rather than an extension of the runtime bakeoff.

---

## 2. Benchmark frozen before implementation

Research 016 and Specification 009 v0.1 now separate:

```text
RH-L
    lexical-addressable retrieval

RH-S
    semantic/paraphrase retrieval diagnostics

RH-R
    relational horizon expansion

RH-A
    applicability / required-context behavior

RH-C
    selective context construction
```

The first implementation gate is only RH-L plus RH-S diagnostics and the retrieval invariants.

The ten RH-L query/required-key pairs and four RH-S paraphrase queries are frozen before production retrieval code is added.

---

## 3. Lexical acceptance envelope

The first production lexical adapter must satisfy:

```text
RH-L required-key Recall@3 = 1.00
critical lexical omissions = 0 / 10
```

and prove:

```text
accepted-current-only indexing
exact revision transparency
deterministic rebuild
bounded results
blank/punctuation query safety
authoritative-state isolation
storage-specific FTS isolation
existing persistence compatibility
Ubuntu + Windows execution
RH-S diagnostic preservation
```

RH-S is intentionally non-gating for the lexical baseline. Its misses are evidence for whether a semantic candidate can add value.

---

## 4. Frozen architecture boundary

The implementation must use:

```text
storage-neutral application retrieval port
    -> SQLite FTS5 adapter
        -> rebuildable derived index
```

The index contains one row per current accepted KnowledgeAsset revision and returns the exact revision ID.

The first baseline does not use:

```text
LLM query rewriting
embedding retrieval
vector database
ANN
fusion
reranking
```

The initial weighted lexical fields and BM25 weights are fixed by Specification 009 before the gate.

---

## 5. Knowledge fixture governance

The existing stress corpus remains a `BENCHMARK_FIXTURE` and is not promoted into accepted authority.

The benchmark may use an isolated deep copy converted to `CANDIDATE_SET`, then exercise the normal candidate import and explicit acceptance path inside a temporary test database. Semantic payloads and identities remain unchanged.

This preserves the governance invariant that benchmark material does not silently become accepted methodological knowledge.

---

## 6. Promotion audit

Promote now:

```text
Research 016
    detailed current retrieval/Horizon benchmark reasoning

Specification 009 v0.1
    frozen first lexical evaluation contract
```

Do not promote any semantic retrieval technology or final HorizonBuilder algorithm.

No new Foundation is required. Foundations 019-020 already define the durable conceptual separation between retrieval, applicability, relevance, and selective context.

---

## 7. Exact continuation

Proceed directly to the frozen lexical implementation:

```text
1. add deterministic benchmark scenario fixture
2. add application KnowledgeRetrievalPort / hit DTO
3. add rebuildable SQLite FTS5 accepted-current adapter
4. execute RH-L + RH-S and RL-01..RL-10
5. preserve a complete lexical result artifact
6. only then decide whether semantic retrieval earns implementation
```

Do not alter RH-L/RH-S cases to fit observed results before the first result boundary is preserved.

Primary sources:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
```