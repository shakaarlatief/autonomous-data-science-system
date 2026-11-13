# Route B: genuine corpus-trained latent-semantic embedding and controlled hybrid, V01

**Date:** 2026-11-13
**Status:** FROZEN BEFORE FIRST LSA-CHANNEL SCORE / EXPLORATORY AND NON-BLIND / ORIGINAL FORMAL R0-P03 UNSCORED
**Rationale:** The owner selected Route B to actually execute the architecture comparison rather than indefinitely improve the reference process. Checkpoint 918 executed twelve original-source primary questions and B0. Checkpoint 919 executed materially different but exposed B1/B2/B3 navigation additions. The remaining missing mechanism is a true semantic vector-space model, not another character n-gram or static keyword relabelling.

## 1. External pretrained-model access assessment, actual observation

At the exact time of this execution, the authorized Windows project environment runs Python 3.13.1 with `uv 0.12.5`, but does not have installed `numpy`, `sklearn`, `torch`, `transformers`, `sentence_transformers`, `onnxruntime`, `fastembed`, or Hugging Face pretrained model weights. The project virtual environment has no `pip`. The separately checked Python 3.11 executable also lacks those packages. An attempted workspace-isolated `uv pip install --target .venv/.r0_p03_b4_deps fastembed>=0.7,<0.9` with an in-workspace cache failed because the authorized Windows sandbox denied its outbound connection to `pypi.org` (Windows socket error 10013); the original default cache attempt was also denied outside the authorized workspace. No package installation succeeded, and neither the repository dependency manifest nor permissions were changed. This is a reproducible **capability HOLD for pretrained neural embedding evaluation**, not a reason to label TF-IDF or character trigrams as neural semantics.

An alternative classical semantic mechanism can run with **Python standard library only**: *latent semantic indexing / latent semantic analysis (LSI/LSA)*, a real model that derives dense semantic-factor coordinates through a low-rank factorization of a word-by-source representation. It is **not pretrained or transformer-based** and may be less semantically powerful, especially for synonyms unseen in the 60 documents. The method and its limits are fixed below before any LSA result exists.

## 2. Exact unchanged prior source/question world

- Original Git source revision `47ed6344a9153dcf366769e95722840fbf1a8f8b`.
- Exact Checkpoint 918 **60** build carrier paths, 20 held-out carrier paths (heldout excluded from embedding training, selection and scoring), **12** coordinator-authored exposed questions, and original source bytes.
- Existing original B0 output **122,682 bytes**, SHA-256 `59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab`.
- Existing Checkpoint 919 B0/B1/B2/B3 comparative trace **92,547 bytes**, SHA-256 `6a2b656432a5b8fbb963b0e8c14220411ed57bbad6127b8a550c05cf93ee0fa2`.
- Exact original model input text is the **first 12,000 Unicode characters** of each source carrier (same as B0 document body). Source metadata, file names, reference answers, author labels, source-required IDs, historical B1 subject labels, and B3 concerns **do not enter the learned semantic space**.
- Each question is embedded as its original plain text. It is not seen by the unsupervised model during fitting or feature/parameter tuning.

## 3. Predeclared mathematical LSA construction

A term `w` is defined by the existing V04 fixed non-stopword tokenization and per-document unique token set, not by character n-grams. Let `D=60` and `df_w` count carrier appearances.

    idf_w = 1 + log((D + 1) / (df_w + 1))

The unnormalized source-word feature is `X[d,w]=idf_w` if `w` occurs in the original 12,000-character source, else zero, then L2-normalize each row to unit norm. This is an **unsupervised vocabulary learned only from 60 source bodies**. Out-of-vocabulary query words are discarded; query known-word IDFs use the same fitted IDF and query row is L2 normalized.

Compute the symmetric **60 x 60** source Gram matrix `G=X X^T` exactly from sparse postings. Compute the leading **16** positive-eigenvalue orthonormal source eigenvectors using deterministic double-orthogonalized power iteration on `G`:

- Random initializer is `random.Random(20261113)` and all source paths/tokens are sorted.
- Exactly **160** power steps per component, with two Gram-Schmidt passes against already selected vectors on every step; recompute Rayleigh quotient after the final step. Stop only on numerical zero, not based on query outcomes.
- Retain up to **16** eigenvectors with positive Rayleigh eigenvalue greater than `1e-10`.
- Persist eigenvalues, per-component normalized residual norms `||G u - lambda u||_2` (do not claim exact SVD convergence if large), original source SHA, fitted vocabulary/term membership counts, original document coordinates and query coordinates.

