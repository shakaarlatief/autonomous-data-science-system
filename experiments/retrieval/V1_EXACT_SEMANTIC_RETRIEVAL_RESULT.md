# V1 Exact Semantic Retrieval Comparator Result

**Date:** 2026-08-22  
**Status:** COMPLETE RESULT, PRIMARY DENSE-ONLY GATE FAILED  
**Specification:** `docs/specifications/010_v1_exact_semantic_retrieval_comparator.md` v0.1  
**Validated source head:** `47e4913d159aa365aad74dbdcf94281055d7d5ba`  
**GitHub Actions workflow:** `V1 semantic retrieval comparator`  
**Run:** `32560811584`

## 1. Candidate

```text
fastembed==0.8.0
BAAI/bge-small-en-v1.5
384 dimensions
query_embed / passage_embed
exact normalized cosine search
corpus size 10
top_k 3
```

FastEmbed remained an experiment-only dependency. The normal locked V1 test suite was executed separately without the semantic candidate dependency.

## 2. Cross-platform outcome

```text
Ubuntu dense comparator          FAIL primary RH-S gate
Ubuntu locked V1 regression      PASS, 38 passed / 2 skipped

Windows dense comparator         FAIL primary RH-S gate
Windows locked V1 regression     PASS, 38 passed / 2 skipped
```

The failure is an evaluation result, not an execution or portability failure. Both platforms produced the same ordered top-three identities for every RH-S and RH-L case, with only small floating-point score differences.

## 3. Dense-channel retrieval quality

```text
RH-L semantic Recall@3     1.00
RH-L semantic MRR          1.00

RH-S Recall@3              0.75
RH-S MRR                   0.75
RH-S critical omissions    1 / 4
```

The frozen primary acceptance envelope required:

```text
RH-S Recall@3              1.00
RH-S critical omissions    0 / 4
RH-S MRR                   > 0.75
```

The candidate therefore fails Specification 010 as a standalone semantic retrieval channel.

## 4. RH-S case result

```text
RH-S01
query:
    positive cases are scarce and overall correctness hides failures on them
expected:
    class-imbalance
result:
    rank 1
interpretation:
    dense retrieval closes the lexical baseline's only semantic miss

RH-S02
expected:
    prediction-time-feature-eligibility
result:
    rank 1

RH-S03
expected:
    temporal-validation
result:
    rank 1

RH-S04
query:
    show how a numeric variable accumulates across its range without choosing buckets
expected:
    ecdf
result:
    absent from dense top 3
    top 3 = random-forest, bagging, histogram
interpretation:
    dense retrieval introduces a different semantic omission on a case the lexical channel solved at rank 1
```

## 5. Complementarity against the lexical control

Checkpoint 135 preserved:

```text
Lexical RH-S Recall@3  0.75
Lexical RH-S MRR       0.75

RH-S01 class-imbalance  MISS
RH-S04 ecdf             rank 1
```

The dense comparator produces:

```text
Dense RH-S Recall@3    0.75
Dense RH-S MRR         0.75

RH-S01 class-imbalance  rank 1
RH-S04 ecdf             MISS
```

Therefore:

```text
lexical alone != sufficient on frozen semantic cases
dense alone   != sufficient on frozen semantic cases
lexical and dense errors are complementary
```

This is positive evidence for testing a bounded fusion method. It is not evidence for replacing FTS5 with dense retrieval.

## 6. RH-L diagnostic

The dense model returned every frozen lexical target at rank 1:

```text
RH-L01 missing-data                         rank 1
RH-L02 class-imbalance                      rank 1
RH-L03 temporal-validation                  rank 1
RH-L04 prediction-time-feature-eligibility  rank 1
RH-L05 ecdf                                 rank 1
RH-L06 histogram                            rank 1
RH-L07 random-forest                        rank 1
RH-L08 gradient-boosted-trees               rank 1
RH-L09 bagging                              rank 1
RH-L10 prediction-moment                    rank 1
```

This rules out the interpretation that the model is broadly poor on the current knowledge corpus. The failure is specifically about ranking one paraphrase target outside top three.

## 7. Operational evidence

Both platforms successfully:

```text
resolved fastembed 0.8.0 ephemerally
used CPU ONNX Runtime
fetched the BGE model from Hugging Face
embedded all 10 passages
executed all RH-S and RH-L queries
```

Approximate hosted-run telemetry:

```text
Ubuntu
    model initialization  ~2.14 s
    corpus embedding      ~1.05 s
    RH-S query total      ~0.17 s
    RH-L query total      ~0.32 s

Windows
    model initialization  ~3.26 s
    corpus embedding      ~0.98 s
    RH-S query total      ~0.25 s
    RH-L query total      ~0.55 s
```

Timing is descriptive only.

The model fetch occurred through unauthenticated Hugging Face Hub requests. This remains visible operational state and is not hidden or vendored into the repository.

## 8. Reproducibility finding: raw byte hashes are platform-sensitive

The comparator initially recorded SHA-256 over raw checked-out fixture bytes. Ubuntu and Windows produced different raw-byte hashes despite identical parsed JSON semantics and identical ranking identities. This is consistent with checkout line-ending normalization.

Therefore raw working-tree bytes are not a suitable cross-platform semantic fixture identity for this experiment.

Future retrieval comparators should record a deterministic canonical-JSON digest, or a Git blob identity, rather than interpreting platform-dependent working-tree byte hashes as semantic-content differences.

This finding does not invalidate the retrieval result because:

```text
parsed fixture content was equivalent
case identifiers and targets were unchanged
ordered retrieval identities matched across platforms
all evaluation metrics matched exactly
```

## 9. Decision

Do not promote dense retrieval as a replacement for lexical retrieval.

Do not tune the model, rewrite RH-S04, increase top-k, or change the passage projection to force a pass.

The measured complementary error pattern is sufficient to justify the next bounded experiment:

```text
production lexical top 3
+ exact dense top 3
-> score-scale-independent rank fusion
-> frozen RH-S and RH-L evaluation
```

No production embedding dependency, vector database, ANN index, reranker, or final fusion architecture is selected by this result.
