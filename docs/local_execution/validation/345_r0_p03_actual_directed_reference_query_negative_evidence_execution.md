# Validation 345: Executed 130-question bidirectional reference and negative-evidence test

**Date:** 2026-11-12
**Status:** ACTUAL_130_SOURCE_REFERENCE_TASKS_EXECUTED / EXACT_RESULT_AND_K_LIMIT_VERIFIED / NO_FORMAL_P03_SELECTION
**Scope:** Validate the actual finite source-derived directed-reference experiment and distinguish index self-consistency from independent original-source truth or authority.
**Authority:** Frozen new directed-reference source-only experiment contract, real executed output and predecessor Checkpoint 908; Research 646, Checkpoint 909.

## Actual saved source-grounded output

    EXECUTED_PROGRAM=experiments/r0_p03_navigation_probe/exploratory_directed_relation_retrieval_v01.py
    SAVED_FILE=experiments/r0_p03_navigation_probe/exploratory_directed_relation_retrieval_result_v01.json
    EXACT_RESULT_BYTES=1692786
    EXACT_RESULT_SHA256=99206720df7dfa6deb788f4abd8428137a55f5ee68962e83f08da79a7775c399
    SOURCE_GIT_REVISION=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    SOURCE_DOCUMENTS=65
    OUTBOUND_REFERENCES=110
    INBOUND_REFERENCES=110
    ALL_130_TASKS=COMPLETE
    FORWARD_TASKS=65
    REVERSE_TASKS=65
    STRUCTURALLY_EMPTY_TASKS=60
    POSITIVE_TASKS=70
    POSITIVE_REFERENCE_OPPORTUNITIES=220
    TOP_TEN_CEILING=208
    BUDGET_TRUNCATED_QUESTIONS=2
    SINGLE_OR_HYBRID_ARMS=12
    P03_FORMAL_SOURCE_GOLD=NONE

Actual run `python -B -m experiments.r0_p03_navigation_probe.exploratory_directed_relation_retrieval_v01 --output` succeeded. Each returned path is a member of the same pinned source population; the source-title query contains no original path target. Three original B0/B1/B2 proxies, prior four RRF combinations, old router, new exact-typed graph index, naive lexical+graph RRF, gated lexical+graph RRF and typed-query router ran on the same 130 query texts. Two real tasks exceed the predeclared K=10 budget and were retained, not suppressed. Reference sets and all rankings are saved per task for independent execution checking.

The direct index returned 208/220 reference instances and no non-neighbor paths (the declared K=10 ceiling). The naive relation+B0 fusion found 186/220 and emitted 600 irrelevant slots over the 60 empty tasks; gated fusion still found 186/220 but emitted none on those empty tasks. Original B0 only found 110/220; broad literal-link B2 proxy found 132/220. These numbers concern **literal source references**, not independent semantics or operational authority.

Old published Checkpoint 908 result SHA-256 `e07bcf10e4f04cbde6cbd08b33fb77c02ca17efa03d1a4dbffb73c7a9439334f` was independently checked before execution. The new typed router delegated all original 74 nonrelation queries to the unchanged previously executed router and exact list parity was confirmed, not scored again.

## Verification and scientific limits

The directed index and the source-derived reference oracle are constructed from the **same 110-edge graph**, so perfect conditional extraction at the K=10 ceiling is structurally expected and not an independent architecture-success claim. These 130 questions deliberately match the implementation's fixed forward/reverse grammar and first-H1 source-title index. No externally blinded source/answer evaluator, human wording generalization, real-world absent-event proof, official R0-P03 source closure, governed editorial B2, concern B3 or model B4 is demonstrated.

The test suite reruns the whole source reading/ranking/scoring process and checks actual full-file SHA-256, complete 130-question inclusion, 74-query regression, structural zero cases, graph inverses and family breakdowns. ## Actual post-execution precommit engineering checks

- The new real 130-query source-derived forward/reverse test, previous Checkpoint 905-908 retrieval experiments, and independent C02 Phase A/B/actual-original safe-evidence boundary tests: **40/40 PASS** (18.56 seconds, isolated ignored temp directory, no pytest cache). The new test recomputes all source/ranking outputs, validates full original JSON byte identity, 65 cases each direction, query parser, forward/reverse inverse graph, false-empty abstention and the 74 historical router cases.
- `scripts/check_current_routing.py`: **PASS**, Checkpoint **909**, `p-three-directed-reference-abstention-tested`, Specification 028 unchanged and latest original experiment `INCOMPLETE`.
- `scripts/check_knowledge_map.py`: **PASS**, 19 knowledge topics, latest Research **646**, all **910** canonical numbered checkpoints (000-909).
- `scripts/check_checkpoint_metadata.py`: **PASS**, **910/910** canonical checkpoints compliant, no warnings/errors.
- `git check-attr text` on the original 1,692,786-byte result JSON: **unset**, preserving exact Git checkout bytes.
- `git diff --check`: exit **0**, only routine Windows tracked-text LF-to-CRLF warnings.
- `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including family-aware repository contracts, project knowledge, checkpoint, Knowledge Map, model collaboration and current-routing gates.

All outcomes above were observed before commit, not inferred from external sources. No claim of post-push publication is made until independently verified. This is not independent gold or formal R0-P03 scoring.
