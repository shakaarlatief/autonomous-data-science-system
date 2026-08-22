# Research 018: Dense Semantic Failure, Complementarity, and RRF Fusion Rationale

**Date:** 2026-08-22  
**Status:** Current bounded retrieval research  
**Scope:** Interprets the completed Specification 010 dense-only result and decides whether one fusion experiment is justified. It does not promote a production embedding model, vector database, ANN index, reranker, or final MethodologicalHorizon ranker.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Evidence now available

The production lexical baseline and exact dense comparator have been evaluated against the same frozen RH-S/RH-L cases.

Lexical control, Checkpoint 135:

```text
RH-L Recall@3  1.00
RH-L MRR       1.00
RH-S Recall@3  0.75
RH-S MRR       0.75
```

Dense candidate, Specification 010 / run `32560811584`:

```text
RH-L semantic Recall@3  1.00
RH-L semantic MRR       1.00
RH-S Recall@3           0.75
RH-S MRR                0.75
```

The aggregate semantic metric does not improve. The per-case error structure does.

---

## 2. The important result is complementary error, not aggregate gain

The two channels fail different frozen cases:

```text
                    Lexical          Dense
RH-S01 imbalance    MISS             rank 1
RH-S02 eligibility  rank 1           rank 1
RH-S03 temporal     rank 1           rank 1
RH-S04 ECDF         rank 1           MISS
```

This means the dense channel did exactly one thing the lexical channel could not do, but simultaneously lost one case lexical handled correctly.

Therefore the evidence rejects two simplistic conclusions:

```text
"dense is better, replace lexical"      FALSE
"dense adds no value, discard it"       TOO STRONG
```

The supported interpretation is:

```text
the channels contain complementary retrieval signal
```

That is the specific empirical condition under which Specification 009 allowed fusion to become decision-relevant.

---

## 3. Why not tune dense retrieval first

Several changes could be made to force the dense channel closer to a pass:

```text
change model
change passage projection
add query instructions
increase top-k
change similarity threshold
rewrite semantic cue text
```

None should happen before testing the already-observed complementarity.

The current result is more informative if left intact. The model is not globally weak: all ten RH-L targets are rank 1 and three of four RH-S targets are rank 1. The miss is a ranking disagreement, not evidence that the embedding stack is unusable.

Tuning now would increase researcher degrees of freedom and weaken the value of the frozen benchmark.

---

## 4. Why score interpolation is not the first fusion method

The lexical channel emits weighted BM25-derived scores while the dense channel emits cosine similarities.

Those score scales have different meanings and ranges. A formula such as:

```text
alpha * lexical_score + (1 - alpha) * cosine_score
```

would immediately introduce:

```text
score normalization choices
alpha tuning
scale sensitivity
benchmark-specific calibration risk
```

The current corpus is too small to justify fitting such parameters.

The first fusion comparator should therefore be rank based.

---

## 5. Reciprocal Rank Fusion is the smallest useful comparator

For a candidate document `d`, Reciprocal Rank Fusion uses only its rank in each channel:

```text
RRF(d) = sum_c 1 / (k + rank_c(d))
```

where a document absent from a channel's retained candidate list contributes zero for that channel.

Advantages for this experiment:

```text
score-scale independent
no learned weights
no model fitting
no query-specific branching
deterministic
works directly on existing top-k outputs
small implementation surface
preserves independent lexical and dense channels
```

Freeze:

```text
channels      lexical + dense
channel depth 3 each
RRF k         60
final top-k   3
weights       equal
```

`k=60` is a conventional dampening constant and, more importantly here, avoids introducing a fitted parameter. The experiment is not intended to prove 60 is globally optimal.

---

## 6. What fusion must prove

The purpose is not merely to create a union containing the answer somewhere.

The fused ranking must satisfy the same bounded retrieval interface:

```text
final top 3 only
```

Primary semantic requirement:

```text
RH-S Recall@3              = 1.00
RH-S critical omissions    = 0 / 4
RH-S MRR                   > 0.75
```

No-regression lexical requirement:

```text
RH-L Recall@3              = 1.00
RH-L MRR                   = 1.00
```

Specific complementarity sentinels:

```text
RH-S01 must retain class-imbalance
RH-S04 must retain ecdf
```

This prevents the fused result from hiding a swap of one omission for another.

---

## 7. Candidate-growth evidence should be measured

For every query record:

```text
lexical top-3 identities
dense top-3 identities
union size
fused top-3 identities
whether the target was lexical-only, dense-only, both, or absent
```

This matters because MethodologicalHorizon construction is not only about recall. Candidate growth affects downstream ranking/context cost.

The internal lexical+dense union may contain more than three items, but the first fused retrieval output remains hard-bounded to three.

---

## 8. Cross-platform fixture identity correction

Specification 010 exposed a reproducibility detail unrelated to retrieval quality: raw SHA-256 over checked-out JSON bytes differed between Ubuntu and Windows, while parsed content and ranking identities were identical.

Future comparator records should use a canonical semantic digest such as:

```text
json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
```

hashed as UTF-8.

This avoids treating line-ending normalization as knowledge-content drift.

---

## 9. Interpretation after fusion

### If RRF fails

Do not tune RRF parameters immediately.

At that point the simple hybrid hypothesis has failed on the frozen corpus. A second embedding candidate or more sophisticated reranking should be considered only if the remaining omission is important enough to justify additional complexity.

### If RRF passes

The supported conclusion is narrow:

```text
lexical + semantic hybrid retrieval earns retention as the leading V1 retrieval hypothesis
```

That would still not select:

```text
FastEmbed permanently
BGE permanently
vector persistence
ANN
vector database
cross-encoder reranking
final semantic threshold
final fusion algorithm at larger scale
```

The next step would be to define the smallest production hybrid seam compatible with D-028, then proceed into RH-R/RH-A MethodologicalHorizon construction.

---

## 10. Decision

A single preregistered RRF comparator is justified.

This decision is based on observed complementary retrieval errors, not on a general preference for hybrid search.

Primary evidence:

```text
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
experiments/retrieval/V1_EXACT_SEMANTIC_RETRIEVAL_RESULT.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
```
