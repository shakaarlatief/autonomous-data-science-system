# V1 Production Lexical Retrieval Result

**Status:** PASS  
**Date:** 2026-08-22  
**Specification:** `docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md` v0.1  
**Source branch:** `v1-methodological-horizon`  
**Validated source head:** `c462365bf64ebe9d676a0d9ce6402bba61e67279`  
**Workflow:** `V1 methodological horizon`  
**Final observable run:** `32559177057`  
**Scope:** First production accepted-current SQLite FTS5 reusable-knowledge retrieval baseline. This result does not validate semantic retrieval, fusion, reranking, full MethodologicalHorizon construction, applicability reasoning, recommendation quality, or selective LLM context assembly.

## 1. Result summary

The preregistered lexical baseline passed its complete RH-L acceptance envelope on both Ubuntu and Windows.

```text
Indexed current accepted assets     10
RH-L required-key Recall@3          1.00
RH-L MRR                            1.00
RH-L critical omissions             0 / 10
Required RH-L target ranked #1      10 / 10
RH-S diagnostic Recall@3            0.75
```

Cross-platform result:

```text
Ubuntu
    frozen lexical benchmark        PASS
    existing V1 Python suite        PASS
    38 passed, 2 skipped

Windows
    frozen lexical benchmark        PASS
    existing V1 Python suite        PASS
    38 passed, 2 skipped
```

The two skipped tests in each broad regression run are the existing PostgreSQL integration cases that require `ADS_TEST_POSTGRES_URL`. PostgreSQL persistence/interchange remains independently validated by its dedicated gates. This retrieval result makes no claim about a PostgreSQL lexical adapter.

The benchmark output was identical across Ubuntu and Windows.

---

## 2. Frozen RH-L lexical-addressable cases

All ten preregistered required assets were returned at rank 1.

### RH-L01

```text
Query:
missing values imputation missing labels

1. missing-data
   revision cfefb760-e70a-4b1a-bb6a-3393334b70fa
   score 12.51949753
```

### RH-L02

```text
Query:
minority class rare event class prevalence

1. class-imbalance
   revision f30b1304-f5c0-4070-9f21-dc27945d866f
   score 16.46335013
```

### RH-L03

```text
Query:
rolling origin chronological split temporal validation

1. temporal-validation
   revision a952de3e-d761-4cab-9318-91b2f25f3231
   score 20.04621206
```

### RH-L04

```text
Query:
feature leakage prediction time feature eligibility

1. prediction-time-feature-eligibility
   revision 8b63f2cd-a1b7-4b2c-939b-5b146c5d7477
   score 11.82270895

2. prediction-moment
   revision 4a3189bb-b007-4efd-a2bd-04a8cc6a4d5c
   score 2.30559022

3. missing-data
   revision cfefb760-e70a-4b1a-bb6a-3393334b70fa
   score 1.50437495
```

### RH-L05

```text
Query:
empirical cumulative distribution ECDF without bins

1. ecdf
   revision 9b6b4a84-526f-4fba-9036-13ad3cc00896
   score 17.39375473

2. histogram
   revision a5035424-0d67-4dfc-9491-dc73df2601ce
   score 5.68882827
```

### RH-L06

```text
Query:
histogram bins quantitative distribution

1. histogram
   revision a5035424-0d67-4dfc-9491-dc73df2601ce
   score 10.35032679

2. ecdf
   revision 9b6b4a84-526f-4fba-9036-13ad3cc00896
   score 5.50874230
```

### RH-L07

```text
Query:
random forest randomized tree ensemble

1. random-forest
   revision fefb0b89-52b5-4353-9eb0-331670c9211c
   score 15.10906979

2. gradient-boosted-trees
   revision 1b9604fc-6cdb-4ff5-b4de-7aafaa157d89
   score 3.94714258
```

### RH-L08

```text
Query:
gradient boosting boosted trees sequential

1. gradient-boosted-trees
   revision 1b9604fc-6cdb-4ff5-b4de-7aafaa157d89
   score 17.00995226

2. random-forest
   revision fefb0b89-52b5-4353-9eb0-331670c9211c
   score 2.07189884
```

### RH-L09

```text
Query:
bootstrap aggregation bagging learners

1. bagging
   revision f0341774-efbb-48a7-b3c7-94820857c7e8
   score 13.10688615

2. random-forest
   revision fefb0b89-52b5-4353-9eb0-331670c9211c
   score 2.17200074
```

### RH-L10

```text
Query:
scoring time prediction moment cutoff

1. prediction-moment
   revision 4a3189bb-b007-4efd-a2bd-04a8cc6a4d5c
   score 7.52739352

2. prediction-time-feature-eligibility
   revision 8b63f2cd-a1b7-4b2c-939b-5b146c5d7477
   score 5.24019866

3. temporal-validation
   revision a952de3e-d761-4cab-9318-91b2f25f3231
   score 1.34701129
```

The observed result is stronger than the frozen minimum `Recall@3 = 1.00`: every lexical-addressable target is rank 1, yielding `MRR = 1.00`.

