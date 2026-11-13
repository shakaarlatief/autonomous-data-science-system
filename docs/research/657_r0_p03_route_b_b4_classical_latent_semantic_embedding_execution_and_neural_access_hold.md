# Research 657: Executed classical B4 latent-semantic embeddings and bounded neural-model access HOLD

**Date:** 2026-11-13
**Status:** ACTUAL_CORPUS_TRAINED_DISTRIBUTIONAL_LSA_B4_EXECUTED / NEGATIVE_AGAINST_EXPOSED_B0 / PRETRAINED_NEURAL_B4_UNAVAILABLE / ORIGINAL_FORMAL_P03_UNSCORED
**Scope:** Continue the owner's explicit Path B actual R0-P03 execution mandate. Evaluate whether a genuine dense *latent-semantic* channel, not the previous lexical character trigram, improves discovery when added to existing original-source B0 and B2 navigation. Preserve independence, source-owner and governing authority boundaries.
**Evidence:** Checkpoint 918 original 12 source-grounded coordinator-authored tasks / 60 build / 20 heldout at Git pin `47ed6344a9153dcf366769e95722840fbf1a8f8b`, Checkpoint 919 original B1/B2/B3 implementation and full trace, before-score model contract `ROUTE_B_B4_LOCAL_LSA_EMBEDDING_CONTRACT_V01.md`, original exact full output and 10 dedicated mathematical/lineage/regression tests.
**Checkpoint:** 920. **Validation:** 356.
**Scientific boundary:** No formal Research 513/559/576 B0–B4 architecture selection or independent source/answer gold. No C01/C02 private case content accessed.

## 1. Actual pretrained-model feasibility observations

I checked the authorized Windows Runtime Bridge project environment before choosing the model, rather than assuming packages or cached neural embeddings existed. Python 3.13.1 / `uv 0.12.5` is available, but `sentence_transformers`, `transformers`, `torch`, `onnxruntime`, `fastembed`, `numpy` and `sklearn` were **not installed** in the authorized project virtual environment. That virtual environment also had no `pip`; a separately checked Python 3.11 environment lacked these packages. Hugging Face pretrained model caches were empty. A cached Torch ResNet-18 computer vision weight file is irrelevant to text semantic embedding.

A first `uv` attempt to install `fastembed` in an isolated target could not write the default cache outside the authorized workspace. The next attempt used an explicit project-isolated cache `.venv/.r0_p03_b4_uv_cache` and an isolated target `.venv/.r0_p03_b4_deps`, **without changing project dependencies or permissions**, but failed to fetch PyPI due Windows network socket permission error `10013` (explicit egress denial). No package was installed, no model was downloaded, and no pretrained embedding execution can be asserted. We did not weaken sandbox security to make the experiment appear complete.

The authorized runtime nevertheless supports **classical latent semantic indexing/analysis** using only the Python standard library. We froze its mathematical method and parameters before the first LSA retrieval output. This is a *real corpus-trained distributional semantic factor model*, but not a pretrained neural language/sentence model. It has no external natural-language paraphrase knowledge and cannot establish the quality of a modern neural B4 arm.

## 2. Implemented mathematical mechanism

Inputs are **exactly the same original sixty Git build carrier bodies** from Checkpoint 918. The 20 already-frozen maintenance documents are excluded from model fitting, retrieval and scoring. All training source bytes, source path IDs and SHA-256s were checked against Checkpoint 918, and only the first **12,000 characters** of each source entered both the B0 text comparator and LSA word feature training. Neither the twelve questions nor their target source IDs, reference answers, W5 subjects, new B3 concerns nor prior rankings were included in training.

The LSA pipeline uses the fixed V04 normalized non-stopword tokenization, unique word membership and document-frequency weights:

\[
\mathrm{idf}(w)=1+\log\left(\frac{61}{\mathrm{df}(w)+1}\right).
\]

Each 60-document source row is L2-normalized. For the resulting `X` with 60 documents and **5,084 word features**, compute the actual sparse-postings Gram matrix `G = XX^T` (**60 × 60**, **20,098 nonzero document-word features**, **138,281 postings pair updates**). Learn **16** positive spectral components from a fixed `random.Random(20261113)` initializer and **160 deterministic orthogonalized power iterations** each. This uses **2,560 Gram matrix-vector products**. The largest saved relative eigen-residual is **0.005716**, so it is correctly reported as an approximation rather than falsely described as an exactly converged SVD.

For eigenpair `(u_k, lambda_k)`, source embedding is `u_{d,k} sqrt(lambda_k)`, while query embedding is the training-source overlap projection `(q X^T u_k)/sqrt(lambda_k)`. Ordinary cosine similarity ranks candidates. This is mathematically a truncated latent semantic word-space model: correlations learned across the original source corpus can contribute to similarity even when individual words differ. It is **not** raw string similarity, char trigrams, a hand-authored category map, or a hidden answer-key lookup. All source vectors, twelve original query vectors, model dimensions, training costs, query OOV counts, cosine values and result paths are preserved.

The four frozen routes use the identical original source world and query texts:

1. **B0 original**: untouched original Checkpoint 918 FTS5 source-text ranking.
2. **B4-LSA dense only**: actual learned 16-dimensional corpus-trained word-semantic vector and cosine ranking.
3. **B4-LSA + B0**: two-channel reciprocal rank fusion with dampening 60 and stable path ties, no label-conditioned weights.
4. **B4-LSA + B2**: same dense result fused with the original Checkpoint 919 B2 source-written editorial link ranking (a structurally motivated but non-authoritative example, not the fully verified original B4 governed-link winner).

