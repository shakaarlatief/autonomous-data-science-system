# Validation 356: Actual original-source LSA latent semantic retrieval, fixed-source controls and exact replay

**Date:** 2026-11-13
**Status:** LSA16_CLASSICAL_SEMANTIC_MODEL_EXECUTED / FULL_ORIGINAL_SOURCE_OUTPUT_SAVED / DEDICATED_TESTS_PASS / REPOSITORY_POSTFLIGHT_PENDING
**Research:** Research 657. **Checkpoint:** 920.
**Source:** Checkpoint 918 frozen original Git B0 and Checkpoint 919 frozen B1/B2/B3 source comparison, no original model or source changes.

## Actual executable observations

The authorized Windows project venv has `uv` but no `fastembed`, `sentence_transformers`, `torch`, `onnxruntime`, `transformers`, `numpy`, `sklearn` or cached text model. The project venv does not contain `pip`; local isolated install initially failed cache access and then a corrected in-workspace `uv` cache/target failed outbound PyPI fetch with Windows socket permission error 10013. No dependency manifest or sandbox policy was changed and no pretrained neural embedding result exists.

Wrote the classical LSA-16 mathematical method contract **before the first model result**, then wrote and ran the pure-standard-library implementation against original 60-source Git build bytes. The first actual run succeeded and exclusively created `route_b_b4_local_lsa_embedding_comparison_result_v01.json`.

    SOURCE_GIT_REVISION=47ed6344a9153dcf366769e95722840fbf1a8f8b
    B0_RESULT_SHA256=59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab
    B123_RESULT_SHA256=6a2b656432a5b8fbb963b0e8c14220411ed57bbad6127b8a550c05cf93ee0fa2
    SEMANTIC=UNSUPERVISED_CLASSICAL_WORD_LSA_DIM16
    DOCS_FIT=60
    DOCS_HELDOUT_EXCLUDED=20
    QUERY_CASES=12
    SOURCE_INPUT_CHARACTER_CAP=12000
    VOCAB_SIZE=5084
    DOC_FEATURE_NONZEROS=20098
    GRAM_SOURCE_DIM=60x60
    FIXED_EIGEN_ITERATIONS_PER_COMPONENT=160
    EIGEN_COMPONENTS_LEARNED=16
    MAX_RELATIVE_EIGEN_RESIDUAL=0.005715826710617903
    RESULT_BYTES=154662
    RESULT_SHA256=59fd12cc78892bf6f97cde88e44fc692729582560011bf81a55f1fc62af0b00f
    DENSE_SOURCE_TOP1=3_OF_12
    DENSE_SOURCE_TOP10=10_OF_12
    DENSE_PLUS_B0_TOP1=5_OF_12
    DENSE_PLUS_B0_TOP10=11_OF_12
    SOURCE_GOLD_INDEPENDENT=false
    PRETRAINED_B4_RUN=false
    FORMAL_R0_P03_SCORE=NONE

All per-case original source inputs, full source SHA, 16-dimensional source and query embeddings, spectral model residuals, exact cosine top-ten candidates and actual B0/B2 RRF rankings are preserved. P01 and P02 are missed by the standalone semantic channel; only P01 by either combined channel.

## Dedicated actual checks

`tests/unit/test_r0_p03_route_b_b4_local_lsa_embedding_v01.py`: **10/10 PASS** (1.55s). Tests cover exact immutable B0/B123 parent bytes, original 60 build source and 20 heldout exclusion, 16-dimensional corpus-trained model with 5,084 word IDF features, exact source Git SHA and stored dense vectors, positive spectral factors and measured residuals, spectral decomposition against synthetic independent diagonal matrix, vector orthogonality and cosine, word OOV/known-word projection, correct projection into learned distributional subspace, actual negative B4 results and unchanged B0 rankings, full exact saved 154,662-byte model rerun and explicit absence of pretrained neural and formal governance claims.

