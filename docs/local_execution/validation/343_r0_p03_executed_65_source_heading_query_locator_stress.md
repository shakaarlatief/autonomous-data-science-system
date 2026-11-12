# Validation 343: Actual 65 historical source-heading query lookup comparison

**Date:** 2026-11-12
**Status:** REAL_65_OF_65_MECHANICAL_QUERIES_EXECUTED / ACTUAL_B0_B1_B2_PROXY_SOURCE_RANK_METRICS
**Scope:** Preserve exact direct-run source-location results and the explicit source/title/answer-authoring limitations, not qualify formal R0-P03 architecture scoring.
**Authority:** Actual `exploratory_65_source_heading_query_stress.py --output` execution; Research 644 / Checkpoint 907.

## Exact verified input/output

    FILE=experiments/r0_p03_navigation_probe/exploratory_65_source_heading_query_stress_result_v01.json
    EXPECTED_LENGTH_BYTES=195216
    EXPECTED_SHA256=497cdfc559f7d2d56c97b12afb33de1210f5f8bf1945ca9978bd7b73b6ad58b4
    SOURCE_REVISION=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    SOURCE_DOCS=65
    SOURCE_LOCAL_FIRST_H1=65
    UNIQUE_SOURCE_H1=65
    FTS5_SHARED_SOURCE_CORPUS=65
    MAX_RETRIEVAL_SLOTS_PER_QUERY=10
    QUERY_FAMILY=MECHANICAL_H1_EXACT_DOCUMENT_LOCATOR
    B1_SUBJECT_ID_FROM_OLD_GOLD=NONE
    B1_INFERRED_TOPICS=54
    B1_LEXICAL_FALLBACKS=11
    B2_SOURCE_MENTION_EDGES=110
    B2_LINK_ADDITIONS_AFTER_SEEDS=306

| Actual exact-document ranking metric | B0-like lexical | B1-like inferred subject | B2-like literal citation |
| --- | ---: | ---: | ---: |
| Hit@1 | 45/65 | 33/65 | 45/65 |
| Hit@10 | 64/65 | 63/65 | 64/65 |
| MRR@10 | 0.803590 | 0.653590 | 0.802949 |
| Returned slots | 650 | 650 | 650 |

All outputs were actually computed over original historical Git source texts, not invented, forecast or transferred from prior reported scenario passes. They are **exact-source-location** outcomes for questions generated from sources' own headings. This gives an independently mechanically constructed task family relative to the old B1-authored nine labels, but it is not unseen corpus/data or human-designed epistemic answer gold.

The new regression suite reruns actual code against the same historical Git objects, verifies 65-of-65 included unique H1 targets, rechecks observed top-k outcomes and exact JSON SHA-256, and tests subject inference and reference traversal on synthetic controls. Original C01/C02 restricted content is not read. Formal R0-P03 remains unscored.

## Engineering verification results

## Actual precommit engineering verification

- New 65-query real-source heading stress, prior B2 literal link proxy and B0/B1 existing pilot plus original C02 source-free boundary regressions: **28/28 PASS** (9.26 seconds, isolated ignored temp directory, no pytest cache).
- `scripts/check_current_routing.py`: **PASS**, current Checkpoint **907**, boundary `p-three-heading-query-generalization-executed`.
- `scripts/check_knowledge_map.py`: **PASS**, Research **644**, **908** numbered canonical checkpoints and 19 topic groups.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **908/908** numbered checkpoints compliant, no errors or warnings.
- `git check-attr text` on exact 195,216-byte result JSON: **unset** to avoid checkout newline conversion.
- `git diff --check`: exit **0**, Windows-only warnings on four ordinary tracked text files.
- Public full integrity `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS** across family-aware contracts, knowledge, checkpoints, Knowledge Map, model collaboration state and routing.
- Actual output file SHA-256 and byte length were independently rechecked **PASS**.

These are precommit actual observations; publication must be independently verified after committing. No formal Research 513 task/gold/arm completion or architecture target selection is asserted.