These are genuine semantic-model executions, but the **formal B4 best-qualified-structured-plus-semantic arm is not yet realized**. A pretrained neural encoder, complete common V03-native relation substrate, equalized source metadata authoring and independent references remain unqualified.

## 3. Actual frozen 12-case results

Original saved source-model output:

    RESULT=experiments/r0_p03_navigation_probe/route_b_b4_local_lsa_embedding_comparison_result_v01.json
    BYTES=154662
    SHA256=59fd12cc78892bf6f97cde88e44fc692729582560011bf81a55f1fc62af0b00f
    SOURCE_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    FIT=60_GIT_ORIGINAL_DOCS_ONLY
    HELDOUT=20_NOT_TOUCHED
    PRIMARY_QUESTIONS=12_IDENTICAL
    MODEL=WORD_TFIDF_LSA16
    PRETRAINED_EMBEDDING_RUN=false

| Executed route | Cited required source@1 | @3 | @5 | @10 | MRR@10 |
| --- | ---: | ---: | ---: | ---: | ---: |
| **B0 original** | **8/12** | 10/12 | 10/12 | 11/12 | **0.761905** |
| LSA-16 semantic cosine only | 3/12 | 7/12 | 7/12 | 10/12 | 0.451389 |
| LSA-16 + B0 RRF | 5/12 | 9/12 | 11/12 | 11/12 | 0.593056 |
| LSA-16 + B2 RRF | 5/12 | 9/12 | 11/12 | 11/12 | 0.593056 |

**The semantic model is weaker than the original lexical baseline on this limited exposed population.** B4-LSA misses both **P01** and **P02** at rank ten; P01 remains absent after both fusion variants. P02's `docs/DECISIONS.md` was B0 rank one but lost in LSA-only and fell to rank **five** after fusion. P03 moves from B0 rank seven to LSA-only rank six and fused rank three, but this improvement does not outweigh the regressions in P01, P02, P05 and P09. All twelve per-arm rankings, full dense scores and actual query vectors remain in the file. No dimension search, model-weight retuning, query rewrite, reference answer correction or source replacement occurred after these results.

This negative result applies to *a classical LSA model trained on just sixty original sources*, and the author had already seen all B0/B1–B3 outcomes. It is **not evidence that pretrained neural embeddings are worse**, nor a fair formal comparison of alternative physical architectures.

## 4. Concrete model and maintenance costs

The LSA fit generates a 5,084-word feature vocabulary, 20,098 sparse source-word nonzeros, 3,600 Gram floating-point entries (3,518 nonzero off-diagonal entries), 2,560 fixed Gram products, 960 stored document latent values and 960 eigenvector values, plus 192 query embedding values. These are operation/representation counts, **not measured elapsed latency or independently recorded manual curation time**. The model uses no external weights, no network runtime and no package installations.

Compare this with the source-cited, exposed B1/B3 authoring of Checkpoint 919 (94 + 78 manual memberships) and just three authentic source-written B2 links. This supports a cautious view: both metadata and latent-semantic approaches can incur nontrivial build effort without improving the particular exposed tasks, while the lexical baseline still misses the very long current-state source. It does **not** prove metadata or embeddings will be generally unhelpful in a larger role-qualified corpus.

## 5. Experimental status and immediate next decision

We have now executed a real **B0 source retrieval**, distinct architecture-shaped **B1/B2/B3** source organization/navigation additions, and one **classical semantic embedding B4-LSA** channel under fixed twelve source-grounded questions, source revision, and 60/20 source membership. The path to executable experiment is therefore no longer merely theoretical.

The original owner-approved Research 513 formal decision still requires: actual common V03-native effect/lineage/authority substrate; source-owned and independently judged B1/B3/B2 annotations; neutral source answers; fair candidate budgets and source completeness; independent nine-case legacy evaluation; held-out metadata assignment F1; zero false-authority assertion gate; and appropriate whole-answer fresh-agent reconstruction. Those remain genuinely unfulfilled, rather than hidden by provisional source-hit@K metrics. Protected C02 evidence HOLD is unchanged.

**Next efficient progress:** qualify the current twelve draft reference answers for *scope and truth* with proportionate independent reviewer where feasible, and run a bounded source-cited full-answer reconstruction evaluation instead of only ranking one source. Alternatively, once a pretrained neural model can be installed through authorized channels and matched source budgets, run a **separately frozen neural B4 attempt** without overwriting these original negative LSA results. Do not turn the current inability to download packages into an indefinite blocker to other R0-P03 tasks.

The physical knowledge architecture, information schema, file layout, CI/CD, branch methods and working procedures all remain open to fundamental change if subsequent evidence supports it.

    R0_P03_RETRIEVAL_B0_B1_B2_B3_CLASSICAL_B4_LSA_EXECUTED=true
    FORMAL_RESEARCH513_SCORE=NONE
    PRETRAINED_NEURAL_B4_RUN=false
    LSA_DENSE_SOURCE_TOP1=3_OF_12
    LSA_DENSE_B0_RRF_TOP1=5_OF_12
    B0_ORIGINAL_TOP1=8_OF_12
    INDEPENDENT_REFERENCE_TRUTH_GOLD=false
    PHYSICAL_ARCHITECTURE_SELECTED=false