## Observed precommit regressions and repository qualification

The following nonoverlapping selected suites **actually executed**, each using unique `--basetemp`, Python `-B` and pytest cache disabled:

| Test scope | Verified result |
| --- | --- |
| New classical 16-dimensional LSA semantic model, spectral/OOV/projection checks, exact Git source and full result replay | **10/10 PASS** (1.43s on latest run) |
| Previous Route B twelve-primary-question B0 corpus/source/answer evidence and exact replay | **9/9 PASS** (0.62s) |
| Previous B1/B2/B3 source-adjacent annotation and original source-written links/complete results | **10/10 PASS** (0.80s) |
| Previous original Git event and externally reported CI workflow/job/step witnesses | **7/7 PASS** (4.18s) |
| Previous T2 V04 no-ID 64-case decision navigation comparison | **9/9 PASS** (0.53s) |
| Native Specification025/028 reference grammar and model collaboration identity/state | **41/41 PASS** (7.75s) |
| Previous T2 V03 two-Git-snapshot decision/temporal status and exact original source | **9/9 PASS** (0.37s) |
| Previous T2 V02 original-source subject identity and unsupported authority abstention | **10/10 PASS** (0.86s) |
| Protected C02 aggregate identities and historical independent reviewer evidence boundaries | **15/15 PASS** (0.20s) |
| Previous T2 V01 status/heading/negative controls | **3/3 PASS** (0.14s) |
| Previous T2 V01 original 120-source Git roster and selected case reconstruction | **2/2 PASS** (27.23s) |
| Previous T2 V01 full original Git-source result replay | **1/1 PASS** (14.82s) |
| Previous T2 V01 failed ranks and saved negative cases | **2/2 PASS** (0.11s) |
| **Selected actually observed nonoverlapping test cases** | **128/128 PASS** |

Repository gates were also observed:
- `scripts/check_current_routing.py`: **PASS**, checkpoint **920**, branch `v1-source-vault-bootstrap-resume`, boundary `p-three-route-b-latent-semantic-model-executed`, original formal R0-P03 outcome **INCOMPLETE**.
- `scripts/check_knowledge_map.py`: **PASS**, Research **657**, **921** canonical numbered checkpoint records and 19 topic groups.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **921/921** numbered checkpoints compliant.
- `git check-attr text` for the exact 154,662-byte original model/result JSON: **unset**, preserving bytes under Git/Windows line-ending conversion.
- `git diff --check`: exit **0**, with routine tracked-text LF/CRLF warnings only.
- Result bytes SHA-256: **PASS**, exact `59fd12cc78892bf6f97cde88e44fc692729582560011bf81a55f1fc62af0b00f`; dedicated tests independently reexecute the entire saved LSA model and compare the full JSON, not just summary numbers.
- An initial concurrent invocation of the full integrity script timed out at the remote command's hard 30-second limit; **it is not counted as a pass**. Retried separately under the same original inputs with no code or result change: `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume` returned **`PUBLIC_REPOSITORY_INTEGRITY=PASS`**, with family-aware repository contracts, Project Knowledge, checkpoint, Knowledge Map, model collaboration and routing checks each PASS.

No dependency installation was successful and no sandbox permissions were altered. The result is a real corpus-trained LSA embedding, but not a neural pretrained model or formal fair B4 architecture arm. The full report and result retain the weaknesses and negative scores.

**Publication and postflight not yet claimed here.** Committed original result bytes, exact remote HEAD, push and clean working tree require separate observed operations, not inference from these precommit tests.

## Scientific scope

Classical unsupervised word-space LSA is a real dense semantic factor model, but **not pretrained neural text embeddings** and not a complete formally qualified B4 architectural arm. Query author and evaluator knew prior B0/B1–B3 results. The common substrate and independent source/answer evidence remain inadequate for Research 513 formal thresholds. No protected C01/C02 task data was accessed or mutated, and the source-owner status HOLDs remain unchanged.