This is a direct approximation to a rank-16 truncated SVD on the source TF-IDF matrix. For singular values `s_k=sqrt(lambda_k)` and original document left-singular coordinates `u_{d,k}`:

    document_dense[d,k] = s_k * u[d,k]
    query_dense[q,k] = sum_d ((Xq dot Xd) * u[d,k] / s_k)

The query therefore projects into the learned corpus latent space through the original source term co-occurrence structure. Normalize query and doc latent vectors for ordinary **cosine similarity**. If a query has no known terms or zero projection, return an empty ranked list. Return top **10** source paths, with stable path tie-breaking.

No target source or reference answer is used during indexing, eigendecomposition, projection or ranking. The reference source is looked up **only after** the complete method output has been computed.

## 4. Fixed comparison arms and limits

Record **three** navigational outputs on identical source context and original twelve questions:

1. `B0_ORIGINAL`: unchanged saved B0 full-body BM25 top ten.
2. `B4_LSA16_DENSE_ONLY_EXPLORATORY`: genuinely learned 16-dimensional **corpus-trained** latent-semantic cosine retrieval top ten. Not a pretrained neural embedding.
3. `B4_LSA16_B0_RRF_EXPLORATORY`: reciprocal-rank fusion of (1) and (2), fixed K=60, stable ties. This is not a full formal B4 structured-arm combination.

Also preserve a fourth arm `B4_LSA16_B2_RRF_EXPLORATORY` combining the original frozen B2 source-written-link arm with the same dense embedding channel. B2 ties B0 on the exposed original source@1 metric and adds only three genuine original written links, so it is the simplest concrete structured exemplar currently available. This is an exploratory approximation, **not** qualification of B4 = best fair B1–B3 with complete historical governing links. Do not change this arm choice after observing B4 outputs.

For every one of twelve questions, persist each top ten original source path, dense cosine score, required-source rank after ranking, original source hash, any query OOV count, and nearest-neighbor evidence. Report hit@1/@3/@5/@10, MRR@10, unchanged B0 baseline results and word-model dimensionality/cost. **No result-driven tuning:** fixed rank=16, 160 iterations, no inverse-document-frequency/term cutoff change, no iterative reranking, and no source-label augmentation after results.

Technical distinction: unlike a pretrained embedding model, LSA can recover correlation between word terms through **within-corpus** co-occurrence but has no external world-language semantics, and may fail on natural paraphrases. It is a genuine *dense latent-semantic* model in the classical IR sense, not direct literal character overlap. Nevertheless the exact original B4 arm and its implementation-effort parity remain **UNQUALIFIED** under Research 513 Section 6.3.

## 5. Scientific safeguards

- The same coordinator has seen B0 and B1/B2/B3 results and source-specific reference labels: **not blind**; the 12 questions/answers are exposed coordinator-created and not complete independently adjudicated answer gold.
- The 60/20 source frame is a provisional source-role/path sample and common V03-native relation substrate remains incomplete.
- No inference of real governing, deployed, accepted or current operative authority is made from text similarity, metadata or retrieved file Status.
- No nine-case independently neutralized legacy packet, no source-owner authenticated B1/B3 metadata, no heldout assignment F1, no post-result answer patch, no full answer reconstruction PASS and **no formal R0-P03 B0–B4 score**.
- The executable and complete original JSON result are exclusive-created, model method/parameters/provenance documented, and exact saved result must be re-executed in focused deterministic tests. Preserve the original JSON bytes with Git `-text`.
- A future qualified pretrained neural B4 remains welcome if weights/compute/permissions can be obtained through normal authorized means without silently changing baseline budgets.

    B4_SEMANTIC_MODEL=CLASSICAL_LSA_RANK16_CORPUS_TRAINED
    PRETRAINED_NEURAL_MODEL=UNAVAILABLE_IN_AUTHORIZED_RUNTIME
    FIT_ORIGINAL_BUILD_SOURCES=60
    HELDOUT_EXCLUDED=20
    QUERY_COUNT=12
    SOURCE_CHARS_PER_DOCUMENT=12000
    LSA_STEPS_PER_COMPONENT=160
    COMPARISON_K=10
    RRF_CONSTANT=60
    OWNER_SELECTED_ARCHITECTURE=false
    FORMAL_R0_P03_SCORE=NONE