---

## 3. Frozen RH-S semantic/paraphrase diagnostics

RH-S was deliberately non-gating for the lexical baseline.

Observed diagnostic result:

```text
Target recovered in top 3     3 / 4
RH-S Recall@3                  0.75
```

### RH-S01

```text
Query:
positive cases are scarce and overall correctness hides failures on them

Target:
class-imbalance

Result:
NO HITS
```

This is the cleanest measured semantic gap in the current corpus. The query expresses class-imbalance/evaluation meaning but has insufficient lexical overlap with the current accepted document projection.

### RH-S02

```text
Query:
the value is unavailable until after the score has already been produced

1. prediction-time-feature-eligibility
   score 2.22716037

2. histogram
   score 1.75794916
```

Target recovered at rank 1.

### RH-S03

```text
Query:
evaluate a model as if each forecast were made using only earlier observations

1. temporal-validation
   score 6.28602673

2. prediction-time-feature-eligibility
   score 1.53433365

3. gradient-boosted-trees
   score 1.42938526
```

Target recovered at rank 1.

### RH-S04

```text
Query:
show how a numeric variable accumulates across its range without choosing buckets

1. ecdf
   score 6.07618199

2. histogram
   score 1.75794916
```

Target recovered at rank 1.

The semantic candidate is therefore decision-relevant, but it is not preselected. The measured question is whether a semantic channel can recover RH-S01 and improve future semantic cases without materially increasing irrelevant candidate/context volume.

---

## 4. Retrieval invariants

Specification 009 RL-01 through RL-10 passed for the current lexical slice.

```text
RL-01  PASS  accepted-current-only indexing
RL-02  PASS  exact accepted revision identity returned
RL-03  PASS  deterministic rebuild and ordered identities
RL-04  PASS  bounded positive limit
RL-05  PASS  blank/whitespace/punctuation query safety
RL-06  PASS  authoritative semantic snapshot unchanged by rebuild/search
RL-07  PASS  FTS5 details remain below the application retrieval port
RL-08  PASS  existing V1 Python regression suite remains green
RL-09  PASS  Ubuntu + Windows execution
RL-10  PASS  all frozen RH-S diagnostics executed and observed
```

The test additionally advances Random Forest to a new accepted revision, rebuilds the derived index, and proves:

```text
historical accepted R1 remains durable in authoritative history
current accepted pointer advances to R2
retrieval returns R2
retrieval no longer returns R1 as current
```

This directly validates the accepted-current retrieval boundary rather than only testing a static corpus.

---

## 5. First validation attempt and diagnostic correction

The first pull-request workflow run was:

```text
32559023163
```

On both operating systems:

```text
frozen lexical benchmark   PASS
broad regression step      FAIL during collection
```

The failure was not caused by the retrieval implementation.

The new workflow invoked:

```text
pytest tests -q
```

while the already-validated runtime workflow uses:

```text
python -m pytest -q
```

The bare `pytest` entry-point did not place the repository root on `sys.path` in the same way, so existing runtime-bakeoff tests failed to import the repository-local `experiments` package:

```text
ModuleNotFoundError: No module named 'experiments'
```

The correction changed only the CI invocation to `python -m pytest`. No frozen benchmark query, required key, ranking weight, retrieval projection, or production behavior changed.

Corrected cross-platform run:

```text
32559082914
Ubuntu PASS
Windows PASS
```

Final observable run after adding benchmark metric output only:

```text
32559177057
Ubuntu PASS
Windows PASS
```

This history is preserved because it distinguishes a workflow-environment defect from a retrieval-quality failure.

---

## 6. Architectural conclusion

The first production lexical retrieval slice is successful for what it was designed to prove:

```text
accepted governed knowledge
    -> rebuildable FTS5 projection
    -> storage-neutral application retrieval port
    -> exact revision-transparent top-k lexical candidates
```

The result does not justify treating lexical search as sufficient for the final MethodologicalHorizon architecture.

It does establish a strong minimum-dependency baseline:

```text
lexical-addressable cases
    perfect top-three recall
    perfect MRR on the frozen corpus

semantic/paraphrase cases
    useful but incomplete coverage
    one clean total miss
```

The next comparator should therefore target the measured semantic gap rather than replacing a lexical channel that already performs strongly on its intended slice.

---

## 7. Exact continuation

Before adding semantic retrieval code:

1. preserve this result through a checkpoint and current routing reconciliation;
2. merge the independently validated lexical slice into the promoted V1 integration branch;
3. create a new bounded semantic-retrieval branch from that merged boundary;
4. compare semantic options against the unchanged RH-S cases and the lexical baseline;
5. prefer an exact/in-process semantic comparator first unless evidence requires ANN/vector infrastructure;
6. evaluate candidate growth as well as recall;
7. introduce fusion only if lexical and semantic channels provide complementary useful retrieval;
8. begin RH-R/RH-A MethodologicalHorizon construction only after retrieval-channel evidence is preserved.

Do not modify the frozen RH-L/RH-S queries retroactively to improve results.