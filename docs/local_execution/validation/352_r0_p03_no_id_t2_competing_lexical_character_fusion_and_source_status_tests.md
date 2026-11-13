# Validation 352: Real T2 no-ID questions, four competing retrieval methods and selective Status hypotheses

**Date:** 2026-11-13
**Status:** V04_ACTUAL_64_CASE_EXECUTION_AND_EXACT_RERUN_VERIFIED / REPOSITORY_INTEGRITY_PENDING_DOCUMENTATION
**Scope:** Fixed 32 manually authored non-ID query topics across two original Git snapshots, fair ranking source-data access, source-status abstention and falsification of independent-identity assumptions.
**Research:** Research 653. **Checkpoint:** 916.
**Authority:** Exclusive-create question manifest, before-run contract, original Git blobs, actual SQLite FTS5/character-ngram/fusion code and complete saved JSON.

## Actual original-source execution evidence

    SNAPSHOT_S0=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    SNAPSHOT_S1=6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3
    FROZEN_MANIFEST_BYTES=8668
    FROZEN_MANIFEST_SHA256=d632b334ec39e88f5fcaa2c1761e0b2f7ea2aa4d5b8126df962b092918495d05
    RESULT_BYTES=245742
    RESULT_SHA256=327278182a3ea6793ca999be9d5b6e179cdf8bbf89d37bdacdf6f6147773dc1b
    TOTAL_REQUEST_SNAPSHOT_CASES=64
    VALID_AUTHOR_TARGET_IN_SNAPSHOT=51
    AUTHOR_TARGET_ABSENT_OR_NO_TARGET_HYPOTHESIS=13
    FULL_SECTION_BM25_TOP_ONE=45/51
    TITLE_BM25_TOP_ONE=37/51
    CHARACTER_3GRAM_TOP_ONE=47/51
    THREE_WAY_RRF_TOP_ONE=47/51
    PROVISIONAL_SOURCE_STATUS_HYPOTHESES=29
    CORRECT_BY_EXPOSED_AUTHOR_LABEL=29
    ABSTAINED_REQUESTS=35
    OPERATIVE_AUTHORITY_ASSERTIONS=0
    TRUE_INDEPENDENT_SOURCE_GOLD=NONE

The question manifest and fixed contract were actually written before authoring/testing the V04 retrieval implementation. The first V04 executable invocation successfully produced the entire exclusive-create result. No method/result files were changed after that saved output. Per-source SHA and exact original line/Status/supersession evidence persist for each admitted hypothesis. Every snapshot queried its own original 35/36 source sections. Evaluation target IDs were accessed only after ranking, not as hidden retrieval inputs.

The first focused pytest run had **8/9 PASS, one test expectation failure**: the test incorrectly assumed the word `use` was a configured stopword. No source/method/output bytes were changed. Only the test's expected literal query expression was corrected to include `"use"`, and the focused rerun then returned **9/9 PASS** (0.47 seconds), including an exact complete `run()` to JSON equality and a synthetic counterexample where the selective gate accepts a wrong referent despite consensus.

## Observed full precommit regression and repository gates

The new method implementation and immutable 64-case result were not changed after their successful exclusive-create execution. The following test groups each completed with successful exit status using isolated scratch and no pytest cache:

| Executed scope | Result |
| --- | --- |
| T2 V04 fixed 32-query manifest, 64 cases, four mechanisms, exact Git source provenance and full deterministic result replay, synthetic unanimously wrong referent | **9/9 PASS** (0.46 seconds) |
| Prior T2 V03 actual two-Git-snapshot decision-section/94-request evidence and temporal scope | **9/9 PASS** (0.27 seconds) |
| Prior T2 V02 exact-source referent and 118-request abstention regression | **10/10 PASS** (0.67 seconds) |
| Governed Specification 025/028 reference audit plus model collaboration uniqueness/state | **41/41 PASS** (6.29 seconds) |
| Previous T2 V01 synthetic boundary and fixed query controls | **3/3 PASS** (0.10 seconds) |
| Previous T2 V01 actual 120-source original Git manifest and query reconstruction | **2/2 PASS** (18.04 seconds) |
| Previous T2 V01 complete exact Git-source replay and result comparison | **1/1 PASS** (17.53 seconds) |
| Previous T2 V01 frozen output and negative-case controls | **2/2 PASS** (0.12 seconds) |
| Protected C02 evidence-boundary/source-free aggregate identity regressions | **15/15 PASS** (0.15 seconds) |
| **Total across unique observed successful test cases** | **92/92 PASS** |

Repository gates:
- `scripts/check_current_routing.py`: **PASS**, checkpoint **916**, branch `v1-source-vault-bootstrap-resume`, current boundary `p-three-t-two-no-id-retrieval-and-selective-status-tested`, formal P03 outcome `INCOMPLETE`.
- `scripts/check_knowledge_map.py`: **PASS**, Research **653**, **917** numbered checkpoint records and 19 topic groups.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **917/917** numbered checkpoint records compliant.
- `git check-attr text` on both frozen manifest and original result JSON: **unset** for both; Git must not rewrite original bytes for Windows checkout.
- `git diff --check`: exit **0**; only routine tracked text LF/CRLF warnings.
- `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including family-aware repository, Project Knowledge, checkpoint, Knowledge Map, model collaboration and routing checks.
- Fixed question bytes **8668** with SHA-256 `d632b334ec39e88f5fcaa2c1761e0b2f7ea2aa4d5b8126df962b092918495d05`; actual output **245742** with SHA-256 `327278182a3ea6793ca999be9d5b6e179cdf8bbf89d37bdacdf6f6147773dc1b`, both checked by dedicated tests and exact replay.

A first routing check **failed** because the new boundary slug exceeded its 64-character schema limit. Only that routing metadata identifier was shortened; the 32 frozen questions, 64-case result and comparator code remained untouched. Repeated routing and full public integrity gates then passed. No post-result retrieval threshold tuning occurred.

This is **precommit** validation. Git publication, exact remote branch HEAD and committed file bytes are not claimed until separate observed commit/push/postflight checks. No original Research 513/559/576 B0-B4 score, production vector/embedding model, independent source-owner gold or current operative governing truth is asserted.
